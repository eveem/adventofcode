def read_input(filename):
    adj_list = {}
    with open(filename, "r") as file:
        for line in file:
            u, _, v, _, d = line.strip().split(" ")
            d = int(d)
            if u not in adj_list:
                adj_list[u] = []
            if v not in adj_list:
                adj_list[v] = []
            adj_list[u].append([v, d])
            adj_list[v].append([u, d])
            
    return adj_list

def find_routes(src, adj_list):
    res = []
    n = len(adj_list.keys())
    def _helper(node, path, weight):
        if len(path) == n:
            res.append(path + [weight])
            return
        
        for nei, w in adj_list[node]:
            if nei not in path:
                path.append(nei)
                weight += w
                _helper(nei, path, weight)
                weight -= w
                path.pop()
    _helper(src, [src], 0)
    return res

def first_star():
    # adj_list = read_input("small_input.txt")
    adj_list = read_input("input.txt")
    min_dist = float("inf")
    for src in adj_list.keys():
        routes = find_routes(src, adj_list)
        for route in routes:
            if route[-1] < min_dist:
                min_dist = route[-1]
    print(f"first star result: {min_dist}")

def second_star():
    adj_list = read_input("small_input.txt")
    # adj_list = read_input("input.txt")
    max_dist = -float("inf")
    for src in adj_list.keys():
        routes = find_routes(src, adj_list)
        for route in routes:
            if route[-1] > max_dist:
                max_dist = route[-1]
    print(f"second star result: {max_dist}")

if __name__ == "__main__":
    first_star()
    second_star()