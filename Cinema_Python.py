peliculas = []
actores = []
perfiles = {}
reparto = {}
usuario = " "
sesion = False
menu = 0
puntos = {pelicula: 0 for pelicula in peliculas} 
listo = False
voto_usuario = {}
primera_ranking = None

while not sesion:
    print ("\nTHE CINEMA PYTHON")
    if puntos:
        ranking = sorted(puntos.items(),key=lambda x: x[1], reverse=True)
        print(ranking)
        primera_ranking = ranking[0][0]
        print (f"La película con más votos es: {primera_ranking}, con {puntos[primera_ranking]} votos!")
    
    usuario = input("Ingrese nombre de usuario: ")
    if usuario not in perfiles:
        print ("Ese usuario no existe.")
        print (f"Registrar usuario nuevo: {usuario.upper()}")
        clave = input("Ingrese contraseña: ")
        perfiles[usuario]=(clave)
    elif usuario in perfiles:
        clave = input("Ingrese contraseña: ")
        if clave == perfiles[usuario]:
            print (f"Sesión iniciada. Bienvenido {usuario}")
            if usuario not in voto_usuario:
                voto_usuario[usuario] = None
            sesion = True
        else: 
            print ("Clave incorrecta.")

    if sesion:
        while menu != 9:
            print ("\nMENÚ:\n1. Agregar/editar/eliminar/mostrar películas.\n2. Agregar/editar/eliminar/mostrar actores.\n3. Agregar actores a película.\n4. Votar por película.\n5. Ver votos.\n6. Ver repartos.\n7. Identificar usuario \n8. Cerrar sesión.\n9. Salir.\n")
            menu = input()
            if menu.isnumeric() and 0<int(menu) <=9:
                menu = int(menu)
            else:
                print ("Ingrese opción válida")

            match menu:
                case 1:
                    menu1 = 0
                    while menu1 != 5:
                        menu1 = input("1. Agregar película.\n2. Editar película.\n3. Eliminar película.\n4. Mostrar películas.\n5. Salir.\n")
                        if menu1 == "1":
                            print ("Agregar película.")
                            pelicula = input("Agregue película: ")
                            if pelicula not in peliculas:
                                peliculas.append(pelicula.lower())
                                puntos[pelicula] = 0
                                print (f"{pelicula} ha sido agregada al sistema.")
                            else:
                                print ("Película ya existe en el sistema.")
                        elif menu1 == "2":
                            print ("Editar película.")
                            pelicula_vieja = input("Ingrese qué película desea editar: ")
                            if pelicula_vieja in peliculas:
                                pelicula_nueva = input(f"Ingrese nombre nuevo para {pelicula_vieja}: ").lower()
                                for i in range(len(peliculas)):
                                    if peliculas[i] == pelicula_vieja:
                                        peliculas[i] = pelicula_nueva
                                print ("Título reemplazado correctamente.")
                                puntos[pelicula_nueva] = puntos.pop(pelicula_vieja)
                                if pelicula_vieja in reparto:
                                    reparto[pelicula_nueva] = reparto.pop(pelicula_vieja)
                            else:
                                print (f"La película '{pelicula_vieja}' no está en el sistema.")
                        elif menu1 == "3":
                            print ("Eliminar película.")
                            pelicula_eliminar = input("Ingrese nombre de la película a eliminar: ").lower()
                            if pelicula_eliminar in peliculas:
                                peliculas.remove(pelicula_eliminar)
                                print (f"{pelicula_eliminar} eliminada correctamente.")
                                puntos.pop(pelicula_eliminar,None)
                            else:
                                print (f"La película {pelicula_eliminar} no se encuentra en el sistema.")
                        elif menu1 == "4":
                            if peliculas:
                                print ("Películas registradas actualmente:")                                
                                for pelicula in peliculas:
                                   print (pelicula)
                            else:
                                print ("No hay películas en el sistema.")
                        elif menu1 == "5":
                            print ("Saliendo...")
                            break
                        else:
                            print ("Ingrese opción válida")

                case 2:
                    menu2 = 0
                    while menu2 != 5:
                        menu2 = input("1. Agregar actor.\n2. Editar actor.\n3. Eliminar actor.\n4. Mostrar actores.\n5. Salir.\n")
                        if menu2 == "1":
                            print ("Agregar actor.")
                            actor = input("Agregue actor: ")
                            if actor not in actores:
                                actores.append(actor)
                            else:
                                print ("Actor ya existe en el sistema.")
                        elif menu2 == "2":
                            print ("Editar actor.")
                            actor_viejo= input("Ingrese qué actor desea editar: ")
                            if actor_viejo in actores:
                                actor_nuevo = input(f"Ingrese nombre nuevo para {actor_viejo}: ")
                                for i in range(len(actores)):
                                    if actores[i] == actor_viejo:
                                        actores[i] = actor_nuevo
                            else:
                                print (f"El actor {actor_viejo} no está en el sistema.")
                        elif menu2 == "3":
                            print ("Eliminar actor.")
                            actor_eliminar = input("Ingrese nombre del actor a eliminar: ")
                            if actor_eliminar in actores:
                                actores.remove(actor_eliminar)
                                print (f"{actor_eliminar} eliminado correctamente.")
                            else:
                                print (f"El actor {actor_eliminar} no se encuentra en el sistema.")
                        elif menu2 == "4":
                            if actores:
                                print ("Lista de actores registrados exitosamente: ")
                                for actor in actores:
                                    print (actor)
                            else:
                                print ("No hay actores.")
                        elif menu2 == "5":
                            print ("Saliendo...")
                            break
                        else:
                            print ("Ingrese opción válida")

                case 3:
                    if actores and peliculas:
                        print ("Agregar actores al reparto de una película.")
                        print ("Actores y películas en el sistema:")
                        print (f"{'ACTORES':<30} {'PELÍCULAS'}")
                        max_len = max(len(actores),len(peliculas))
                        for i in range(max_len):
                            actor = actores[i] if i<len(actores) else ""
                            pelicula = peliculas[i] if i<len(peliculas) else ""
                            print (f"{actor:<30}{pelicula}")

                        pelicula_reparto = input("Ingrese el nombre de la película: ")
                        if pelicula_reparto in peliculas:
                            actor_reparto = input("Ingrese nombre del actor: ")
                            if actor_reparto in actores:
                                if pelicula_reparto not in reparto:
                                    reparto[pelicula_reparto] = []
                                if actor_reparto not in reparto[pelicula_reparto]:
                                    reparto[pelicula_reparto].append(actor_reparto)
                                    print (f"¡{actor_reparto} agregado al reparto de {pelicula_reparto} exitosamente!")
                                else:
                                    print (f"{actor_reparto} ya está en el reparto")
                            else:
                                print ("Ese actor no existe en el sistema.")
                        else:
                            print ("Esa película no existe en el sistema.")
                    else:
                        print ("Deben de haber actores y películas ingresados antes de asignar actores al reparto.")
                
                case 4:
                    print ("Votar")
                    if peliculas:
                        if usuario in voto_usuario and voto_usuario[usuario] != None:
                            print (f"Ya votaste por {voto_usuario[usuario]}. Sólo puedes votar una vez")
                        else:
                            print ("Las películas disponibles son:")
                            for pelicula in peliculas:
                                print (pelicula)
                            votando = input("Película a votar: ")
                            if votando in peliculas:
                                seguir = input(f"No podrá cambiar su voto, seguro que desea votar por {votando.upper()}? (1. Sí/2. No)")
                                if seguir == "1":
                                    puntos[votando]+=1
                                    voto_usuario[usuario] = votando
                                    print (f"Votaste por {votando}")
                                elif seguir == "2":
                                    voto_usuario[usuario]=None
                                    continue
                                else:
                                    print ("Opción inválida.")
                            else:
                                print ("Esa película no está en el sistema.")
                    else:
                        print ("No hay películas en el sistema.")

                case 5:
                    print ("Votos:")
                    for pelicula in puntos:
                        print (f"{pelicula}:{puntos[pelicula]} votos")

                case 6:
                    print ("Reparto de las películas:")
                    if not reparto:
                        print ("No hay ningún reparto registrado.")
                    else:
                        for pelicula,actores in reparto.items():
                            print (f"{pelicula}: {actores}")

                case 7:
                    print (f"Usuario: {usuario}")
                    if usuario in voto_usuario and voto_usuario[usuario] != None:
                        print (f"Votó por: {votando}")
                    else:
                        print ("No ha votado.")

                case 8:
                    print ("Cerrando sesión...")
                    sesion = False
                    break

                case 9:
                    print ("Saliendo...")
                    print (f"La pelicula con más votos fue: {primera_ranking}")
