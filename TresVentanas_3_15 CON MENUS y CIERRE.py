import PySimpleGUI as sg
from os import path





SETTINGS_FILE1 = path.join(path.dirname(__file__), r'MeteoSensors.cfg') # Nombre del archivo de configuracion de sensores 
SETTINGS_FILE2 = path.join(path.dirname(__file__), r'MeteoComm.cfg')    # Nombre del archivo de configuracion de comunicaciones
#SETTINGS_FILE3 = path.join(path.dirname(__file__), r'MeteoData.cfg')   # Expansion futura, Nombre del archivo de configuracion de almacenamiento



DEFAULT_SETTINGS = { 'user_data_folder': None , 'theme': sg.theme(), }
Settings = DEFAULT_SETTINGS
# "Map" from the settings dictionary keys to the window's element keys
SETTINGS_KEYS_TO_ELEMENT_KEYS = { 'Directorio': '-USER FOLDER-' , 'theme': '-THEME-'}



## Variables booleanas, representando los sensores usados,
## True sensor se usa / False sensor no se usa
## Se acceden desde todo el firmware

BM280 = False
SEN1591 = False
VEML6030 = False
SI1145 = False
SPS30 = False
MQ7 = False
SCD30 = False
CCS811 = False
AS3935 = False
LORATXRX = False
Geiger = False


# construye la primera ventana
def make_window1():
     layout = [[sg.Menu(menu_def, background_color='lightsteelblue',text_color='navy', disabled_text_color='yellow', font='Verdana', pad=(10,10))],
              [sg.Text('Inicio'), sg.Text('      ', k='-OUTPUT-')],
              [sg.Text(size=(80,40), k='-OUTPUT2-')],
              [sg.Button('Configurar_sensores'), sg.Button('Configurar_COMM'), sg.Button('Exit')]]
     return sg.Window('Primera Ventana', layout, finalize=True)


#SE DEFINE EL MENU
menu_def=['&Config', ['&Sensores', '&Comm']],


# construye la segunda ventana, conf sensores
def make_window2():
     layout = [[sg.Text(SETTINGS_FILE1)],
              # [sg.Input(key=SETTINGS_FILE1, enable_events=True)],
              #[sg.Text(key=SETTINGS_FILE1, enable_events=True)], 
              [sg.Checkbox('BM280', key='BM280', enable_events=True)],
              [sg.Checkbox('SEN15901', key='SEN1591', enable_events=True)],
              [sg.Checkbox('VEML6030', key='VEML6030', enable_events=True)],
              [sg.Checkbox('SI1145', key='SI1145', enable_events=True)],
              [sg.Checkbox('SPS30', key='SPS30', enable_events=True)],
              [sg.Checkbox('MQ7', key='MQ7', enable_events=True)],
              [sg.Checkbox('SCD30', key='SCD30', enable_events=True)],
              [sg.Checkbox('CCS811', key='CCS811', enable_events=True)],
              [sg.Checkbox('AS3935', key='AS3935', enable_events=True)],
              [sg.Checkbox('LORATXRX', key='LORATXRX', enable_events=True)],
              [sg.Checkbox('Geiger', key='Geiger', enable_events=True)],
              [sg.Button('Inicio'),sg.Button('Configurar_COMM'),sg.Button('Grabar_CFGS'), sg.Button('Exit')]]  
     return sg.Window('Segunda ventana', layout, finalize=True)


# construye la tercera ventana conf comunicaciones
def make_window3():
      layout = [[sg.Text(SETTINGS_FILE2)],
               [sg.Checkbox('WIFI')],
               [sg.Checkbox('Network')],
               [sg.Checkbox('bluethoot')],
               [sg.Checkbox('RS232')],
               [sg.Checkbox('LORA')],
               [sg.Checkbox('OTRO')],
               [sg.Button('Inicio'),sg.Button('Configurar_sensores'),sg.Button('Grabar_CFGC'), sg.Button('Exit')]]
      return sg.Window('Tercera ventana', layout, finalize=True)


window1, window2, window3 = make_window1(), None, None


