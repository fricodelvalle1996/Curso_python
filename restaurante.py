from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = '' #almacena la cantidad de numeros que se vayan presionando en la calculadora
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero): #función para pulsado de botones en la calculadora
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END) #sirve para evitar que al pulsar un boton, se imprima en pantalla ese boton y todos los anteriores pulsados (sin usar esto si pulsamos 1, 2 y 3 se imprimiría 112123)
    visor_calculadora.insert(END, operador) #insertar desde el fin de la calculadora la variable operador


def borrar(): #función para borrar en la calculadora
    global operador #para eliminar lo que había antes
    operador = '' #para eliminar lo que había antes
    visor_calculadora.delete(0, END)


def obtener_resultado(): #para calcular el resultado total de la calculadora
    global operador
    resultado = str(eval(operador)) #evalúa una cadena de texto que contiene una expresión o instrucción válida de Python y devuelve el resultado de esa evaluación. Básicamente, toma una cadena y la interpreta como código Python, realizando los cálculos o ejecutando las instrucciones correspondientes. eval nos da un integer que pasamos a string
    visor_calculadora.delete(0, END) #eliminamos lo que hay en el visor
    visor_calculadora.insert(0, resultado) #agregamos el resultado
    operador = '' #reseteamos el string de las operaciones


def revisar_check(): #revisa si los checks están activados para establecer el estado del cuadro de comida (activado o bloqueado)
    x = 0 #contador para contar los indices de cada una de las listas de comida
    for c in cuadros_comida:
        if variables_comida[x].get() == 1: #en cada check revisa si está activado (ya que al estar activado devuelve el valor 1)
            cuadros_comida[x].config(state=NORMAL) #el cuadro de comida correspondiente pasa a estar activo
            if cuadros_comida[x].get() == '0': #SE FIJA SI EL VALOR ES 0 (no si el checkbox está activo o no)
                cuadros_comida[x].delete(0, END) #elimina el 0 cuando activamos alguna comida
            cuadros_comida[x].focus() #focus sirve para poner el cursor enfocado en ese elemento en particular
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0') #para que vuelva al estado inicial cuando desmarcamos el checkbox
        x += 1 #para que funcione el loop

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def total():
    sub_total_comida = 0 #totales de las comidas
    p = 0 #contador para el loop
    for cantidad in texto_comida: #texto_comida almacena la cantidad de cada comida que se ha marcado
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p]) #cantidad es una variable de tipo StringVar, hay que transformarla
        p += 1 #para que funcione el loop

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres #suma de subtotales
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}') #imprimimos los valores obtenidos a través de la función en su cuadro correspondiente. Se redondean los valores a 2 decimales
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo(): #generamos el ticket
    texto_recibo.delete(1.0, END) #borramos tickets anteriores
    num_recibo = f'N# - {random.randint(1000, 9999)}' #numero de recibo aleatorio
    fecha = datetime.datetime.now() #fecha actual
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}' #cadena string con la fecha actual
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n') #insertamos al final
    texto_recibo.insert(END, f'*' * 47 + '\n') #línea separadora
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n') #encabezados
    texto_recibo.insert(END, f'-' * 54 + '\n') #línea separadora

    x = 0 #contador del loop
    for comida in texto_comida:
        if comida.get() != '0': #se comprueba si el numero de cada comida es DIFERENTE a 0
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t' #insertamos la comida consumida y el número de items
                                     f'$ {int(comida.get()) * precios_comida[x]}\n') #multiplicacion del precio por unidades
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                     f'$ {int(postres.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n') #línea separadora
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n') #subtotal de la comida
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n') #subtotal de la bebida
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costo_postres.get()}\n') #subtotal de los postres
    texto_recibo.insert(END, f'-' * 54 + '\n') #línea separadora
    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Le esperamos pronto')


def guardar(): #el recibo o ticket se guarda en un archivo de texto en el pc
    info_recibo = texto_recibo.get(1.0, END) #obtenemos el contenido desde el principio (1.0) hasta el final (END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt') #Estamos pidiendo que se guarde como un archivo. Modo "w" es modo de escritura. defaultextension es la extesion del archivo (txt)
    archivo.write(info_recibo) #escribimos en el archivo todo el texto del recibo
    archivo.close() #cerramos
    messagebox.showinfo('Información', 'Su recibo se ha guardado') #texto informativo


def resetear(): #reseteamos toda la máquina para "atender a un nuevo cliente" y generar otro ticket
    texto_recibo.delete(0.1, END) #texto del recibo

    for texto in texto_comida: #las unidades de las comidas seleccionadas vuelven a 0
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida: #los cuadros de las unidades de las comidas seleccionadas vuelven a estar desactivados
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida: #desactivamos los checkboxes
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    var_costo_comida.set('') #vaciamos los costes acumulados
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1020x630+0+0') #TAMAÑO+UBICACION(X)+UBICACION(Y)

