from enum import Enum

from anytree import Node, findall, find


def parse_day7_a():
    with open("day7.txt", "r") as f:
        data = tuple(f.read().splitlines())

    return data


class FileType(Enum):
    FILE = 0
    DIRECTORY = 1


def parse_console_output(data):
    root = Node("/", type=FileType.DIRECTORY, size=0)

    curr = root
    for line in data:
        line_split = line.split()

        if line_split[0] == "$":
            cmd = line_split[1]
            if cmd == "cd":
                arg = line_split[2]
                if arg == "/":
                    curr = root
                elif arg == "..":
                    curr = curr.parent
                else:
                    curr = find(curr, lambda node: node.name == arg and node.type == FileType.DIRECTORY
                                                   and node.parent == curr)
            elif cmd == "ls":
                pass

        else:
            if line_split[0] == "dir":
                _ = Node(line_split[1], parent=curr, type=FileType.DIRECTORY, size=0)
            else:
                _ = Node(line_split[1], parent=curr, type=FileType.FILE, size=int(line_split[0]))

    return root


def calculate_dir_sizes(node):
    if node.type == FileType.FILE:
        return node.size

    for x in node.children:
        node.size += calculate_dir_sizes(x)

    return node.size


def sum_of_dir_sizes(data):
    dir_tree = parse_console_output(data)
    calculate_dir_sizes(dir_tree)
    # print(RenderTree(dir_tree, style=AsciiStyle()))

    ans = 0
    for x in findall(dir_tree, filter_=lambda node: node.size <= 100000 and node.type == FileType.DIRECTORY):
        ans += x.size

    return ans


def day7_a():
    data = parse_day7_a()
    print("day7_a = {}".format(sum_of_dir_sizes(data)))


def find_size_of_smallest_dir_to_remove(data):
    dir_tree = parse_console_output(data)

    disk_space = 70000000
    free_space_required = 30000000
    space_used = calculate_dir_sizes(dir_tree)
    space_unused = disk_space - space_used
    free_space_missing = free_space_required - space_unused
    # print("space_used = {}, space_unused = {}".format(space_used, space_unused))

    return min([x.size for x in findall(dir_tree, filter_=lambda node: node.size >= free_space_missing
                and node.type == FileType.DIRECTORY)])


def day7_b():
    data = parse_day7_a()
    print("day7_b = {}".format(find_size_of_smallest_dir_to_remove(data)))
