class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


class Directory:
    def __init__(self, name, parent=None):
        self.store = {}
        self.name = name
        self.parent = parent
        self.size = -1

    def add(self, item):
        if item.name not in self.store:
            self.store[item.name] = item

    def get_size(self):
        if self.size != -1:
            return self.size
        self.size = sum([item.get_size() for item in self.store.values()])
        return self.size

    def get_next_directory(self, cd_parameter):
        if cd_parameter == '..':
            return self.parent
        elif cd_parameter == '/':
            return root
        else:
            return self.store[cd_parameter]

    def get_subdirectories(self):
        return [item for item in self.store.values() if type(item) == Directory]


with open('day7.txt') as f:
    data = [line.strip() for line in f]
    commands = []
    curr = []
    for line in data:
        if line.startswith("$"):
            if curr:
                commands.append(curr)
            curr = [line]
        else:
            curr.append(line)
    commands.append(curr)

    root = Directory("/")
    curr = root
    for command, *result in commands:
        if command.startswith("$ cd"):
            path = command[5:]
            curr = curr.get_next_directory(path)
        else:
            for file in result:
                size, name = file.split()
                if size.isdigit():
                    item = File(name, int(size))
                else:
                    item = Directory(name, curr)
                curr.add(item)


def total_size_at_most_k(directory, k):
    answer = 0
    directory_size = directory.get_size()
    if directory_size <= k:
        answer += directory.get_size()

    for subdirectory in directory.get_subdirectories():
        answer += total_size_at_most_k(subdirectory, k)
    return answer


def smallest_directory_size_at_least_k(directory, k):
    answer = float('inf')
    if directory.get_size() >= k:
        answer = min(directory.get_size(), answer)

    for subdirectory in directory.get_subdirectories():
        answer = min(smallest_directory_size_at_least_k(
            subdirectory, k), answer)
    return answer


print("Part 1:", total_size_at_most_k(root, 100000))

TOTAL = 70000000
REQUIRED = 30000000

current_space = TOTAL - root.get_size()
minimum_to_cut = REQUIRED - current_space

print("Part 2:", smallest_directory_size_at_least_k(root, minimum_to_cut))
