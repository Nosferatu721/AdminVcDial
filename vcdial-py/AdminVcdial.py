from Principal import *
import datetime
import urllib3



# Credenciales Database
IP_SERVIDOR = '41785A3245774C6D41775232446D4C3441784C335A6D7030' #site 2 5A6D526D416D5A6C5A78486D416D5A6A5A78486D416D57535A6D566D5A6A3D3D #localhost: 41785A3245774C6D41775232446D4C3441784C335A6D7030 #site7: 5A6D526D416D5A6C5A7A486D416D5A6A5A7A486D416D57795A6D566D5A6A3D3D
USUARIO_SERVIDOR = '41775A324D77706D414A4C325A6D706C417A443D'
CONTRASENA_SERVIDOR = '417770324147706D416D443242474D7A417A4832416D4C31417A48324147706C417752324C6D4C6D417A4C335A6D41755A6D566D5A515A6C5A6D4E3D'
BD_SERVIDOR = '417744325A77706A41484C3341774C35416D56334151703141775232446D703241775A3241514C3541775232446A3D3D'

#Constantes globales
ESTADO_REGISTRO = 'Activo'
CONSULTA_REGISTRO = 'ControlInicioBot'
BD_QUERY = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
NOMBRE_BOT = str(sys.argv[1]).strip()  
urllib3.disable_warnings()
Respuesta = ""

#Variables globales
#global driver



#Obtener linea del script
def getLinea():
    linea = sys._getframe(1).f_lineno
    return f"Linea: {linea}"

#Inicia sesión y retorna el listado de campañas disponibles
def obtenerListaCampanas(codTarea, ipVcidial, usuarioVcidial, contrasenaVcidial):
    ipVcidial = str(ipVcidial).strip()
    usuarioVcidial = str(usuarioVcidial).strip()
    contrasenaVcidial = str(contrasenaVcidial).strip()

    try:
        FuncPrograma.indicarAutenticando(codTarea, 'Inicio')
        # Codigo de descarga del estado actual de la campaña, limpia el codigo HTML dejando solo los datos que necesitamos
        try:
            Respuesta = requests.get(f"http://" + str(usuarioVcidial) + ":" + str(contrasenaVcidial) + "@" + str(ipVcidial) + "/vicidial/admin.php?ADD=10", verify=False)
        except Exception as e:
            if "Name or service not known" in str(e):
                Respuesta = requests.get(f"https://" + str(usuarioVcidial) + ":" + str(contrasenaVcidial) + "@" + str(ipVcidial) + "/vicidial/admin.php?ADD=10", verify=False)

        if Respuesta.status_code == 200:
            Respuesta = str(Respuesta.text).split("<center><TABLE width=750 cellspacing=0 cellpadding=1>")[1]
            Respuesta = str(Respuesta).split("</TABLE></center>")[0]
            Respuesta = Respuesta.replace("<tr bgcolor=black>", "")
            Respuesta = Respuesta.replace("<td NOWRAP>", "")
            Respuesta = Respuesta.replace("<font size=1 color=white align=left>", "")
            Respuesta = Respuesta.replace("<B>ID Campaña</B></td><font size=1 color=white>", "")
            Respuesta = Respuesta.replace('<td>', "")
            Respuesta = Respuesta.replace("<font size=1 color=black>PortaEsp</a>", "")
            Respuesta = Respuesta.replace("records_list_y", "")
            Respuesta = Respuesta.replace("class=", "")
            Respuesta = Respuesta.replace("window.document.location", "")

            Respuesta = str(Respuesta).split("\n")
            Respuesta.pop(0)
            Respuesta.pop(0)

            """se recorre la array interna producida al separar por salto de linea la respuesta del http
            luego validamos al recorrer la array interna que sea la posicion 3 y la agregamos a la Array contenedora de datos"""
            ArrayCampanas = []
            for index in range(0, len(Respuesta)):
                Respuesta[index] = str(Respuesta[index]).split("campaign_id")
                for indexinterno in range(0, len(Respuesta[index])):
                    if indexinterno == 3:
                        ArrayCampanas.append(Respuesta[index][indexinterno])

            for index in range(0, len(ArrayCampanas)):
                ArrayCampanas[index] = str(ArrayCampanas[index]).split('"')[0]
                ArrayCampanas[index] = str(ArrayCampanas[index]).strip("=").strip()

            FuncPrograma.indicarAutenticando(codTarea, 'Fin')

        else:
            return 'CREDENCIALES INVALIDAS'

    except requests.exceptions.ConnectionError as e:
        return 'CREDENCIALES INVALIDAS'
    except Exception as e:
        print("Archivo log")

    texto = "|".join(ArrayCampanas)
    return texto

