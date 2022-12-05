
def parse_day5_a():
    with open("day5.txt", "r") as f:
        raw_data = list(f.read().splitlines())

    crates_raw = []

    n = 0
    for line in raw_data:
        if len(line) == 0:
            break
        crates_raw.append(line)
        n += 1

    num_of_stacks = int(crates_raw[-1][33])
    crates_raw.pop()
    crates_raw.reverse()
    crates = [[] for _ in range(num_of_stacks)]

    for line in crates_raw:
        j = 0
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                crates[j].append(line[i])
            j += 1

    procedures = []
    for i in range(n + 1, len(raw_data)):
        procedure_raw = raw_data[i].split()
        procedures.append((int(procedure_raw[1]), int(procedure_raw[3]), int(procedure_raw[5])))

    return crates, tuple(procedures)


def find_top_crates(data):
    crates = data[0]

    # (amount, from, to)
    for a, f, t in data[1]:
        for i in range(a):
            crates[t - 1].append(crates[f - 1].pop())

    return ''.join([x[-1] for x in crates])


def day5_a():
    data = parse_day5_a()
    print("day5_a = {}".format(find_top_crates(data)))


def find_top_crates_fifo(data):
    crates = data[0]

    # (amount, from, to)
    for a, f, t in data[1]:
        crates[t - 1] += crates[f - 1][-a:]
        crates[f - 1] = crates[f - 1][:len(crates[f - 1]) - a]

    return ''.join([x[-1] for x in crates])


def day5_b():
    data = parse_day5_a()
    print("day5_b = {}".format(find_top_crates_fifo(data)))
