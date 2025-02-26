"""
    V 15.0
    Nesta versão inserimos o campo de pesquisa na tela que tem a tabela. Para isso 
    adicionamos um referência para um componente TextField no nosso dicionário de
    componentes. Em seguida, adicionamos um TextField na nossa árvore de componentes
    da View e utilizamos a referência. Neste campo TextField nós também passamos a
    função pesquisar como argumento para o parâmetro on_change. Essa função será
    chamada toda vez que o utuário digitar alguma coisa neste campo de texto.
    Na função pesquisar estamos recuperando o valor que o usuário digitou e estamos
    passando essa string como argumento da função filtrar_dados. A função filtrar
    dados utiliza essa informação para filtrar do banco de dados somente os cadastros
    cujo nome ou telefone tenha como substring o valor da query. Os cadastos filtrados
    sofrem um mapeamento para construir as linhas da tabela. A lista de retorno da 
    funçõa filtrar_dados atualiza as linhas correntes da tabela. Como houve mudança
    nos componentes visuais da tela, foi necessário chamar a função update da página.

"""
import flet as ft
import controle as con

def main(page: ft.Page):   
    con.init(page)         
    page.title = "Sistema de cadastro"           
    page.on_route_change = con.controle_de_rota  
    page.theme_mode  = "light"
    page.go('1')


ft.app(target=main)

