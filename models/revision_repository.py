
class RevisionRepository:

    def __init__(self):

        self.revisiones = []

    def guardar(self, revision):

        self.revisiones.append(revision)

    def listar(self):

        return self.revisiones

    def buscar_por_id(self, id):

        for revision in self.revisiones:

            if revision.id == id:
                return revision

        return None