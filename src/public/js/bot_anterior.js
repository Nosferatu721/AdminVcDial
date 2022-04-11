document.addEventListener("DOMContentLoaded", (e) => {
  const containerLoader = document.getElementById("containerLoader"),
    messageLoader = document.getElementById("messageLoader"),
    cargarLoader = (message = "Cargando...") => {
      containerLoader.classList.remove("displayNone");
      messageLoader.textContent = message;
      setTimeout(() => { }, 1000);
    },
    ocultarLoader = () => {
      containerLoader.classList.add("displayNone");
      messageLoader.textContent = "";
    };

  const mostrarBots = () => {
    const recursivaMostrarBots = () => {
      const containerBots = document.getElementById("containerBots"),
        cantidad_bots = document.getElementById("cantidad_bots");
      getData("/bot/all").then((res) => {
        let arrBots = res.result;
        cantidad_bots.textContent = arrBots.length;
        containerBots.innerHTML = "";
        for (let i = 0; i < arrBots.length; i += 3) {
          const divRow = document.createElement("div");
          divRow.classList.add("rowBots");

          const hr = document.createElement("hr");
          hr.setAttribute("id", "showCaseBackgroundLine");

          // Crear contenedor de cada Bot
          const divBotA = document.createElement("div");
          const divBotB = document.createElement("div");
          const divBotC = document.createElement("div");

          // Asignar Clases
          divBotA.className = "cardBot a";
          divBotB.className = "cardBot b";
          divBotC.className = "cardBot c";

          // Agregar info del Bot
          const htmlCardBot = (idBot, dato2, dato3, dato4, dato5, dato6, detenido) => {
            let html = ``;
            if (detenido) {
              html = `
            <a href="#" id="btn_eliminar" data-id_eliminar="${idBot}" class="btn_eliminar medium material-icons">close</a>
            <div class="title_bot">${dato2}</div>
            <div>'Detenido'</div>
            <img src="img/robotzzz.gif" alt="">
            <div class="botones">
              <a href="#" id="btn_activar" data-id_activar="${idBot}" class="blue-text btn_activar">Activar</a>
            </div>
            `;
            } else {
              html = `
            <a href="#" id="btn_eliminar" data-id_eliminar="${idBot}" class="btn_eliminar medium material-icons">close</a>
            <a href="#modal_config_bot" id="btn_config" data-id_config="${idBot}" class="material-icons btn_config modal-trigger">settings</a>
            <div class="title_bot">${dato2}</div>
            <div>Agentes Conectados: <span>${dato3}</span></div>
            <div>Agentes en Llamada: <span>${dato4}</span></div>
            <div>Metodo de Marcado: <span>${dato5}</span></div>
            <div>Nivel de Marcador: <span>${dato6}</span></div>
            <div class="botones">
              <a href="#" id="btn_detener" data-id_detener="${idBot}" class="red-text btn_detener">Detener</a>
              <a href="#modal_ver_mas" id="btn_ver_mas" data-id_ver_mas="${idBot}" class="red-text btn_ver_mas modal-trigger">Ver Mas</a>
            </div>
            `;
            }
            return html;
          };
          arrBots[i].BOT_CDETALLE11 ? (divBotA.innerHTML = htmlCardBot(arrBots[i].PKBOT_NCODIGO, arrBots[i].BOT_CDETALLE, arrBots[i].BOT_CDETALLE11.agentesConectados, arrBots[i].BOT_CDETALLE11.agentesEnLlamada, arrBots[i].BOT_CDETALLE11.metodoMarcado, arrBots[i].BOT_CDETALLE11.nivelMarcado, arrBots[i].BOT_CDETALLE7)) : (divBotA.innerHTML = htmlCardBot(arrBots[i].PKBOT_NCODIGO, arrBots[i].BOT_CDETALLE, "...", "...", "...", "...", arrBots[i].BOT_CDETALLE7));
          if (!(i + 1 === arrBots.length)) {
            arrBots[i + 1].BOT_CDETALLE11
              ? (divBotB.innerHTML = htmlCardBot(arrBots[i + 1].PKBOT_NCODIGO, arrBots[i + 1].BOT_CDETALLE, arrBots[i + 1].BOT_CDETALLE11.agentesConectados, arrBots[i + 1].BOT_CDETALLE11.agentesEnLlamada, arrBots[i + 1].BOT_CDETALLE11.metodoMarcado, arrBots[i + 1].BOT_CDETALLE11.nivelMarcado, arrBots[i + 1].BOT_CDETALLE7))
              : (divBotB.innerHTML = htmlCardBot(arrBots[i + 1].PKBOT_NCODIGO, arrBots[i + 1].BOT_CDETALLE, "...", "...", "...", "...", arrBots[i + 1].BOT_CDETALLE7));
            if (!(i + 2 === arrBots.length)) {
              arrBots[i + 2].BOT_CDETALLE11
                ? (divBotC.innerHTML = htmlCardBot(arrBots[i + 2].PKBOT_NCODIGO, arrBots[i + 2].BOT_CDETALLE, arrBots[i + 2].BOT_CDETALLE11.agentesConectados, arrBots[i + 2].BOT_CDETALLE11.agentesEnLlamada, arrBots[i + 2].BOT_CDETALLE11.metodoMarcado, arrBots[i + 2].BOT_CDETALLE11.nivelMarcado, arrBots[i + 2].BOT_CDETALLE7))
                : (divBotC.innerHTML = htmlCardBot(arrBots[i + 2].PKBOT_NCODIGO, arrBots[i + 2].BOT_CDETALLE, "...", "...", "...", "...", arrBots[i + 2].BOT_CDETALLE7));
            } else {
              divBotC.classList.add("hidden");
            }
          } else {
            divBotB.classList.add("hidden");
            divBotC.classList.add("hidden");
          }
          // Agregar Contenedore Bot a el div Padre
          divRow.append(hr, divBotA, divBotB, divBotC);
          containerBots.append(divRow);
        }
        animacionesListBots();
        eliminar();
        configBot();
        verMas();
        detener();
        activar();
        setTimeout(() => {
          recursivaMostrarBots();
        }, 4000);
      });
    };
    recursivaMostrarBots();
  };

  const animacionesListBots = () => {
    $(function () {
      $(".cardBot").on("click", function () {
        if ($(this).hasClass("a")) {
          $(".b").removeClass("activeB");
          $(".c").removeClass("activeC");
          $(this).toggleClass("activeA");
        } else if ($(this).hasClass("b")) {
          $(".a").removeClass("activeA");
          $(".c").removeClass("activeC");
          $(this).toggleClass("activeB");
        } else if ($(this).hasClass("c")) {
          $(".a").removeClass("activeA");
          $(".b").removeClass("activeB");
          $(this).toggleClass("activeC");
        }
      });
    });
  };

  let intervalVerMas = 0;
  const verMas = () => {
    document.querySelectorAll("[data-id_ver_mas]").forEach((btn_ver_mas_bot) => {
      btn_ver_mas_bot.addEventListener("click", (e) => {
        const recursivaVerMas = () => {
          clearTimeout(intervalVerMas);
          const modal_infoBot = document.querySelector("#modal_infoBot"),
            modal_nombreBot = document.getElementById("modal_nombreBot");
          let id_ver_mas = e.target.dataset.id_ver_mas;
          getData(`/bot/verMas/${id_ver_mas}`).then((res) => {
            // Nombre del Bot
            modal_nombreBot.textContent = res.result.BOT_CDETALLE;
            // Info Bot
            let data = res.result.BOT_CDETALLE11;
            html = ``;
            html = `
                <div class="item">Nivel de Marcado: <span>${data.nivelMarcado}</span></div>
                <div class="item">Tronco de Corta / Fill: <span>${data.troncoCortaFIll}</span></div>
                <div class="item">Filtro: <span>${data.filtro}</span></div>
                <div class="item">Tiempo: <span>${data.tiempo}</span></div>
                <div class="item">Registros Marcables: <span>${data.registrosMarcables}</span></div>
                <div class="item">Llamadas de hoy: <span>${data.llamadasHoy}</span></div>
                <div class="item">Agentes AVG: <span>${data.agentesAVG}</span></div>
                <div class="item">Método Marcado: <span>${data.metodoMarcado}</span></div>
                <div class="item">Hopper(min/auto): <span>${data.hopper}</span></div>
                <div class="item">Caído / Contestado: <span>${data.caidoContestado}</span></div>
                <div class="item">DL IDF: <span>${data.dlDif}</span></div>
                <div class="item">Estados: <span>${data.estados}</span></div>
                <div class="item">Regitros Hopper: <span>${data.registrosHopper}</span></div>
                <div class="item">Porcentaje de Perdidas: <span>${data.porcentajePerdidas}</span></div>
                <div class="item">DIF: <span>${data.dif}</span></div>
                <div class="item">Orden: <span>${data.orden}</span></div>
                <div class="titulo">Llamadas</div>
                <div class="item">Que Colocan: <span>${data.llamadasQueColocan}</span></div>
                <div class="item">Timbrando: <span>${data.llamadasTimbrando}</span></div>
                <div class="item">A la Espera: <span>${data.llamadasEsperaAgente}</span></div>
                <div class="item">En IVR: <span>${data.llamadasEnIVR}</span></div>
                <div class="titulo">Agentes</div>
                <div class="item">Conectados: <span>${data.agentesConectados}</span></div>
                <div class="item">En Llamada: <span>${data.agentesEnLlamada}</span></div>
                <div class="item">Esperando: <span>${data.agentesEsperando}</span></div>
                <div class="item">Pausados: <span>${data.agentesPausados}</span></div>
                <div class="item">En Llamadas Muertas: <span>${data.agentesLlamadasMuertas}</span></div>
                <div class="item">En TIP: <span>${data.agentesEnTIP}</span></div>
              `;
            // Info Agentes
            let agentesCount = res.arrAgentes[0][0].split(" ").indexOf("ERROR:");
            if (agentesCount !== 0) {
              // Estructura de la Tabla
              html += `
              <div class="table-agentes" id="modal_infoAgentes">
                <table class="centered highlight">
                  <thead>
                    <tr>
                      <th>Usuario</th>
                      <th>Nombre</th>
                      <th>Session</th>
                      <th>ID Cliente</th>
                      <th>Estado</th>
                      <th>Campaña</th>
                    </tr>
                  </thead>
                  <tbody>
              `;
              let htmlTable = ``;
              res.arrAgentes.forEach((element) => {
                htmlTable += `
                  <tr>
                    <td>${element[0]}</td>
                    <td>${element[7]}</td>
                    <td>${element[2]}</td>
                    <td>${element[4]}</td>
                    <td>${element[3]}</td>
                    <td>${element[1]}</td>
                  </tr>
                  `;
              });
              html += htmlTable;
              html += `
                    </tbody>
                  </table>
                </div>
                `;
              modal_infoBot.innerHTML = html;
            } else {
              html += `<div class="titulo">Sin Agentes</div>`;
              modal_infoBot.innerHTML = html;
            }
            intervalVerMas = setTimeout(() => {
              recursivaVerMas();
            }, 4000);
          });
        };
        recursivaVerMas();
      });
    });
  };

  const eliminar = () => {
    document.querySelectorAll("[data-id_eliminar]").forEach((btn_detener_bot) => {
      btn_detener_bot.addEventListener("click", (e) => {
        let id_eliminar = e.target.dataset.id_eliminar;
        Swal.fire({
          title: "¿Desea Eliminar El Bot?",
          showCancelButton: true,
          confirmButtonColor: 'rgb(202, 5, 29)',
          confirmButtonText: "Si",
        }).then((result) => {
          if (result.isConfirmed) {
            cargarLoader("Eliminando");
            getData(`/bot/detener/${id_eliminar}`).then((res) => {
              setTimeout(() => {
                deleteData(`/bot/${id_eliminar}`).then((res) => {
                  mostrarBots();
                  ocultarLoader();
                  Toast.fire({
                    icon: "success",
                    title: "Bot Eliminado",
                  });
                });
              }, 5000);
            });
          }
        });
      });
    });
  };

  const activar = () => {
    document.querySelectorAll("[data-id_activar]").forEach((btn_detener_bot) => {
      btn_detener_bot.addEventListener("click", (e) => {
        let id_activar = e.target.dataset.id_activar;
        Swal.fire({
          title: "¿Desea Activar El Bot?",
          showCancelButton: true,
          confirmButtonColor: 'rgb(202, 5, 29)',
          confirmButtonText: `Si`,
        }).then((result) => {
          if (result.isConfirmed) {
            cargarLoader("Activando Bot");
            getData(`/bot/activar/${id_activar}`).then((res) => {
              mostrarBots();
              ocultarLoader();
              Toast.fire({
                icon: "success",
                title: "Bot Activado",
              });
            });
          }
        });
      });
    });
  };

  const detener = () => {
    document.querySelectorAll("[data-id_detener]").forEach((btn_detener_bot) => {
      btn_detener_bot.addEventListener("click", (e) => {
        let id_detener = e.target.dataset.id_detener;
        Swal.fire({
          title: "¿Desea Detener El Bot?",
          showCancelButton: true,
          confirmButtonColor: 'rgb(202, 5, 29)',
          confirmButtonText: `Si`,
        }).then((result) => {
          if (result.isConfirmed) {
            cargarLoader("Deteniendo Bot");
            getData(`/bot/detener/${id_detener}`).then((res) => {
              mostrarBots();
              ocultarLoader();
              Toast.fire({
                icon: "success",
                title: "Bot Detenido",
              });
            });
          }
        });
      });
    });
  };

  mostrarBots();

  const validarFormConfigBot = (periodoCambio, limiteDisponible, selectRatio) => {
    // Si la Ip no tiene el Formato Correcto
    let errorMessage = "";
    // Si es Numero
    if (isNaN(parseInt(periodoCambio)) || isNaN(parseInt(limiteDisponible))) {
      errorMessage = "Valores No Numericos";
    }
    // Si Estan Vacios
    if (!periodoCambio || !limiteDisponible || !selectRatio) {
      errorMessage = "Campos Vacios";
    }
    if (errorMessage) {
      Toast.fire({
        icon: "error",
        title: errorMessage,
      });
      return false;
    }
    return true;
  };

  let id_config = 0;
  const configBot = () => {
    const periodoCambio = document.getElementById("periodoCambio"),
      limiteDisponible = document.getElementById("limiteDisponible"),
      selectRatio = document.getElementById("selectRatio"),
      formConfig_nombreBot = document.getElementById("formConfig_nombreBot");
    // Al dar Click en Configurar
    document.querySelectorAll("[data-id_config]").forEach((btn_config) => {
      btn_config.addEventListener("click", (e) => {
        id_config = e.target.dataset.id_config;
        cargarLoader("Cargando Configuración");
        getData(`/bot/porId/${id_config}`).then((res) => {
          [periodoCambio, limiteDisponible].forEach((input) => {
            input.nextElementSibling.classList.add("active");
          });
          formConfig_nombreBot.textContent = `Configurar ${res.result.BOT_CDETALLE}`;
          periodoCambio.value = res.result.BOT_CDETALLE13;
          limiteDisponible.value = res.result.BOT_CDETALLE14;
          selectRatio.value = res.result.BOT_CDETALLE12;
          // Siguiente Codigo apunta al Span
          periodoCambio.nextElementSibling.nextElementSibling.textContent = `Actual: ${res.result.BOT_CDETALLE13} seg`;
          limiteDisponible.nextElementSibling.nextElementSibling.textContent = `Actual: ${res.result.BOT_CDETALLE14} agentes`;
          selectRatio.nextElementSibling.textContent = `Actual: ${res.result.BOT_CDETALLE12}`;
          ocultarLoader();
        });
      });
    });
  };

  // Al dar Click en Aplicar
  const btn_aplicar_config = document.getElementById("btn_aplicar_config");
  btn_aplicar_config.addEventListener("click", (e) => {
    e.preventDefault();
    if (!validarFormConfigBot(periodoCambio.value, limiteDisponible.value, selectRatio.value)) {
      return;
    }
    cargarLoader("Aplicando Configuración");
    postData("/bot/config", {
      id_config,
      periodoCambio: periodoCambio.value,
      limiteDisponible: limiteDisponible.value,
      selectRatio: selectRatio.value,
    }).then((res) => {
      ocultarLoader();
      Toast.fire({
        icon: "success",
        title: "Bot Actualizado",
      });
      let instance = M.Modal.getInstance(elemsModal[1]);
      instance.close();
    });
  });

  const validarFormCrearBot = (nombre_bot, user, ip, password) => {
    // Si la Ip no tiene el Formato Correcto
    let errorMessage = "";
    // let re = new RegExp("^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$");
    // let ipValida = re.test(ip);
    // if (!ipValida) {
    //   errorMessage = "IP Invalida";
    // }
    // Si el Nombre del Bot es incorrecto
    if (nombre_bot.length > 18) {
      errorMessage = "Nombre Bot Incorrecto";
    }
    // Si Estan Vacios
    if (!nombre_bot || !user || !ip || !password) {
      errorMessage = "Campos Vacios";
    }
    if (errorMessage) {
      Toast.fire({
        icon: "error",
        title: errorMessage,
      });
      return false;
    }
    return true;
  };

  const btn_crear_bot = document.getElementById("btn_crear_bot"),
    btn_limpiarFromCrearBot = document.querySelector("#modal_crear_bot #btn_limpiar"),
    btn_agregar_camp = document.getElementById("btn_agregar_camp"),
    nombre_bot = document.getElementById("nombre_bot"),
    ip = document.getElementById("ip"),
    user = document.getElementById("user"),
    password = document.getElementById("password"),
    selectCamp = document.getElementById("selectCamp");
  let id_bot;
  // Limpiar Form para Crear Bot
  btn_limpiarFromCrearBot.addEventListener("click", (e) => {
    limpiarCampos([nombre_bot, ip, user, password]);
  });
  // Para a Mayusculas
  inputsMayus([nombre_bot]);
  // Al dar Click en Crear Bot
  btn_crear_bot.addEventListener("click", function (e) {
    e.preventDefault();
    if (!validarFormCrearBot(nombre_bot.value, user.value, ip.value, password.value)) {
      return;
    }
    postData("/bot/new", {
      nombre_bot: nombre_bot.value,
      user: user.value,
      ip: ip.value,
      password: password.value,
    }).then((res) => {
      if (res.nombre_bot) {
        Toast.fire({
          icon: "info",
          title: `El Bot <span style="color: red;">${res.nombre_bot}</span> ya existe`,
        });
      } else if (res.result) {
        id_bot = res.result.insertId;
        cargarLoader("Autenticando");
        const recursivaGetCamp = () => {
          setTimeout(() => {
            getData(`/bot/getCamp/${id_bot}`).then((res) => {
              console.info("Esperando Campañas... ಠ_ಠ");
              if (res.result.BOT_CDETALLE5) {
                nombre_bot.setAttribute("disabled", "");
                user.setAttribute("disabled", "");
                ip.setAttribute("disabled", "");
                password.setAttribute("disabled", "");
                let campañas = res.result.BOT_CDETALLE5.split("|");
                campañas = campañas.map((camp) => `<option value="${camp}">${camp}</option>`);
                campañas.forEach((camp) => {
                  selectCamp.innerHTML += camp;
                });
                selectCamp.classList.remove("displayNone");
                btn_agregar_camp.classList.remove("displayNone");
                btn_crear_bot.classList.add("displayNone");
                ocultarLoader();
              } else if (res.result.BOT_CDETALLE7 === "CREDENCIALES INVALIDAS") {
                ocultarLoader();
                Toast.fire({
                  icon: "error",
                  title: "Credenciales Incorrectas",
                });
                deleteData(`/bot/${id_bot}`);
              } else {
                recursivaGetCamp();
              }
            });
          }, 1000);
        };
        recursivaGetCamp();
      }
    });
  });
  // Al dar Click en Agregar Campaña
  btn_agregar_camp.addEventListener("click", (e) => {
    e.preventDefault();
    const selectCamp = document.getElementById("selectCamp"),
      inputs = document.querySelectorAll(".form-new-bot input[disabled]"),
      labels = document.querySelectorAll(".form-new-bot label");
    cargarLoader();
    postData("/bot/agregarCamp", { id_bot, selectCamp: selectCamp.value, ip: ip.value }).then((res) => {
      if (res.campExiste) {
        Toast.fire({
          icon: "info",
          title: `Ya existe un Bot con la Ip <span style="color: #2980b9;">${ip.value}</span> y la Campaña <span style="color: #2980b9;">${selectCamp.value}</span>, se llama <span style="color: #e58e26;">${res.result}</span>`,
        });
        selectCamp.innerHTML = "";
        selectCamp.classList.add("displayNone");
        inputs.forEach((input) => {
          input.removeAttribute("disabled");
        });
        btn_agregar_camp.classList.add("displayNone");
        btn_crear_bot.classList.remove("displayNone");
        // deleteData(`/bot/${id_bot}`);
      } else if (res.result) {
        if (!res.result[0].affectedRows) {
          Toast.fire({
            icon: "warning",
            title: "Tiempo de espera agotado, crea otra vez el Bot",
          });
        } else {
          Toast.fire({
            icon: "success",
            title: `Bot <span style="color: #2980b9;">${nombre_bot.value}</span> creado 😁`,
          });
          let instance = M.Modal.getInstance(elemsModal[0]);
          instance.close();
          selectCamp.innerHTML = "";
          selectCamp.classList.add("displayNone");
          inputs.forEach((input) => {
            input.removeAttribute("disabled");
            input.value = "";
          });
          labels.forEach((label) => label.classList.remove("active"));
          btn_agregar_camp.classList.add("displayNone");
          btn_crear_bot.classList.remove("displayNone");
          mostrarBots();
        }
      }
      ocultarLoader();
    });
  });
});
