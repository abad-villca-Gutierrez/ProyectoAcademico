
import pytest

from models.revision import Revision
from models.estado_revision import EstadoRevision
from models.revision_repository import RevisionRepository
from models.revision_review_service import RevisionReviewService


def test_deberia_aprobar_revision():

    repository = RevisionRepository()

    revision = Revision(
        1,
        "API",
        "Nuevo endpoint"
    )

    repository.guardar(revision)

    service = RevisionReviewService(repository)

    service.aprobar_revision(1)

    assert revision.estado == EstadoRevision.APROBADA


def test_deberia_rechazar_revision():

    repository = RevisionRepository()

    revision = Revision(
        1,
        "UI",
        "Cambio dashboard"
    )

    repository.guardar(revision)

    service = RevisionReviewService(repository)

    service.rechazar_revision(1)

    assert revision.estado == EstadoRevision.RECHAZADA


def test_no_deberia_procesar_dos_veces():

    repository = RevisionRepository()

    revision = Revision(
        1,
        "Security",
        "Fix auth"
    )

    repository.guardar(revision)

    service = RevisionReviewService(repository)

    service.aprobar_revision(1)

    with pytest.raises(ValueError):

        service.aprobar_revision(1)