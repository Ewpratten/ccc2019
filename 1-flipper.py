def answer(grid:list):
    for line in grid:
        print(f"{line[0]} {line[1]}")
    exit()

opcodes = {
    "V" : lambda x: [[x[0][1], x[0][0]], [x[1][1], x[1][0]]],
    "H" : lambda x: [x[1], x[0]]
}

## Program start ##
operations = input().strip()
grid = [[1,2], [3,4]]

if operations == "":
    answer(grid)

for operation in operations:
    grid = opcodes[operation.upper()](grid)

answer(grid)