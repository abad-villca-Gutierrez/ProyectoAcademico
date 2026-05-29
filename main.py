
from models.revision_repository import RevisionRepository
from models.revision_service import RevisionService
from models.revision_review_service import RevisionReviewService


repository = RevisionRepository()

revision_service = RevisionService(repository)

review_service = RevisionReviewService(repository)


revision_service.registrar_revision(
    "Corrección Login",
    "Se corrigió autenticación"
)

revision_service.registrar_revision(
    "Cambio UI",
    "Nuevo dashboard"
)


review_service.aprobar_revision(1)

review_service.rechazar_revision(2)


for revision in repository.listar():

    print("ID:", revision.id)
    print("Título:", revision.titulo)
    print("Descripción:", revision.descripcion)
    print("Estado:", revision.estado.value)
    print("----------------------")