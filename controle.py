# utilizar os conceitos de manipulação de lista dicionario, lista, filtro = flet 

banco_de_dados = []

def salvar(nome, telefone, cpf):
    #verifica se há cpf repetidos
    if cpf_disponivel(cpf):
        cadastro = {
            "nome": nome, "telefone": telefone, "cpf":cpf
        }        


        banco_de_dados.append(cadastro)
        return "Usuário salvo com sucesso"
    else:
        return "Erro ao cadastrar usuário, CPF já utilizado!"


def pesquisar_por_nome(pesquisa):
    pesquisar = [formatar(cadastros) for cadastros in banco_de_dados
            if cadastros["nome"].startswith(pesquisa)]
    
    if not pesquisar:
        return "Usuário não encontrado"
    else:
        return pesquisar 

def listar_todos():
    return [formatar(cadastro) for cadastro in banco_de_dados]

def formatar(cadastro):
    return f"\nnome: {cadastro["nome"]}\ntelefone: {cadastro["telefone"]}\ncpf: {cadastro["cpf"]}\n"


def cpf_disponivel(cpf):
    lista = [cadastro for cadastro in banco_de_dados 
             if cadastro['cpf'] == cpf]
    return len(lista) == 0

#########################################


"""
def verificar_cpfs_repetidos():
    cpfs = [cadastro["cpf"] for cadastro in banco_de_dados]
    cpfs_repetidos = set([cpf for cpf in cpfs if cpfs.count(cpf) > 1])
    return cpfs_repetidos"""

"""def cpf_duplicado(cpf):
    lista = [cadastro for cadastro in banco_de_dados 
             if cadastro['cpf'] == cpf]
    return len(lista) > 0
"""
