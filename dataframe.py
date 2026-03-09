class Array:
    def __init__(self, capacidad_inicial: int = 10):
        """
        Inicializa un array con una capacidad y longitud iniciales.
        :param capacidad_inicial: La capacidad inicial del array (opcional).

        """
        self._capacidad: int = capacidad_inicial
        self._longitud: int = 0
        self._datos: list = [None] * self._capacidad

    # Getters
    def get_longitud(self) -> int:
        return self._longitud

    def get_capacidad(self) -> int:
        return self._capacidad

    def get_datos(self) -> list:  # Es un array
        return self._datos

    # Setters
    def set_longitud(self, nueva_longitud: int) -> None:
        self._longitud = nueva_longitud

    def set_dato(self, dato: any, posicion: int) -> None:
        self._datos[posicion] = dato

    def set_array(self, array: list) -> None:
        self._datos = array

    def set_capacidad(self, nueva_capacidad: int) -> None:
        self._capacidad = nueva_capacidad

    # Metodo para insertar un elemento en el array en una posición específica
    def insertar(self, elemento: any, posicion: int = None) -> bool:
        """
        Inserta un elemento en el array en una posición específica o al final. Si el array está lleno, lo redimensiona.
        :param elemento: El elemento a insertar.
        :param posicion: La posición donde insertar (opcional).
        :return bool: `True` si la inserción fue exitosa.
        :raise IndexError: Si la posición está fuera del rango permitido.
        """
        if self.get_longitud() >= self.get_capacidad():
            self.redimensionar()

        if posicion is None:
            # Si no se proporciona posición, insertar al final
            self.set_dato(elemento, self.get_longitud())
        else:
            # Validar que la posición estÃ© dentro del rango
            if posicion < 0 or posicion > self.get_longitud():
                raise IndexError(f"No se puede insertar en la posición {posicion}")

            # Desplazar los elementos a la derecha para hacer espacio
            for i in range(self.get_longitud(), posicion, -1):
                self.set_dato(self.obtener(i - 1), i)

            # Insertar el elemento en la posiciÃ³n deseada
            self.set_dato(elemento, posicion)

        # Incrementar la longitud
        self.set_longitud(self.get_longitud() + 1)
        return True

    # Metodo para eliminar un elemento en una posición específica
    def eliminar(self, posicion: int) -> bool:
        """
        Elimina un elemento en una posición específica y desplaza los elementos restantes hacia la izquierda.
        :param posicion: La posición del elemento a eliminar.
        :return bool: 'True' si se ha podido eliminar
        :raise IndexError: Si la posición está fuera del rango permitido.
        """
        if posicion < 0 or posicion >= self.get_longitud():
            raise IndexError(f"No se puede eliminar en la posición {posicion}")

        for i in range(posicion, self.get_longitud() - 1):
            self.set_dato(self.get_datos()[i + 1], i)

        self.set_dato(None, self.get_longitud() - 1)
        self.set_longitud(self.get_longitud() - 1)
        return True

    # Metodo para redimensionar el array
    def redimensionar(self) -> None:
        """
        Aumenta la capacidad del array al doble de su tamaño actual.
        """
        nueva_capacidad: int = self.get_capacidad() * 2
        nuevos_datos: list = [None] * nueva_capacidad
        for i in range(self.get_longitud()):
            nuevos_datos[i] = self.get_datos()[i]
        self.set_array(nuevos_datos)
        self.set_capacidad(nueva_capacidad)

    # Metodo para obtener un elemento de una posición específica
    def obtener(self, posicion: int) -> object:
        """
        Obtiene el elemento en una posición específica del array.
        :param posicion: La posición del elemento a obtener.
        :return object El elemento en la posición solicitada.
        :raise IndexError: Si la posición está fuera del rango permitido.
        """
        return self.get_datos()[posicion]

    # Metodo para representar el array como un string
    def __str__(self) -> str:
        """
        Representa el array como un string con los elementos hasta la longitud actual.
        :return Una cadena representando los elementos del array.
        """
        return str(self.get_datos()[:self.get_longitud()])

    # Metodo para insertar una fila en el DataFrame


