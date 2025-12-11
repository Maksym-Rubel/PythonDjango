
print("---------------------Task 1 ---------------------")

def FilterNumber(numbers,functionlamd):
    result = []
    for number in numbers:
        if functionlamd(number):
            result.append(number)
    return result

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = FilterNumber(numbers, lambda x: x % 2 == 0)
print(even_numbers)  

morethan5_numbers = FilterNumber(numbers, lambda x: x >= 5)
print(even_numbers)  


print("---------------------Task 2 ---------------------")

def yaldNumber(numbers,start,end):
    for number in numbers:
        if start <= number <= end:
            yield number

for i in yaldNumber(numbers,3,8):
    print(i)