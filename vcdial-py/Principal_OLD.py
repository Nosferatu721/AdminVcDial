import base64
import codecs
import os
from posixpath import dirname
import sys
import datetime
import csv
import subprocess
import random
import string
import time
import pymysql
import shutil
import json
import requests


# Credenciales Database
IP_SERVIDOR = '41785A3245774C6D41775232446D4C3441784C335A6D7030'#localhost: 41785A3245774C6D41775232446D4C3441784C335A6D7030 #site7: 5A6D526D416D5A6C5A7A486D416D5A6A5A7A486D416D57795A6D566D5A6A3D3D
USUARIO_SERVIDOR = '41775A324D77706D414A4C325A6D706C417A443D'
CONTRASENA_SERVIDOR = '417770324147706D416D443242474D7A417A4832416D4C31417A48324147706C417752324C6D4C6D417A4C335A6D41755A6D566D5A515A6C5A6D4E3D'
BD_SERVIDOR = '417744325A77706A41484C3341774C35416D56334151703141775232446D703241775A3241514C3541775232446A3D3D'

#Constantes globales
NOMBRE_BOT = str(sys.argv[1]).strip()
print(NOMBRE_BOT)

class FuncGlobales():
        
    def Encrypt(O0OO00OOOOOOOO00O):
        if O0OO00OOOOOOOO00O.strip() == '' or O0OO00OOOOOOOO00O.strip() == None:
            return 'Error'
        O0OO00OOOOOOOO00O = str(O0OO00OOOOOOOO00O.strip())
        try:
            O0OO00OOOOOOOO00O = ''.join(hex(ord(O0O00O0O000OO000O))[2:] for O0O00O0O000OO000O in O0OO00OOOOOOOO00O)
        except:
            return 'Error'
        O0OO00OOOOOOOO00O = O0OO00OOOOOOOO00O.upper()
        try:
            O0OO00OOOOOOOO00O = base64.b64encode(O0OO00OOOOOOOO00O.encode(
                str(''.join([chr(int(''.join(c), 16)) for c in zip('7574662D38'[0::2], '7574662D38'[1::2])]))))
            O0OO00OOOOOOOO00O = str(O0OO00OOOOOOOO00O, str(
                ''.join([chr(int(''.join(c), 16)) for c in zip('7574662D38'[0::2], '7574662D38'[1::2])])))
            O0OO00OOOOOOOO00O = codecs.encode(O0OO00OOOOOOOO00O, str(
                ''.join([chr(int(''.join(c), 16)) for c in zip('726F745F3133'[0::2], '726F745F3133'[1::2])])))
        except:
            return 'Error'
        try:
            O0OO00OOOOOOOO00O = ''.join(
                hex(ord(OOO00000OOOO00OO0))[2:] for OOO00000OOOO00OO0 in O0OO00OOOOOOOO00O)  # line:21
        except:
            return 'Error'
        O0OO00OOOOOOOO00O = O0OO00OOOOOOOO00O.upper()
        O0OO00OOOOOOOO00O = str(O0OO00OOOOOOOO00O.strip())
        return O0OO00OOOOOOOO00O
    
    def DeCrypt(OOOOOOOO000000OO0):
        if OOOOOOOO000000OO0.strip() == '' or OOOOOOOO000000OO0.strip() == None:
            return 'Error'
        OOOOOOOO000000OO0 = str(OOOOOOOO000000OO0.strip())
        try:
            OOOOOOOO000000OO0 = ''.join([chr(int(''.join(O0O000000O0O00O00), 16)) for O0O000000O0O00O00 in
                                         zip(OOOOOOOO000000OO0[0::2], OOOOOOOO000000OO0[1::2])])
        except:
            return 'Error'
        try:
            OOOOOOOO000000OO0 = codecs.decode(OOOOOOOO000000OO0, str(
                ''.join([chr(int(''.join(c), 16)) for c in zip('726F745F3133'[0::2], '726F745F3133'[1::2])])))
        except:
            return 'Error'
        try:
            OOOOOOOO000000OO0 = OOOOOOOO000000OO0.encode(
                str(''.join([chr(int(''.join(c), 16)) for c in zip('6173636969'[0::2], '6173636969'[1::2])])))
            OOOOOOOO000000OO0 = base64.b64decode(OOOOOOOO000000OO0)
            OOOOOOOO000000OO0 = OOOOOOOO000000OO0.decode(
                str(''.join([chr(int(''.join(c), 16)) for c in zip('6173636969'[0::2], '6173636969'[1::2])])))
        except:
            return 'Error'
        try:
            OOOOOOOO000000OO0 = ''.join([chr(int(''.join(OO0O0O0OOOO0O0000), 16)) for OO0O0O0OOOO0O0000 in
                                         zip(OOOOOOOO000000OO0[0::2], OOOOOOOO000000OO0[1::2])])
        except:
            return 'Error'
        OOOOOOOO000000OO0 = str(OOOOOOOO000000OO0.strip())
        return OOOOOOOO000000OO0

    #Obtener linea del script
    def getLinea():
        return sys._getframe(1).f_lineno

    def obtenerRutas():

        #ruta de este archivo .py, incluyendo el nombre de este archivo
        ejecutablePrograma = str(os.path.realpath(sys.argv[0]))
        #ruta contenedora de este archivo .py
        rutaEjecutablePrograma = str(os.path.dirname(os.path.realpath(sys.argv[0])))

        return {"ejecutablePrograma": ejecutablePrograma, "rutaEjecutablePrograma": rutaEjecutablePrograma}

    def WLog(Data):
        rutaEjecutablePrograma = FuncGlobales.obtenerRutas()['rutaEjecutablePrograma']
        try:
            fechaActual = datetime.datetime.now().strftime("%d%m%y")
        except:
            fechaActual = datetime.now().strftime("%d%m%y")

        if not os.path.exists(str(os.path.join(rutaEjecutablePrograma, "Log"))):
            os.makedirs(str(os.path.join(rutaEjecutablePrograma, "Log")))

        Archivo = str(os.path.join(rutaEjecutablePrograma, "Log", "Log_Error_" + str(fechaActual).strip() + ".txt"))
        File_Exist = os.path.isfile(Archivo)
        Comprobar = "FALSE"
        if File_Exist == True:
            #os.remove(Archivo)
            Comprobar = "OK"
        elif File_Exist == False:
            #os.mkdir(path)
            Comprobar = "OK"
        else:
            Comprobar = "FALSE"

        if Comprobar == "OK":
            try:
                Array = []
                myData = [str(Data)]
                Array.append(myData)
                myFile = open(Archivo, 'a+', newline='', encoding="utf-8")
                with myFile:
                    writer = csv.writer(myFile, delimiter=";")
                    writer.writerows(Array)
                myFile.close()
                return 1
            except Exception as e:
                FuncGlobales.controlError(e)
    
    def controlError(e):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        try:
            fechaActual = datetime.datetime.now().strftime("%d/%m/%y  %H:%M")
        except:
            fechaActual = datetime.now().strftime("%d/%m/%y  %H:%M")
        Data = f"{fechaActual} - {e} - {exc_type} - {fname} - Line: {exc_tb.tb_lineno}"
        FuncGlobales.WLog(Data)
        # SE GUARDA REGISTRO EN LA BASE DE DATOS
        try:
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            connectionMySQL.autocommit(True)
            with connectionMySQL.cursor() as cursor:
                BDquery = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
                ESTADO_REGISTRO = 'Activo'
                CONSULTA_REGISTRO = 'ControlInicioBot'
                sql = f'UPDATE {BDquery}.tbl_rbots SET BOT_CDETALLE20 = "{Data}" WHERE BOT_NCONSULTA = "{CONSULTA_REGISTRO}" AND BOT_CDETALLE = "{NOMBRE_BOT}" AND BOT_CESTADO = "{ESTADO_REGISTRO}"'
                print(sql)
                cursor.execute(sql)

                connectionMySQL.commit()   
                print(NOMBRE_BOT, '>>> Update de error en base de datos')
        except print('No se pudo realizar el update del error en la base de datos', f'Linea: {exc_tb.tb_lineno}'):
            pass
            

