def connect_bridges(G):
    result = []
    visited = [0]

    while (len(visited)) < len(G):
        min_cost = float('inf')
        a = -1
        b = -1
        for i in range(len(G)):
            for j in range(len(G)):
                if i in visited and j not in visited:
                    if G[i][j] != 0 and G[i][j] < min_cost:
                        min_cost = G[i][j]
                        a = i
                        b = j
        if b == -1:
            return None
        visited.append(b)
        result.append((a, b, G[a][b]))
    return result