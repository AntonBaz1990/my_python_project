import os

os.system('cls')
import random

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def showmatrix() :
    return f'{matrix[0]} {matrix[1]} {matrix[2]} \n{matrix[3]} {matrix[4]} { matrix[5]} \n{matrix[6]} {matrix[7]} {matrix[8]} \n'



def check () :
    if matrix[0] == matrix[1] == matrix[2]:
        print(f'WINNER!!! {matrix[0]}')
        return 1
    if matrix[3] == matrix[4] == matrix[5]:
        print(f'WINNER!!! {matrix[0]}')
        return 1
    if matrix[6] == matrix[7] == matrix[8]:
        print(f'WINNER!!! {matrix[0]}')
        return 1
    if matrix[0] == matrix[3] == matrix[6]:
        print(f'WINNER!!! {matrix[0]}')
        return 1
    if matrix[1] == matrix[4] == matrix[7]:
        print(f'WINNER!!! {matrix[0]}')
        return 1
    if matrix[2] == matrix[5] == matrix[8]:
        print(f'WINNER!!! {matrix[0]}')
        return 1
    if matrix[0] == matrix[4] == matrix[8]:
        print(f'WINNER!!! {matrix[0]}')
        return 1
    if matrix[2] == matrix[4] == matrix[6]:
        print(f'WINNER!!! {matrix[0]}')
        return 1   
    else : return 0      

 


























def player () :
    while True:
        try :
            number = int(input("Введите номер ячейки: "))
            if (matrix[number-1] != 'x') and (matrix[number-1] != 'O') :        
             matrix[number-1] = 'x'
             break
            else :
                print('Неверный ввод!!! Ячейка занята')

        except :
            print('неверный ход!!!')





def comp(matrix) :
    for i in range(0, len(matrix)) :
        if (matrix[i] !='x') and (matrix[i] !='O') :
            matrix[i] ='O'
            return
   
showmatrix()
while True:       
    player ()
    showmatrix()
    if check () == 1:
        break
    comp(matrix)
    showmatrix() 
    if check () == 1:
        break

    
