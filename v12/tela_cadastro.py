import flet as ft
import v12.controle as con 


def view():     
    return ft.View(
                "tela1",
                [                           
                    ft.Column([
                        ft.Row([
                            ft.Container(content=ft.Text('Nome:', size=20), width=150),
                            ft.TextField(label='Nome', ref=con.componentes['tf_nome'])
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Telefone:', size=20), width=150),
                            ft.TextField(label='Telefone', ref=con.componentes['tf_telefone'])
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('CPF:', size=20), width=150),
                            ft.TextField(label='Cpf',ref=con.componentes['tf_cpf'])
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Endereço:', size=20), width=150),
                            ft.TextField(label='Endereço', multiline=True, ref=con.componentes['tf_endereco'])
                        ]),#Row 
                        ft.Row([
                            ft.Container(content=ft.Text('E-mail:', size=20), width=150),
                            ft.TextField(label='E-mail', ref=con.componentes['tf_email'])
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Sexo:', size=20), width=150),
                            ft.RadioGroup(
                                ref=con.componentes['tf_sexo'],
                                content=ft.Row([
                                    ft.Radio(value='1', label='M'),
                                    ft.Radio(value='2', label='F')
                                ])
                            )
                        ]),#Row
                        ft.Row([
                            ft.Container(content=ft.Text('Uf:', size=20), width=150),
                            ft.Dropdown(
                                ref=con.componentes['tf_uf'], 
                                label='UF', 
                                options=[
                                    ft.dropdown.Option('PA'),
                                    ft.dropdown.Option('SP'),
                                    ft.dropdown.Option('RJ'),
                                    ft.dropdown.Option('MA'),
                                    ft.dropdown.Option('RS')
                                ]
                            )
                        ]),
                        ft.ElevatedButton('Cadastrar', icon='save', on_click=con.cadastrar(con.componentes))
                    ])                  
                ],
                navigation_bar=con.barra_navegacao()             
            )