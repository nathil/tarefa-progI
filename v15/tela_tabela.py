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
                    ft.TextField(ref=componentes['tf_pesquisa'], label='Pesquisar', icon='search',
                                 on_change=pesquisar),              
                    ft.DataTable(
                            width=float('inf'),
                            ref=componentes['tabela'],                                                    
                            columns=[
                                ft.DataColumn(ft.Text("Nome")),
                                ft.DataColumn(ft.Text("Telefone")),                                                                                                
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
                ft.DataCell(ft.Text(cadastro['telefone']))                                                           
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
            #if query in cadastro['nome'] or query in cadastro['telefone']
        ]

def pesquisar(e):
    query = componentes['tf_pesquisa'].current.value
    componentes['tabela'].current.rows = filtrar_dados(query)
    con.page.update()

