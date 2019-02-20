def roundUp(number:float)->int:
    split = [int(i) for i in str(number).split(".")]
    if split[1] >0:
        return split[0]+1
    return split[0]

## Program Start ##
n, k = [int(i) for i in input().strip().split(" ")][-2:]

scores = sorted([int(i) for i in input().strip().split(" ")])

min_days = roundUp(n/k)

output = 0
for i in range(0, min_days):
    output += scores[len(scores) -1 -i]

print(output)