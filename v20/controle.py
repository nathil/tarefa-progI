import tela_cadastro, tela_tabela, tela_atualizar
import flet as ft
import banco_de_dados as bd
import controle as con

def init(p):
    global page, telas, banco_de_dados
    page = p
    banco_de_dados = bd.carregar_banco_de_dados()
    telas = {
        '1': tela_cadastro.view(),
        '2': tela_tabela.view(),
        '3': tela_atualizar.view()
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
    
"""
No arquivo controle, criamos as funções salvar, remover e atualizar.
Essas funções uutilizam as funções do banco de dados.
Observer que as funções remover e atualizar precisam chamar a 
função atualizar_banco_de_dados para poder reescrever todo o arquivo com o novo estado
da lista. A função carregar_banco_de_dados também é uilizada na inicialização do banco,
dentro da função init deste arquivo.
"""
def salvar(usuario):        
    con.banco_de_dados = bd.salvar(usuario)

def remover(usuario):
    con.banco_de_dados.remove(usuario)
    bd.atualizar_banco_de_dados(con.banco_de_dados)

def atualizar(usuario, idx):
    con.banco_de_dados[idx] = usuario
    bd.atualizar_banco_de_dados(con.banco_de_dados)