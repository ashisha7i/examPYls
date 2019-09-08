for counter in range (1, 6):
    age = input(str(counter) + ": Enter age (-1 to exit): ")

    num = int(age)

    if num == -1:
        print("Exiting on user request")
        break

    if 0 < num <= 11:
        print("Child")
    elif 11 < num < 18:
        print("Teen")
    elif 18 <= num <= 60:
        print("Adult")
    else:
        print("Senior")


# Function 1
def test():
    print("Test called")

test()

# Scope
name = "Python"

def test_loop():
    n = 1
    while n < 5:
        name = "Not Python"
        print(name)
        n = n + 1

test_loop()
print("Out of the loop")
print(name)

# Function Example
def add(x, y):
    return x + y


n1 = input("Enter first number :")
n2 = input("Enter second number :")

print(n1 + n2)

n1 = int(n1)
n2 = int(n2)

print(n1 + n2)
z = add(n1, n2) + 10

print(z)


# Sort List (Before and After)
# Lists
my_list = [] # Empty list

print(str(my_list))
print(len(my_list))

my_list.append(1) # Append to the list

my_list.append(20) # Append to the list
my_list.append(15) # Append to the list
my_list.append(3) # Append to the list

print(str(my_list))

my_list.sort()

print(str(my_list))
print(len(my_list))


# For in over a list
# Lists
my_list = [] # Empty list

my_list.append("Ashish") # Append to the list
my_list.append("Rakhi") # Append to the list
my_list.append("Kaashvi") # Append to the list
my_list.append("Pranshu") # Append to the list

for name in my_list:
    print(name)


# Lists
my_list = [] # Empty list

my_list.append("Ashish") # Append to the list
my_list.append("Rakhi") # Append to the list
my_list.append("Kaashvi") # Append to the list
my_list.append("Pranshu") # Append to the list

my_list.sort(reverse=True) # Sorting the list

# This will iterate over the list
for name in my_list:
    print(name)

