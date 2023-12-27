file = open("../day1/input.txt", "r")

result = 0

for line in file:
    arr = []
    outcome = 0
    for i in range(len(line)):
        if line[i].isdigit():
            print(line[i])
            arr.append(line[i])
    firstDigit = arr[0]
    lastDigit = arr[-1]
    print(arr)
    concat = firstDigit + lastDigit
    outcome = int(concat)
    result = result + outcome

print(result)
file.close

#
# def checkNumberOfLines(f):
#     x = 0
#     for line in f.readlines():
#         x = x + 1
#     print(x)
#     file.close()
