import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora IPv6"
    
    #CAMBIAR TEMA DE LA APP
    page.window_resizable=True #no permitir la resizable
    page.theme_mode=ft.ThemeMode.DARK #cambiar el tema de la aplicación
    page.window_max_width=470 #tamaño de ancho
    page.window_max_height=720 #tamaño de alto
    page.window_min_width=420
    page.window_min_height=720
    page.update() #actualizar las propiedades
    
    
    #CAMBIAR LA UBICACION
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER #contenido centrado verticalmente
    
    #pedir la direccion ipv6
    tb1 = ft.TextField(label="Dirección IPv6")
    page.add(tb1)
    
    #agregar un espacio para que el boton y el textfield tengan una separación y no se vean pegados
    
    boton_enviar = ft.ElevatedButton("Calcular la direccion")
    page.add(boton_enviar) #agregar el boton para calcular la direccion ip (esto hace la funcionalidad)
    
    #menu de navegacion
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.ARTICLE_ROUNDED, label="Regla 1"),
            ft.NavigationDestination(icon=ft.icons.ARTICLE_ROUNDED, label="Regla 2"),
            ft.NavigationDestination(icon=ft.icons.ARTICLE_ROUNDED, label="Ambas reglas")
        ]
    )
    
ft.app(target=main)