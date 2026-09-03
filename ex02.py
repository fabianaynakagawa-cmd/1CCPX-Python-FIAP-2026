email = input('Digite aqui sua lista de emails (separado por vírgula): ')
lista_emails = email.split(", ")

usuario = []
contagem_dominio = dict()

for emails in lista_emails:
    parte = emails.split('@')
    dominio = parte[1]

    if dominio not in contagem_dominio:
        contagem_dominio[dominio] = 1
    else:
        contagem_dominio[dominio] += 1

    usuario.append(parte[0])

tuple_usuario = tuple(usuario)

# Trocar primeiro e último usando a, b = b, a
a = tuple_usuario[0]
b = tuple_usuario[-1]
a, b = b, a

# Reconstruindo a tupla com a troca aplicada
lista_troca = list(tuple_usuario)
lista_troca[0] = a
lista_troca[-1] = b
tupla_trocada = tuple(lista_troca)

# Relatório final
print('Relatório:')
print(f'Quantidade de e-mails por domínio: {contagem_dominio}')
print(f'Lista de usuários: {tuple_usuario}')
print(f'Após troca de posições: {tupla_trocada}')