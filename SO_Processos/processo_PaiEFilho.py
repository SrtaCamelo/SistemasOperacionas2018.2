#Sistemas Operacionas 2018.2
#Raissa Camelo
#Atividade: Processos - Pai e Filho

from anytree import Node, RenderTree

#-----------Estuturas-------------


def process2():
    print("Processo filho")
def process3():
    print("Processo filho dois")
def create_process():
    print("Entrou no processo Pai")
    process2()
    process3()
    print("Saiu do pai")


#------------------Main Code------------
create_process()