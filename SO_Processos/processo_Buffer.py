#Sistemas Operacionas 2018.2
#Raissa Camelo
#Atividade: Processos - Buffer

#----------------Def Structs---------------
buffer = []
buffer_size = 5
buffer_index = 0

def appendBuffer(item,buffer_index):
    if buffer_index < buffer_size:
        buffer.append(item)
        buffer_index += 1
        print("Um item foi adicionado ao Buffer")
    else:
        print("Não pode adicionar ao Buffer, está lotado")
    return buffer_index
def removeBuffer(buffer_index):
    if buffer_index > 0:
        buffer.pop()
        buffer_index -= 1
        print("Item removido do buffer")
    else:
        print("Não pode remover, buffer vazio")
    return buffer_index

#-------------------Main-----------------------
#----- A: add no buffer
#----- R: remove do buffer
while True:
    print(buffer)
    char = input("Digite a opção: \n")
    if char == 'A':
        item = input("Digite item a ser add:\n")
        buffer_index = appendBuffer(item,buffer_index)
    elif char == 'R':
        buffer_index = removeBuffer(buffer_index)
