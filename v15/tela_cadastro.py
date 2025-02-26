import flet as ft
import controle as con

componentes = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](),               
        #add todos os compontens da tela aqui
    }

def view():     
    return ft.View(
                "tela1",
                [      
                    ft.Container(content=ft.Text("Cadastro", size=20)),
                    ft.TextField(label='Nome', ref=componentes['tf_nome'], autofocus=True),
                    ft.TextField(label='Telefone', ref=componentes['tf_telefone'], on_submit=cadastrar),
                    ft.Row(
                        [
                            ft.ElevatedButton('Cadastrar', icon='save', on_click=cadastrar),
                        ],
                        alignment=ft.MainAxisAlignment.END                   
                    ),                                                                                 
                ],
                navigation_bar=con.barra_navegacao(), 
                appbar= ft.AppBar(            
                    title=ft.Text("Sistema de cadastro"),
                    center_title=False,
                    bgcolor=ft.colors.SURFACE_VARIANT,                    
                ),                   
            )

def cadastrar(e):    
    usuario = {
        'nome' : componentes['tf_nome'].current.value,
        'telefone' : componentes['tf_telefone'].current.value
    }    
    
    con.banco_de_dados.append(usuario)
    componentes['tf_nome'].current.value = ""
    componentes['tf_telefone'].current.value = ""    
    con.page.update()
