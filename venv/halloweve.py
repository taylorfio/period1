
def print_halloween():
    print("Happy Halloween!")


print_halloween()


def print_halloween_1(times):
    for x in range(times):
        print("Happy Halloween!")


print_halloween_1(7)


def print_halloween_2(inner, outer):
    for x in range(outer):
        print("test")
        for y in range(inner):
            print("Happy Halloween!")


print_halloween_2(3, 4)


def print_halloween_3(inner):
    if inner > 7:
        return True
    elif inner == 7:
        return False
    else:
        return "Boo"


print(print_halloween_3(8))


