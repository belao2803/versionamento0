candidatos = {
    1 : {'nome:' "Luiz Inacio", 'partido:' "PT"},
    2 : {'nome:' "Deodoro da Fonseca", 'partido:' "PRE"},
    3 : {'nome:' "Prudente de Morais", 'partido:' "PL"},
    4 : {'nome:' "Jair Bolsonaro", 'partido:' "PL"}
}

Governo = int(input("Digite o Numero do seu Candidato: "))

if Governo in candidatos:
    print(candidatos[Governo])
else:
    print("Candidato não encontrado.")