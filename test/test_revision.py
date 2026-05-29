from models.revision import Revision
from models.estado_revision import EstadoRevision


def test_toda_revision_nueva_inicia_pendiente():

    revision = Revision(
        1,
        "Bug Login",
        "Corrección autenticación"
    )

    assert revision.estado == EstadoRevision.PENDIENTE