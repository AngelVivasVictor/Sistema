# -*- coding: utf-8 -*-

# Librerías necesarias

# Descripccion y estructura
"""
   ""Nombre del proyecto: sistema de facturacion de un supermercado
   
   -Estructuras de los diccionarios:-----------------------------------------------------------------------------------------------------------------------------
        #Diccionarios: clientes, productos, proveedores, ventas
        ""--Clientes = {id_cliente: [nombre completo, dni, direccion, localidad, codigo postal, telefono, mail, activo]}
        ""--Productos = {id producto:[nombre, cantidad, precio unitario, costo, id_proveedor, activo]}
        ""--Proveedores = {id_proveedor: [cuit, razon social, telefono, mail, direccion, activo]}
        ""--Formas_pago = {id_pago: "efectivo"}
          NOTA:en los MENUS "Cliente, Productos, Proveedores" deben tener la siguentes operaciones: 
                #-ingresar datos nuevos, consultar, modificar y eliminar (cambiar el estado de true o false en campo activo)
        ""-Ventas = {id_ticket: [dni, fecha, hora, {id_producto: [cantidad, precio_unitario]}, total, forma_pago]}
"""
# """Definición de funciones"""

#  Menu principal.
def menu(): # Imprimir mensaje de bienvenida y opciones del menú principal
    print "\nSistema de Facturacio del Supermercado.\n\nMenu Principal."
    print "\n\t1. Menu de Clientes."
    print "\n\t2. Menu de Productos"
    print "\n\t3. Menu de Provedores."
    print "\n\t4. Salir."
    ingreso = raw_input("\n\tIngrese una opcion: ")  # Solicitar ingreso de opción al usuario y validarla
    opcion =  validacion(ingreso)
    return opcion # Retornar la opción seleccionada

def menu_clientes():  # Imprimir mensaje de bienvenida y opciones del menú de clientes
    print "\nSistema de Facturacion del Supermercado.\n\nMenu de Clientes."
    print "\n\t1. Ingresar un nuevo clientes."
    print "\n\t2. Consultar informacion de un cliente"
    print "\n\t3. Modificar datos de un cliente."
    print "\n\t4. Eliminar."
    print "\n\t5. <--- Volver al menu principal."
    ingreso = raw_input("\n\tIngrese una opcion: ")   # Solicitar ingreso de opción al usuario y validarla 
    opcion = menu_validacion(ingreso)
    return opcion  # Retornar la opción seleccionada


# Inico del programa.
opcion = menu()  # Mostrar el menú principal y obtener la opción seleccionada
while opcion <= range(1, 4) and opcion != 4: # Iniciar un bucle mientras la opción sea válida y no sea la opción de salir
    if opcion == 1:  # Si la opción es 1 (Menú de Clientes)      
        seleccion = menu_clientes()  # Mostrar el menú de clientes y obtener la opción seleccionada
          # Según la opción seleccionada, realizar la acción correspondiente
        if seleccion == 1: # Opción 1: Ingresar un nuevo cliente
            print"\n\tLa interfaz 'Ingresar un nuevo clientes' esta en desarrollo.\n"
            seleccion = menu_clientes() # Vuelve al menú cliente, hasta que se desarrolle esta funcionalidad
        elif seleccion == 2:  # Opción 2: Consultar información de un cliente
            print"\n\tLa interfaz 'Consultar informacion de un cliente' esta en desarrollo.\n"
            print"\n"
            seleccion = menu_clientes()  # Vuelve al menú cliente, hasta que se desarrolle esta funcionalidad 
        elif seleccion == 3:  # Opción 3: Modificar datos de un cliente
            print"\n\tLa interfaz 'Modificar datos de un cliente.' esta en desarrollo.\n"
            print"\n"
            seleccion = menu_clientes()  # Vuelve al menú cliente, hasta que se desarrolle esta funcionalidad
        elif seleccion == 4:  # Opción 4: Eliminar un cliente
            print"\n\tLa interfaz 'Eliminar.' esta en desarrollo.\n"
            print"\n"
            seleccion = menu_clientes() # Vuelve al menú cliente, hasta que se desarrolle esta funcionalidad
        if seleccion == 5: # Opción 5: Volver al menú principal 
            print"\n"
            opcion = menu() # Vuelve al menú principal
            print"\n"
    elif opcion == 2: # Si la opción es 2 (Menú de Productos)
        print "\n\tMenu de productos esta en desarrollo"
        opcion = menu()  # Vuelve al menú principal
    elif opcion == 3: # Si la opción es 2 (Menú de Productos) 
        print "\n\tMenu de provedores esta en desarrollo"
        opcion = menu()  # Vuelve al menú principal
print "\n\tA salido exitosamente" # Fin del programa