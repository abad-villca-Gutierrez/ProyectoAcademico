
class RevisionReviewService:

    def __init__(self, repository):

        self.repository = repository

    def aprobar_revision(self, id):

        revision = self.repository.buscar_por_id(id)

        revision.aprobar()

    def rechazar_revision(self, id):

        revision = self.repository.buscar_por_id(id)

        revision.rechazar()