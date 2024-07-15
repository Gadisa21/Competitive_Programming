t = int(input())

for _ in range(t):
    n, p = map(int, input().split())
    # A função map() é uma função embutida que permite aplicar uma função a todos os elementos de um ou mais iteráveis, como listas
    
    # Lê-se os valores de a e b
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # Cria-se uma lista de pares (custo b, número máximo a)
    vec = [(b[i], a[i]) for i in range(n)]
    
    # Ordena-se a lista com base no custo crescente de compartilhamento
    vec.sort()
    
    # Inicializa-se o custo total com p
    res = p
    # Inicializa-se o número total de residentes notificados com 1 
    reached = 1
    
    j = 0
    while reached < n:
        if vec[j][0] > p:
            # Se o custo de compartilhamento do residente for mais alto do que p
            res += p
            reached += 1
        else:
            # Se não, usa-se o residente para compartilhar
            if reached + vec[j][1] > n:
                # Se o residente pode alcançar mais residentes do que os restantes a serem notificados
                res += vec[j][0] * (n - reached)
                reached = n
            else:
                # Se não, o residente compartilha com o máximo de residentes que ele pode
                res += vec[j][0] * vec[j][1]
                reached += vec[j][1]
        j += 1

    print(res)