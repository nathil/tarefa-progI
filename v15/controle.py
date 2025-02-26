import tela_cadastro, tela_tabela
import flet as ft

def init(p):
    global page, telas, banco_de_dados
    page = p
    banco_de_dados = []
    telas = {
        '1': tela_cadastro.view(),
        '2': tela_tabela.view()
    }


def controle_de_rota(route_event):
    page.views.clear()    
    page.views.append(telas[route_event.route])          
    page.update()


def barra_navegacao():
    return ft.NavigationBar(
                        destinations=[
                            ft.NavigationBarDestination(icon=ft.icons.SAVE, label="Cadastrar"),
                            ft.NavigationBarDestination(icon=ft.icons.SEARCH, label="Listar"),                            
                        ],
                        on_change= navegacao 
            )#NavigationBar


def navegacao(e):
    if e.control.selected_index+1 == 2:
        tela_tabela.componentes["tabela"].current.rows = tela_tabela.atualizar_tabela()
        
    page.go(str(e.control.selected_index+1))
    