# lee el archivo de texto de configuracion de sensores
def read_settings_file_sensors (SETTINGS_FILE1):
     F = open(SETTINGS_FILE1, mode="r")
     countS = 0
     while(True):
          #read next line
          lineS = F.readline()
          #if line is empty, you are done with all lines in the file
          if not lineS:
             break
          #you can access the line
          # print(lineS.strip())
          countS +=1
          if lineS.find("True") != -1 : 
              if countS == 1 :
                   BM280=True
                   window2['BM280'].Update (value = True)
              if countS == 2 :
                   SEN1591 = True
                   window2['SEN1591'].Update (value = True)
              if countS == 3 :
                   VEML6030 = True
                   window2['VEML6030'].Update (value = True)
              if countS == 4 :
                   SI1145 = True
                   window2['SI1145'].Update (value = True)
              if countS == 5 :
                   SPS30 = True
                   window2['SPS30'].Update (value = True)
              if countS == 6 :
                   MQ7 = True
                   window2['MQ7'].Update (value = True)
              if countS == 7 :
                   SCD30 = True
                   window2['SCD30'].Update (value = True)
              if countS == 8 :
                   CCS811 = True
                   window2['CCS811'].Update (value = True)
              if countS == 9 :
                   AS3935 = True
                   window2['AS3935'].Update (value = True)
              if countS == 10 :
                   LORATXRX = True
                   window2['LORATXRX'].Update (value = True)
              if countS == 11 :
                   Geiger = True
                   window2['Geiger'].Update (value = True)
 
     F.close
     # print(countS, "lineas leidas")      


# Guarda el archivo conf de sensores
def save_settings_file_sensors (SETTINGS_FILE1):
      F = open(SETTINGS_FILE1, mode="w")
      if BM280==True: 
          F.write("BM280, True \r")
      else :
          F.write("BM280, False \r")

      if SEN1591 == True:
          F.write("SEN1591, True \r")
      else:
          F.write("SEN1591, False \r")

      if VEML6030 == True:
          F.write("VEML6030, True \r")
      else:
          F.write("VEML6030, False \r")

      if SI1145 == True:
          F.write("SI1145, True \r")
      else:
          F.write("SI1145, False \r")

      if SPS30 == True:
          F.write("SPS30, True \r")
      else:
          F.write("SPS30, False \r")

      if  MQ7 == True:
          F.write("MQ7, True \r")
      else:
          F.write("MQ7, False \r")

      if  SCD30 == True:
          F.write("SCD30, True \r")
      else:
          F.write("SCD30, False \r")

      if  CCS811 == True:
          F.write("CCS811, True \r")
      else:
          F.write("CCS811, False \r")

      if  AS3935 == True:
          F.write("AS3935, True \r")
      else:
          F.write("AS3935, False \r")

      if LORATXRX == True:
          F.write("LORATXRX, True \r")
      else:
          F.write("LORATXRX, False \r")

      if Geiger == True:
          F.write("Geiger, True \r")
      else:
          F.write("Geiger, False \r")

      F.close







     

# bucle principal, lee eventos de los controles y reacciona.

while True:
    window, event, values = sg.read_all_windows()

    if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
        window1.close()

    if window == window2 and event in (sg.WIN_CLOSED, 'Exit'):
        window2.close()

    if window == window3 and event in (sg.WIN_CLOSED, 'Exit'):
        window3.close()


    if window == window1:
	#SE COMPRUEBAN LOS EVENTOS DE LOS MENUS
        if event == 'Sensores':
            window2 = make_window2()

        elif event == 'Comm':
            window2 = make_window3()

	#SE COMPRUEBAN LOS EVENTOS DE LOS BOTONES
        if event == 'Configurar_sensores':
            window1.hide()
            window2 = make_window2()
            read_settings_file_sensors (SETTINGS_FILE1)

        elif event == 'Configurar_COMM':
            window1.hide()
            window3 = make_window3()

        elif event == 'Exit':
            window1.close()


    if window == window2:
        if event == 'Configurar_COMM':
            window2.hide()
            window3 = make_window3()

        elif event == 'Inicio':
            window2.hide()
            window1.un_hide()

        elif event == 'Grabar_CFGS':
           save_settings_file_sensors (SETTINGS_FILE1)

        elif event == 'BM280':
           BM280=(window2['BM280'].get())

        elif event == 'SEN1591':
           SEN1591= (window2['SEN1591'].get())

        elif event == 'VEML6030':
           VEML6030= window2['VEML6030'].get()

        elif event == 'SI1145':
           SI1145= window2['SI1145'].get()

        elif event == 'SPS30':
           SPS30=window2['SPS30'].get()

        elif event == 'MQ7':
           MQ7 = window2['MQ7'].get()

        elif event == 'SCD30':
           SCD30= window2['SCD30'].get()

        elif event == 'CCS811':
           CCS811= window2['CCS811'].get()

        elif event == 'AS3935':
           AS3935= window2['AS3935'].get()

        elif event == 'LORATXRX':
           LORATXRX= window2['LORATXRX'].get()

        elif event == 'Geiger':
           Geiger= window2['Geiger'].get()

        elif event == 'Exit':
            window2.close()


    if window == window3:
        if event == 'Inicio':
            window3.hide()
            window1.un_hide()

        if event == 'Configurar_sensores':
            window3.hide()
            window2 = make_window2()
            read_settings_file_sensors (SETTINGS_FILE1)

        elif event == 'Inicio':
            window3.hide()
            window1.un_hide()

        elif event == 'Exit':
            window3.close()

        

window.close()

# termina