#Identifica la campaña solicitada y obtiene  el tiempo real de la gestión
def validarCampana(ipVicidial, usuarioVcidial, contrasenaVcidial, campanaSeleccionada, codTarea):
        
    ipVicidial = str(ipVicidial).strip()
    usuarioVcidial = str(usuarioVcidial).strip()
    contrasenaVcidial = str(contrasenaVcidial).strip()
    campanaSeleccionada =str(campanaSeleccionada).strip()
    codTarea =str(codTarea).strip()

    #Monitor en tiempo real
    #parametrosRatio = FuncPrograma.controlParametrosRatio(EjecutablePrograma)
    #tiempoEspera = FuncPrograma.controlParametrosPrograma(0)
    intervaloAdmin = int(FuncPrograma.intervaloControl(codTarea))

    contador = intervaloAdmin
    correcto = True
    while correcto == True: #while de validarCampaña (1)
        
        intervaloAdmin = int(FuncPrograma.intervaloControl(codTarea))

        #Verificar si se pide cancelar el proceso actual
        cancelarTarea = FuncPrograma.controlDetenerBot(codTarea)
        #print('cancelar tarea? => ', cancelarTarea)
        if cancelarTarea == 'DETENER':
            correcto = False
            print(NOMBRE_BOT, '>>> Bot detenido por el usuario. En validarCamapana()', getLinea())
            break
        
        try:    


            #Codigo Nuevo
            """llamadasQueColocan = "0"
            llamadasTimbrando = "0"
            llamadasEsperaAgente = "0"
            llamadasEnIVR = "0"
            agentesConectados = "0"
            agentesEnLlamada = "0"
            agentesEsperando = "0"
            agentesPausados = "0"
            agentesLlamadasMuertas = "0"
            agentesEnTIP = "0"
"""

            # Codigo de descarga del estado actual de la campaña, limpia el codigo HTML dejando solo los datos que necesitamos
            try:
                try:
                    Respuesta = requests.post(f"http://" + str(usuarioVcidial) + ":" + str(contrasenaVcidial) + "@" + str(ipVicidial) + "/vicidial/AST_timeonVDADall.php?RTajax=1&DB=0&groups[]=" + str(campanaSeleccionada) + "&user_group_filter[]=ALL-GROUPS&ingroup_filter[]=ALL-INGROUPS&adastats=&SIPmonitorLINK=&IAXmonitorLINK=&usergroup=&UGdisplay=0UidORname=1&orderby=timeup&SERVdisplay=0&CALLSdisplay=1&PHONEdisplay=0&CUSTPHONEdisplay=0&CUSTINFOdisplay=0&with_inbound=Y&monitor_active=&monitor_phone=&ALLINGROUPstats=&DROPINGROUPstats=&NOLEADSalert=&CARRIERstats=0&PRESETstats=0&AGENTtimeSTATS=0&parkSTATS=0&SLAinSTATS=0&INGROUPcolorOVERRIDE=&droppedOFtotal=&report_display_type=TEXT", verify=False)
                except Exception as e:
                    if "Name or service not known" in str(e):
                        Respuesta = requests.post(f"https://" + str(usuarioVcidial) + ":" + str(contrasenaVcidial) + "@" + str(ipVicidial) + "/vicidial/AST_timeonVDADall.php?RTajax=1&DB=0&groups[]=" + str(campanaSeleccionada) + "&user_group_filter[]=ALL-GROUPS&ingroup_filter[]=ALL-INGROUPS&adastats=&SIPmonitorLINK=&IAXmonitorLINK=&usergroup=&UGdisplay=0UidORname=1&orderby=timeup&SERVdisplay=0&CALLSdisplay=1&PHONEdisplay=0&CUSTPHONEdisplay=0&CUSTINFOdisplay=0&with_inbound=Y&monitor_active=&monitor_phone=&ALLINGROUPstats=&DROPINGROUPstats=&NOLEADSalert=&CARRIERstats=0&PRESETstats=0&AGENTtimeSTATS=0&parkSTATS=0&SLAinSTATS=0&INGROUPcolorOVERRIDE=&droppedOFtotal=&report_display_type=TEXT", verify=False)

                if int(Respuesta.status_code) == 200:

                    Respuesta = str(Respuesta.text).split("+----------------+------------------------+-----------+-----------------+---------+------------+-------+------+-------------------</tr>")[0]
                    Respuesta = Respuesta.split("<!-- ajax-mode -->")[1]
                    Respuesta = Respuesta.replace("&nbsp;", "").replace("no hay chats en vivo de espera", "")
                    Respuesta = Respuesta.replace('<b><font size=6 face="courier">', "")
                    Respuesta = Respuesta.replace('</font></b>', "")
                    Respuesta = Respuesta.replace('<FONT class="b1">', "")
                    Respuesta = Respuesta.replace('<FONT class="b2">', "").replace('<FONT class="b3">', "").replace('<FONT class="b4">', "").replace('<FONT class="b5">', "").replace('<FONT class="b6">',"").replace('<FONT class="b7">', "")
                    Respuesta = Respuesta.replace('<PRE><FONT SIZE=2>', "")
                    Respuesta = Respuesta.replace('<TD ALIGN=RIGHT><font class="top_settings_key">', "").replace('</TD>', '').replace('</font><TD ALIGN=LEFT><font class="top_settings_val">', '').replace('<BR>', '').replace('<table cellpadding=0 cellspacing=0>', '')
                    Respuesta = Respuesta.replace('<BR><table cellpadding=0 cellspacing=0><TR>', '').replace('<TR>','').replace('</TR>', '').replace('<font class="top_settings_val">', '').replace('</font>', '').replace('</FONT>', '').replace('<TD ALIGN=LEFT COLSPAN=8><TD ALIGN=LEFT COLSPAN=8></TABLE></FORM>','').replace('\n\n', '')
                    Respuesta = Respuesta.split("\n")


                    # Separa los valores del estado actual de las llamadas y agentes conectados
                    try:
                        Respuesta.pop(len(Respuesta) - 2)
                        for index in range(0, len(Respuesta)):
                            Respuesta[index] = str(Respuesta[index]).strip()

                            if Respuesta[index] == "" or Respuesta[index] == None:
                                Respuesta.pop(index)
                    except:
                        pass

                    PrimeraTabla = Respuesta[0]
                    Respuesta.pop(0)

                    # Separamos la primera tabla en cada ":" para extraer los datos de Vicidial
                    PrimeraTabla = PrimeraTabla.split(":")
                    nivelMarcado = str(PrimeraTabla[1]).strip().split(" ")[0]
                    troncoCortaFIll = str(PrimeraTabla[2]).strip().split(" ")[0]
                    filtro = str(PrimeraTabla[3]).strip().split(" ")[0]
                    registrosMarcables = str(PrimeraTabla[7]).strip().split(" ")[0]
                    llamadasHoy = str(PrimeraTabla[8]).strip().split(" ")[0]
                    agentesAVG = str(PrimeraTabla[9]).strip().split(" ")[0]
                    metodoMarcado = str(PrimeraTabla[10]).strip().split(" ")[0]
                    hopper = str(PrimeraTabla[11]).strip().split(" ")[0]
                    caidoContestado = str(PrimeraTabla[12]).strip().split(" ")[0]
                    dlDif = str(PrimeraTabla[13]).strip().split(" ")[0]
                    estados = str(PrimeraTabla[14]).strip().split("<a")[0].strip()
                    registrosHopper = str(PrimeraTabla[15]).strip().split(" ")[0]
                    porcentajePerdidas = str(PrimeraTabla[16]).strip().split(" ")[0]
                    dif = str(PrimeraTabla[17]).strip().split(" ")[0]
                    orden = str(PrimeraTabla[18]).strip().split(" ")[0]

                    Comprobar = False

                    if "NO LLAMADA REALES DE ESPERA"  in str(Respuesta) or "NO LIVE CALLS WAITING" in str(Respuesta) or "AGENTES SIN LLAMADAS"  in str(Respuesta) or "NO AGENTS ON CALLS" in str(Respuesta):
                        Comprobar = False
                    else:
                        Comprobar = True


                    if Comprobar == True:

                        SegundaTabla = Respuesta
                        # separa cada uno de los datos obtenidos y deja solo el primer elemento con el dato solicitado
                        for index in range(0, len(SegundaTabla)):
                            SegundaTabla[index] = str(SegundaTabla[index]).split(" ")[0]

                        # Asigna cada valor del estado actual de los asesores y llamadas a las variables correspondientes
                        llamadasQueColocan = str(SegundaTabla[0]).strip()
                        llamadasTimbrando = str(SegundaTabla[1]).strip()
                        llamadasEsperaAgente = str(SegundaTabla[2]).strip()
                        llamadasEnIVR = str(SegundaTabla[3]).strip()
                        agentesConectados = str(SegundaTabla[4]).strip()
                        agentesEnLlamada = str(SegundaTabla[5]).strip()
                        agentesEsperando = str(SegundaTabla[6]).strip()
                        agentesPausados = str(SegundaTabla[7]).strip()
                        agentesLlamadasMuertas = str(SegundaTabla[8]).strip()
                        agentesEnTIP = str(SegundaTabla[9]).strip()

                    elif Comprobar == False:



                        llamadasQueColocan = "0"
                        llamadasTimbrando = "0"
                        llamadasEsperaAgente = "0"
                        llamadasEnIVR = "0"

                        agentesConectados = "0"
                        agentesEnLlamada = "0"
                        agentesEsperando = "0"
                        agentesPausados = "0"
                        agentesLlamadasMuertas = "0"
                        agentesEnTIP = "0"

                        if "NO LLAMADA REALES DE ESPERA" in str(Respuesta) or "NO LIVE CALLS WAITING" in str(Respuesta):

                            if "AGENTES SIN LLAMADAS"  in str(Respuesta) or "NO AGENTS ON CALLS" in str(Respuesta):
                                pass
                            else:
                                SegundaTabla = Respuesta
                                # separa cada uno de los datos obtenidos y deja solo el primer elemento con el dato solicitado
                                for index in range(0, len(SegundaTabla)):
                                    SegundaTabla[index] = str(SegundaTabla[index]).split(" ")[0]

                                agentesConectados = str(SegundaTabla[1]).strip()
                                agentesEnLlamada = str(SegundaTabla[2]).strip()
                                agentesEsperando = str(SegundaTabla[3]).strip()
                                agentesPausados = str(SegundaTabla[4]).strip()
                                agentesLlamadasMuertas = str(SegundaTabla[5]).strip()
                                agentesEnTIP = str(SegundaTabla[6]).strip()


                else:

                    return 'CREDENCIALES INVALIDAS'

            except requests.exceptions.ConnectionError as e:

                return 'CREDENCIALES INVALIDAS'

            except Exception as e:
                FuncGlobales.controlError(e)
                print(e)

            try:
                tiempo = datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
            except:
                tiempo = datetime.now().strftime("%d/%m/%y %H:%M:%S")
                print(agentesAVG)

            dataJSON = {
                "nivelMarcado": nivelMarcado,
                "troncoCortaFIll": troncoCortaFIll,
                "filtro": filtro,
                "tiempo": tiempo,
                "registrosMarcables": registrosMarcables,
                "llamadasHoy": llamadasHoy,
                "agentesAVG": agentesAVG,
                "metodoMarcado": metodoMarcado,
                "hopper": hopper,
                "caidoContestado": caidoContestado,
                "dlDif": dlDif,
                "estados": estados,
                "registrosHopper": registrosHopper,
                "porcentajePerdidas": porcentajePerdidas,
                "dif": dif,
                "orden": orden,
                "llamadasQueColocan": llamadasQueColocan,
                "llamadasTimbrando": llamadasTimbrando,
                "llamadasEsperaAgente": llamadasEsperaAgente,
                "llamadasEnIVR": llamadasEnIVR,
                "agentesConectados": agentesConectados,
                "agentesEnLlamada": agentesEnLlamada,
                "agentesEsperando": agentesEsperando,
                "agentesPausados": agentesPausados,
                "agentesLlamadasMuertas": agentesLlamadasMuertas,
                "agentesEnTIP": agentesEnTIP
            }

            print("\n", NOMBRE_BOT, ">>>", dataJSON, "\n")
            #Convierte el diccionario en un JSON string
            dataJSON = json.dumps(dataJSON)
            continuarEjecucion = True

            cancelarTarea = str(FuncPrograma.controlDetenerBot(codTarea)).strip()
            if cancelarTarea == 'DETENER':
                correcto = False
                isPaginaCargada = True
                continuarEjecucion = False
                print(NOMBRE_BOT, '>>> Bot detenido por el usuario. En validarCampana() ', getLinea())
                break
                
            if continuarEjecucion == True:
                FuncPrograma.insertarDatosTiempoReal(codTarea, dataJSON)
                retorno = FuncPrograma.controlMetodoMarcado(codTarea) #Retorna un dic
                nuevoMetodoMarcado = str(retorno['metodoMarcado']).strip()
                limiteDisponibilidadDB = retorno['disponibilidadHardLimit']
                
                #Controla el limite de disponibilidad en (adapt-hard-limit)
                if int(agentesEsperando) >= int(limiteDisponibilidadDB) and nuevoMetodoMarcado != 'RATIO':
                    nuevoMetodoMarcado = 'RATIO'
                
                print(NOMBRE_BOT, f'>>> Método marcado obtenido: {nuevoMetodoMarcado}, hard_limit obtenido: {limiteDisponibilidadDB}.')
                
                if nuevoMetodoMarcado == metodoMarcado:
                    pass
                else:
                    #Cambia el método de marcado mediante API
                    try:
                        requests.get(f"http://{ipVicidial}/vicidial/non_agent_api.php?source=test&user={usuarioVcidial}&pass={contrasenaVcidial}&function=update_campaign&campaign_id={campanaSeleccionada}&dial_method={nuevoMetodoMarcado}", verify=False)
                    except Exception as e:
                        if "Name or service not known" in str(e):
                            requests.get(f"https://{ipVicidial}/vicidial/non_agent_api.php?source=test&user={usuarioVcidial}&pass={contrasenaVcidial}&function=update_campaign&campaign_id={campanaSeleccionada}&dial_method={nuevoMetodoMarcado}", verify=False)

                    print(NOMBRE_BOT, f">>> Método de marcado cambiado a: '{nuevoMetodoMarcado}'")
                
                
                #Administrar el nivel de marcado segun la cantidad de asesores a la espera por llamada
                if nuevoMetodoMarcado == 'RATIO':
                    
                    if contador >= intervaloAdmin:
                        contador = 0
                        
                        if int(agentesEsperando) > 1:
                            
                            nuevoRatio = float(nivelMarcado) + float(0.1)
                            if nuevoRatio > float(2.5):
                                nuevoRatio = float(2.5)
                                
                            nuevoRatio = round(nuevoRatio, 1)
                            if float(nuevoRatio) == float(nivelMarcado):
                                pass
                            else:
                                try:
                                    requests.get(f"http://{ipVicidial}/vicidial/non_agent_api.php?source=test&user={usuarioVcidial}&pass={contrasenaVcidial}&function=update_campaign&campaign_id={campanaSeleccionada}&auto_dial_level={nuevoRatio}", verify=False)
                                except Exception as e:
                                    if "Name or service not known" in str(e):
                                        requests.get(f"https://{ipVicidial}/vicidial/non_agent_api.php?source=test&user={usuarioVcidial}&pass={contrasenaVcidial}&function=update_campaign&campaign_id={campanaSeleccionada}&auto_dial_level={nuevoRatio}", verify=False)
                                # driver.switch_to.window(driver.window_handles[1])
                        
                        elif int(agentesEsperando) <=1:
                            nuevoRatio = float(nivelMarcado) - float(0.1)
                            if nuevoRatio < 1:
                                nuevoRatio = 1
                            
                            nuevoRatio = round(nuevoRatio, 1)
                            if float(nuevoRatio) == float(nivelMarcado):
                                pass
                            else:
                                try:
                                    requests.get(f'http://{ipVicidial}/vicidial/non_agent_api.php?source=test&user={usuarioVcidial}&pass={contrasenaVcidial}&function=update_campaign&campaign_id={campanaSeleccionada}&auto_dial_level={nuevoRatio}', verify=False)
                                except Exception as e:
                                    if "Name or service not known" in str(e):
                                        requests.get(f'https://{ipVicidial}/vicidial/non_agent_api.php?source=test&user={usuarioVcidial}&pass={contrasenaVcidial}&function=update_campaign&campaign_id={campanaSeleccionada}&auto_dial_level={nuevoRatio}', verify=False)
                                # driver.switch_to.window(driver.window_handles[1])
                    else:
                        contador = contador + 1
                        time.sleep(1)  
                        
        except Exception as e:
                continuarEjecucion = False
                FuncGlobales.controlError(e)
                time.sleep(2)
                #time.sleep(int(TiempoEspera))
                print(e, getLinea())

