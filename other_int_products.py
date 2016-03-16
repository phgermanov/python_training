def get_products_of_other_ints(input):
    output = [1]*len(input)
    counter = 0
    for i in range(len(input)):
        for j in range(len(input)):
            counter += 1
            if i != j:
                output[i]*=input[j]
    print (counter)
    return output

def get_products_of_other_ints2(input):
    output = [1]*len(input)
    counter = 0
    for i in range(len(input)):
        for j in range(len(input)):
            counter += 1
            if i != j:
                output[i]*=input[j]
    print (counter)
    return output

input = [1, 7, 0, 4]
print(get_products_of_other_ints(input))