# evitar maximizar
aplicacion.resizable(0, 0) #También se puede poner (False, False)

# titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturación")

# color de fondo de la ventana
aplicacion.config(bg='burlywood') #bg es background, el color se selecciona mediante el sistema RGB o mediante sus "nombres" (https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Los_nombres_de_los_colores)

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT) #relief es relieve (puede ser flat, raised, sunken, groove, ridge) y bd es el grosor del borde
panel_superior.pack(side=TOP) #lanzamos el panel dentro de la habitación

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4', #fg es es el color de las letras (FOREGROUND)
                        font=('Dosis', 58), bg='burlywood', width=27) #width es el ancho de la etiqueta
etiqueta_titulo.grid(row=0, column=0) #grid es cuadrícula. Seleccionamos la columna y fila en la que aparece

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50) #con el bg le damos un color de fondo gris y con el padx lo extendemos por los laterales
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'), #es un LabelFrame (un cuadro que viene con la etiqueta incorporada)
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo', 'coredero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# generar items comida
variables_comida = [] #Se crea esta lista para asignar los valores de los checkbuttons a cada variable
cuadros_comida = [] #vamos a agregar cuadros donde se contabilice cuantas unidades se pide de cada producto
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crear checkbutton
    variables_comida.append('') #le agregamos un elemento vació a la lista por cada elemento de la lista de comidas
    variables_comida[contador] = IntVar() #transformamos cada elemento en un integer
    comida = Checkbutton(panel_comidas, #creamos los checkbuttons dentro del panel de comidas
                         text=comida.title(), #Hace la primera letra de cada elemento de la lista mayúscula
                         font=('Dosis', 19, 'bold',),
                         onvalue=1, #valor cuando el checkbutton está activado
                         offvalue=0, #valor cuando el checkbutton está desactivado
                         variable=variables_comida[contador], #estamos creando las variables donde se almacenan los estados de los checkbuttons
                         command=revisar_check) #implementamos la función revisar check para los checkbuttons

    comida.grid(row=contador,
                column=0,
                sticky=W) #texto justificado en el lado izquierdo

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar() #la convertimos en una variable de tipo string
    texto_comida[contador].set('0') #establecemos que su valor por defecto sea 0
    cuadros_comida[contador] = Entry(panel_comidas, #cuadro de entrada. Ubicado en el panel comidas
                                     font=('Dosis', 18, 'bold'),
                                     bd=1, #borde
                                     width=6, #ancho
                                     state=DISABLED, #ESTADO. Desactivado (hasta que se active el checkbox)
                                     textvariable=texto_comida[contador]) #asociado a su comida correspondiente
    cuadros_comida[contador].grid(row=contador, #ubicado al lado del checkbox
                                  column=1)
    contador += 1 #necesario para que funcione el loop

# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    # crear checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador],
                         command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    contador += 1


# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar() #
var_impuestos = StringVar() #
var_total = StringVar() #

# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4', #background
                              fg='white') #foreground
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly', #solo lectura
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41) #padx es la separación

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postres = Label(panel_costos,
                              text='Costo Postres',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = [] #para ubicarlos en diferentes columnas

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white', #color de frente (letra)
                   bg='azure4', #color de fondo
                   bd=1, #borde
                   width=9) #ancho del botón

    botones_creados.append(boton)

    boton.grid(row=0, #lo ubicamos en la cuadrícula
               column=columnas)
    columnas += 1 #necesario para que funcione el loop y trabaje con todos los botones

botones_creados[0].config(command=total) #asignamos las funciones creadas para cada botón a cada botón
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10) #altura de texto (?)
texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32, #ancho de la calculadora
                          bd=1) #borde
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4) #ancho de la columna (o ampliación de la columna)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = [] #Lista donde vamos almacenando los botones con el loop

fila = 1 #para hacer un loop (la fila 0 ya está ocupada por el visor)
columna = 0 #para crear columnas de la 1 a la 3 en un loop
for boton in botones_calculadora: #creamos el loop para ahorrar líneas de código
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8) #Ancho de cada botón

    botones_guardados.append(boton) #guardamos el botón creado con el loop

    boton.grid(row=fila,
               column=columna)

    if columna == 3: #estos loops son para cuadrar la calculadora (#C)
        fila += 1 #C

    columna += 1 #C

    if columna == 4: #C
        columna = 0 #C

botones_guardados[0].config(command=lambda : click_boton('7')) #Permite asignar una función a un evento específico, como hacer clic en un botón. Cuando se produce el evento, la función especificada se ejecuta. Por ejemplo, al usar boton.config(command=funcion) se asocia la función funcion al evento de clic en el botón.
botones_guardados[1].config(command=lambda : click_boton('8')) #"command" se utiliza para asignar una función existente a un evento de un widget, mientras que "lambda" se utiliza para crear una función anónima rápida y simple que se ejecutará en el evento especificado.
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))



# evitar que la pantalla se cierre
aplicacion.mainloop()
