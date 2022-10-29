from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido

from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato


class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        print("Listar todas los partidos")
        return self.repositorioPartido.findAll()

    def create(self,elPartido):
        print("Crear un partido")
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self,id):
        print("Mostrando partido con id ", id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return  elPartido.__dict__

    def update(self, id, elPartido):
        print("Actualizando el partido con id ", id)
        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        print("Elimiando partido con id ", id)
        return self.repositorioPartido.delete(id)

    def asignarCandidato(self,id,id_candidato):
        partidoActual = Partido(self.repositorioPartido.findById(id))
        CandidatoActual = Candidato(self.repositorioCandidato.findById(id_candidato))
        partidoActual.candidato = candidatoActual
        return self.repositorioPartido.save(partidoActual)