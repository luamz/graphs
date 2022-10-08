# https://www.beecrowd.com.br/judge/en/problems/view/1081

def read_input(n_cases):
    matrices = []
    for i in range(n_cases):
        n_vertices, e = map(int, input().split())
        mat = [[0] * n_vertices for i in range(n_vertices)]
        for j in range(e):
            a1, a2 = map(int, input().split())
            mat[a1][a2] = 1
        matrices.append(mat)

    return matrices


def next_segment(check, n_vertices):
    for i in range(n_vertices):
        # Check the list of marked vertices if there are still vertices to be visited
        if check[i] == 0:
            return i


def visit(matrix, check, v, n_vertices, counter):
    # print('{} - Visiting vertex {}'.format(counter, v))
    if check[v] == 1:
        return

    check[v] = 1

    for w in range(n_vertices):
        if matrix[v][w] == 1:
            if check[w] == 0:
                # print("Tempo: {} ----- Visiting Neighbor: {}\n\n".format(counter, w))

                # Ensure blank line between segments
                if counter == 0:
                    print()
                    counter = 1

                # print('{}- Going from vertex {} to vertex {}'.format(counter, v, w))
                print("{}{}-{} pathR(G,{})".format("  " * counter, v, w, w))
                visit(matrix, check, w, n_vertices, counter+1)
            else:
                print("{}{}-{}".format("  " * counter, v, w))

    # Don't add a blank line if the vertex has no neighbors
    if counter == 0:
        counter = 1

    # If it still has other segments
    if counter == 1:
        next = next_segment(check, n_vertices)
        if next:
            # print('\n ---- Going to next segment on vertex {} ----\n'.format(next))
            visit(matrix, check, next, n_vertices, 0)

    return


def run_case(matrix):
    n_vertices = len(matrix)
    check = n_vertices * [0]
    visit(matrix, check, 0, n_vertices, 1)


def main():
    n_cases = int(input())
    matrices = read_input(n_cases)
    caso = 1
    for matrix in matrices:
        print('Case {}:'.format(caso))
        run_case(matrix)

        caso = caso + 1
        print()


if __name__ == "__main__":
    main()