class FuncPrograma():
    
    def indicarAutenticando(codTarea, accion):
        ESTADO_REGISTRO = "Activo"
        CONSULTA_REGISTRO = "ControlInicioBot"
        BDquery = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
        
        try:
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            connectionMySQL.autocommit(True)
            with connectionMySQL.cursor() as cursor:
                
                if accion == "Inicio":
                    sql = f"UPDATE {BDquery}.tbl_rbots SET BOT_CDETALLE7 = 'AUTENTICANDO' WHERE PKBOT_NCODIGO = '{codTarea}' AND BOT_CESTADO = '{ESTADO_REGISTRO}' AND BOT_NCONSULTA = '{CONSULTA_REGISTRO}'"
                    #print(sql)
                    print(NOMBRE_BOT, '>>> Indicando "AUTENTICANDO" en BD...')
                    cursor.execute(sql)
                    connectionMySQL.commit()
                elif accion == "Fin":
                    sql = f"UPDATE {BDquery}.tbl_rbots SET BOT_CDETALLE7 = NULL WHERE PKBOT_NCODIGO = '{codTarea}' AND BOT_CESTADO = '{ESTADO_REGISTRO}' AND BOT_NCONSULTA = '{CONSULTA_REGISTRO}'"
                    #print(sql)
                    print(NOMBRE_BOT, '>>> Autenticado.')
                    cursor.execute(sql)
                    connectionMySQL.commit()
                
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            Comprobar = "Error Consulta SQL2: " + str(code) + ", " + str(message)

        except pymysql.DatabaseError as error3:
            print(">>>>>>>>>>>>>", error3)
            Comprobar = "Error Consulta SQL2: " + str(error3)

        except pymysql.MySQLError as error4:
            print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
            Comprobar = "Error Consulta SQL2: " + error4

        except Exception as e:
            FuncGlobales.controlError(e)

        try:
            cursor.fetchall()
        except:
            pass

        try:
            connectionMySQL.close()
        except:
            pass

        #return Array
    
    def controlParametrosPrograma(estadoBot):
        
        try:    
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            with connectionMySQL.cursor() as cursor:
                ESTADO_REGISTRO = 'Activo'
                BDquery = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
                ejecutablePrograma = FuncGlobales.obtenerRutas()['ejecutablePrograma']
                
                #Se busca el tiempo de espera establecido en BD
                sql = f"SELECT EST_CDETALLE FROM {BDquery}.tbl_restandar WHERE EST_CCONSULTA = 'ControlTiempoEspera' AND EST_CESTADO = '{ESTADO_REGISTRO}' ORDER BY PKEST_NCODIGO ASC LIMIT 1;"
                cursor.execute(sql)
                rows = cursor.fetchall()
                if len(rows) > 0:
                    for row in rows:
                        tiempoEspera = row['EST_CDETALLE']
                        break
                
                ''' Envio ping vivo '''
                #Se busca el id del ControlTiempoActivo (si no existe se crea en else)
                sql = f"SELECT PKEST_NCODIGO FROM {BDquery}.tbl_restandar WHERE EST_CCONSULTA = 'ControlTiempoActivo' AND EST_CDETALLE = '{ejecutablePrograma}' AND EST_CESTADO = '{ESTADO_REGISTRO}' ORDER BY PKEST_NCODIGO ASC LIMIT 1;"
                print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                if len(rows) >= 1:
                    
                    for row in rows:
                        #global RegistroPing
                        registroPing = row['PKEST_NCODIGO']
                        break
                    
                    sql = f"UPDATE {BDquery}.tbl_restandar SET EST_CDETALLE1 = '{estadoBot}' WHERE PKEST_NCODIGO = '{registroPing}'"
                    print(sql)
                    cursor.execute(sql)
                    connectionMySQL.commit()
                else:
                    sql = f"INSERT INTO {BDquery}.tbl_restandar (EST_CCONSULTA, EST_CDETALLE, EST_CDETALLE1, EST_CDETALLE_REGISTRO, EST_CESTADO) VALUES ('ControlTiempoActivo', '{ejecutablePrograma}', '{estadoBot}', 'Registrado por el sistema', 'Activo')"
                    print(sql)
                    cursor.execute(sql)

                connectionMySQL.commit()
                        
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            Comprobar = "Error Consulta SQL2: " + str(code) + ", " + str(message)

        except pymysql.DatabaseError as error3:
            print(">>>>>>>>>>>>>", error3)
            Comprobar = "Error Consulta SQL2: " + str(error3)

        except pymysql.MySQLError as error4:
            print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
            Comprobar = "Error Consulta SQL2: " + error4


        except Exception as e:
            FuncGlobales.controlError(e)

        try:
            cursor.fetchall()
        except:
            pass

        try:
            connectionMySQL.close()
        except:
            pass

        return tiempoEspera
        
    def controlDetenerBot(codTarea):
        
        try:
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            connectionMySQL.autocommit(True)
            with connectionMySQL.cursor() as cursor:
                
                ESTADO_REGISTRO = 'Activo'
                CONSULTA_REGISTRO = 'ControlInicioBot'
                BDquery = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
                sql = f"SELECT BOT_CDETALLE7 FROM {BDquery}.tbl_rbots WHERE PKBOT_NCODIGO = '{codTarea}' AND BOT_NCONSULTA = '{CONSULTA_REGISTRO}' AND BOT_CESTADO = '{ESTADO_REGISTRO}'"
                #print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                if len(rows) > 0:
                    for row in rows:
                        cancelarTarea = row['BOT_CDETALLE7']
                        break
                else:
                    cancelarTarea = ""

                connectionMySQL.commit()

        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            Comprobar = "Error Consulta SQL2: " + str(code) + ", " + str(message)

        except pymysql.DatabaseError as error3:
            print(">>>>>>>>>>>>>", error3)
            Comprobar = "Error Consulta SQL2: " + str(error3)

        except pymysql.MySQLError as error4:
            print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
            Comprobar = "Error Consulta SQL2: " + error4

        except Exception as e:
            FuncGlobales.controlError(e)

        return cancelarTarea
    
    def controlLimpiarBase(nombreProgramaPrincipal):
        
        try:
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            connectionMySQL.autocommit(True)
            with connectionMySQL.cursor() as cursor:
                
                ESTADO_REGISTRO = 'Activo'
                CONSULTA_REGISTRO = 'ControlInicioTareas'
                BDquery = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
                sql = f"SELECT PKEST2_NCODIGO FROM {BDquery}.tbl_restandar2 WHERE EST2_CCONSULTA = '{CONSULTA_REGISTRO}' AND EST2_CDETALLE = '{nombreProgramaPrincipal}' AND EST2_CESTADO = '{ESTADO_REGISTRO}' ORDER BY PKEST2_NCODIGO ASC"
                print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                if len(rows) > 0:
                    for row in rows:
                        codTareaVieja = row['PKEST2_NCODIGO']
                        
                        sql = f"DELETE FROM {BDquery}.tbl_restandar2 WHERE (PKEST2_NCODIGO = '{codTareaVieja}')"
                        print(sql)
                        cursor.execute(sql)
                        connectionMySQL.commit()
                
                        sql = f"SELECT PKTEM_NCODIGO FROM {BDquery}.tbl_rtemporal_admin WHERE FKTEM_CPKEST2_NCODIGO = '{codTareaVieja}'"
                        print(sql)
                        cursor.execute(sql)
                        rows = cursor.fetchall()
                        if len(rows) > 0:
                            codTemporalVieja = row['PKTEM_NCODIGO']
                            
                            sql = f"DELETE FROM {BDquery}.tbl_rtemporal_admin WHERE (PKTEM_NCODIGO = '{codTemporalVieja}'"
                            print(sql)
                            cursor.execute(sql)
                            connectionMySQL.commit()
                            
                            sql = f"DELETE FROM {BDquery}.tbl_detalle_temporal_admin WHERE (FKDETTEM_NPKTEM_NCODIGO = '{codTemporalVieja}'"
                            print(sql)
                            cursor.execute(sql)
                            connectionMySQL.commit()
                            
                connectionMySQL.commit()
                
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            Comprobar = "Error Consulta SQL2: " + str(code) + ", " + str(message)

        except pymysql.DatabaseError as error3:
            print(">>>>>>>>>>>>>", error3)
            Comprobar = "Error Consulta SQL2: " + str(error3)

        except pymysql.MySQLError as error4:
            print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
            Comprobar = "Error Consulta SQL2: " + error4

        except Exception as e:
            FuncGlobales.controlError(e)

        try:
            cursor.fetchall()
        except:
            pass

        try:
            connectionMySQL.close()
        except:
            pass      
    
    def controlParametrosRatio(nombreProgramaPrincipal):
        try:
            
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            connectionMySQL.autocommit(True)
            with connectionMySQL.cursor() as cursor:
                Array = []
                BDquery = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
                ESTADO_REGISTRO = 'Activo'
                sql = f"SELECT EST_CDETALLE, EST_CDETALLE1 FROM {BDquery}.tbl_restandar WHERE EST_CCONSULTA = 'ControlRatio' AND EST_CDETALLE2 = '{nombreProgramaPrincipal} AND EST_CESTADO = {ESTADO_REGISTRO}' ORDER BY PKEST_NCODIGO"
                print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                if len(rows) > 0:
                    for row in rows:
                        rango = row['EST_CDETALLE']
                        ratio = row['EST_CDETALLE1']
                        Array.append([rango, ratio])
                else:
                    Array = []
                    CAM_GENERICAS = 'SinCampana'
                    sql = f"SELECT EST_CDETALLE, EST_CDETALLE1 FROM {BDquery}.tbl_restandar WHERE EST_CCONSULTA = 'ControlRatio' AND EST_CDETALLE2 = '{CAM_GENERICAS}' AND EST_CESTADO = '{ESTADO_REGISTRO}' ORDER BY PKEST_NCODIGO;"
                    print(sql)
                    cursor.execute(sql)
                    rows = cursor.fetchall()
                    if len(rows) > 0:
                        for row in rows:
                            rango = row['EST_CDETALLE']
                            ratio = row['EST_CDETALLE1']
                            Array.append([rango, ratio])
                    
                connectionMySQL.commit()
                
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            Comprobar = "Error Consulta SQL2: " + str(code) + ", " + str(message)

        except pymysql.DatabaseError as error3:
            print(">>>>>>>>>>>>>", error3)
            Comprobar = "Error Consulta SQL2: " + str(error3)

        except pymysql.MySQLError as error4:
            print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
            Comprobar = "Error Consulta SQL2: " + error4


        except Exception as e:
            FuncGlobales.controlError(e)

        try:
            cursor.fetchall()
        except:
            pass

        try:
            connectionMySQL.close()
        except:
            pass

        return Array

    def insertarDatosTiempoReal(codTarea, dataJSON):         
        
        #Limpieza de datos
        codTarea = str(codTarea).strip()
        dataJSON = str(dataJSON).strip()
        
        try:
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            
            with connectionMySQL.cursor() as cursor:
                BDquery = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
                ESTADO_REGISTRO = 'Activo'
                CONSULTA_REGISTRO = 'ControlInicioBot'
                
                sql = f"UPDATE {BDquery}.tbl_rbots SET BOT_CDETALLE11 = '{dataJSON}' WHERE BOT_NCONSULTA = '{CONSULTA_REGISTRO}' AND PKBOT_NCODIGO = '{codTarea}' AND BOT_CESTADO = '{ESTADO_REGISTRO}'"
                #print(sql)
                cursor.execute(sql)

                connectionMySQL.commit()   
                
                print(NOMBRE_BOT, '>>> Update correcto dataJSON')
                
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            Comprobar = "Error Consulta SQL2: " + str(code) + ", " + str(message)

        except pymysql.DatabaseError as error3:
            print(">>>>>>>>>>>>>", error3)
            Comprobar = "Error Consulta SQL2: " + str(error3)

        except pymysql.MySQLError as error4:
            print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
            Comprobar = "Error Consulta SQL2: " + error4

        except Exception as e:
            FuncGlobales.controlError(e)

        try:
            cursor.fetchall()
        except:
            pass

        try:
            connectionMySQL.close()
        except:
            pass
    
    def controlMetodoMarcado(codTarea):
        try:
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            connectionMySQL.autocommit(True)
            with connectionMySQL.cursor() as cursor:
                BDquery = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
                ESTADO_REGISTRO = 'Activo'
                CONSULTA_REGISTRO = 'ControlInicioBot'                
                sql = f"SELECT BOT_CDETALLE12, BOT_CDETALLE14 FROM {BDquery}.tbl_rbots WHERE PKBOT_NCODIGO = '{codTarea}' AND BOT_NCONSULTA = '{CONSULTA_REGISTRO}' AND BOT_CESTADO = '{ESTADO_REGISTRO}' ORDER BY PKBOT_NCODIGO ASC LIMIT 1;"
                #print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                if len(rows) > 0:
                    for row in rows:
                        metodoMarcado = row['BOT_CDETALLE12']
                        disponibilidadHardLimit = row['BOT_CDETALLE14']
                        break
                else:
                    metodoMarcado = "RATIO"
                    disponibilidadHardLimit = '5'
                    sql = f"INSERT INTO {BDquery}.tbl_rbots (BOT_CDETALLE12, BOT_CDETALLE14) VALUES ('{metodoMarcado}', '{disponibilidadHardLimit}') WHERE PKBOT_NCODIGO = '{codTarea}' AND BOT_CESTADO = '{ESTADO_REGISTRO}'"
                    print(sql)
                    cursor.execute(sql)
                
                connectionMySQL.commit()
                print(NOMBRE_BOT, '>>> Consultando método de marcado y hard_limit en la BD...')
            
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            Comprobar = "Error Consulta SQL2: " + str(code) + ", " + str(message)

        except pymysql.DatabaseError as error3:
            print(">>>>>>>>>>>>>", error3)
            Comprobar = "Error Consulta SQL2: " + str(error3)

        except pymysql.MySQLError as error4:
            print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
            Comprobar = "Error Consulta SQL2: " + error4

        except Exception as e:
            FuncGlobales.controlError(e)

        try:
            cursor.fetchall()
        except:
            pass

        try:
            connectionMySQL.close()
        except:
            pass

        return {"metodoMarcado": metodoMarcado, "disponibilidadHardLimit": disponibilidadHardLimit}

    def cambioRatio(driver, dialMethod, dialLevel):
        try:
            driver.switch_to.window(driver.window_handles[0])
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, 'dial_method')))
            Select(driver.find_element_by_name('dial_method')).select_by_visible_text(dialMethod)
            
            if DialLavel == '':
                pass
            else:
                try:
                    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, 'auto_dial_level')))
                    Select(driver.find_element_by_name('auto_dial_level')).select_by_visible_text(str(dialLevel).strip())
                except:
                    pass
            
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, 'SUBMIT')))
            driver.find_element_by_name("SUBMIT").click()
            
            carga = False
            while carga == False:
                carga = FuncGlobales.paginaCargada(driver)
                
        except Exception as e:
            FuncGlobales.controlError(e) 

    def intervaloControl(codTarea):
        try:
            connectionMySQL = pymysql.connect(host=FuncGlobales.DeCrypt(IP_SERVIDOR),user=FuncGlobales.DeCrypt(USUARIO_SERVIDOR),password=FuncGlobales.DeCrypt(CONTRASENA_SERVIDOR),db=FuncGlobales.DeCrypt(BD_SERVIDOR), charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            connectionMySQL.autocommit(True)
            with connectionMySQL.cursor() as cursor:
                BDquery = str(FuncGlobales.DeCrypt(BD_SERVIDOR)).strip()
                ESTADO_REGISTRO = 'Activo'
                CONSULTA_REGISTRO = 'ControlInicioBot'           
                sql = f"SELECT BOT_CDETALLE13 FROM {BDquery}.tbl_rbots WHERE PKBOT_NCODIGO = '{codTarea}' AND BOT_NCONSULTA = '{CONSULTA_REGISTRO}' AND BOT_CESTADO = '{ESTADO_REGISTRO}' ORDER BY PKBOT_NCODIGO ASC LIMIT 1;"
                #print(sql)
                cursor.execute(sql)
                rows = cursor.fetchall()
                if len(rows) > 0:
                    for row in rows:
                        intervaloAdmin = row['BOT_CDETALLE13']
                        break
                
                connectionMySQL.commit()
            
        except pymysql.InternalError as error:
            code, message = error.args
            print(">>>>>>>>>>>>>", code, message)
            Comprobar = "Error Consulta SQL2: " + str(code) + ", " + str(message)

        except pymysql.DatabaseError as error3:
            print(">>>>>>>>>>>>>", error3)
            Comprobar = "Error Consulta SQL2: " + str(error3)

        except pymysql.MySQLError as error4:
            print('Got error {!r}, errno is {}'.format(error4, error4.args[0]))
            Comprobar = "Error Consulta SQL2: " + error4

        except Exception as e:
            FuncGlobales.controlError(e)

        try:
            cursor.fetchall()
        except:
            pass

        try:
            connectionMySQL.close()
        except:
            pass

        return intervaloAdmin


