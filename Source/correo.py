"""Este módulo contiene la clase Correo correspondiente al primer TDA"""
import random
class Correo:
    """Clase Correo que modela un correo, cuenta con un atributo de clase que permite definir el identificador único de cada correo.
    Además, cuenta con subclases que son Fecha para gestionar la fecha de envío y recepción, ErrorMensajeNoEnviado y ErrorCamposNoCompletos
    para gestionar posibles errores"""

    _numero_correos: int = 0
    class ErrorMensajeNoEnviado(Exception):
        """#Error que se lanzara cuando intentes enviar un correo ya enviado"""
        def __init__(self,mensaje :str):
            super().__init__(mensaje)

    class ErrorCamposNoCompletos(Exception):
        """Error que saltara si no todos los campos del mensaje han sido rellenados"""
        def __init__(self,mensaje : str):
            super().__init__(mensaje)

    class ErrorCorreoYaEnviado(Exception):
        """Error que saltara si se intenta modificar un correo ya enviado"""
        def __init__(self,mensaje:str):
            super().__init__(mensaje)

    class ErrorCamposAusentes(Exception):
        """Excepción lanzada cuando se intenta modificar un correo sin introducir nuevos parámetros"""
        def __init__(self,mensaje:str):
            super().__init__(mensaje)

    #clase fecha necesaria para gestionar la fecha de envío y recepcion del correo
    class Fecha:
        """Clase fecha necesaria para gestionar la fecha de envío y recepción del correo"""
        def __init__(self):
            """Constructor de la clase fecha, no recibe datos como parametros, se inicializa de manera aleatoria pero
            con coherencia. Tiene los atributos de año, mes, día, hora y minuto"""
            self._mes: int = random.randint(1, 12)

            #para el mes se debe tener en cuenta que no todos los meses tienen los mismos dias
            if self._mes == 2:
                self._dia: int = random.randint(1, 28)
            elif self._mes == 4 or self._mes == 6 or self._mes == 9 or self._mes == 11:
                self._dia: int = random.randint(1, 30)
            else:
                self._dia: int = random.randint(1, 31)

            self._anyo: int = random.randint(2000,2024)

            self._hora: int = random.randint(0, 23)

            self._minuto: int = random.randint(0, 59)

            self._segundo: int = random.randint(0, 59)

        # Métodos getter
        def _get_dia(self) -> int:
            return self._dia

        def _get_mes(self) -> int:
            return self._mes

        def _get_anyo(self) -> int:
            return self._anyo

        def _get_hora(self) -> int:
            return self._hora

        def _get_minuto(self) -> int:
            return self._minuto

        def _get_segundo(self) -> int:
            return self._segundo

        # Métodos setter
        def _set_dia(self, dia: int) -> None:
            """Debe recibir un natural como parámetro entre 1 y 31 (ambos inclusive) y dependiendo de cada mes"""
            self._dia = dia

        def _set_mes(self, mes: int) -> None:
            """Debe recibir un número natural entre 1 y 12 (ambos inclusive)"""
            self._mes = mes

        def _set_anyo(self, anyo: int) -> None:
            """Debe recibir un natural mayor al año actual"""
            self._anyo = anyo

        def _set_hora(self, hora: int) -> None:
            """"Debe recibir un natural entre 0 y 23 (ambos inclusive)"""
            self._hora = hora

        def _set_minuto(self, minuto: int) -> None:
            """Debe recibir un natural entre 0 y 59 (ambos inclusive)"""
            self._minuto = minuto

        def _set_segundo(self, segundo: int) -> None:
            """Debe recibir un natural entre 0 y 59 (ambos inclusive)"""
            self._segundo = segundo

        def tiempo_de_espera(self) -> "Correo.Fecha":
            """Metodo auxiliar que genera una nueva fecha sumando valores aleatorios a partir de una fecha dada, simulando
            el tiempo de espera de envío de un correo, considerando los años bisiestos.
            :return fecha"""

            segundos_a_sumar: int = random.randint(10, 59)
            minutos_a_sumar: int = random.randint(0, 120)
            horas_a_sumar: int = 0
            dias_a_sumar: int = 0

            # Calculamos los nuevos minutos y segundos
            nuevo_minuto: int = self._get_minuto() + minutos_a_sumar
            nuevo_segundo: int = self._get_segundo() + segundos_a_sumar

            # Control de casos para ver si se supera el número máximo de segundos, minutos, horas, días, meses y años
            if nuevo_segundo >= 60:
                nuevo_segundo %= 60
                nuevo_minuto += 1

            if nuevo_minuto >= 60:
                nuevo_minuto %= 60
                horas_a_sumar += 1

            nueva_hora: int = self._get_hora() + horas_a_sumar
            if nueva_hora >= 24:
                nueva_hora %= 24
                dias_a_sumar += 1

            # Definir los días de cada mes (comúnmente, sin tener en cuenta años bisiestos)
            dias_por_mes: list[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            mes_actual :int  = self._get_mes()
            dia_actual : int  = self._get_dia()

            # Ajustar días del mes actual considerando que febrero puede tener 29 días en un año bisiesto
            anyo_actual : int = self._get_anyo()

            # Función para verificar si el año es bisiesto
            def es_bisiesto(anyo: int) -> bool:
                return anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0)

            # Si el año es bisiesto, febrero tiene 29 días
            if es_bisiesto(anyo_actual):
                dias_por_mes[1] = 29  # Febrero tiene 29 días

            # Ajuste de días y meses
            if dia_actual > dias_por_mes[mes_actual - 1]:
                dia_actual -= dias_por_mes[mes_actual - 1]
                mes_actual += 1

            if mes_actual > 12:
                mes_actual = 1
                anyo_actual += 1

            # Creación de la nueva fecha con la modificación
            nueva_fecha : "Correo.Fecha"= Correo.Fecha()
            nueva_fecha._set_anyo(anyo_actual)
            nueva_fecha._set_mes(mes_actual)
            nueva_fecha._set_dia(dia_actual)
            nueva_fecha._set_hora(nueva_hora)
            nueva_fecha._set_minuto(nuevo_minuto)
            nueva_fecha._set_segundo(nuevo_segundo)

            return nueva_fecha

        def __str__(self) -> str:
            """Da una representacion informal en cadena de texto de la subclase fecha """
            return f"{self._get_dia()}/{self._get_mes()}/{self._get_anyo()} a las {self._get_hora()}:{self._get_minuto()}:{self._get_segundo()}"

    #para crear un correo, sino se añaden parametros se creara vacio por defecto, y como borrador.
    def __init__(self,remitente : str =None, destinatario: str = None , asunto : str = None, mensaje : str = None ):
        """
                Inicializa una instancia de la clase Correo.

                :param remitente: Dirección de correo del remitente. Por defecto None.
                :param destinatario: Dirección de correo del destinatario. Por defecto es None.
                :param asunto: Asunto del correo. Por defecto None.
                :param mensaje: Contenido del mensaje del correo. Por defecto es None.
                """
        self._remitente: str = remitente
        self._destinatario: str = destinatario
        self._asunto: str = asunto
        self._mensaje: str = mensaje
        self._borrador: bool = True   #Para gestionar si un correo ha sido o no enviado.
        if not self._borrador:
            self._fecha_envio: Correo.Fecha = self.Fecha()
            self._fecha_recepcion: Correo.Fecha = self._fecha_envio.tiempo_de_espera()
        else:
            self._fecha_envio = None
            self._fecha_recepcion = None
        self._leido: bool = False
        self._identificador: int = Correo._get_numero_correos()
        Correo._set_numero_correos(Correo._get_numero_correos()+1)

    #Métodos Getter
    @classmethod
    def _get_numero_correos(cls) ->int:
        return cls._numero_correos

    @classmethod
    def _set_numero_correos(cls, numero : int )-> None:
        cls._numero_correos = numero

    def _get_remitente(self) -> str:
        return self._remitente

    def _get_destinatario(self) -> str:
        return self._destinatario

    def _get_asunto(self) -> str:
        return self._asunto

    def _get_mensaje(self) -> str:
        return self._mensaje

    def _get_fecha_envio(self) -> "Correo.Fecha":
        if self._fecha_envio is None:
            raise Correo.ErrorMensajeNoEnviado("Un borrador no tiene fecha de envio")
        return self._fecha_envio

    def _get_fecha_recepcion(self) -> "Correo.Fecha":
        if self._fecha_recepcion is None:
            raise Correo.ErrorMensajeNoEnviado("Un borrador no tiene fecha de recepcion")
        return self._fecha_recepcion

    def _get_borrador(self) -> bool:
        return self._borrador

    def _get_leido(self) -> bool:
        return self._leido

    def _get_identificador(self) -> int:
        return self._identificador

    # Métodos Setter
    def _set_remitente(self, remitente: str) -> None:
        """Recibe un nuevo remitente de tipo string"""
        self._remitente = remitente

    def _set_destinatario(self, destinatario: str) -> None:
        """Recibe un nuevo destinatario de tipo string"""
        self._destinatario = destinatario

    def _set_asunto(self, asunto: str) -> None:
        """Recibe un nuevo asunto de tipo string"""
        self._asunto = asunto

    def _set_mensaje(self, mensaje: str) -> None:
        """Recibe un nuevo mensaje de tipo string"""
        self._mensaje = mensaje

    def _set_borrador(self, borrador: bool) -> None:
        """Recibe un nuevo borrador de tipo string"""
        self._borrador = borrador

    def _set_leido(self, leido: bool) -> None:
        """Recibe un booleano"""
        self._leido = leido

    def _set_fecha_envio(self, fecha_envio: "Correo.Fecha") -> None:
        """Recibe una fecha de tipo Coorreo.Fecha"""
        self._fecha_envio = fecha_envio

    def _set_fecha_recepcion(self, fecha_recepcion: "Correo.Fecha") -> None:
        """"Recibe una fecha de tipo Coorreo.Fecha"""
        self._fecha_recepcion = fecha_recepcion


    def cambiar_estado_de_lectura(self) -> bool:
        """"Metodo que cambia el estado de lectura siempre y cuando el mensaje haya sido enviado.
            :raise Correo.ErrorMensajeNoEnviado si el mensaje no ha sido enviado
            :return True si se ha cambiado el estado de lectura"""
            #No devuelvo un booleano para saber a que estado de lectura cambia el correo
        if self._get_borrador():
            raise Correo.ErrorMensajeNoEnviado("El correo no ha sido enviado, no se puede cambiar su estado de lectura.")
        else:
            if self._get_leido():
                self._set_leido(False)
                return True
            else:
                self._set_leido(True)
                return True


    def _campos_obligatorios_rellenados(self) -> bool:
        """metodo auxiliar que comprueba si los datos estan completos para poder enviar el correo
            :return True si el correo tiene todos sus campos rellenados, False en caso contrario"""
        if self._get_remitente() is not None and self._get_destinatario() is not None and self._get_asunto() is not None and self._get_mensaje() is not None:
            return True
        else: return False

    #metodo auxiliar para especificar los campos que faltan para ser mas especifico en el error
    def _datos_por_rellenar(self) -> str:
        """metodo auxiliar para especificar los campos que faltan para ser mas especifico en el error
            :return Un mensaje con los datos que faltan por rellenar."""
        datos: str =""
        if not self._get_remitente():
           datos+=" remitente"
        if not self._get_destinatario():
            datos+=" destinatario"
        if not self._get_asunto():
            datos+=" asunto"
        if not self._get_mensaje():
            datos+=" mensaje"
        return datos

    def enviar_correo(self) -> bool:
        """Metodo que permite enviar un correo
            :raise Correo.ErrorMensajeNoEnviado si el mensaje ya ha sido enviado
            :raise Correo.ErrorCamposNoCompletos si el cuerpo del mensaje es incompleto
            :return True si el correo ha sido enviado"""
        if self._campos_obligatorios_rellenados():
            self._set_borrador(False)
            self._set_leido(False)
            self._set_fecha_envio(Correo.Fecha())
            self._set_fecha_recepcion(self._get_fecha_envio().tiempo_de_espera())
            return True
        elif not self._get_borrador():
            raise Correo.ErrorCorreoYaEnviado("El correo ya ha sido enviado anteriormente.")
        else: raise  Correo.ErrorCamposNoCompletos(f"Mensaje no enviado.Falta por rellenar: {self._datos_por_rellenar()}.")

    #metodo sobrecargado para que un mismo metodo realize todas las funcionalidades
    def modificar_campos(self, remitente: str = None, destinatario: str = None, asunto: str = None, cuerpo: str = None) -> bool:
        """Metodo que permite modificar los campos de un correo que aún está en borrador.
            :param remitente: Nueva dirección de correo del remitente. Por defecto es None.
            :param destinatario: Nueva dirección de correo del destinatario. Por defecto es None.
            :param asunto: Nuevo asunto del correo. Por defecto es None.
            :param cuerpo: Nuevo cuerpo del mensaje. Por defecto es None.
            :return: True si se modificarón los datos.
            :raises ErrorCorreoYaEnviado: Si se intenta modificar un correo ya enviado.
            :raises ErrorCamposAusentes: Si se intenta modifixar un correo sin introducir nuevos parametros.
                """
        if not self._get_borrador():
            raise Correo.ErrorCorreoYaEnviado("No se puede modificar un mensaje previamente enviado.")


        if remitente is not None:
            self._set_remitente(remitente)
            print(f"Remitente modificado correctamente a: {remitente}")

        if destinatario is not None:
            self._set_destinatario(destinatario)
            print(f"Destinatario modificado correctamente a: {destinatario}")

        if asunto is not None:
            self._set_asunto(asunto)
            print(f"Asunto modificado correctamente a: {asunto}")

        if cuerpo is not None:
            self._set_mensaje(cuerpo)
            print(f"Mensaje modificado correctamente a: {cuerpo}")

        if cuerpo is None and asunto is None and remitente is None and destinatario is None and asunto is None:
            raise Correo.ErrorCamposAusentes("No se realizó ninguna modificación. No se proporcionaron parámetros.")

        return True

    #metodo que busca la palabra en el asunto y el mensaje
    def buscar_palabra(self, palabra_a_buscar) -> bool:
        """Busca una palabra dentro del mensaje del correo.
            :param palabra_a_buscar: Palabra que se buscará dentro del contenido del mensaje.
            :return: True si la palabra está en el mensaje, False en caso contrario."""
        capacidad: int = 30
        palabras: list[str] = ["" for _ in range(capacidad)]  # inicializando "array" por defecto 30
        palabra : str = ""
        i: int = 0
        for char in self._get_asunto() + " " + self._get_mensaje():
            if char != " " and char != "," and char != "." and char != "!" and char and char != "?" and char != "¿" and char != "@" and char != "%" and char != "":
                palabra += char
            else:
                if i == capacidad -1:
                    nuevas_palabras = ["" for _ in range(capacidad*2)]
                    for j in range(capacidad):
                        nuevas_palabras[j] = palabras[j]
                    palabras = nuevas_palabras
                    capacidad *= 2
                if i < capacidad:
                    palabras[i] = palabra
                    palabra = ""
                    i += 1
        j: int = 0
        encontrado: bool = False
        while j < capacidad and not encontrado:
            if palabras[j] == palabra_a_buscar:
                encontrado = True
            j += 1
        return encontrado

    def __str__(self) -> str :
        """Devuelve una representación en cadena del correo."""
        mensaje : str  = f"Remitente: {self._get_remitente()}\n"
        mensaje += f"Destinatario: {self._get_destinatario()}\n"
        mensaje += f"Asunto: {self._get_asunto()}\n"
        mensaje += f"Mensaje: {self._get_mensaje()}\n"
        if not self._get_borrador():
            mensaje += f"Enviado el {self._get_fecha_envio().__str__()}\n"
            mensaje += f"Recibido el {self._get_fecha_recepcion().__str__()}"
        return mensaje

    def __eq__(self, otro :"Correo")->bool:
        """Metodo mágico empleado para la comparación de igualdad entre dos correos
            :return: True si sus identificadores coinciden, False en caso contrario."""
        return  self._get_identificador() == otro._get_identificador()








