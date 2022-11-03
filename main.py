from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorMesa import ControladorMesa
app = Flask(__name__)
cors = CORS(app)
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")
        self.repositorioPartido = RepositorioPartido()
        """self.repositorioCandidato = RepositorioCandidato()"""

    def index(self):
        print("Listar todas los partidos")
        return self.repositorioPartido.findAll()

    def create(self,infoPartido):
        print("Crear un partido")
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self,id):
        print("Mostrando partido con id ", id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        print("Actualizando partido con id ", id)
        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        print("Elimiando partido con id ", id)
        return self.repositorioPartido.delete(id)

    """
    def asignarCandidato(self,id,idCandidato):
        partidoActual = Partido(self.repositorioPartido.findById(id))
        CandidatoActual = Candidato(self.repositorioCandidato.findById(idCandidato))
        partidoActual.candidato = CandidatoActual
        return self.repositorioPartido.save(partidoActual)
    """