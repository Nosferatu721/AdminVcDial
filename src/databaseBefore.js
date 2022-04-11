const mysql = require("mysql2");
const { database } = require("./keys");
// require("dotenv").config();

let conn = mysql.createConnection({
  host: database.host,
  user: database.user,
  database: database.database,
  password: database.password,
  dateStrings: true,
});

try {
  conn.query("SELECT 1");
  console.log("Connected DB ༼ つ ◕_◕ ༽つ");
} catch (error) {
  conn = mysql.createConnection({
    host: database.host,
    user: database.user,
    database: database.database,
    password: database.password,
    dateStrings: true,
  });
  console.log("Connected DB ༼ つ ◕_◕ ༽つ");
}

module.exports = conn;
