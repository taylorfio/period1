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


import math
restart = 0
while restart == 0: # variable for restarting code
    user_input = input("Quick_Pythagoras, Tip_Calculator, or Temperature_Converter   ")
    while user_input != "Quick_Pythagoras" and user_input != "Tip_Calculator" and user_input != "Temperature_Converter":
        print("error")  # Defensive programming
        user_input = input("Quick_Pythagoras, Tip_Calculator, or Temperature_Converter   ")
    if user_input == "Quick_Pythagoras":
        a = int(input("enter value a    "))
        b = int(input("enter value b    "))
        c = math.sqrt((a * a)+(b * b))
        print("the hypotenuse is " + str(round(c, 2)))
        ending = input("do you want to continue: yes or no  ")  # code to restart
        if ending == "no":
            restart = restart + 1
    if user_input == "Tip_Calculator":
        bill = int(input("enter a total for a bill  "))
        tip = int(input("enter a percentage for the tip "))
        tip = tip / 100
        total = bill * tip
        print("leave " + str(total) + " for the tip")
        ending = input("do you want to continue: yes or no  ")  # code to restart
        if ending == "no":
            restart = restart + 1
    if user_input == "Temperature_Converter":
        option = input("Celsius - Fahrenheit or Fahrenheit - Celsius    ")
        if option == "Celsius - Fahrenheit":
            Celsius = int(input("enter the Celsius  "))
            temp = int(Celsius * 9 / 5) + 32
            print("the temperature in fahrenheit is " + str(temp))
        if option == "Fahrenheit - Celsius":
            Fahrenheit = int(input("enter the Fahrenheit  "))
            temp = int(Fahrenheit - 32) * 5 / 9
            print("the temperature in celsius is " + str(temp))
        ending = input("do you want to continue: yes or no  ") # code to restart the entire thing
        if ending == "no":
            restart = restart + 1

