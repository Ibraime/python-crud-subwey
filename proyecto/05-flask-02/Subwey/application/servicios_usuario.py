# application/servicio_usuario.py

class ServicioUsuario:
    """
    Servicio de usuarios.

    Actúa como capa intermedia entre la presentación
    y el repositorio de usuarios.

    Encapsula la lógica de negocio relacionada con usuarios.
    """

    def __init__(self, repo):
        """
        Inicializa el servicio con un repositorio.

        :param repo: Repositorio de usuarios.
        """
        self._repo = repo

    def listar_usuarios(self):
        """
        Obtiene todos los usuarios registrados.

        :return: Lista de objetos Usuario.
        """
        return self._repo.listar()

    def crear_usuario(self, nombre):
        """
        Crea un nuevo usuario en el sistema.

        :param nombre: Nombre del usuario.
        """
        self._repo.crear(nombre)

    def eliminar_usuario(self, nombre):
        """
        Elimina un usuario del sistema.

        :param nombre: Nombre del usuario a eliminar.
        """
        self._repo.eliminar(nombre)

    def actualizar_usuario(self, antiguo_nombre, nuevo_nombre):
        """
        Actualiza el nombre de un usuario existente.

        :param antiguo_nombre: Nombre actual del usuario.
        :param nuevo_nombre: Nuevo nombre a asignar.
        """
        self._repo.actualizar(antiguo_nombre, nuevo_nombre)