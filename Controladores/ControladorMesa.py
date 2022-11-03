from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato

class ControladorMesa():
    def __init__(self):
        print(" Controlador Mesa Funcionando OK")
        self.repositorioMesa = RepositorioMesa()

    def index(self):
        print("Listar todos las Mesas")
        return self.repositorioMesa.findAll()

    def create(self, infoMesa):
        print("Crear una Mesa")
        laMesa = Mesa(infoMesa)
        return self.repositorioMesa.save(laMesa)

    def show(self, id):
        print("Mostrando una Mesa con id ", id)
        laMesa = Mesa(self.repositorioMesa.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
        print("Actualizando Mesa con id ", id)
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        mesaActual.numeromesa = infoMesa["numeromesa"]
        mesaActual.cedulasinscritas = infoMesa["cedulasinscritas"]
        return self.repositorioMesa.save(mesaActual)

    def delete(self, id):
        print("Elimiando Mesa con id ", id)
        return self.repositorioMesa.delete(id)


    def asignarCandidato(self, id, idCandidato):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        candidatoActual = Candidato(self.repositorioCandidato.findById(idCandidato))
        mesaActual.candidato = candidatoActual
        return self.repositorioMesa.save(mesaActual)


