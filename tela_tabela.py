import flet as ft
import controle as con

def view():     
    return ft.View(
                "tela2",
                [                           
                    ft.DataTable(
                        width=float('inf'),
                        ref=con.componentes['tf_tabela'],
                        columns=[
                            ft.DataColumn(ft.Text('Nome')),
                            ft.DataColumn(ft.Text('Telefone')),
                            ft.DataColumn(ft.Text('CPF')),
                            ft.DataColumn(ft.Text('Endereço')),
                            ft.DataColumn(ft.Text('E-mail')),
                            ft.DataColumn(ft.Text('Sexo')),
                            ft.DataColumn(ft.Text('Uf'))
                        ]
                    )               
                ],
                navigation_bar=con.barra_navegacao()                    
            )