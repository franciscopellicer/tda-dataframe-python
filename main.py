from correo import Correo
from gestor_correo import GestorCorreo
from dataframe import DataFrame , Array
if __name__ == '__main__':

    print("Probando el TDA correo:")
    print()
    #creando un correo vacio
    correo_vacio = Correo()
    #creando un correo con cuerpo
    correo_rellenado= Correo(remitente= "fran@um.es", destinatario = "alvaro@um.es",
                             asunto="Proyecto", mensaje="Tenemos que reunirnos urgentemente para terminarlo")
    print("Mostrando correo rellenado:")
    print(correo_rellenado)
    print()
    #enviamos el correo completo
    print("Enviando el correo rellenado:")
    enviado : bool= correo_rellenado.enviar_correo()
    print(enviado)
    print()
    #intentamos enviar el correo vacio
    print("Intentando enviar el correo vacio:")
    try:
        correo_vacio.enviar_correo()
    except Correo.ErrorCamposNoCompletos as error:
        print(error)
    print()
    print("Cambiando el estado de lectura del correo rellenado")
    correo_rellenado.cambiar_estado_de_lectura()
    print()
    print("Rellenando los datos del correo vacio")
    correo_vacio.modificar_campos(remitente="paco@um.es", destinatario="alex@um.es", asunto="proyecto",cuerpo="No logro abrir el proyecto")
    print()
    print("Imprimiendo el nuevo correo: \n")
    print(correo_vacio)
    print()
    print("Intentando editar un correo ya enviado")
    try:
        correo_rellenado.modificar_campos()
    except Correo.ErrorCorreoYaEnviado as error:
        print(error)
    print()
    print("Buscando la palabra `proyecto´ en el correo que antes era vacio")
    print(correo_vacio.buscar_palabra("proyecto"))
    print()
    print("Buscando la palabra `papa´ en el correo rellenado desde el principio")
    print(correo_rellenado.buscar_palabra("papa"))




    print("-------------------------\nProbando el TDA gestor de correo:")
    print()
    print("Creando gestor 1 con una contraseña válida:")
    gestor_1 = GestorCorreo(usuario="paco@um.es", contrasenya="paquitoum38")
    print()
    print("Intentando crear un gestor 2 con una contraseña no válida")
    try:
        gestor_2 = GestorCorreo(usuario="fran@um.es", contrasenya="fran1")

    except GestorCorreo.ErrorContrasenyaInvalida as error:
        print(error)

    finally:
        print("Creando el gestor 2 con una contraseña válida")
        gestor_2 = GestorCorreo(usuario="fran@um.es", contrasenya="fran2005")
    print()
    print("Cambiando las contraseña del gestor 1")
    gestor_1.cambiar_contrasenya("paquitochocolatero")
    print()
    print("Intentando cambiar la contrseña del gestor 2")
    try:
        gestor_2.cambiar_contrasenya("fran2005")
    except GestorCorreo.ErrorContrasenyaInvalida as error:
        print(error)
    print()
    print("Añadiendo criterios de spam al gestor 1")
    gestor_1.anyadir_criterios_de_spam("caca")
    gestor_1.anyadir_criterios_de_spam("culo")
    gestor_1.anyadir_criterios_de_spam("pedo")
    gestor_1.anyadir_criterios_de_spam("pis")
    print()
    print("Mostrando los criterios de spam del gestor 1")
    print(gestor_1.mostrar_bandeja("criterios de spam"))
    print(f"Longitud de la bandeja de spam:{gestor_1.len("criterios de spam")}")
    print()
    print("Añadiendo criterios de spam al gestor 2")
    gestor_2.anyadir_criterios_de_spam("tonto")
    gestor_2.anyadir_criterios_de_spam("inutil")
    gestor_2.anyadir_criterios_de_spam("idiota")
    gestor_2.anyadir_criterios_de_spam("retrasado")
    print()
    print("Mostrando los criterios de spam del gestor 2")
    print(gestor_2.mostrar_bandeja("criterios de spam"))
    print()
    #En nuestro programa no se pueden añadir criterios repetidos
    print("Intentando añadir un criterio repetido al gestor 1")
    try:
        gestor_1.anyadir_criterios_de_spam("pis")
    except GestorCorreo.ErrorCriterioRepetido as error:
        print(error)

    print()
    print("Eliminando un criterio del gestor1")
    gestor_1.eliminar_criterios_de_spam("pis")
    print(f"Criterios de spam gestor 1: {gestor_1.mostrar_bandeja('criterios de spam')}")
    print()
    print("Intentando eliminar un criterio del gestor2 que no existe")
    try:
        gestor_2.eliminar_criterios_de_spam("pis")
    except GestorCorreo.ErrorCriterioNoEncontrado as error:
        print(error)
    print()
    print("Creando correos desde el gestor 1, uno de ellos vacio")
    correo1 = gestor_1.redactar_correo(destinatario="lopez@um.es", asunto="caca",mensaje="Eres idiota y tonto")
    correo2 = gestor_1.redactar_correo()
    print()
    print("Mostrando bandeja de borradores del gestor 1")
    print(gestor_1.mostrar_bandeja("bandeja de borradores"))
    print()
    print("Creando correos desde el gestor 2, uno de ellos vacio")
    correo3 = gestor_2.redactar_correo(destinatario="paco@um.es", asunto="tonto",mensaje="Me hago pis")
    correo4 = gestor_2.redactar_correo()
    print()
    print("Mostrando bandeja de borradores del gestor 2")
    print(gestor_2.mostrar_bandeja("bandeja de borradores"))
    print()
    print("Modificando el correo vacio del gestor 1")
    gestor_1.modificar_correo(correo2,"lopez@um.es","disculpas","Siento haberle llamado idiota")
    print(correo2)
    print()
    print("Modificando el correo vacio del gestor 2")
    gestor_2.modificar_correo(correo4, "paco@um.es", "correo", "No le perdono semejante falta de respeto")
    print(correo4)
    print()
    print("Enviando el correo uno al gestor 2, (debería ir a spam)")
    gestor_1.enviar_correo(correo1,gestor_2)
    print()
    print("Comprobando que el correo recibido esta en spam")
    print(gestor_2.mostrar_bandeja("bandeja de spam"))
    print()
    print("Cambiando el estado de lectura del correo enviado")
    print(gestor_2.cambiar_estado_lectura(correo1))
    print()
    print("Eliminando un correo del gestor 2 en la bandeja de spam")
    gestor_2.eliminar_correo(correo1,bandeja_spam=True)
    print(gestor_2.mostrar_bandeja("bandeja de spam"))
    print()
    print("Buscando correos con la palabra idiota ")
    gestor_1.busqueda_de_correos("idiota",bandeja_salida=True, bandeja_borradores=True)
    print()
    print("Buscando correos con la frase: Eres idiota y tonto")
    gestor_1.busqueda_de_correos("Eres idiota y tonto", bandeja_salida=True)
    print()
    print("--------------------------")
    print("Probando el Tda Dataframe")
    # Crear el DataFrame con las columnas "Nombre" y "Edad"
    columnas = Array()
    columnas.insertar("Nombre")
    columnas.insertar("Edad")
    df = DataFrame(columnas, capacidad_inicial=2)

    # Insertar filas en el DataFrame
    fila1 = Array()
    fila1.insertar("Carlos")
    fila1.insertar(30)
    df.insertar_fila(fila1)

    fila2 = Array()
    fila2.insertar("Ana")
    fila2.insertar(25)
    df.insertar_fila(fila2)

    fila3 = Array()
    fila3.insertar("Luis")
    fila3.insertar(35)
    df.insertar_fila(fila3)

    fila4 = Array()
    fila4.insertar("Maria")
    fila4.insertar(28)
    df.insertar_fila(fila4, posicion=1)

    # Verificar el DataFrame despuÃ©s de insertar las primeras filas
    print("DataFrame después de insertar 4 filas:")
    print(df)

    # Insertar una nueva columna "Ciudad" con los valores
    ciudades = Array()
    ciudades.insertar("Madrid")
    ciudades.insertar("Barcelona")
    ciudades.insertar("Sevilla")
    ciudades.insertar("Valencia")
    df.insertar_columna("Ciudad", ciudades)

    print("\nDataFrame después de insertar la columna 'Ciudad':")
    print(df)

    # Insertar una nueva columna "Pais" sin valores, lo que debe rellenarse con None
    df.insertar_columna("Pais")

    print("\nDataFrame después de insertar la columna 'Pais' (sin valores):")
    print(df)

    # Pruebas de visualizar un rango de filas
    print("\nVisualizando filas del índice 1 al 3:")
    df.visualizar_rango_filas(1, 3)

    # Pruebas de visualizar una fila especÃ­fica
    print("\nVisualizando fila en el índice 2:")
    df.visualizar_fila(2)

    # Pruebas de visualizar los valores de una columna especÃ­fica
    print("\nVisualizando valores de la columna 'Ciudad':")
    df.visualizar_columna("Ciudad")

    # Eliminar una fila (fila en posiciÃ³n 3)
    df.eliminar_fila(3)
    print("\nDataFrame después de eliminar la fila en la posición 3:")
    print(df)

    # Eliminar una columna ("Edad")
    df.eliminar_columna("Edad")
    print("\nDataFrame después de eliminar la columna 'Edad':")
    print(df)

    # Pruebas de otras funcionalidades
    cantidad_filas_mostrar = 2
    print(f"\nPrimeras {cantidad_filas_mostrar} filas (head):")
    for i in range(cantidad_filas_mostrar):
        print(df.head(cantidad_filas_mostrar)[i])

    cantidad_filas_eliminar = 1
    print(f"\nÚltimas {cantidad_filas_eliminar} filas (tail):")
    for i in range(cantidad_filas_eliminar):
        print(df.tail(cantidad_filas_eliminar)[i])

    print("\nForma del DataFrame (shape):", df.shape())

    # Insertar una columna numÃ©rica para probar max_columna y mean_columna
    edades = Array()
    edades.insertar(30)
    edades.insertar(25)
    edades.insertar(35)
    df.insertar_columna("Edad", edades)
    print("\nDataFrame después de insertar nuevamente la columna 'Edad':")
    print(df)

    # Obtener el valor mÃ¡ximo y la media de la columna "Edad"
    print("\nValor máximo en la columna 'Edad':", df.max_columna("Edad"))
    print("Valor medio en la columna 'Edad':", df.mean_columna("Edad"))

    # Verificar existencia de columnas
    columna_a_comprobar = "Edad"
    if df.columna_existe(columna_a_comprobar):
        print(f"\nLa columna '{columna_a_comprobar}' existe en el DataFrame.")
    else:
        print(f"La columna '{columna_a_comprobar}' NO existe en el DataFrame.")

    #Reemplazando los valores nulos por valor definido
    valor_reemplazo = 69
    print(f"\nReemplazando los valores nulos por {valor_reemplazo} ")

    df.reemplazar_nulos(valor_reemplazo)
    print(df)
    # Visualizar filas con valores nulos
    print()
    df.visualizar_filas_nulas()
