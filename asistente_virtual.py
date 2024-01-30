#importamos todas las bibliotecas que vamos a utilizar
import pyttsx3 #hace que el sistema pueda hablar con nosotros
import speech_recognition as sr #SpeechRecognition. Reconoce nuestra voz y la transforma en texto. Le cambiamos el nombre para invocarlo + fácil
import pywhatkit #Permite que el sistema pueda abrir sitios como Youtube, Wikipedia, etc.
import yfinance as yf #Yahoo Finance. Nos conecta con las bolsas de acciones y con información de diferentes empresas
import pyjokes #Nos cuenta chistes
import webbrowser #maneja el navegador de internet
import datetime
import wikipedia #

#Para saber de que voces disponemos en el sistema:
#engine = pyttsx3.init()
#for voz in engine.getProperty('voices'):
#    print(voz)


# opciones de voz / idioma
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0' #no está en mi pc
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0' #no está en mi pc


# escuchar nuestro microfono y devolver el audio comotexto
def trasformar_audio_en_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera (ayuda a solucionar problemas de volumen o de sonido)
        r.pause_threshold = 0.8 #umbral de espera

        # informar que comenzó la grabación (nos ayuda como programadores a saber que ya ha empezado a grabar)
        print("Ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-es") #le metemos la fuente de audio y el idioma del locutor

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:

            # prueba de que no comprendio el audio
            print("Ups, no he entendido nada")

            # devolver error
            return "Sigo esperando"

        # en caso de no resolver el pedido (no lo puede transformar en string)
        except sr.RequestError:

            # prueba de que no resolvió el pedido
            print("Ups, no hay servicio")

            # devolver error
            return "Sigo esperando"

        # error inesperado
        except:

            # prueba de que no comprendio el audio
            print("Ups, algo ha salido mal")

            # devolver error
            return "Sigo esperando"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):

    # encender el motor de pyttsx3
    engine = pyttsx3.init() #enciende el motor. Comunmente se usa "engine" para la variable
    engine.setProperty('voice', id3)

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait() #para que el motor inicie la reproducción del discurso y se detenga hasta que se haya completado la reproducción.
    #Es importante llamar a engine.runAndWait() después de haber configurado el texto y otras propiedades, ya que garantiza que el discurso se reproducirá por completo antes de que el programa continúe ejecutándose.


# informar el dia de la semana
def pedir_dia():

    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}

    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# informar que hora es
def pedir_hora():

    # crear una variab;e con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas, {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # decir la hora
    hablar(hora)


# funcion saludo inicial
def saludo_inicial():

    # crear variable condatos de hora
    hora = datetime.datetime.now()
    if hora.hour < 5 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 5 <= hora.hour < 15:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    # decir el saludo
    hablar(f'{momento}, soy Helena, tu asistente personal. Por favor, dime en qué te puedo ayudar')


# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable de corte (para el loop)
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = trasformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Por supuesto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue #vuelve al principio del bucle sin checkear lo que viene a continuación
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en ello')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '') #queremos eliminar "busca en wikipedia" del string
            wikipedia.set_lang('es') #lenguaje de la wikipedia
            resultado = wikipedia.summary(pedido, sentences=1) #queremos que solo lea el primer párrafo de la wiki (sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('Me pongo manos a la obra')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('¡Qué temazo!, ahora mismo te lo pongo')
            pywhatkit.playonyt(pedido) #reproduce en youtube
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es')) #bromas en español
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip() # empieza a comprobar a partir de la palabra "de" (por ejemplo diremos: precio de las acciones de Tesla). -1 es para quedarnos con la última palabra que es la empresa. strip es para eliminar los espacios en blanco
            cartera = {'apple':'APPL', #esta cartera es para asociar una accion con un nombre resumido (que es por lo que se busca la accion en google)
                       'amazon':'AMZN',
                       'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion] #buscamos la empresa mediante el diccionaro creado
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice'] #así se extrae la información sobre el precio de las acciones de la empresa
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar("Perdón pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar("Me voy a descansar, cualquier cosa me avisas máquina")
            break


pedir_cosas()
