import controle as c

msg = c.salvar("Fernanda", "980776622", "123")
print(msg)
msg = c.salvar("José", "980672351", "321")
print(msg)
msg = c.salvar("Maria", "9288997382", "321")
print(msg)

resultado = c.pesquisar_por_nome("José")
print("Usuário encontrado: ", *resultado, sep="\n")

resultado = c.listar_todos()
print(*resultado, sep="\n")
