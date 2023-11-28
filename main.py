import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora IPv6"
    
    #CAMBIAR TEMA DE LA APP
    page.window_resizable=True #no permitir la resizable
    page.theme_mode=ft.ThemeMode.DARK #cambiar el tema de la aplicación
    page.window_width=470 #tamaño de ancho
    page.window_height=720 #tamaño de alto
    page.update() #actualizar las propiedades
    
    #CAMBIAR LA UBICACION
    page.vertical_alignment=ft.MainAxisAlignment.CENTER #contentenido centrado horizontalmente
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER #contenido centrado verticalmente

    page.add(ft.Text(
            "Selecciona una regla para empezar :)",
            size=25,
            #color=ft.colors.WHITE,
            weight=ft.FontWeight.NORMAL,
        ),)

    def calculadoraDirIp(e):
        page.controls.clear() #limpiamos el cotenido de nuestra pagina (caché)
        destino_navegacion = e.control.selected_index #Esto almacena el indice del boton que presiona el usuario
        
        #controlamos los casos
        if destino_navegacion == 0:
            #pedir la direccion ipv6
            tb1 = ft.TextField(label="Dirección IPv6")
            page.add(tb1) #agregar el textfield 
            #agregar un espacio para que el boton y el textfield tengan una separación y no se vean pegados
            page.add(ft.Text(value="\n"))
            #agregar el boton para calcular
            boton_enviar = ft.ElevatedButton("Calcular la dirección", height=60)
            page.add(boton_enviar) #agregar el boton para calcular la direccion ip (esto hace la funcionalidad)
            
        elif destino_navegacion == 1:
            #pedir la direccion ipv6
            tb1 = ft.TextField(label="Dirección IPv6")
            page.add(tb1) #agregar el textfield 
            #agregar un espacio para que el boton y el textfield tengan una separación y no se vean pegados
            page.add(ft.Text(value="\n"))
            #agregar el boton para calcular
            boton_enviar = ft.ElevatedButton("Calcular la dirección", height=60)
            page.add(boton_enviar) #agregar el boton para calcular la direccion ip (esto hace la funcionalidad)
            
        elif destino_navegacion == 2:
            #pedir la direccion ipv6
            tb1 = ft.TextField(label="Dirección IPv6")
            page.add(tb1) #agregar el textfield 
            #agregar un espacio para que el boton y el textfield tengan una separación y no se vean pegados
            page.add(ft.Text(value="\n"))
            #agregar el boton para calcular
            boton_enviar = ft.ElevatedButton("Calcular la dirección", height=60)
            page.add(boton_enviar) #agregar el boton para calcular la direccion ip (esto hace la funcionalidad)
            
        else:
            page.add(ft.Text(value="No se ha seleccionado ninguna regla"))

    #menu de navegacion
    page.navigation_bar = ft.NavigationBar(
    destinations=[
        ft.NavigationDestination(icon=ft.icons.ARTICLE_ROUNDED, label="Regla 1"),
        ft.NavigationDestination(icon=ft.icons.ARTICLE_ROUNDED, label="Regla 2"),
        ft.NavigationDestination(icon=ft.icons.ARTICLE_ROUNDED, label="Ambas reglas")
        ],
        on_change = calculadoraDirIp
    )
    
    page.add(page.navigation_bar)
    page.update()


    
ft.app(target=main)