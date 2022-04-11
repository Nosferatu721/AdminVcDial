const mysql = require("mysql2");
const { exec, spawn } = require('child_process');
const { database } = require("./keys");
// require("dotenv").config();

let conn = mysql.createConnection({
  host: database.host,
  user: database.user,
  database: database.database,
  password: database.password,
  dateStrings: true,
});

// * Valida si se desconecta Node y DB
// conn.end();
try {
  conn.query("SELECT 1");
  console.log("Connected DB ༼ つ ◕_◕ ༽つ");
  const sql = "SELECT PKCRE_NCODIGO, CRE_CNOMBRE, CRE_CAPELLIDO FROM dbp_usuarios.tbl_rcredencial LIMIT 10";
  setInterval(() => {
    conn
      .promise()
      .query(sql)
      .then(([result, fields]) => {
        console.log("Todo Correcto");
      })
      .catch((err) => console.log("ERROR::", err));
  }, 1800000);
} catch (error) {
  if (error) {
    let posicion = error.message.indexOf("Can't add new command when connection is in closed state");
    if (posicion !== -1) {
      console.log("Disconnected DB :(");
      conn = mysql.createConnection({
        host: database.host,
        user: database.user,
        database: database.database,
        password: database.password,
        dateStrings: true,
      });
      console.log("Reconected DB ༼ つ ◕_◕ ༽つ");
    }
  }
}

const ejecutarPython = (nombre_bot) => {
  const child = spawn('python3', ['-u', 'vcdial-py/AdminVcdial.py', nombre_bot]);
  child.stdout.on('data', (data) => {
    console.log(`stdout:\n${data}`);
  });
  child.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
};

const reactivarBots = async () => {
  console.log('--- Reactivando Bots ---'.italic);
  let [rows] = await conn.promise().query(`SELECT * FROM dbp_virtualvcdial.tbl_rbots WHERE BOT_CDETALLE1 = '3'`);
  let listNamesBots = await rows.map((row) => row.BOT_CDETALLE);
  if (rows.length > 0) {
    conn
    .promise()
    .query(`UPDATE dbp_virtualvcdial.tbl_rbots SET BOT_CDETALLE1 = '0' WHERE BOT_CDETALLE1 = '3'`)
    .then(([resultUpd]) => {
      listNamesBots.forEach((element) => {
        console.log('Se ejecuto', element);
        ejecutarPython(element);
      });
    });
    console.log('--- Bots Reactivos ---');
  } else {
    console.log('--- Sin Bots Por Reactivar ---');
  }
};
reactivarBots();

module.exports = conn;
