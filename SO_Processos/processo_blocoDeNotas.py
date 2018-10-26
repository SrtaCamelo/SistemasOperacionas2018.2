#Sistemas Operacionas 2018.2
#Raissa Camelo
#Atividade: Processos - Programa
#---------------------
import os
import msvcrt
#---------------------Definição da Estrutura (SO)----------
process_list = []
#-------------------Definição de funções--------------------------
def inicialize_process():
    estado_processo_bdn = ""
    buffer_bdn = ""
    open = True
    estado_processo_bdn = "New"
    print(estado_processo_bdn)
    return open, estado_processo_bdn, buffer_bdn
def run_process(estado_processo_bdn):
    estado_processo_bdn = "Running"
    print(estado_processo_bdn)
def make_wait_process(estado_processo_bdn):
    estado_processo_bdn = "Waiting"
    print(estado_processo_bdn)
def resume_process(estado_processo_bdn):
    run_process(estado_processo_bdn)
def terminate_process(open,estado_processo_bdn,buffer_bdn):
    open = False
    buffer_bdn = ""
    estado_processo_bdn = "Terminated"
    print(estado_processo_bdn)
    return open
def save_file(buffer_bdn,estado_processo_bdn):
    print("Saving File")
    print(buffer_bdn)
    resume_process(estado_processo_bdn)

def minimize(estado_processo_bdn, buffer_bdn):
    tuple = (estado_processo_bdn,buffer_bdn)
    process_list.append(tuple)
    so()

def re_open():
    tuple = process_list[-1]
    estado_processo_bdn = tuple[0]
    buffer_bdn = tuple[1]
    resume_process(estado_processo_bdn)
    blocoDeNotas(False,open, estado_processo_bdn, buffer_bdn)

"""
-----"BOTÕES":
X - EXIT
C - SAVE FILE
V - MINIMIZE
"""
def blocoDeNotas(new,open, estado_processo_bdn, buffer_bdn):
    if new:
        open, estado_processo_bdn, buffer_bdn = inicialize_process()
        run_process(estado_processo_bdn)
    while open:
        input_stream = input()
        buffer_bdn += input_stream
        if input_stream == 'X':
            open = terminate_process(open, estado_processo_bdn,buffer_bdn)
        elif input_stream == 'C':
            make_wait_process(estado_processo_bdn)
            save_file(buffer_bdn,estado_processo_bdn)
        elif input_stream == 'V':
            make_wait_process(estado_processo_bdn)
            minimize(estado_processo_bdn,buffer_bdn)


#--------------------Código Principal-----------------------------
#--------Call : Bloco de Notas-----------------------------
"""
BOTÕES:
B : Abre o Bloco de Notas
V : Muda pra janela do bloco de notas (minimizada)
"""
def so():
    on = True
    while on:
        input_stream = input()
        if input_stream == 'B':
            blocoDeNotas(True,"","","")
        elif input_stream == 'V':
            re_open()
#----------Turn On S.O
so()

