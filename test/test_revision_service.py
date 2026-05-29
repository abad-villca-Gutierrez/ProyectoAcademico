
import pytest

from models.revision_service import RevisionService
from models.revision_repository import RevisionRepository


def test_deberia_registrar_revision():

    repository = RevisionRepository()

    service = RevisionService(repository)

    service.registrar_revision(
        "Corrección Login",
        "Se corrigió autenticación"
    )

    assert len(repository.listar()) == 1


def test_no_deberia_registrar_sin_titulo():

    repository = RevisionRepository()

    service = RevisionService(repository)

    with pytest.raises(ValueError):

        service.registrar_revision(
            "",
            "Descripción válida"
        )


def test_no_deberia_registrar_sin_descripcion():

    repository = RevisionRepository()

    service = RevisionService(repository)

    with pytest.raises(ValueError):

        service.registrar_revision(
            "Título válido",
            ""
        )