print("-------------Task 1--------------")
numbers = [3, 14, 1, 25, 9, 100]
result = []
for i in numbers:
    if i > 10:
        result.append(i)
print("Result ==>", result)


print("-------------Task 2--------------")
numbers = ['apple', 'banana', 'apple', 'orange', 'apple']
result = 0
word = "apple"
for i in numbers:
    if i == "apple":
        result+=1
print("Result word apple ==>", result)



print("-------------Task 3--------------")
num1 = {1, 2, 3}
num2 = {3, 4, 5}
result = num1 ^ num2
print("Result uniqual ==>", result)


print("-------------Task 4--------------")
dataM = [(1, 5), (2, 1), (3, 4)]
result = sorted(dataM,key = lambda x: x[1])
print("Result sorted ==>", result)

print("-------------Task 5--------------")
lresult = []
datain = [[1, 2], [3, 4, 5], [6]]
for i in datain:
    for x in i:
        lresult.append(x)
print("Result last ==>", lresult)

