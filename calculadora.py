from tkinter import *
raiz=Tk()
miframe=Frame(raiz)
miframe.pack()
operacion=""
resultado=0
#-----PANTALLA-----
numeropantalla=StringVar()
pantalla=Entry(miframe, textvariable=numeropantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#48a259", justify="right")
#-------------pulsa botones de teclado*------------
def numeropulsado(num):
	global operacion
	if operacion!="":
		numeropantalla.set(num)
		operacion=""
	else:
		numeropantalla.set(numeropantalla.get()+num)
#------Función suma------
def suma(num):
	global operacion
	global resultado
	resultado+=int(num) #operación de incremento+=: resultado=resultado+int(num)
	operacion="suma"
	numeropantalla.set(resultado)
#------------función el resultado
def elresultado():
	global resultado
	numeropantalla.set(resultado+int(numeropantalla.get()))
	resultado=0
#-----------Fila1-----
button7=Button(miframe, text="7", width=3, command=lambda:numeropulsado("7"))
button7.grid(row=2,column=1)
button8=Button(miframe, text="8", width=3, command=lambda:numeropulsado("8"))
button8.grid(row=2,column=2)
button9=Button(miframe, text="9", width=3, command=lambda:numeropulsado("9"))
button9.grid(row=2,column=3)
buttondiv=Button(miframe, text="/", width=3)
buttondiv.grid(row=2,column=4)

#-----------Fila2------
button4=Button(miframe, text="4", width=3, command=lambda:numeropulsado("4"))
button4.grid(row=3,column=1)
button5=Button(miframe, text="5", width=3, command=lambda:numeropulsado("5"))
button5.grid(row=3,column=2)
button6=Button(miframe, text="6", width=3, command=lambda:numeropulsado("6"))
button6.grid(row=3,column=3)
buttonmult=Button(miframe, text="*", width=3)
buttonmult.grid(row=3,column=4)

#-----------Fila3------
button1=Button(miframe, text="1", width=3, command=lambda:numeropulsado("1"))
button1.grid(row=4,column=1)
button2=Button(miframe, text="2", width=3, command=lambda:numeropulsado("2"))
button2.grid(row=4,column=2)
button3=Button(miframe, text="3", width=3, command=lambda:numeropulsado("3"))
button3.grid(row=4,column=3)
buttonmenos=Button(miframe, text="-", width=3)
buttonmenos.grid(row=4,column=4)

#-----------Fila4------
button0=Button(miframe, text="0", width=3, command=lambda:numeropulsado("0"))
button0.grid(row=5,column=1)
buttonpunto=Button(miframe, text=".", width=3, command=lambda:numeropulsado("."))
buttonpunto.grid(row=5,column=2)
buttonigual=Button(miframe, text="=", width=3, command=lambda:elresultado())
buttonigual.grid(row=5,column=3)
buttonmas=Button(miframe, text="+", width=3, command=lambda:suma(numeropantalla.get()))
buttonmas.grid(row=5,column=4)


raiz.mainloop()