quantity = 0
sum = 0
product = 1
first_max = 0
second_max = 0
index_max = -1
index = 0
even = -1
odd = 0
while True:
    x = int(input("Enter the number = "))
    if x ==0:
        break
    quantity +=1
    sum += x
    product += x
    if x % 2 ==0:
        even +=1
    else:
        odd +=1
    if x > first_max:
        firts_max, second_max = x,first_max
        count_max = 1
        index_max = index
    elif x == first_max:
        count_max +=1
    elif x > second_max:
        index += 1
    print (f'The quantity of elements is: {quantity}')
    print(f'The sum of elements is: {sum}')
    print(f'The product of elements is: {product}')
    print(f'The average of elements is: {sum / quantity}')
    print(f'The first max is: {first_max}')
    print(f'The second max is: {second_max}')
    print(f'The quantity of max elements is: {count_max}')
    print(f'The index of first max element is: {index_max}')
    print(f'The even is: {even}')
    print(f'The odd is: {odd}')



