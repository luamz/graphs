# https://www.beecrowd.com.br/judge/en/problems/view/1152

import heapq

def kruskal(n, m):
    total_illuminated = 0
    min_cost = 0
    H = []
    C = [[] * n for i in range(n)]
    S = []

    for j in range(m):
        a, b, c = map(int, input().split())  # Edge from a to b with cost c
        total_illuminated = total_illuminated + c
        heapq.heappush(H, (c, a, b))

    for i in range(n):
        C[i].append(i)  # Each C[i] is initialized with i
        S.append(i) # S[i] is the set to which vertex i belongs

    cont = 0
    while cont < n-1:
        c, a, b = heapq.heappop(H)    

        if S[a] != S[b]:  # If edges join different trees...
            min_cost = min_cost + c
            p = S[a]
            q = S[b]
            if q < p:
                p, q = q, p
            for j in C[q]:          
                S[j] = p
            C[p].extend(C[q])        # Join C[p] and C[q]
            C[q] = []                # Empty C[q]
            cont = cont + 1
    
    return total_illuminated-min_cost


def main():
    answers = []
    while True:
        n, m = map(int, input().split())
        if 0 == n == m:
            break
        answers.append(kruskal(n,m))
    for answer in answers:
        print(answer)


if __name__ == '__main__':
    main()
