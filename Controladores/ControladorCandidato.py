from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido


class ControladorCandidato():
    def __init__(self):    #este es el constructor del controlador
        print("Creando Controlador Candidato")
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()



    def index(self):     #simula la información de forma de diccionario
        print("Listar todos los candidatos")
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        print("Crear un candidato")
        nuevoCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):     #id es el parámetro de entrada y retorna un diccionario con la info
        print("Mostrando un candidato con id ", id)
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):   #aquí de actualiza la info del candidato
        print("Actualizando candidato con id ", id)
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.resolucion_acreditacion = infoCandidato["resolucion_acreditacion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)

    def delete(self, id):
        print("Eliminando candidato con id ", id)
        return self.repositorioCandidato.delete(id)

    def asignarPartido(self, id, idPartido):
        print("Asignando un candidato a un partido")
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(idPartido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)


