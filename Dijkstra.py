# https://www.beecrowd.com.br/judge/en/problems/view/1123

import heapq


def alter_priority(w, L, D):
    for i in range(len(D)):
        if D[i][1] == w:
            pos = i
            break
    D[pos] = (L[w], w)
    heapq._siftdown(D, 0, pos)
    return


def generates_cost_matrix(n, infty):
    cost = []
    for i in range(n):
        line = []
        for j in range(n):
            if i == j:
                line.append(0)
            else:
                line.append(infty)
        cost.append(line)
    return cost


def on_route(v_city, route):
    return v_city in route


def are_neighbors(a, b):
    return (a - b) == 1 or (a - b) == -1


def dijkstra(n_out, cost, n_cities, destination, k_root, infty):
    check = [0] * n_cities
    L = [infty] * n_cities
    L[k_root] = 0

    D = [(0, k_root)]
    for w in range(0, n_cities):
        if w != k_root:
            heapq.heappush(D, (L[w], w))

    # print(k_root)
    # print(D)
    # print(P)

    while D:
        Lmin, v = heapq.heappop(D)
        check[v] = 0
        for w in n_out[v]:
            if check[w] == 0:
                if Lmin + cost[v][w] < L[w]:
                    L[w] = Lmin + cost[v][w]
                    alter_priority(w, L, D)

    # print(D)
    # print(P)

    return L[destination]


def main():
    answers = []
    infty = 50000
    while True:
        n_cities, m_roads, c_route, k_root = map(int, input().split())
        if 0 == n_cities == m_roads == c_route == k_root:
            break
        n_out = [[] * n_cities for i in range(n_cities)]
        cost = generates_cost_matrix(n_cities, infty)
        route = list(range(c_route))
        destination = c_route-1

        for estrada in range(m_roads):
            u_city, v_city, p_cost = map(int, input().split())
            if (not on_route(v_city, route) and not on_route(u_city, route)) or \
                    (on_route(v_city, route) and on_route(u_city, route)
                     and are_neighbors(u_city, v_city)):
                n_out[u_city].append(v_city)
                n_out[v_city].append(u_city)
                cost[u_city][v_city] = p_cost
                cost[v_city][u_city] = p_cost

            elif on_route(v_city, route) and not on_route(u_city, route):
                n_out[u_city].append(v_city)
                cost[u_city][v_city] = p_cost

            elif not on_route(v_city, route) and on_route(u_city, route):
                n_out[v_city].append(u_city)
                cost[v_city][u_city] = p_cost

        answers.append(dijkstra(n_out, cost, n_cities, destination, k_root, infty))

    for answer in answers:
        print(answer)


if __name__ == '__main__':
    main()
