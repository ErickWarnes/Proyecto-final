class usuario():

    numUsuarios = 0

    def __init__(self, nombre, contra):
        self.nombre = nombre
        self.contra = contra

        self.conectado = False
        self.intentos = 3

        usuario.numUsuarios+=1
    
    def conectar(self):
        myContra = input("Ingrese su contraseña: ")
        if myContra==self.contra:
            print('Se ha conectado con exito')
            self.conectado = True
        else:
            self.intentos-=1
            if self.intentos > 0:
                print('Contraseña Incorrecta, Intentelo nuevamente')
                print('Intentos Restantes', self.intentos)
                self.conectar()
            else:
                print('Error, Ha agotado sus intentos.')

    def desconectar(self):
        if self.conectado:
            print('Se cerro sesion con exito!')
            self.conectado = False
        else:
            print('Error, no inció sesion')
    
    def __str__(self):
        if self.conectado:
            conect = 'Conectado'
        else:
            conect = 'Desconectado'
        return f'{self.nombre} {conect}'

user1 = usuario(input('Ingrese Usuario: '),input('Ingrese Password: '))
print(user1)

user1.conectar()
print(user1)

user1.desconectar()
print(user1)
