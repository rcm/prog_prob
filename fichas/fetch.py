import os

alunos = """pg47607;Ricardo da Silva Correia;https://github.com/ricardocorreia99/Trabalhos-de-casa-Programa-o-probabilistica
pg47474;Maria Inês Machado Correia Brioso Dias;https://github.com/ines-correiadias/Programacao_Probabilistica_FICHAS.git
pg47446;Márcio Eduardo Lima Mano;https://github.com/mArcio-Lmano/prog_prob2021
pg47622;Rodrigo da Silva Gomes Peres Coelho;https://github.com/RodrigoCoelho7/Probabilistic-Programming.git
pg47264;Irving Leander Reascos Valencia;https://github.com/LeanderReascos/probabilistic_programming
pg45927;Catarina Assis Quintela Madaleno;https://github.com/catarinamadaleno/prog_prob
a89135;Pedro Daniel Lopes Mendes;https://github.com/DanieMendes/Prog_Prob
pg47339;João Pedro Sá Gomes;https://github.com/JoaoPedro9400/Fichas-PP
pg46949;Alexandre de Jesus Sousa e silva;https://github.com/alexandre04032000/Ficha2
pg47478;Maria João Barroso Portela;https://github.com/MJoaoPortela/Programa-o-Probabilistica
a89140;Tomás Esperança Ferreira;https://github.com/TomasAcadem/ProgProb"""

alunos = [linha.split(";") for linha in alunos.splitlines()]
current = os.getcwd()
for num,nome,git in alunos:
    print(num, nome.replace(" ", "_"), git)
    dir = nome.replace(" ", "_")
    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok = True)
        os.chdir(dir)
        os.system(f"git clone {git}")
        os.chdir(current)
