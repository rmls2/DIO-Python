saida = []

def total_de_garrafas(): 

    T = int(input())
    for i in range(T):
        entrada = input()
        n, k = entrada.split(' ')

        n = int(n)
        k = int(k)

        garrafas_sobradas = n%k
        
        garrafas_trocadas = n // k 
        
        total = garrafas_trocadas + garrafas_sobradas
        saida.append(total)
    
    return saida
  
for i in total_de_garrafas():
    print(i)

# saida = []
# def total_de_garrafas(lista): 

#     T = int(input())
#     for i in range(T):
#         entrada = input()
#         n, k = entrada.split(' ')

#         n = int(n)
#         k = int(k)

#         garrafas_sobradas = n%k
        
#         garrafas_trocadas = n // k 
        
#         total = garrafas_trocadas + garrafas_sobradas
#         saida.append(total)
#         print(total)
    
  

# total_de_garrafas()