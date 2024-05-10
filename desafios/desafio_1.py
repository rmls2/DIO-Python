N = int(input())
casos = ''

while(N > 0):
    count = 0
    indice_B = 0

    A = input()
    B = ''
    for i in A: 
        indice_B +=1 
        if i == ' ':
            B = A[indice_B:]
            break
    A = A[:indice_B-1]
    
    print('este é o A:{}, este é o B:{}'.format(A, B))

    diferenca_A_B = len(A) - len(B)

    if len(A) >= len(B):
        for i in range(len(B)):
            if A[diferenca_A_B] == B[i]:
                count += 1
                diferenca_A_B += 1  
        if count == len(B):
            print('encaixa') 
        else:
            print('nao encaixa')         
    else:
        print('nao encaixa')  
    N -= 1