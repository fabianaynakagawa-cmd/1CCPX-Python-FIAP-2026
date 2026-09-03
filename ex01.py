email = (input('Digite aqui su lista de emails (separado por virgula): '))
lista_emails = email.split(", ")

contagem_dominio = dict()   

for emails in lista_emails:
    parte = emails.split("@")
    dominio = parte[1]

    if dominio not in contagem_dominio:
        contagem_dominio[dominio] = 1
    else:
        contagem_dominio[dominio] += 1
print(contagem_dominio)