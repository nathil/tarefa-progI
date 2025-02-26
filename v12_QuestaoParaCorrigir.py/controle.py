import v12.tela_cadastro as tela_cadastro, v12.tela_tabela as tela_tabela
import flet as ft

componentes = { 
    'tf_nome': ft.Ref[ft.TextField](), 
    'tf_telefone': ft.Ref[ft.TextField](), 
    'tf_cpf': ft.Ref[ft.TextField](), 
    'tf_endereco': ft.Ref[ft.TextField](), 
    'tf_email': ft.Ref[ft.TextField](), 
    'tf_sexo': ft.Ref[ft.RadioGroup](), 
    'tf_uf': ft.Ref[ft.Dropdown](),
    'tf_tabela': ft.Ref[ft.DataTable]()
} 

def preencher_linha_tabela(cadastro):
    return [
                ft.DataCell(ft.Text(cadastro['nome'])),
                ft.DataCell(ft.Text(cadastro['telefone'])),
                ft.DataCell(ft.Text(cadastro['cpf'])),
                ft.DataCell(ft.Text(cadastro['endereco'])),
                ft.DataCell(ft.Text(cadastro['email'])),
                ft.DataCell(ft.Text(cadastro['sexo'])),
                ft.DataCell(ft.Text(cadastro['uf']))
        ]

def atualizar_tabela():
    return [
            ft.DataRow(cells=preencher_linha_tabela(cadastro))
            for cadastro in banco_de_dados
        ]

banco_de_dados = []

def cadastrar(e): 
    usuario = {
        'nome' : componentes['tf_nome'].current.value,
        'telefone' : componentes['tf_telefone'].current.value,
        'cpf' : componentes['tf_cpf'].current.value,
        'endereco' : componentes['tf_endereco'].current.value,
        'sexo' : componentes['tf_email'].current.value,
        'email' : componentes['tf_sexo'].current.value,
        'uf' : componentes['tf_uf'].current.value
    }

    banco_de_dados.append(usuario) 
    componentes['tf_nome'].current.value = ""
    componentes['tf_telefone'].current.value = ""
    componentes['tf_cpf'].current.value = ""
    componentes['tf_endereco'].current.value = ""
    componentes['tf_email'].current.value = ""
    componentes['tf_sexo'].current.value = ""
    componentes['tf_uf'].current.value = ""
    componentes['tf_tabela'].current.rows = atualizar_tabela()
    page.update()

def init(p):
    global page, telas
    page = p
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
                        on_change= lambda e: page.go(str(e.control.selected_index+1))
            )#NavigationBar