def iniciarPrograma():
    
    #global TiempoEspera
    #global driver

    #variable while principal
    continuarPrincipal = True
    #variable códifo interno de while principal
    continuarEjecucion = True
    
    while continuarPrincipal == True: #While (1) - principal
        continuarPrincipal=False
        try:
            ''' tiempoEspera = FuncPrograma.controlParametrosPrograma(0)
            time.sleep(int(tiempoEspera)) '''
            
            time.sleep(2)
            
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            connectionMySQL.autocommit(True)
            with connectionMySQL.cursor() as cursor:
                
                ''' 1. Trae credenciales insertadas por Node en BD para loguearse '''
                sql = f"SELECT PKBOT_NCODIGO, BOT_CDETALLE2, BOT_CDETALLE3, BOT_CDETALLE4 FROM {BD_QUERY}.tbl_rbots WHERE BOT_CDETALLE = '{NOMBRE_BOT}' AND BOT_CDETALLE1 = '0' AND BOT_CESTADO = '{ESTADO_REGISTRO}'"
                print(sql)
                print(NOMBRE_BOT, '>>> Obteniendo credenciales...')
                cursor.execute(sql)
                rows = cursor.fetchall()

                
                if len(rows) > 0:
                    for row in rows:
                        COD_TAREA = row['PKBOT_NCODIGO']
                        IP_VCIDIAL = row['BOT_CDETALLE2']
                        USUARIO_VCIDIAL = row['BOT_CDETALLE3']
                        CONTRASENA_VCIDIAL = row['BOT_CDETALLE4']
                        continuarEjecucion = True
                        break

                ''' 2. Ejecuta chrome driver '''
                if continuarEjecucion == True:
                    print(NOMBRE_BOT, '>>> Ejecutando Hilo Bot...')
                    Respuesta = ""
                    #Cambiamos a una peticion Http
                    try:
                        Respuesta = requests.get(f"http://" + str(USUARIO_VCIDIAL) + ":" + str(CONTRASENA_VCIDIAL) + "@" + str(IP_VCIDIAL) + "/vicidial/admin.php", verify=False)
                    except Exception as e:
                        if "Name or service not known" in str(e):
                            Respuesta = requests.get(f"https://" + str(USUARIO_VCIDIAL) + ":" + str(CONTRASENA_VCIDIAL) + "@" + str(IP_VCIDIAL) + "/vicidial/admin.php", verify=False)

                    if Respuesta.status_code == 200:
                        continuarEjecucion = True
                    else:
                        continuarEjecucion = False

                ''' 3. Inicia sesión en página y trae el listado de campañas'''
                if continuarEjecucion == True:
                    campanasDisponibles = obtenerListaCampanas(COD_TAREA, IP_VCIDIAL, USUARIO_VCIDIAL, CONTRASENA_VCIDIAL)

                    if (campanasDisponibles == 'CREDENCIALES INVALIDAS'):
                        ''' 3.1. Setea "CREDENCIALES INVALIDAS" en la BD / Setea el bot en "2" y finaliza el proceso. Si Node quiere reingresar con el bot, debe sobre escribir el registro en BD'''
                        sql = f"UPDATE {BD_QUERY}.tbl_rbots SET BOT_CDETALLE1 = '2', BOT_CDETALLE7 = 'CREDENCIALES INVALIDAS' WHERE PKBOT_NCODIGO = '{COD_TAREA}' AND BOT_CESTADO = '{ESTADO_REGISTRO}'"
                        #print(sql)
                        print(NOMBRE_BOT, '>>> Crendenciales invalidas...')
                        cursor.execute(sql)
                        connectionMySQL.commit()
                        continuarEjecucion = False
                    
                    elif(campanasDisponibles == 0):
                        ''' 3.2. Setea "SIN CAMPANAS" en la BD / Setea el bot en "2" y finaliza el proceso. Si Node quiere reingresar con el bot, debe sobre escribir el registro en BD                        '''
                        sql = f"UPDATE {BD_QUERY}.tbl_rbots SET BOT_CDETALLE1 = '2', BOT_CDETALLE7 = 'SIN CAMPANAS' WHERE PKBOT_NCODIGO = '{COD_TAREA}' AND BOT_CESTADO = '{ESTADO_REGISTRO}'"
                        #print(sql)
                        print(NOMBRE_BOT, '>>> Crendenciales invalidas...')
                        cursor.execute(sql)
                        connectionMySQL.commit()
                        continuarEjecucion = False
                        
                        # Cierre del driver actual
                        driver.quit()
            
                    elif (campanasDisponibles != '') or (campanasDisponibles != None):
                        ''' 3.3. Guarda el listado de campañas en la BD '''
                        sql = f"UPDATE {BD_QUERY}.tbl_rbots SET BOT_CDETALLE5 = '{campanasDisponibles}' WHERE PKBOT_NCODIGO = '{COD_TAREA}' AND BOT_CESTADO = '{ESTADO_REGISTRO}'"
                        #print(sql)
                        print(NOMBRE_BOT, '>>> Guardando listado de campañas en la BD...')
                        cursor.execute(sql)
                        connectionMySQL.commit()
                        continuarEjecucion = True
                            
                ''' 4. Setea el bot en 3'''
                if continuarEjecucion == True:
                    sql = f"UPDATE {BD_QUERY}.tbl_rbots SET BOT_CDETALLE1 = '3' WHERE BOT_NCONSULTA = '{CONSULTA_REGISTRO}' AND BOT_CDETALLE = '{NOMBRE_BOT}' AND BOT_CESTADO = '{ESTADO_REGISTRO}'"
                    cursor.execute(sql)
                    connectionMySQL.commit()
                    if cursor.rowcount > 0:
                        #Update correcto, seteado en 3
                        print(NOMBRE_BOT, '>>> Bot actualizado con estado 3 en BD (Activo y con tareas)')
                        continuarEjecucion = True
                    else:
                        print(NOMBRE_BOT, 'XXX No se pudo activar el bot a estado 3')
                        continuarEjecucion = False
                        
                ''' 5. El bot queda a la espera de la selección de una campaña '''
                if continuarEjecucion == True:
                    isCampanaSeleccionada = False #¿Está la campaña seleccionada?
                    continuarEjecucion = False
                    ejecutablePrograma = FuncGlobales.obtenerRutas()['ejecutablePrograma']
                    tiempoEspera = 0
                    
                    while isCampanaSeleccionada == False: #while (1.1)
                        #time.sleep(int(tiempoEspera))
                        time.sleep(2)
                        #tiempoEspera = FuncPrograma.controlParametrosPrograma(1)
                        
                        #Si tiempo de espera es mayor a 60 
                        tiempoEspera = tiempoEspera + 2
                        
                        ''' 5.1. Si se demora más de 60 segundos, se cierra el bot y se elimina de la BD '''
                        if(tiempoEspera > 60):
                            #Borrar registro y cerrar el bot
                            cancelarTarea = FuncPrograma.controlDetenerBot(COD_TAREA)
                            sql = f"DELETE FROM {BD_QUERY}.tbl_rbots WHERE PKBOT_NCODIGO = '{COD_TAREA}' AND BOT_CDETALLE = '{NOMBRE_BOT}' AND BOT_CESTADO = '{ESTADO_REGISTRO}' ORDER BY PKBOT_NCODIGO ASC;"
                            cursor.execute(sql)
                            connectionMySQL.commit()
                            
                            continuarEjecucion = False
                            continuarPrincipal = False
                            print(NOMBRE_BOT, '>>> Tiempo de espera agotado, bot cerrado')
                            break
                        
                        sql = f"SELECT BOT_CDETALLE6 FROM {BD_QUERY}.tbl_rbots WHERE PKBOT_NCODIGO = '{COD_TAREA}' AND BOT_NCONSULTA = '{CONSULTA_REGISTRO}' AND BOT_CDETALLE = '{NOMBRE_BOT}' AND BOT_CDETALLE5 IS NOT NULL AND BOT_CESTADO = '{ESTADO_REGISTRO}' ORDER BY PKBOT_NCODIGO ASC;"
                        print(NOMBRE_BOT, '>>> Esperando a que se seleccione una campaña...')
                        #print(sql)
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        if len(rows) > 0:
                            for row in rows:
                                campanaSeleccionada = row['BOT_CDETALLE6']
                                
                                if (campanaSeleccionada != '') and (campanaSeleccionada != None):
                                    isCampanaSeleccionada = True
                                    continuarEjecucion = True
                                    print(NOMBRE_BOT, '>>> Campana seleccionada => ', campanaSeleccionada)
                                else:
                                    isCampanaSeleccionada = False
                                break
                            
                        cancelarTarea = FuncPrograma.controlDetenerBot(COD_TAREA)
                        if cancelarTarea == 'DETENER':
                            print(NOMBRE_BOT, '>>> Bot detenido por el usuario.', 'En iniciarPrograma() ' + getLinea())
                            continuarEjecucion = False
                            continuarPrincipal = False
                            break
                            
                ''' 6. Valida campaña? Baja los datos de campaña?'''
                if continuarEjecucion == True:
                    validarCampana(IP_VCIDIAL, USUARIO_VCIDIAL, CONTRASENA_VCIDIAL, campanaSeleccionada, COD_TAREA)
                    
        except pymysql.InternalError as InternalError:
            code, message = InternalError.args
            print(">>>>>>>>>>>>>", code, message)
            Comprobar = "Error Consulta SQL2: " + str(code) + ", " + str(message)

        except pymysql.DatabaseError as DBError:
            print(">>>>>>>>>>>>>", DBError)
            Comprobar = "Error Consulta SQL2: " + str(DBError)

        except pymysql.MySQLError as MySQLError:
            print('Got error {!r}, errno is {}'.format(MySQLError, MySQLError.args[0]))
            Comprobar = "Error Consulta SQL2: " + MySQLError

        except Exception as e:
            #Imprime en archivo log
            FuncGlobales.controlError(e)
            #print(str(e), str(getLinea()))


#print(FuncGlobales.Encrypt('172.70.7.23'))
#exit()
iniciarPrograma()