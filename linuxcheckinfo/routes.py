import os, time
import json
import requests
import distro, socket
import netifaces as net_ifaces
from datetime import datetime
from flask import Flask, request, render_template, jsonify
from app import app


datetime_now_str = str(datetime.now())
datetime = datetime_now_str

distro_linux_info = distro.linux_distribution(full_distribution_name=False)
hostname = socket.gethostname()
ip_local_address = socket.gethostbyname(hostname)

socket_inet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_connect = socket_inet.connect(("8.8.8.8", 80))
ip_inet_addr = socket_inet.getsockname()[0]



@app.route('/', methods=["GET", "POST"])
@app.route('/home/', methods=["GET", "POST"])
def home():
#    if request.method == 'GET':
    print('Bienvenido al Servidor de Pruebas!')
    print('datetime ', datetime)
    print('distro_linux_info ', distro_linux_info)
    print('hostname ', hostname)
    #print('ip_local_address ', ip_local_address)
    print('ip_inet_addr ', ip_inet_addr)
    #return render_template('templates/home.html', datetime=datetime, distro_linux_info=distro_linux_info, hostname=hostname, ip_local_address=ip_local_address, ip_inet_addr=ip_inet_addr)
    #return 'Fecha y hora' + datetime + '\n', 'Distro ' + distro_linux_info + '\n', 'Hostname ' + hostname + '\n', 'IP Local ' + ip_local_address + '\n', 'IP Publica' + ip_inet_addr + '\n'
    #return 'Fecha y hora' + datetime + '\n' + 'Distro ' + distro_linux_info + '\n'
    #json_data = {'testing_server': 'Servidor de Pruebas', 'datetime': datetime, 'distro_linux_info': distro_linux_info, 'hostname': hostname, 'ip_inet_addr': ip_inet_addr}
    #print(json_data)
    #return json.dumps(json_data)
    json_data = jsonify({'testing_server': 'Servidor de Pruebas', 'datetime': datetime, 'distro_linux_info': distro_linux_info, 'hostname': hostname, 'ip_inet_addr': ip_inet_addr})
    return json_data


#@app.route('/home_index/', methods=["GET", "POST"])
#def home_index():
#    return render_template('templates/home_index.html')


####--------------------------------------------------------------------------------------------------------------
## curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://127.0.0.7:5007//api/home/info
####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
@app.route('/api/home/info', methods=["GET"])
def api_home():
    if request.method == 'GET':
       print('Bienvenido al Servidor de Pruebas!')
       print('datetime ', datetime)
       print('distro_linux_info ', distro_linux_info)
       print('hostname ', hostname)
       print('ip_local_address ', ip_local_address)
       print('ip_inet_addr ', ip_inet_addr)
       json_data = {'testing_server': 'Servidor de Pruebas', 'datetime': datetime, 'distro_linux_info': distro_linux_info, 'hostname': hostname, 'ip_local_address': ip_local_address, 'ip_inet_addr': ip_inet_addr}
       print(json_data)
       return json.dumps(json_data)
    else:
       json_message = {'Error': 'Request Error!', 'Message': 'Method Not Allowed!'}
       return json.dumps(json_message)


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------


####--------------------------------------------------------------------------------------------------------------
####--------------------------------------------------------------------------------------------------------------
