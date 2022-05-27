import time
import paramiko
from getpass import getpass

#12345678
HOST = "127.0.0.1" #Direccion ip del servidor al que me quiero conectar, en nuestro caso una ip equivalente a localhost
#HOST = "255.255.255.0"
USER = "prueba" #Username con el que me voy a conectar

if __name__ == "__main__":
    client = paramiko.SSHClient() #Creo el cliente con el que me voy a conectar
    client.set_missing_host_key_policy( paramiko.AutoAddPolicy() )#Le indica a paramiko que vamos a ingresar al servidor usando 
                                                                  #nuestras propias credenciales (es decir, las que se le dan al client)
                                                                  #A su vez, esto le da al cliente una clave de verificacion para asegurarse de que
                                                                  #nuestro cliente es con el que nos queremos conectar y ningun otro con objetivos maliciosos
                                                                  #Esto tiene la funcion de aumentar la seguridad, y en un servidor privado, es muy posible
                                                                  #que el no usar esta clave de verificacion, prohiba el ingreso del cliente al servidor
                                                                  #como es el caso de los servidores con openssh (nuestro caso)

    password = getpass ("Ingrese su contraseña: ") #Le pide al usuario que ingrese su contraseña
    client.connect(HOST, port=2200, username=USER, password=password) #Carga los datos con los que se conecta el cliente al servidor

    sftp_client = client.open_sftp() #abro un intercambio de archivos (secure file transfer protocol)
    
    sftp_client.put( #digo que archivos quiero cargar al servidor poniendo
        "", #el path del archivo local que quiero enviar
        "" #Y el path de a donde lo quiero mandar en el servidor (recordar poner el /nombre_del_archivo)
    )
    sftp_client.get( #Digo que archivos quiero descargar del servidor poniendo
        "", #El path del archivo a descargar del servidor
        "" #El path de a donde quiero enviar el archivo en mi pc (recordar poner el /nombre_del_archivo)
    )

    stdin, stout, sterr = client.exec_command("echo hola") #Hago que el cliente ejecute el comando ls, dando como resultado un stdin, 
                                                    # stout y sterr

    time.sleep(1)

    result = stout.read().decode() #Fija al resultado como el standar output del comando, lo hace legible, y lo transforma en un string 

    print (result) #muestra el stout, del ls, es decir, result

    client.close #cierro la conexion 
