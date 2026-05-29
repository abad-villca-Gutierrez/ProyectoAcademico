

from models.revision import Revision


class RevisionService:

    def __init__(self, repository):

        self.repository = repository
        self.id_actual = 1

   

    def obtener_revisiones(self):

        return self.repository.listar()