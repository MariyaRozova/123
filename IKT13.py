
"""""""""""""""""""""""""""""""""""""""""""""""""""
��������� ��� ���������� ��� ���������� ��������� 
                ����� ������
                                                
"""""""""""""""""""""""""""""""""""""""""""""""""""

#�����������:
"""����������� ����� ���������"""
# ��� - 13, 1 ����
#2014


"""���������� ������� ������ ������� �� ������������� ������ 
             � ��� ����������� ������"""
             
def poisk1(dana_stroka, stroka2, stroka, rez_stroka):
    for char in dana_stroka:
        #���������� ����������� ������ ������� � ��������. 
        #����� ���������������� ������: �������� ������
        index=stroka.find(char)
        if index==-1:
            #��������� ������
            index=stroka2.find(char)
            #���� ������ �� �����, �� �� ��� ������ ��������� 
            #� ��� �� "���������" � �������������� ������ (� �������, ������)
            if index==-1:
                rez_stroka=rez_stroka+char
            else:
                #��� ������ - ��������� �����, ����� � ���������� ��� �������
                #�������������� �� ������ ������
                rez_stroka=poisk(index,stroka2,shag,rez_stroka)
        #������� ����������� ���������� �������
        else:
            rez_stroka=poisk(index,stroka,shag,rez_stroka)
    return rez_stroka
    
    
"""������� ������������ ������ �������
�� ������������� ������ � ������, ���������������
             �� ��������������� ����"""
             
def poisk(index,stroka,shag,rez_stroka):
#�������� ������� �� ����������� ���������� �������� ��������� ������
    if index<(len(stroka)-shag): 
            rez_stroka=rez_stroka+str(stroka[index+shag])
#���� ������, ����� � ����� ��������, � ������� x ��� y, 
#�� ��������� � ��� ������� ������ ��� ������
    else:
        m=shag-len(stroka)+index #��������� ������ �������-������
        rez_stroka=rez_stroka+str(stroka[m])
    return rez_stroka

    
"""������, ������������ � �������� ��������������"""

stroka="abcdefghijklmnopqrstuvwxyz"
stroka2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rez_stroka=""   
    
"""���� ������, ������� ����� ������������ ��� �����������"""

dana_stroka=raw_input("Enter string:") 

#��������� ���������� � ������� ��� ���������� ����
sh=raw_input("Do you know step?(y/n)")

#���� ��� ��������
if sh=="y":    
    shag=int(raw_input("Enter step:")) #���� ����
    rez_stroka=poisk1(dana_stroka, stroka2, stroka, rez_stroka)
    print (rez_stroka)
#���� ��� �� ��������    
else:
    print(" ")
    print ("possible decryption:") #������� ��������� ������������� ��������� 
    print(" ")
    for shag in range(1,27): 
        rez_stroka=poisk1(dana_stroka, stroka2, stroka, rez_stroka)
        print (rez_stroka+" step="+str(shag))
        rez_stroka=""
        