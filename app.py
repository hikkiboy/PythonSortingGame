import random

array = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(array)
sortedlist = array[:]
sortedlist.sort()
print("seu objetivo: ", sortedlist)
print("sua lista: ",array)
op = int(input('Escolhe o número para mover: '))
MoveCount = 0

while True:
    for x in array:
        if op == x:
            change = int(input('escolha um numero para trocar de lugar com o escolhido: '))
            currentPos = array.index(op)
            futurePos = array.index(change)
            
            if currentPos > futurePos:
                
                array.pop(currentPos)
                array.pop(futurePos)
                array.insert(futurePos,op)
                array.insert(currentPos, change)
                print(array)
                MoveCount += 1
                if sortedlist == array:
                    print(f"Parabéns ! Você ganhou em {MoveCount} movimentos!")
                    break
                else:
                    op = int(input('Escolha outro número para mover: '))
                
            elif futurePos > currentPos:
                array.pop(currentPos)
                array.pop(futurePos - 1)
                array.insert(futurePos - 1,op)
                array.insert(currentPos, change)
                print(array)
                MoveCount += 1
                if sortedlist == array:
                    print(f"Parabéns ! Você ganhou em {MoveCount} movimentos!")
                    break
                else:
                    op = int(input('Escolha outro número para mover: '))
                


