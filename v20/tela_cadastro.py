import flet as ft
import controle as con

componentes = {
        'tf_nome': ft.Ref[ft.TextField](),
        'tf_telefone': ft.Ref[ft.TextField](),     
        'tf_cpf':ft.Ref[ft.TextField](), 
        'tf_endereco':ft.Ref[ft.TextField](),
        'tf_email':ft.Ref[ft.TextField](),
        'tf_sexo':ft.Ref[ft.RadioGroup](),
        'tf_uf':ft.Ref[ft.Dropdown]()
        #add todos os compontens da tela aqui
    }

def view():     
    return ft.View(
                "tela1",
                [      
                    ft.Container(content=ft.Text("Cadastro", size=20)),
                                        ft.Column([
                        ft.Row([
                            ft.Container(content=ft.Text('Nome:', size=20), width=150),
                            ft.TextField(label='Nome', ref=componentes['tf_nome'])
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Telefone:', size=20), width=150),
                            ft.TextField(label='Telefone', ref=componentes['tf_telefone'])
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('CPF:', size=20), width=150),
                            ft.TextField(label='Cpf',ref=componentes['tf_cpf'])
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Endereço:', size=20), width=150),
                            ft.TextField(label='Endereço', multiline=True, ref=componentes['tf_endereco'])
                        ]),#Row 
                        ft.Row([
                            ft.Container(content=ft.Text('E-mail:', size=20), width=150),
                            ft.TextField(label='E-mail', ref=componentes['tf_email'])
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Sexo:', size=20), width=150),
                            ft.RadioGroup(
                                ref=componentes['tf_sexo'],
                                content=ft.Row([
                                    ft.Radio(value='1', label='M'),
                                    ft.Radio(value='2', label='F')
                                ])
                            )
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Uf:', size=20), width=150),
                            ft.Dropdown(
                                ref=componentes['tf_uf'], 
                                label='UF', 
                                options=[
                                    ft.dropdown.Option('PA'),
                                    ft.dropdown.Option('SP'),
                                    ft.dropdown.Option('RJ'),
                                    ft.dropdown.Option('MA'),
                                    ft.dropdown.Option('RS')
                                ])
                            ]
                        ),
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
        ]
    )

"""
A função cadastrar foi modificada para utilizar a função salvar do arquivo controle
"""
def cadastrar(e):    
    usuario = {        
        'nome' : componentes['tf_nome'].current.value,
        'telefone' : componentes['tf_telefone'].current.value
    }    
    
    con.salvar(usuario)
    componentes['tf_nome'].current.value = ""
    componentes['tf_telefone'].current.value = ""    
    con.page.update()