class DataFrame:
    class TamanyoFilasColumnasError(Exception):
        """
        Excepción personalizada para indicar que el tamaño de la columna no coincide con el número de filas.
        """

        def __init__(self, message: str):
            super().__init__(message)

    class ColumnaNoExisteError(Exception):
        """
        Excepción personalizada para indicar que una columna no fue encontrada en el DataFrame.
        """

        def __init__(self, message: str):
            super().__init__(message)

    class NumeroDeFilasExcedidoError(ValueError):
        """
        Excepción personalizada para el caso cuando el número de filas solicitado es mayor
        que el número de filas en el DataFrame.
        """

        def __init__(self, mensaje: str):
            super().__init__(mensaje)
            self.mensaje = mensaje

    class ValoresInvalidosColumnaError(Exception):
        """
        Excepción personalizada para indicar que no hay valores válidos en una columna
        para realizar una operación como calcular la media.
        """

        def __init__(self, nombre_columna: str):
            self.nombre_columna = nombre_columna
            super().__init__(f"No hay valores válidos en la columna '{nombre_columna}' para calcular la media.")

    class TipoDatoInvalidoError(Exception):
        """
        Excepción personalizada que se lanza cuando un valor en una columna no es de
        tipo `int`, `float` o `None`.
        """

        def __init__(self, mensaje: str):
            super().__init__(mensaje)
            self.mensaje = mensaje

    def __init__(self, columnas: Array, capacidad_inicial: int = 10):
        self._columnas : Array= columnas  # Array que contiene las columnas del DataFrame
        self._capacidad : int = capacidad_inicial
        # Crear una lista de filas, donde cada fila es un Array con la misma longitud que las columnas
        self._dataframe = [Array(self._columnas.get_longitud()) for _ in range(self._capacidad)]
        self._num_filas : int = 0

    def _actualizar_num_filas(self, cantidad_filas: int):
        self._num_filas = cantidad_filas

    def _get_num_filas(self) -> int:
        return self._num_filas

    def _get_capacidad(self) -> int:
        return self._capacidad


    def _get_columnas(self):
        return self._columnas

    def _get_dataframe(self):
        return self._dataframe

    def _redimensionar(self):
        """
        Redimensiona el DataFrame duplicando su capacidad.
        """
        nueva_capacidad = self._capacidad * 2
        nuevos_datos = [Array(self._columnas.get_longitud()) for _ in range(nueva_capacidad)]

        for i in range(self._num_filas):
            nuevos_datos[i] = self._dataframe[i]

        self._dataframe = nuevos_datos
        self._capacidad = nueva_capacidad
    def insertar_fila(self, fila: Array, posicion=None) -> bool:
        """
        Inserta una fila en una posición específica del DataFrame. Si no se especifica la posición,
        la fila se inserta al final.
        :param fila : La fila a insertar. Debe ser un Array con la misma longitud que las columnas.
        :param posicion : La posición en la que se insertará la fila. Si no se proporciona,
        la fila se inserta al final.
        :return bool: 'True' si se ha podido eliminar
        :raise IndexError: Si la posición está fuera de rango.
        :raise TamanyoFilasColumnasError: Si la fila no tiene el mismo número de elementos que las columnas.
        """
        # Verificar si la fila tiene el mismo nÃºmero de columnas que el DataFrame
        if fila.get_longitud() != self._get_columnas().get_longitud():
            raise DataFrame.TamanyoFilasColumnasError("La fila debe tener el mismo número de elementos que las columnas.")

        # Verificar si hay espacio suficiente para insertar la fila
        if self._get_num_filas() >= self._get_capacidad():
            self._redimensionar()

        # Si no se proporciona una posición, la fila se inserta al final
        if posicion is None:
            posicion = self._get_num_filas()

        # Validar que la posición está dentro del rango
        if posicion < 0 or posicion > self._get_num_filas():
            raise IndexError("Posición fuera de rango.")

        # Desplazar las filas existentes a la derecha
        for i in range(self._get_num_filas(), posicion, -1):
            self._dataframe[i] = self._dataframe[i - 1]

        # Insertar la fila en la posición deseada
        self._get_dataframe()[posicion] = fila

        # Incrementar el número de filas
        self._actualizar_num_filas(self._get_num_filas() + 1)
        return True

    def insertar_columna(self, nombre_columna: str, datos_columna: Array = None) -> bool:
        """
        Inserta una nueva columna en el DataFrame. Si no se proporcionan datos de columna,
        se llenan con `None`. Si los datos no coinciden exactamente con el número de filas,
        se completan los datos faltantes con `None` hasta alcanzar el número de filas.
        :param nombre_columna: El nombre de la columna a insertar.
        :param datos_columna. Los datos a insertar en la columna (opcional, por defecto es None).
        :return bool: `True` si la columna se inserta correctamente.
        :raise TamanyoFilasColumnasError: Si el número de elementos de la columna excede el número de filas.
        """
        self._get_columnas().insertar(nombre_columna)

        if datos_columna is None:
            # Si no hay datos proporcionados, llenar con None
            for i in range(self._get_num_filas()):
                self._get_dataframe()[i].insertar(None)
        else:
            # Verificar si los datos exceden el nÃºmero de filas
            if datos_columna.get_longitud() > self._get_num_filas():
                raise DataFrame.TamanyoFilasColumnasError(
                    f"El número de elementos de la columna ({datos_columna.get_longitud()}) excede el número de filas ({self._get_num_filas()})."
                )

            # Insertar los datos proporcionados y completar con None si faltan filas
            for i in range(self._get_num_filas()):
                if i < datos_columna.get_longitud():
                    self._get_dataframe()[i].insertar(datos_columna.obtener(i))
                else:
                    self._get_dataframe()[i].insertar(None)

        return True

    def eliminar_columna(self, nombre_columna: str) -> bool:
        """
        Elimina una columna en el DataFrame por su nombre.
        :param nombre_columna: El nombre de la columna a eliminar.
        :return bool: `True` si la columna se elimina correctamente.
        :raise ColimnaNoExiste: Si no se encuentra la columna.
        """
        columna_encontrada = False
        i = 0
        posicion_columna = None

        while i < self._get_columnas().get_longitud() and not columna_encontrada:
            if self._get_columnas().obtener(i) == nombre_columna:
                columna_encontrada = True
                posicion_columna = i
            i += 1

        if not columna_encontrada:
            raise DataFrame.ColumnaNoExisteError(f"Columna '{nombre_columna}' no encontrada.")

        for i in range(self._get_num_filas()):
            self._get_dataframe()[i].eliminar(posicion_columna)

        self._get_columnas().eliminar(posicion_columna)

        return True

    def eliminar_fila(self, posicion: int) -> bool:
        """
        Elimina una fila en el DataFrame en la posición especificada y desplaza las filas restantes hacia arriba.
        :param posicion: La posición de la fila a eliminar
        :return bool: `True` si la fila se elimina correctamente.
        :raise IndexError: Si la posición de la fila está fuera del rango permitido.
        """
        if posicion < 0 or posicion >= self._get_num_filas():
            raise IndexError("Posición fuera de rango")

        for i in range(posicion, self._get_num_filas() - 1):
            for j in range(self._get_columnas().get_longitud()):
                self._get_dataframe()[i].set_dato(self._get_dataframe()[i + 1].obtener(j), j)

        for j in range(self._get_columnas().get_longitud()):
            self._get_dataframe()[self._get_num_filas() - 1].set_dato(None, j)

        self._actualizar_num_filas(self._get_num_filas() - 1)

        return True

        # Verificar si una columna existe por su nombre

    def columna_existe(self, nombre_columna: str) -> bool:
        """
        Verifica si una columna existe en el DataFrame según su nombre.
        :param: El nombre de la columna a buscar (str).
        :return bool: `True` si la columna existe en el DataFrame, `False` en caso contrario.
        """
        i = 0
        while i < self._get_columnas().get_longitud():
            if self._get_columnas().obtener(i) == nombre_columna:
                return True
            i += 1
        return False

    # Obtener las primeras n-filas
    def head(self, n_filas: int) -> list[Array]:
        """
        Obtiene las primeras n filas del DataFrame.
        :param n_filas: El número de filas a obtener desde el inicio (int).
        :return Array: Un array de las primeras n filas del DataFrame.
        :raise NumeroDeFilasExcedidoError: Si n es mayor que el número de filas en el DataFrame.
        """
        if n_filas > self._get_num_filas():
            raise DataFrame.NumeroDeFilasExcedidoError(f"{n_filas} no puede ser mayor que el número de filas.")
        return [self._get_dataframe()[i] for i in range(n_filas)]

    # Obtener las últimas n filas
    def tail(self, n_filas: int) -> list[Array]:
        """
        Obtiene las últimas n filas del DataFrame.
        :param n_filas: El número de filas a obtener desde el final (int).
        :return Array: Un array de las últimas n filas del DataFrame.
        :return NumeroDeFilasExcedidoError: Si n es mayor que el nÃºmero de filas en el DataFrame.
        """
        if n_filas > self._get_num_filas():
            raise DataFrame.NumeroDeFilasExcedidoError(f"{n_filas} no puede ser mayor que el número de filas.")
        return [self._get_dataframe()[i] for i in range(self._get_num_filas() - n_filas, self._get_num_filas())]

    # Obtener la forma (shape) del DataFrame
    def shape(self) -> tuple:
        """
        Obtiene la forma del DataFrame, es decir, el número de filas y columnas.
        :return tuple: Una tupla (num_filas, num_columnas), donde num_filas es el número de filas
        y num_columnas es el número de columnas del DataFrame (int, int).
        """
        # Aqui se tiene en cuenta que el tamaÃ±o del dataframe empieza a partir de los datos, y no desde la'primera'fila que inidica lo que hay en cada columna. Si se contase eso, solo haria falta poner un +1 en filas
        return self._get_num_filas(), self._get_columnas().get_longitud()

    # Metodo para obtener el valor mÃ¡ximo de una columna
    def max_columna(self, nombre_columna: str) -> float:
        """
        Obtiene el valor mÃ¡ximo de una columna específica del DataFrame, asegurándose
        de que todos los valores sean `int`, `float` o `None`.
        :param nombre_columna: El nombre de la columna para la cual calcular el valor mÃ¡ximo (str).
        :return float: El valor mÃ¡ximo encontrado en la columna.
        :raise ColumnaNoExisteError: Si la columna no se encuentra en el DataFrame.
        :raise ipoDatoInvalidoError: Si algÃºn valor de la columna no es `int`, `float` o `None`.
        """
        # Buscar la posiciÃ³n de la columna
        columna_encontrada = False
        i = 0
        posicion_columna = None  # Necesitamos el Ã­ndice de la columna
        while i < self._get_columnas().get_longitud() and not columna_encontrada:
            if self._get_columnas().obtener(i) == nombre_columna:
                columna_encontrada = True
                posicion_columna = i
            i += 1

        if not columna_encontrada:
            raise DataFrame.ColumnaNoExisteError(f"Columna '{nombre_columna}' no encontrada.")

        # Verificar que todos los valores sean `int`, `float` o `None`
        for i in range(self._get_num_filas()):
            valor = self._get_dataframe()[i].obtener(posicion_columna)
            if not (isinstance(valor, (int, float)) or valor is None):
                raise DataFrame.TipoDatoInvalidoError(
                    f"Valor inválido en la columna '{nombre_columna}': {valor}. "
                    f"Se esperaban únicamente valores de tipo int, float o None."
                )

        # Calcular el valor mÃ¡ximo de la columna
        max_valor = None
        for i in range(self._get_num_filas()):
            valor = self._get_dataframe()[i].obtener(posicion_columna)
            if isinstance(valor, (int, float)):  # Ignorar valores None
                if max_valor is None or valor > max_valor:
                    max_valor = valor

        return max_valor

    # Metodo para obtener el valor medio de una columna
    def mean_columna(self, nombre_columna: str) -> float:
        """
        Obtiene el valor medio (promedio) de los valores en una columna específica.
        :param nombre_columna: El nombre de la columna para la cual calcular la media (str).
        :return float: El valor medio de los valores en la columna (float).
        :raise ColumnaNoExisteError: Si la columna no se encuentra o si no hay valores vÃ¡lidos para calcular la media.
        :raise ValoresInvalidosColumnaError: Si no hay valores vÃ¡lidos (numÃ©ricos) en la columna para calcular la media.
        """
        # Buscar la posiciÃ³n de la columna
        columna_encontrada = False
        i = 0
        posicion_columna = None
        while i < self._get_columnas().get_longitud() and not columna_encontrada:
            if self._get_columnas().obtener(i) == nombre_columna:
                columna_encontrada = True
                posicion_columna = i
            i += 1

        if not columna_encontrada:
            raise DataFrame.ColumnaNoExisteError(f"Columna '{nombre_columna}' no encontrada.")

        # Calcular la media de la columna
        suma = 0
        count = 0
        for i in range(self._get_num_filas()):
            valor = self._get_dataframe()[i].obtener(posicion_columna)
            # Solo considerar valores numÃ©ricos
            if isinstance(valor, (int, float)):
                suma += valor
                count += 1
            elif valor is not None:  # Asi si no son numeros y no es None porque no se ha puesto ese valor en esa posicion, no entra a lanzar el error
                raise DataFrame.ValoresInvalidosColumnaError(
                    f"Valor no numÃ©rico encontrado en la columna '{nombre_columna}': {valor}. Solo se permiten números enteros o floats."
                )

        if count == 0:
            raise DataFrame.ValoresInvalidosColumnaError(
                f"No hay valores válidos en la columna '{nombre_columna}' para calcular la media.")

        return suma / count

    def reemplazar_nulos(self, valor_reemplazo: object) -> None:
        """
        Reemplaza todos los valores nulos (None) del DataFrame con un valor proporcionado.
        :param valor_reemplazo: El valor que sustituirá los valores nulos.
        """
        # Recorremos cada fila del DataFrame
        for i in range(self._get_num_filas()):
            fila = self._get_dataframe()[i]

            # Reemplazamos todos los valores nulos en cada fila
            for j in range(fila.get_longitud()):
                if fila.obtener(j) is None: #Si no hay None no hace nada
                    fila.set_dato(valor_reemplazo, j)


    def visualizar_filas_nulas(self) -> None:
        """
        Identifica y visualiza el conjunto de filas que contienen, al menos, una celda con valor nulo.
        También muestra el índice de cada fila con valores nulos.
        """

        filas_nulas = [None] * self._get_num_filas()  # Preparamos espacio suficiente para las filas con nulos
        indices_filas_nulas = [None] * self._get_num_filas()  # Lo mismo para los Ã­ndices
        idx = 0  # Inicializamos el Ã­ndice de las filas
        contador = 0  # Contador para llevar el registro de cuÃ¡ntas filas con nulos hemos encontrado

        while idx < self._get_num_filas():
            fila = self._get_dataframe()[idx]  # Obtener la fila actual
            fila_con_nulo = False  # Variable para verificar si la fila tiene un valor nulo

            # Comprobamos si hay algÃºn valor nulo en la fila
            col_idx = 0
            while col_idx < self._get_columnas().get_longitud() and not fila_con_nulo:
                valor = fila.obtener(col_idx)  # Obtener el valor de la columna actual
                if valor is None:
                    fila_con_nulo = True  # Si encontramos un valor nulo, marcamos la fila
                col_idx += 1

            if fila_con_nulo:
                filas_nulas[contador] = fila  # Asignamos la fila con nulos
                indices_filas_nulas[contador] = idx  # Asignamos el Ã­ndice de la fila
                contador += 1  # Incrementamos el contador de filas con nulos

            idx += 1  # Pasamos a la siguiente fila

        # Mostrar las filas que contienen valores nulos
        if contador > 0:
            print("Filas con valores nulos:")
            fila_idx = 0
            while fila_idx < contador:
                print(f"Índice de fila {indices_filas_nulas[fila_idx]}: {filas_nulas[fila_idx]}")
                fila_idx += 1
        else:
            print("No se encontraron filas con valores nulos.")

    # Visualizar un rango de filas entre dos índices
    def visualizar_rango_filas(self, inicio: int, fin: int) -> None:
        """
        Muestra un rango de filas del DataFrame entre los índices especificados, con un formato alineado.
        :param inicio : índice inicial del rango de filas a visualizar.
        :param fin : índice final del rango de filas a visualizar.
        :raise IndexError: Si el rango de índices es inválido.
        """
        if inicio < 0 or fin >= self._get_num_filas() or inicio > fin:
            raise IndexError("El rango de índices no es válido.")

        # Definir el ancho mÃ¡ximo de las columnas para mantener la alineación
        espacio_columna = 15

        # Mostrar los nombres de las columnas
        for i in range(self._get_columnas().get_longitud()):
            columna = self._get_columnas().obtener(i)
            print(f"{columna:<{espacio_columna}}", end=" | " if i < self._get_columnas().get_longitud() - 1 else "\n")

        # Mostrar las filas del rango
        for fila_idx in range(inicio, fin + 1):
            for j in range(self._get_columnas().get_longitud()):
                valor = self._get_dataframe()[fila_idx].obtener(j)
                print(f"{'NaN':<{espacio_columna}}" if valor is None else f"{valor:<{espacio_columna}}",
                      # El uso de :< es para que se vea mejor en pantalla, en la funcion str, se dice lo que hace
                      end=" | " if j < self._get_columnas().get_longitud() - 1 else "\n")  # Tenemos en cuenta si se ha llegado al final de la lsita o no para saltar de linea

    # Mostrar el contenido de una fila específica
    def visualizar_fila(self, indice: int) -> None:
        """
        Muestra el contenido de una fila específica del DataFrame, con formato alineado.
        :param indice: índice de la fila a visualizar.
        :raise IndexError: Si el índice de la fila está fuera del rango válido.
        """
        if indice < 0 or indice >= self._get_num_filas():
            raise IndexError("Índice de fila fuera de rango.")

        # Definir el ancho mÃ¡ximo de las columnas para mantener la alineación
        espacio_columna = 15

        # Mostrar los nombres de las columnas
        for i in range(self._get_columnas().get_longitud()):
            columna = self._get_columnas().obtener(i)
            print(f"{columna:<{espacio_columna}}", end=" | " if i < self._get_columnas().get_longitud() - 1 else "\n")

        # Mostrar la fila especificada
        for j in range(self._get_columnas().get_longitud()):
            valor = self._get_dataframe()[indice].obtener(j)
            print(f"{'NaN':<{espacio_columna}}" if valor is None else f"{valor:<{espacio_columna}}",
                  end=" | " if j < self._get_columnas().get_longitud() - 1 else "\n")

    # Mostrar los valores de una columna especÃ­fica
    def visualizar_columna(self, nombre_columna: str):
        """
        Muestra los valores de una columna específica del DataFrame.
        :param nombre_columna: Nombre de la columna cuyos valores se desean visualizar.
        :raise ColumnaNoExisteError: Si la columna con el nombre especificado no existe en el DataFrame.
        """
        # Buscar la posiciÃ³n de la columna
        columna_encontrada = False
        posicion_columna = None
        i = 0
        while i < self._get_columnas().get_longitud() and not columna_encontrada:
            if self._get_columnas().obtener(i) == nombre_columna:
                columna_encontrada = True
                posicion_columna = i
            i += 1

        if not columna_encontrada:
            raise DataFrame.ColumnaNoExisteError(f"Columna '{nombre_columna}' no encontrada.")

        # Definir el ancho máximo de las columnas para mantener la alineación
        espacio_columna = 15

        # Mostrar el nombre de la columna
        print(f"{nombre_columna:<{espacio_columna}}")

        # Mostrar los valores de la columna
        for i in range(self._get_num_filas()):
            valor = self._get_dataframe()[i].obtener(posicion_columna)
            print(f"{'NaN':<{espacio_columna}}" if valor is None else f"{valor:<{espacio_columna}}",
                  end="\n")

    def __str__(self) -> str:
        """
        Genera una representación en formato de tabla del DataFrame, sustituyendo los valores None por 'NaN'
        y alineando las columnas con un tamaño fijo.
        :return str: Una cadena de texto que representa el DataFrame en formato tabular.
        """
        espacio_columna = 15  # Establecer el tamaño del espacio para las columnas

        resultado = ""

        # Mostrar los encabezados de las columnas
        for i in range(self._get_columnas().get_longitud()):
            columna = self._get_columnas().obtener(i)
            resultado += f"{columna:<{espacio_columna}}"  # Alineado a la izquierda con un tamaño fijo
            if i < self._get_columnas().get_longitud() - 1:
                resultado += " | "  # Separador entre columnas
        resultado += "\n"  # Nueva línea después de los encabezados

        # Obtener el número de filas con datos
        num_filas = self._get_num_filas()

        # Mostrar las filas del DataFrame
        for i in range(num_filas):
            fila = self._get_dataframe()[i]
            for j in range(fila.get_longitud()):
                valor = fila.obtener(j)
                if valor is None:
                    resultado += f"{'NaN':<{espacio_columna}}"  # Reemplazar None por 'NaN'
                else:
                    resultado += f"{valor:<{espacio_columna}}"  # Mostrar el valor alineado
                if j < fila.get_longitud() - 1:
                    resultado += " | "  # Separador entre columnas
            resultado += "\n"  # Nueva línea después de cada fila

        return resultado

    """NOTA: He buscado por internet acerca de como mostrar el dataframe de manera ordenada para qeu si una palabra tiene muchas letras este como indexada
    para ello hemos usado lo de :<. No obstante no se pide la visualización de cada una de las partes , pero lo hago para asegurarme de que las funciones 
    funcionan correctamente"""



