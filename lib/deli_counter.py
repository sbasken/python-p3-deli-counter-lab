katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    elif len(katz_deli) > 0:
        message="The line is currently:"
        for index in range(len(katz_deli)):
            name = katz_deli[index]
            message += f" {index+1}. {name}"
        print(message)

print(line(katz_deli))

def take_a_number(list, name):
    if len(list) == 0:
        list.append(name)
        print(f"Welcome, {name}. You are number 1 in line.")
    else:
        list.append(name)
        number = len(list)
        print(f"Welcome, {name}. You are number {number} in line.")

def now_serving(list):
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else:
        name=list[0]
        del list[0]
        print(f"Currently serving {name}.")