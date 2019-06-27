file = open('1000-digit', "r")
num = file.read()

i = 0
multiple = num[i] + num[i+1] + num[i+2] + num[i+3]
product = 0

def calculation(string):
    counter = 0
    prod = 1
    while counter < len(string):
        prod = prod * int(string[counter])
        counter = counter + 1
    return prod

while i < len(num) - 3:
    if int(calculation(multiple)) > product:
        product = int(calculation(multiple))
        i = i + 1

print(product)
