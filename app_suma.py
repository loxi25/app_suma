# Se importa la libreria tkinter con todas sus funciones
from tkinter import *

# -----------------------------
# Funciones de la app
# -----------------------------


# -----------------------------
# Ventana principal de la app
# -----------------------------

# Se declara una variable llamada ventana principal,que adquiere las caracteristicas de un objeto de tipo Tk()
ventana_principal = Tk()

# Titulo de la ventana
ventana_principal.title("oscar sanchez")

# Tamaño de la ventana
ventana_principal.geometry("800x500")  

# Deshabilitar boton maximizar de la ventana
ventana_principal.resizable(0,0)

# Color de fondo de la pantalla
ventana_principal.config(bg="black")

#-----------------
#variables globales 
#-----------------

a = StringVar()
b = StringVar()
c = IntVar()




# -----------------------------
# Frame 1
# -----------------------------

frame_1 = Frame(ventana_principal)
frame_1.config(bg="ivory", width=780, height=240)
frame_1.place(x=10, y=10)


# etiqueta para el titulo de la app
titulo = Label(frame_1, text="colegio san jose de guanenta")
titulo.config(bg="yellow", fg= "blue",font=("arial", 6 ))
titulo.place(x=390,y=10)

# imagen (logo de la app)
logo = PhotoImage(file="image/btn-suma.png")
label_logo = Label(frame_1, image=logo)
label_logo.place(x=10,y = 10)

# etiqueta para subtitulo 1 de la app
subtitulo1 = Label(frame_1 , text= "especialidad en sistemas ")
subtitulo1.config(bg="yellow",fg ="blue" , font=("Arial",12)  )
subtitulo1.place(x = 390,y=40)

# etiqueta para subtitulo 2 de la app
subtitulo2 = Label(frame_1, text =" suma de dos enteros  " )
subtitulo2.config(bg="ivory2" , fg="blue", font=("arial", 15), anchor = CENTER   )
subtitulo2.place(x = 390 , y = 70)


# etiqueta para el primer valor - A
label_a = Label(frame_1, text ="a " )
label_a.config(bg="ivory2" , fg="blue", font=("arial", 20), anchor = CENTER   )
label_a.place(x = 390 , y = 120)

    # entry para el primer valor 

entry_a = Entry(frame_1, width=4 , textvariable = a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x = 487 , y = 120)


label_b = Label(frame_1, text =" b  " )
label_b.config(bg="ivory2" , fg="blue", font=("arial", 20), anchor = CENTER   )
label_b.place(x = 585 , y = 120)

    # entry para el segundo valor 
    
entry_b = Entry(frame_1, width=4 , textvariable = a)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.focus_set()
entry_b.place(x = 682 , y = 120)
# -----------------------------
# Frame 2
# -----------------------------

frame_2 = Frame(ventana_principal)
frame_2.config(bg="ivory2", width=780, height=120)
frame_2.place(x=10, y=260)


# boton para sumar
bt_sumar = Button(frame_2, text="sumar ", width=10)


# -----------------------------
# Frame 3
# -----------------------------


frame_3= Frame(ventana_principal)
frame_3.config(bg="ivory2", width=780, height=120)
frame_3.place(x=10, y=390)


# Metodo principal que despliega la ventana en pantalla
ventana_principal.mainloop()