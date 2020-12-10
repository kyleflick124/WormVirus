import socket
import os
import requests
import json

def cpfile():
    file = open("recv-"+ cliente[0] +".txt", "wb")
    recvData = con.recv(8192)
    while recvData:
        file.write(recvData)
        recvData = con.recv(8192)
    file.close()
    print('Arquivo recebido!')

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    ptext = json.loads(text)
    print('')
    print('-----INFO-----')
    print('CIDADE:', ptext['city'])
    print('ESTADO:', ptext['regionName'])
    print('PAIS:', ptext['country'])
    print('PROVEDOR:', ptext['isp'])
    print('EMPRESA:', ptext['org'])
    print('IP:', ptext['query'])
    print('---------------')
    print('')

HOST = ###    INSIRA O IP DO HOST AQUI    ###    # Endereco IP do Servidor
PORT = ###   INSIRA A PORTA DO HOST AQUI   ###    # Porta que o Servidor está
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen()

while True:
    con, cliente = tcp.accept()
    print('')
    print('Conectado por', cliente[0])
    resp = requests.get('http://ip-api.com/json/'+ cliente[0] +'?fields=country,regionName,city,isp,org,query')
    jprint(resp.json())

    msg = 'oi'
    while msg != 'exit':
        msg = input()
        con.send(str.encode(msg))

    cpfile()
        
    print('Finalizando conexao com', cliente[0])
    con.close()
