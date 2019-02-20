primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
## Funcitons ##

def getOtherPrime(index, inpt):
    return (2*inpt - index)

## Program Start ##
cases_count = int(input().strip())
cases = []

# edge cases
if not 1<= cases_count <= 1000:
    exit()

while len(cases) < cases_count:
    case = int(input().strip())
    cases.append(case)

output = []
# iterate through each case
for case in cases:
    for prime in primes:
        possible_prime = getOtherPrime(prime, case)
        if possible_prime in primes:
            if (possible_prime + prime) /2 == case:
                output.append([prime, possible_prime])
                break

for line in output:
    print(str(line[0])+ " " +str(line[1]))