#Sistemas Operacionas 2018.2
#Raissa Camelo
#Atividade: Processos - Pai e Filho

from anytree import Node, RenderTree

#-----------Estuturas-------------
process_list = []

def create_process(parent_id, parent):
    process_id = parent_id + 1

#------------------Main Code------------
"""
BOTÕES:
N : Cria novo processo (Filho)
V : Muda pra janela do bloco de notas (minimizada)
"""
def so():
    on = True
    while on:
        input_stream = input()
        if input_stream == 'B':
            create_process(0,0)
        elif input_stream == 'V':
#----------Turn On S.O
so()