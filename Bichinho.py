class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 20
        self.saude = 80
        self.idade = 1
    def AlterarNome(self, novoNome):
        self.nome = novoNome
    def AlterarFome(self, valorF):
        self.fome += valorF
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0
    def AlterarSaude(self, valorS):
        self.saude += valorS
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0
    def AlterarIdade(self):
        self.idade += 1
    def RetornarNome(self):
        return self.nome
    def RetornarFome(self):
        return self.fome
    def RetornarSaude(self):
        return self.saude
    def RetornarIdade(self):
        return self.idade
    def RetornarHumor(self):
        humor = self.saude + self.fome 
        return humor

nomeB = input('Qual o nome que deseja colocar no seu bichinho? ')
Bichinho = BichinhoVirtual(nome = nomeB)
while (Bichinho.saude > 0) and (Bichinho.fome < 100):
    Bichinho.AlterarFome(+2)
    Bichinho.AlterarSaude(-2)
    Bichinho.AlterarIdade()
    resposta = input(f"""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
     \nOlá meu nome é {Bichinho.nome}. \n
     Humor: {Bichinho.RetornarHumor()}\n
     Idade: {Bichinho.RetornarIdade()}\n
     Fome: {Bichinho.RetornarFome()}\n
     Saude: {Bichinho.RetornarSaude()}\n
     O que você deseja fazer comigo agora? \n
     1- Alimentar (-10 de fome)\n
     2- Dormir (+10 de saúde)\n
     3- Alterar nome\n
     Resposta: """)
    print('\n')
    if resposta == '1':
        Bichinho.AlterarFome(-10)
        print("-10 de fome! Obrigado!")
    elif resposta == '2':
        Bichinho.AlterarSaude(+10)
        print("+10 de saúde! Obrigado!")
    elif resposta == '3':
        nome2 = input('Qual nome deseja colocar? \n')
        Bichinho.AlterarNome(nome2)
    else:
        print('Escolha um número válido!')
else:
    print(f"""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\n{Bichinho.nome} morreu!\n""")
