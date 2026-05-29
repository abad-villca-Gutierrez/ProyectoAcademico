
from models.estado_revision import EstadoRevision


class Revision:

    def __init__(
            self,
            id,
            titulo,
            descripcion
    ):

        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = EstadoRevision.PENDIENTE

    