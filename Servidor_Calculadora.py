import socket
class Calculadora:
    def __init__(self,n1,n2):
        self.sumar=n1+n2
        self.restar=n1-n2
        self.multiplicar=n1*n2
        try:
            self.dividir=n1/n2
        except ZeroDivisionError:
            print('\n!ADVERTENCIA¡ \nNo podra realizar la Division de: '+str(n1)+'/'+str(n2))
            conn.sendall('''No se puede desarrollar la division debido a que denominador es: 0'''.encode())
            conn.close()

numero_mensaje = 0
num=0
num2=0



HOST='127.0.0.1'
PORT= 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()
print('Servidor encendido, esperando conexiones....')

conn, addr =s.accept()
print('Conexion establecida desde: ', addr)

while True:
    try:
        if numero_mensaje == 0:
            conn.sendall('''\nHola este servidor dispone una calculadora simple para realizar operaciones basicas en matematicas como:\n\n CALCULADORA\n1.SUMA\n2.RESTA\n3.MULTIPLICACION\n4.DIVISION\n5.SALIR\n\n Asi que si deseas realizar alguna de estas operaciones solo debes ingresar el numeral correspondiente de dicha operacion: '''.encode())
            numero_mensaje=1
            data =int(conn.recv(1024).decode())
        if not data:
            break
        print('Mensaje recibido del cliente: ',data)

        if (data>=1) and (data<=4):
            print('Es un numero')
            if (data>=1) and (data<=5):
                conn.sendall('Digite un numero: '.encode())
                num= int(conn.recv(1024).decode())
                print('(Mensaje recibido del Cliente): ',num)

                conn.sendall('Digite otro numero: '.encode())
                num2=int(conn.recv(1024).decode())
                print('(Mensaje recibido del Cliente): ',num2)

                operar=Calculadora(num,num2)
            if data == 5:
                print('Salir')
                conn.sendall('SALIR!'.encode())
                conn.close()
                break
        try:
            if num2 != 0:
                opc = data
                diccionario = {1: operar.sumar, 2: operar.restar, 3: operar.multiplicar, 4: operar.dividir}


        except ValueError:
                print("Se ingreso un valor no valido!")

        try:
            diccionario[opc]

            if opc == 1:
                print('El resultado de: ' + str(num) + ' + ' + str(num2) + ' = ' + str(operar.sumar))
                resul=operar.sumar
                resul=str(resul)
                conn.sendall(('El resultado de la suma es: '+resul).encode())
                conn.close()
                break

            elif opc == 2:
                print('El resultado de: ' + str(num) + ' - ' + str(num2) + ' = ' + str(operar.restar))
                resul = operar.restar
                resul = str(resul)
                conn.sendall(('La resta es: ' + resul).encode())
                conn.close()
                break
            elif opc == 3:
                print('El resultado de: ' + str(num) + ' x ' + str(num2) + ' = ' + str(operar.multiplicar))
                resul = operar.multiplicar
                resul = str(resul)
                conn.sendall(('El resultado de la multiplicacion es: ' + resul).encode())
                conn.close()
                break
            elif opc == 4:
                    print('El resultado de: ' + str(num) + ' / ' + str(num2) + ' = ' + str(operar.dividir))
                    resul = operar.division
                    resul = str(resul)
            conn.sendall(('El resultado de la division es: ' + resul).encode())
            conn.close()
            break
        except:
                print('No se puede desarrollar la operacion!')

    except:
        print("Tipo dato no valido")
        conn.sendall('Esta introduciendo un valor no valido '.encode())
        conn.close()
    break

