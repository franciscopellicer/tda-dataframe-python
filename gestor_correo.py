"""Modulo que alberga el segundo TDA GestorCorreo"""

from Source.correo import Correo

class GestorCorreo:
    """Clase que representa un gestor de correo que permite administrar
       las distintas bandejas que contienen correos así como gestionar
       los criterios de spam y realizar operaciones relacionadas con los correos.
        """
    #Hago la clase privada para que no se puedan instanciar un objeto de la clase bag en el main
    class _Bag:
        """Clase interna que implementa una bag para almacenar elementos
            en una estructura de lista enlazada sin importar el orden.
            """
        class Nodo:
            """Representa un nodo dentro de la bolsa que contiene un elemento y
               una referencia al siguiente nodo."""
            def __init__(self, elemento : object):
                """Inicializa un nuevo nodo con el elemento proporcionado.
                :param elemento: El elemento que almacenará el nodo."""

                self._elemento :object = elemento
                self._siguiente: "GestorCorreo._Bag.Nodo" = None

            def siguiente(self) -> "GestorCorreo._Bag.Nodo":
                """Devuelve el siguiente nodo en la lista.
                   :return: El siguiente nodo."""
                return self._siguiente

            def elemento(self)-> object:
                """Devuelve el objeto almacenado en el nodo.
                   :return: El elemento almacenado en el nodo."""
                return self._elemento

            def set_siguiente(self, siguiente: "GestorCorreo._Bag.Nodo"):
                """Establece el siguiente nodo del nodo actual.
                   :param siguiente: El siguiente nodo."""
                self._siguiente = siguiente

            def set_elemento(self, elemento:object)-> None:
                """ Establece el elemento del nodo.
                    :param elemento: El nuevo elemento a almacenar en el nodo."""
                self._elemento = elemento

        def __init__(self):
            """Inicializa la bolsa vacía con longitud 0."""
            self._primer_nodo: "GestorCorreo._Bag.Nodo" = None
            self._longitud: int = 0

        def get_primer_nodo(self) -> "GestorCorreo._Bag.Nodo":
            return self._primer_nodo

        def _set_primer_nodo(self, primer_nodo: "GestorCorreo._Bag.Nodo" )-> None:
            """Establece el primer nodo de la bolsa.
               :param primer_nodo: El nodo a establecer como primer nodo."""
            self._primer_nodo = primer_nodo

        def _set_longitud(self, longitud:int) -> None:
            """Establece la longitud de la bolsa.
               :param longitud: La longitud de la bolsa."""
            self._longitud = longitud

        def len(self) -> int:
            """Metodo que devuelve la longitud de la bolsa
               :return: La longitud de la bolsa."""
            return self._longitud

        def contains(self, elemento: object) -> bool:
            """Verifica si un elemento está contenido en la bolsa.
               :param elemento: El elemento a buscar.
               :return: True si el elemento está en la bolsa, False de lo contrario."""
            actual = self.get_primer_nodo()
            while actual is not None and actual.elemento() != elemento:
                actual = actual.siguiente()
            return actual is not None

        def add_item(self, elemento: object)->bool:
            """Metodo que añade un nuevo elemento a la bolsa.
               :param elemento: El elemento a añadir
               :return True, si se añadió correctamente ."""
            nuevo_nodo = GestorCorreo._Bag.Nodo(elemento)
            nuevo_nodo.set_siguiente(self.get_primer_nodo())
            self._set_primer_nodo(nuevo_nodo)
            self._set_longitud(self.len() + 1)
            return True

        def remove_item(self, elemento: object) -> bool:
            """Elimina un elemento de la bolsa.
               :param elemento: El elemento a eliminar.
               :return: True si el elemento fue eliminado, False si no se encontró."""
            actual = self.get_primer_nodo()
            anterior = None
            while actual is not None and actual.elemento() != elemento:
                anterior = actual
                actual = actual.siguiente()
            if actual is not None:
                if anterior is None:  # El elemento está en el primer nodo
                    self._set_primer_nodo(actual.siguiente())
                else:  # El elemento está en un nodo intermedio
                    anterior.set_siguiente(actual.siguiente())
                self._set_longitud(self.len() - 1)
                return True
            return False

        def iterator(self) -> iter:
            """Metodo que recorre todos los elementos de la bolsa.
               :return: Un iterador sobre los elementos de la bolsa."""
            actual = self.get_primer_nodo()
            while actual is not None:
                yield actual.elemento()
                actual = actual.siguiente()

    class ErrorBandejaInexistente(Exception):
        """Excepción lanzada cuando se intenta acceder a una bandeja que no existe."""
        def __init__(self, mensaje :str):
            super().__init__(mensaje)

    class ErrorCriterioRepetido(Exception):
        """Error lanzado cuando se intenta añadir un criterio que ya está en la lista de criterios de spam"""
        def __init__(self, mensaje :str):
            super().__init__(mensaje)

    class ErrorCriterioNoEncontrado(Exception):
        """Error lanzado cuando se intenta eliminar un criterio que no esta en la lista de criterios de spam"""
        def __init__(self, mensaje :str):
            super().__init__(mensaje)

    class ErrorCorreoNoEncontrado(Exception):
        """Error lanzado cuando no se encuentra un error en una carpeta específica"""
        def __init__(self, mensaje :str):
            super().__init__(mensaje)

    class ErrorParametrosIncompletos(Exception):
        """Excepción lanzada cuando los parámetros proporcionados en ciertos metodos son incompletos."""
        def __init__(self, mensaje :str):
            super().__init__(mensaje)

    class ErrorBusquedaNoValida(Exception):
        """Error lanzado cuando se intenta realizar una busqueda de correos que no se ajusta a los parametros establecidos"""
        def __init__(self, mensaje :str):
            super().__init__(mensaje)

    class ErrorContrasenyaInvalida(Exception):
        """Error lanzado cunado se intenta cambiar la contraseña por la que tienes actualmente"""
        def __init__(self, mensaje :str):
            super().__init__(mensaje)

    class ErrorDestinatarioNoValido(Exception):
        """Error lanzado cunado se intenta enviar un correo a un objeto que no es de tipo GestorCorreo"""
        def __init__(self, mensaje :str):
            super().__init__(mensaje)

    def __init__(self, usuario: str , contrasenya : str):
        """Constructor del gestor de correo, sus atributos son usuario y contraseña que son recibidos como parametros, las
            distintas bandejas de correos, los criterios de spam, y la loongitud de cada una de las estructuras
            :param usuario: Usuario del gestor.
            :param contrasenya: contraseña del gestor, debe contener al menos 8 caracteres
            :raise GestorCorreo.ErrorContrasenyaInvalida si la contraseña no contiene al menos 8 caracteres.
            """
        if len(contrasenya) < 8:
            raise GestorCorreo.ErrorContrasenyaInvalida("La contrseña debe tener al menos 8 caracteres")
        else:
            self._usuario :str = usuario
            self.__contrasenya : str = contrasenya
            self._bandeja_de_entrada : "GestorCorreo._Bag" = GestorCorreo._Bag()
            self._bandeja_de_salida : "GestorCorreo._Bag" = GestorCorreo._Bag()
            self._bandeja_de_borradores : "GestorCorreo._Bag" = GestorCorreo._Bag()
            self._bandeja_de_spam : "GestorCorreo._Bag" = GestorCorreo._Bag()
            self._criterios_de_spam: "GestorCorreo._Bag" = GestorCorreo._Bag()

    #metodos getter
    def _get_usuario(self) -> str :
        return self._usuario

    def _get_bandeja_entrada(self) -> "GestorCorreo._Bag":
        return self._bandeja_de_entrada

    def _get_bandeja_salida(self)-> "GestorCorreo._Bag":
        return self._bandeja_de_salida

    def _get_bandeja_spam(self)-> "GestorCorreo._Bag":
        return self._bandeja_de_spam

    def _get_bandeja_borradores(self)-> "GestorCorreo._Bag":
        return self._bandeja_de_borradores

    def _get_criterios_de_spam(self)-> "GestorCorreo._Bag":
        return self._criterios_de_spam

    def __get_contrasenya(self) -> str:
        return self.__contrasenya

    def __set_contrasenya(self, contrasenya:str)->None:
        self.__contrasenya = contrasenya

    def _que_bandeja_es(self, bandeja: str) -> "GestorCorreo._Bag":
        """Metodo auxiliar que a través de un string si coincide con las bandejas ,te devuelve esta misma
           :param bandeja: el tipo de bandeja que quieras obtener.
           :return el tipo de bandeja introducida o criterios de spam
           :raise GestorCorreo.ErrorBandejaInexistente si el string introducido no coincide con ninguna bandeja"""
        if bandeja == "bandeja de entrada":
            return self._get_bandeja_entrada()
        elif bandeja == "bandeja de salida":
            return self._get_bandeja_salida()
        elif bandeja == "bandeja de borradores":
            return self._get_bandeja_borradores()
        elif bandeja == "bandeja de spam":
            return self._get_bandeja_spam()
        elif bandeja == "criterios de spam":
            return self._get_criterios_de_spam()
        else: raise GestorCorreo.ErrorBandejaInexistente (f"La bandeja debe ser: `bandeja de entrada´, `bandeja de salida´,"
                                                         "`bandeja de borradores´, `bandeja de spam´ o `criterios de spam´")

    def len(self, bandeja : str) -> int :
        """Metodo que permite obtener el número de correos en la bandeja seleccionada
        :param bandeja: bandeja de la que quieres obtener el número de correos
        :return numero de correos de la bandeja seleccionada"""
        return self._que_bandeja_es(bandeja).len()

    #Funcionalidad extra.
    def mostrar_bandeja(self,bandeja_a_mostrar : str) -> str:
        """Muestra todos los correos de una bandeja o los criterios de criterios de spam.
           :return un string con todos los elementos"""
        bandeja = self._que_bandeja_es(bandeja_a_mostrar)
        return "[" + ", ".join(str(elemento) for elemento in bandeja.iterator()) + "]"


    def cambiar_contrasenya(self, contrasenya:str) ->bool:
        """Metodo que cambia la contraseña del gestor de correo.
           :param contrasenya: Nueva contraseña a establecer.
           :return: True si se modificó correctamente la contraseña.
            :raises GestorCorreo.ErrorContrasenyaInvalida: Si la nueva contraseña coincide con la anterior."""
        if  len(contrasenya) < 8:
            raise GestorCorreo.ErrorContrasenyaInvalida(f"La nueva contraseña del gestor {self._get_usuario()} debe contener al menos 8 caracteres.")
        elif self.__get_contrasenya() ==contrasenya:
            raise GestorCorreo.ErrorContrasenyaInvalida(f"La nueva contraseña del gestor {self._get_usuario()} no puede coincidar con la anterior.")
        else:
            self.__set_contrasenya(contrasenya)
            return True

    def anyadir_criterios_de_spam(self, criterio : str) -> bool:
        """Añade un nuevo criterio de spam si no existe previamente.
           :param criterio: Criterio de spam a añadir.
           :raises GestorCorreo.ErrorCriterioRepetido: Si el criterio ya existe en la lista de spam.
           :return:True si se añadió correctamente el criterio de spam."""

        if self._get_criterios_de_spam().contains(criterio):
            raise GestorCorreo.ErrorCriterioRepetido(f"El criterio: {criterio}, ya se encuentra en la lista de criterios de spam")
        self._get_criterios_de_spam().add_item(criterio)
        return True


    def eliminar_criterios_de_spam(self, criterio : str) -> bool:
        """Elimina un criterio de spam si existe en la lista.
           :param criterio: Criterio de spam a eliminar.
           :raises GestorCorreo.ErrorCriterioNoEncontrado: Si el criterio no está en la lista de spam.
           :return:True si se eliminó el criterio de spam."""
        if not self._get_criterios_de_spam().contains(criterio):
            raise GestorCorreo.ErrorCriterioNoEncontrado(f"El criterio: {criterio}, no se encuentra en la lista de criterios de spam")

        self._get_criterios_de_spam().remove_item(criterio)
        return True

    def redactar_correo(self, destinatario: str = None, asunto: str = None, mensaje: str = None) -> Correo:
        """Crea un nuevo correo y lo almacena en la bandeja de borradores.
           :param destinatario: Dirección del destinatario.
           :param asunto: Asunto del correo.
           :param mensaje: Contenido del mensaje.
           :return: Mensaje confirmando que el correo ha sido redactado y almacenado."""
        correo = Correo(remitente=self._get_usuario(), destinatario=destinatario, asunto=asunto, mensaje=mensaje)
        self._get_bandeja_borradores().add_item(correo)
        return correo

    def modificar_correo(self, correo : Correo,destinatario: str = None, asunto: str = None, mensaje: str = None)->bool:
        """Modifica los campos de un correo si este se encuentra en la bandeja de borradores.
           :param correo: Instancia del correo a modificar.
           :param destinatario: Nuevo destinatario (opcional).
           :param asunto: Nuevo asunto (opcional).
           :param mensaje: Nuevo mensaje (opcional).
           :raises GestorCorreo.ErrorCorreoNoEncontrado: Si el correo no está en la bandeja de borradores.
           :return: True si se modificó correctamente."""
        if not self._get_bandeja_borradores().contains(correo):
            raise GestorCorreo.ErrorCorreoNoEncontrado(f"El correo: {print(correo)} seleccionado no se encuentra en la bandeja de borradores")
        if self._get_bandeja_borradores().contains(correo) and (destinatario is not None or asunto is not None or mensaje is not None):
            correo.modificar_campos(destinatario = destinatario, asunto = asunto, cuerpo= mensaje)
            return True

    #El metodo buscar palabra en correo no vale para una estructura iterada
    def _buscar_criterios_en_correo(self,correo:Correo) -> bool:
        """Metodo auxiliar que permite buscar una palabra dentro de un correo.
        :param correo: Correo en el que buscar.
        :return encontrado: True si se encontró la palabra, False en caso contrario.
        """
        actual = self._get_criterios_de_spam().get_primer_nodo()
        encontrado = False
        while actual is not None and not encontrado:
                if correo.buscar_palabra(actual.elemento()):
                    encontrado = True
                actual =actual.siguiente()
        return encontrado
    def enviar_correo(self, correo: Correo, destinatario: "GestorCorreo")->bool:
        """Envía un correo a un destinatario y lo clasifica según criterios de spam.
               :param correo: Correo a enviar.
               :param destinatario: Gestor de correo del destinatario.
               :raises: GestorCorreo.ErrorCorreoNoEncontrado si el correo no está en la bandeja de borradores.
               :raises GestorCorreo.ErrorDestinatarioNoValido si se intenta enviar el correo a un objeto que no es de tipo GestorCorreo.
               :return: True si se ha enviado el correo."""

        # Verificar que el correo esté en la bandeja de borradores
        if not self._get_bandeja_borradores().contains(correo):
            raise GestorCorreo.ErrorCorreoNoEncontrado("El correo no se encuentra en la bandeja de borradores")

        if type(destinatario) != GestorCorreo:
            raise GestorCorreo.ErrorDestinatarioNoValido(f"El destinatario {destinatario} no es valido")

            # Mover el correo a la bandeja de salida
        self._get_bandeja_borradores().remove_item(correo)
        self._get_bandeja_salida().add_item(correo)

            # Enviar el correo
        enviado = correo.enviar_correo()

        if enviado:
            if destinatario._buscar_criterios_en_correo(correo):
                destinatario._get_bandeja_spam().add_item(correo)
            else:
                destinatario._get_bandeja_entrada().add_item(correo)
        return True
    def cambiar_estado_lectura(self, correo: Correo)->bool:
        """Cambia el estado de lectura de un correo si se encuentra en la bandeja de spam o borradores.
            :param correo: El correo cuyo estado de lectura se desea cambiar.
            :return True si se cambió el estado de lectura correctamente.
            :raise: GestorCorreo.ErrorCorreoNoEncontrado: Si el correo no se encuentra en la bandeja de spam o entrada."""
        if self._get_bandeja_spam().contains(correo) or self._get_bandeja_borradores().contains(correo):
            return correo.cambiar_estado_de_lectura()
        else: raise GestorCorreo.ErrorCorreoNoEncontrado("El correo no se encuentra en la bandeja de spam o entrada")


    def eliminar_correo(self, correo : Correo, bandeja_entrada : bool = None , bandeja_salida: bool = None, bandeja_borradores: bool = None, bandeja_spam : bool = None) -> bool:
        """Elimina un correo de una bandeja específica, los parametros de bandejas son booleanos, si se desea
            eliminar el correo de una bandeja especifica se deberá marcar como True.
           :param correo: Correo a eliminar.
           :param bandeja_entrada: Si el correo se desea eliminar de la bandeja de entrada.
           :param bandeja_salida: Si el correo se desea eliminar de la bandeja de salida.
           :param bandeja_borradores: Si el correo se desea eliminar de la bandeja de borradores.
           :param bandeja_spam: Si el correo se desea eliminar de la bandeja de spam.
           :return True si se ha eliminado el correo.
           :raise: GestorCorreo.ErrorParametrosIncompletos si no se especifica una bandeja de la que eliminar el mensaje.
           :raise GestorCorreo.ErrorCorreoNoEncontrado: Si el correo no está en la bandeja indicada."""
        if bandeja_entrada is None and bandeja_salida is None and bandeja_borradores is None and bandeja_spam is None:
            raise GestorCorreo.ErrorParametrosIncompletos("Debe introducir al menos una bandeja en la que eliminar un correo")
        elif bandeja_entrada is not None:
            if self._get_bandeja_entrada().contains(correo):
                GestorCorreo._Bag.remove_item(self._get_bandeja_entrada(), correo)
                return True
        #Puedo hacer return True ya que sé que un correo solo puede estar en una bandeja, por lo que si se encuentra en una bandeja te ahorras buscarlo en las demás.
        elif bandeja_salida is not None:
            if self._get_bandeja_salida().contains(correo):
                GestorCorreo._Bag.remove_item(self._get_bandeja_salida(), correo)
                return True

        elif bandeja_borradores is not None:
            if self._get_bandeja_borradores().contains(correo):
                GestorCorreo._Bag.remove_item(self._get_bandeja_borradores(), correo)
                return True

        elif bandeja_spam is not None:
            if self._get_bandeja_spam().contains(correo):
                GestorCorreo._Bag.remove_item(self._get_bandeja_spam(), correo)
                return True

        else: raise GestorCorreo.ErrorCorreoNoEncontrado("El correo no ha sido encontrado en la carpeta o las carpetas seleccionadas.")


    def _buscar_palabras_en_bandeja(self, palabras: str, bandeja_a_buscar: str) -> iter:
        """Metodo auxiliar que busca palabras o frases en los correos de una bandeja.
        :param palabras: Palabras o frases a buscar (cadena).
        :param bandeja_a_buscar: Bandeja donde se buscarán las palabras.
        :yields: Los correos donde se encontraron las palabras.
        """
        # primero separo las palabras recibidas en palabras individuales en caso de ser una frase lo que hay que buscar
        lista_palabras: GestorCorreo._Bag = GestorCorreo._Bag()
        palabra: str = ""
        for char in palabras:
            if char != "," and char != "." and char != "!" and char and char != "?" and char != "¿" and char != "@" and char != "%":
                palabra += char
            else:
                nuevo_nodo = GestorCorreo._Bag.Nodo(palabra)
                lista_palabras.add_item(nuevo_nodo)
                palabra = ""
        correo_actual = self._que_bandeja_es(bandeja_a_buscar).get_primer_nodo()

        while correo_actual is not None:
            palabra_actual = lista_palabras.get_primer_nodo()
            palabras_encontradas = 0
            total_palabras = lista_palabras.len()
            while palabra_actual is not None:
                if correo_actual.elemento().buscar_palabra(palabra_actual.elemento()):
                    palabras_encontradas +=1
                palabra_actual = palabra_actual.siguiente()
            if palabras_encontradas == total_palabras:
                yield correo_actual.elemento()
                print(correo_actual.elemento())
            correo_actual = correo_actual.siguiente()



    def busqueda_de_correos(self, cadena_texto: str, bandeja_entrada: bool = None, bandeja_salida: bool = None,
                            bandeja_borradores: bool = None, bandeja_spam: bool = None) -> str:
        """Metodo que perimite obtener los correos de manera textual donde se encuentre una palabra u oración.
           :param cadena_texto: Texto de la palabra a buscar
           :param bandeja_entrada: booleano,marcado como True, si se desea buscar en la bandeja de entrada.
           :param bandeja_salida: booleano,marcado como True, si se desea buscar en la bandeja de salida.
           :param bandeja_borradores: booleano,marcado como True, si se desea buscar en la bandeja de borradores.
           :param bandeja_spam: booleano,marcado como True, si se desea buscar en la bandeja de spam.
           :return mensaje con todos los correos de manera textual
           :raise GestorCorreo.ErrorBusquedaNoValida si no se introduce ninguna bandeja o se intenta buscar palabras no válidas.
           """

        if cadena_texto is None or cadena_texto == "" or cadena_texto == " ":
            raise GestorCorreo.ErrorBusquedaNoValida(
                "El texto a buscar debe ser distinto a None, un texto vacío o un espacio en blanco")

        if bandeja_entrada is None and bandeja_salida is None and bandeja_borradores is None and bandeja_spam is None:
            raise GestorCorreo.ErrorBusquedaNoValida(
                "Debe introducir al menos una bandeja en la que buscar los caracteres")
        mensaje: str = "["
        if bandeja_entrada is not None:
            bandeja = self._buscar_palabras_en_bandeja(palabras=cadena_texto, bandeja_a_buscar="bandeja de entrada")
            mensaje += ", ".join(str(elemento) for elemento in bandeja)
        if bandeja_salida is not None:
            bandeja = self._buscar_palabras_en_bandeja(palabras=cadena_texto, bandeja_a_buscar="bandeja de salida")
            mensaje += ", ".join(str(elemento) for elemento in bandeja)
        if bandeja_borradores is not None:
            bandeja = self._buscar_palabras_en_bandeja(palabras=cadena_texto, bandeja_a_buscar="bandeja de borradores")
            mensaje += ", ".join(str(elemento) for elemento in bandeja)
        if bandeja_spam is not None:
            bandeja = self._buscar_palabras_en_bandeja(palabras=cadena_texto, bandeja_a_buscar="bandeja de spam")
            mensaje += ", ".join(str(elemento) for elemento in bandeja)
        mensaje += "]"
        return mensaje









