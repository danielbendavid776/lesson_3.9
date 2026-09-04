def my_div(a,b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a/b

number_a = int(input('enter a number: '))
number_b = int(input('enter another number: '))

print(my_div(number_a,number_b))