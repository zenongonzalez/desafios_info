from lista_inmuebles import inmuebles

# Funcion para agregar un inmueble nuevo a la lista
def agregar_inmueble():
    
    ''' Crea un dict(nuevo_inmueble) y lo agrega a list(inmuebles). no necesita parametros, se va creando mediante preguntas al usuario.'''
    
    inmueble = {'año': None, 'metros': None, 'habitaciones':None, 'garaje': None, 'zona': None, 'estado': None }

    while True:
        año_ingresado = input('Ingrese numericamente el año de creacion del inmueble:\n-> ')
        if año_ingresado.isdigit() and int(año_ingresado) >= 2000:
            año_ingresado = int(año_ingresado)
            inmueble['año'] = año_ingresado
            print(f'Datos Guardados. AÑO = {año_ingresado}\n')
        else:
            print('No operamos con inmuebles anteriores al año 2000 o forma no numerica')
            continue

        metro_ingresado = input('Ingrese los metros cuadrados del inmueble:\n-> ')
        if metro_ingresado.isdigit() and int(metro_ingresado) >= 60:
            metro_ingresado = int(metro_ingresado)
            inmueble['metros'] = metro_ingresado
            print(f'Datos guardados. METROS = {metro_ingresado}\n')
        else:
            while True:
                print('No operamos con inmuebles menores a 60 metros cuadrados')
                x = input('Ingrese un valor en metros cuadrados valido:\n-> ')
                if x.isdigit() and int(x) >= 60:
                    x = int(x)
                    inmueble['metros'] = x
                    print(f'Datos guardados. METROS = {x}\n')
                    break
                else:
                    continue
    
        habitacion_ingresado = input('Ingrese la cantidad numerica de habitaciones del inmueble:\n-> ')
        if habitacion_ingresado.isdigit() and int(habitacion_ingresado) >= 2:
            habitacion_ingresado = int(habitacion_ingresado)
            inmueble['habitaciones'] = habitacion_ingresado
            print(f'Datos guardados. HABITACIONES = {habitacion_ingresado}\n')
        else:
            while True:
                print('No operamos con inmuebles de menos de 2 habitaciones.')
                x = input('Ingrese una cantidad numerica de habitaciones valida:\n-> ')
                if x.isdigit() and int(x) >= 2:
                    x = int(x)
                    inmueble['habitaciones'] = x
                    print(f'Datos guardados. HABITACIONES = {x}\n')
                    break
                else:
                    continue
            
        garaje_ingresado = input('Ingrese SI/NO. ¿el inmueble posee garaje?:\n-> ').lower()
        if garaje_ingresado == 'si':
            inmueble['garaje'] = True
            print('Datos guardados. GARAJE = True\n')
        elif garaje_ingresado == 'no':
            inmueble['garaje'] = False
            print('Datos guardados. GARAJE = False\n')
        else: 
            while True:
                print('Las opciones disponibles son SI/NO')
                x = input('¿El inmueble posee garaje?:\n ->').lower()
                if x == 'si':
                    inmueble['garaje'] = True
                    print('Datos guardados. GARAJE = True\n')
                    break
                elif x == 'no':
                    inmueble['garaje'] == False
                    print('Datos guardados. GARAJE = False\n')
                    break
                else:
                    continue
                    
        zona_ingresado = input('Las zonas ingresadas solo pueden ser \'A\',\'B\',\'C\'.\nIngrese la zona del inmueble:\n-> ').upper()
        if zona_ingresado == 'A' or zona_ingresado == 'B' or zona_ingresado == 'C':
            inmueble['zona'] = zona_ingresado
            print(f'Datos guardados. ZONA = {zona_ingresado}\n')
        else:
            while True:
                print('Las opciones disponibles son A,B,C')
                x = input('¿En cual de estas zonas se encuentra el inmueble?:\n ->').upper()
                if x == 'A' or x == 'B' or x == 'C':
                    inmueble['zona'] = x
                    print(f'Datos guardados. ZONA = {x}\n')
                    break
                else:
                    continue
            
        estado_ingresado = input('Ingrese el estado del inmueble.\nLas opciones son: \'Disponible\',\'Reservado\',\'Vendido\'\n-> ').capitalize()
        if estado_ingresado == 'Disponible' or estado_ingresado == 'Reservado' or estado_ingresado == 'Vendido':
            inmueble['estado'] = estado_ingresado
            print(f'Datos guardados. ESTADO = {estado_ingresado}\n')
        else:
            while True:
                print('Las opciones disponibles son Disponible, Reservado, Vendido.')
                x = input('¿En que estado se encuentra el inmueble?:\n ->').capitalize()
                if x == 'Disponible' or x == 'Reservado' or x == 'Vendido':
                    inmueble['estado'] = x
                    print(f'Datos guardados. ESTADO = {x}\n')
                    break
                else:
                    continue
                
        inmuebles.append(inmueble)
        print(f'\nInmueble agregado con exito!\n{inmueble}')
        break

agregar_inmueble()