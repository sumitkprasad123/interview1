
def reverse(str):
    rev=""
    length = len(str)-1
    for i in range(length,-1,-1):
        rev += str[i]
    return rev

str = input("Enter any string input: ")
x = reverse(str)

print(x)