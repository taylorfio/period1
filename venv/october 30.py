def hello_print(first_half):
    second_half = " World!"

    return first_half + second_half


print(hello_print("Hello"))


def number_function(a, b):
    total = a + b
    return total


a = int(input("give number"))
b = int(input("give number"))
print(number_function(a, b))


def if_true_function(x, y):
    if x == y:
        answer = "true"
    if x != y:
        answer = "false"
    return answer


x = int(input("give number"))
y = int(input("give number"))
print(if_true_function(x, y))
