from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://equipo1:56789@cluster0.j1sapjk.mongodb.net/bd-votacion-registraduria?retryWrites=true&w=majority",tlsCAFile=ca)

db = client.test
print("hola mundo¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")

baseDatos = client["bd-votacion-registraduria"]
print(baseDatos.list_collection_names())


@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":"+str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])