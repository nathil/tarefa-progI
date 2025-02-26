import flet as ft
import controle as con
import re

componentes = {        
        'tabela': ft.Ref[ft.DataTable](),   
        'tf_pesquisa': ft.Ref[ft.TextField]()    
        #add todos os compontens da tela aqui
    }

def view():     
    return ft.View(
                "tela2",
                [             
                    ft.TextField(ref=componentes['tf_pesquisa'], label='pesquisar', icon='search',
                                 on_change=pesquisar),              
                    ft.DataTable(
                            width=float('inf'),
                            ref=componentes['tabela'],                                                    
                            columns=[
                                ft.DataColumn(ft.Text("Nome")),
                                ft.DataColumn(ft.Text("Telefone")),      
                                ft.DataColumn(ft.Text("Cpf")), 
                                ft.DataColumn(ft.Text("Endereço")), 
                                ft.DataColumn(ft.Text("E-mail")), 
                                ft.DataColumn(ft.Text("Sexo")), 
                                ft.DataColumn(ft.Text("Uf")), 
                                ft.DataColumn(ft.Text("Ações")),                                                       
                            ],
                            #rows=[] são ser carregadas dinamicamente
                         ),                                                                         
                ],
                navigation_bar=con.barra_navegacao(), 
                appbar= ft.AppBar(            
                    title=ft.Text("Sistema de cadastro"),
                    center_title=False,
                    bgcolor=ft.colors.SURFACE_VARIANT,                    
                ),                   
            )
def atualizar_tabela():
    return [
            ft.DataRow(cells=preencher_linha_tabela(cadastro)) for cadastro in con.banco_de_dados
        ]


def preencher_linha_tabela(cadastro):
    return [
                ft.DataCell(ft.Text(cadastro['nome'])),
                ft.DataCell(ft.Text(cadastro['telefone'])),
                ft.DataCell(ft.Text(cadastro['cpf'])),
                ft.DataCell(ft.Text(cadastro['endereco'])),
                ft.DataCell(ft.Text(cadastro['email'])),
                ft.DataCell(ft.Text(cadastro['sexo'])),
                ft.DataCell(ft.Text(cadastro['uf'])),
                ft.DataCell(ft.Row(
                     [
                            ft.IconButton(
                                icon=ft.icons.EDIT,
                                icon_color="blue",
                                icon_size=35,
                                tooltip="Atualizar",  
                                key=cadastro,
                                on_click=atualizar                              
                            ),
                            ft.IconButton(
                                icon=ft.icons.REMOVE_CIRCLE,
                                icon_color="red",
                                icon_size=35,
                                tooltip="Remover",
                                key=cadastro,
                                on_click=deletar
                            ),
                        ]
                ))                                                           
        ]



def remover_acentos(txt: str) -> str:
    txt = re.sub("[âãáà]", "a", txt) 
    txt = re.sub("[êéè]", "e", txt)  
    txt = re.sub("[îíì]", "i", txt) 
    txt = re.sub("[ôõóò]", "o", txt) 
    txt = re.sub("[ûúù]", "u", txt) 
    return txt 


def validar_filtro(query, cadastro):
    tem_letra = bool(re.search('[a-zA-Z]', query))
    if tem_letra:
        query_min = query.lower() 
        query_min = remover_acentos(query_min) #removendo todas as vogais acentuadas 
        if query_min in remover_acentos(cadastro['nome'].lower()):
            return True
    return query in cadastro['telefone']


def filtrar_dados(query):
    return [
            ft.DataRow(cells=preencher_linha_tabela(cadastro))
            for cadastro in con.banco_de_dados
            if validar_filtro(query, cadastro)
        ]

def pesquisar(e):
    query = componentes['tf_pesquisa'].current.value
    componentes['tabela'].current.rows = filtrar_dados(query)
    con.page.update()

"""
A função deletar foi modificada para utilizar a função salvar do arquivo controle
"""
def deletar(e):
    usuario = e.control.key
    con.remover(usuario)
    componentes['tabela'].current.rows = atualizar_tabela()
    con.page.update()

def atualizar(e):
    usuario = e.control.key    
    con.tela_atualizar.init(usuario)
    con.page.go('3')

#fazer a mesma coisa da tarefa da pesquisa, refinar mais e aumentar o formulario 