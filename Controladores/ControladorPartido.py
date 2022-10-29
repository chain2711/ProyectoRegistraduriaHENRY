from Repositorios.RepositorioPartido import RepositorioPartido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Partido import Partido
from Modelos.Candidato import Candidato


class ControladorPartido():
    def __init__(self):
        print("Creando ControladorPartido")
        self.repositorioPartido = RepositorioPartido()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        print("Listar todas los partidos")
        return self.repositorioPartido.findAll()

    def create(self,infoPartido,idCandidato):
        print("Crear un partido")
        nuevoPartido = Partido(infoPartido)
        elCandidato = Candidato(self.repositorioCandidato.findById(idCandidato))
        nuevoPartido.candidato = elCandidato
        return self.repositorioPartido.save(nuevoPartido)

    def show(self,id):
        print("Mostrando partido con id ", id)
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido,idCandidato):
        print("Actualizando partido con id ", id)
        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        elCandidato = Candidato(self.repositorioCandidato.findById(idCandidato))
        partidoActual.candidato = elCandidato
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        print("Elimiando partido con id ", id)
        return self.repositorioPartido.delete(id)

    def asignarCandidato(self,id,idCandidato):
        partidoActual = Partido(self.repositorioPartido.findById(id))
        CandidatoActual = Candidato(self.repositorioCandidato.findById(idCandidato))
        partidoActual.candidato = CandidatoActual
        return self.repositorioPartido.save(partidoActual)
