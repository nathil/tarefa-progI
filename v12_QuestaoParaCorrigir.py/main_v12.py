
import flet as ft
import v12.controle as con

def main(page: ft.Page):  
    con.init(page)         
    page.title = "Sistema de cadastro"           
    page.on_route_change = con.controle_de_rota  
    page.theme_mode  = "light"
    page.go('1')


ft.app(target=main)