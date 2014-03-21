
"""""""""""""""""""""""""""""""""""""""""""""""""""
Программа для зашифровки или дешифровки сообщений 
                шифра Цезаря
                                                
"""""""""""""""""""""""""""""""""""""""""""""""""""

#Подготовила:
"""Решетникова Мария Федоровна"""
# ИКТ - 13, 1 курс
#2014


"""Обобщенная функция поиска символа из зашифрованной строки 
             и его последующая замена"""
             
def poisk1(dana_stroka, stroka2, stroka, rez_stroka):
    for char in dana_stroka:
        #Вычисление порядкового номера символа в алфавите. 
        #Самый распространенный случай: строчный символ
        index=stroka.find(char)
        if index==-1:
            #Прописной символ
            index=stroka2.find(char)
            #если символ не буква, то мы его просто переносим 
            #в том же "состоянии" в результирующую строку (к примеру, пробел)
            if index==-1:
                rez_stroka=rez_stroka+char
            else:
                #сли символ - заглавная буква, поиск и нахождение его индекса
                #осуществляется по второй строке
                rez_stroka=poisk(index,stroka2,shag,rez_stroka)
        #обычная расшифровка прописного символа
        else:
            rez_stroka=poisk(index,stroka,shag,rez_stroka)
    return rez_stroka
    
    
"""Функция производящая замену символа
из зашифрованной строки в символ, соответствующий
             ее расшифрованному коду"""
             
def poisk(index,stroka,shag,rez_stroka):
#Проверка символа на возможность реализации простого алгоритма замены
    if index<(len(stroka)-shag): 
            rez_stroka=rez_stroka+str(stroka[index+shag])
#Если символ, стоит в конце алфавита, к примеру x или y, 
#то прибавить к его индексу просто шаг нельзя
    else:
        m=shag-len(stroka)+index #вычисляем индекс символа-замены
        rez_stroka=rez_stroka+str(stroka[m])
    return rez_stroka

    
"""Строки, используемые в функциях преобразования"""

stroka="abcdefghijklmnopqrstuvwxyz"
stroka2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rez_stroka=""   
    
"""ВВод строки, которую нужно расшифровать или зашифровать"""

dana_stroka=raw_input("Enter string:") 

#Получение информации о наличии или отсутствии шага
sh=raw_input("Do you know step?(y/n)")

#Если шаг известен
if sh=="y":    
    shag=int(raw_input("Enter step:")) #ввод шага
    rez_stroka=poisk1(dana_stroka, stroka2, stroka, rez_stroka)
    print (rez_stroka)
#если шаг не известен    
else:
    print(" ")
    print ("possible decryption:") #выводим возможные зашифрованные сообщения 
    print(" ")
    for shag in range(1,27): 
        rez_stroka=poisk1(dana_stroka, stroka2, stroka, rez_stroka)
        print (rez_stroka+" step="+str(shag))
        rez_stroka=""
        