from tkinter import*

# Ventana Principal
root = Tk()
root.title('Login Usuario')

# Main Frame
mainFrame = Frame(root)
mainFrame.pack()
mainFrame.config(width=480, height=320, bg='lightblue')

titulo = Label(mainFrame,text='Login User', font=('Arial', 32))
titulo.grid(column=0, row=0, padx=10, columnspan=2)

# Textos y titulos
nombreLabel = Label(mainFrame, text='Nombre: ')
nombreLabel.grid(column=0, row=1)
passLabel = Label(mainFrame, text='Contraseña: ')
passLabel.grid(column=0, row=2)

# Entradas
nombreUsuario = StringVar()
nombreEntry = Entry(mainFrame, textvariable=nombreUsuario)
nombreEntry.grid(column=1, row=1)

root.mainloop()