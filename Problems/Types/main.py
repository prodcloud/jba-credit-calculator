# the variable "args" is already defined
# my_list = [int(args[1]), int(args[2]), int(args[3]), int(args[4])]  # your code here
my_list = []

for item in args:
    if item == "script.py":
        continue

    my_list.append(int(item))

print(str(my_list))
