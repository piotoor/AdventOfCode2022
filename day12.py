import heapq
import sys


def parse_day12_a():
    with open("day12.txt", "r") as f:
        raw_data = list(f.read().splitlines())

    s, t = find_src_trgt(raw_data)
    data = [list(map(lambda a: 0 if a == "S" else (25 if a == "E" else ord(a) - 97), list(x))) for x in raw_data]

    return data, s, t


def dijkstra(data, source, condition):
    dist = {}
    prev = {}
    neighbours = [[set() for _ in data[0]] for _ in data]
    qq = []
    heapq.heappush(qq, (source, 0))

    for r in range(len(data)):
        for c in range(len(data[r])):
            curr = (r, c)
            dist[curr] = sys.maxsize

            for i in range(max(0, r - 1), min(r + 2, len(data))):
                for j in range(max(0, c - 1), min(c + 2, len(data[0]))):
                    if (i == r and j == c) or (i != r and j != c) or condition(data, i, j, r, c):
                        continue
                    # if data[i][j] == data[r][c] or data[i][j] == data[r][c] + 1:
                    neighbours[r][c].add((i, j))

    dist[source] = 0

    while len(qq) > 0:
        curr, d = heapq.heappop(qq)

        r, c = curr
        for ngh in neighbours[r][c]:
            i, j = ngh
            alt = dist[curr] + 1

            if alt < dist[ngh]:
                dist[ngh] = alt
                prev[ngh] = curr
                heapq.heappush(qq, (ngh, dist[ngh]))

    return dist, prev


def print_path(data, path, target):
    data_str = ""
    data_ = data.copy()
    node = target

    print(target)
    p = []
    n = 1
    while node in path:
        print(path[node])
        p.append(path[node])
        node = path[node]
        n += 1

    for i in range(len(data_)):
        for j in range(len(data_[0])):
            if (i, j) in p:
                data_[i][j] = chr(data_[i][j] + 97).upper()
            else:
                data_[i][j] = chr(data_[i][j] + 97)
        data_str += "".join(data[i]) + '\n'
    print(data_str)


def find_src_trgt(data):
    src = (0, 0)
    trgt = (0, 0)

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                src = (i, j)
            if data[i][j] == "E":
                trgt = (i, j)

    return src, trgt


def find_shortest_path(data, source, target):
    # print("source = {}, target = {}".format(source, target))
    dist, prev = dijkstra(data, source, lambda d, i, j, r, c: (d[i][j] > d[r][c] + 1))
    # print_path(data, prev, target)
    # print("len = {}".format(len(dist)))
    # print(dist[target])
    return dist[target]


def find_shortest_path_from_any_a(data, source):
    dist, prev = dijkstra(data, source, lambda d, ii, jj, r, c: (d[ii][jj] < d[r][c] - 1))
    min_dist_from_a = sys.maxsize

    for i, j in dist:
        if data[i][j] == 0:
            min_dist_from_a = min(min_dist_from_a, dist[(i, j)])

    return min_dist_from_a


def day12_a():
    data, s, t = parse_day12_a()
    print("day12_a = {}".format(find_shortest_path(data, s, t)))


def day12_b():
    data, s, t = parse_day12_a()
    print("day12_b = {}".format(find_shortest_path_from_any_a(data, t)))
