# First Function
def hello():
    print('Hello from the other side')

# A function named pack() that accepts three arguments,
# and returns a single list with the three arguments inside as list elements.


def pack(cont1, cont2, cont3):
    return [cont1, cont2, cont3]

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list),
# and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". The function should not return anything.


def eat_lunch(my_lst):
    if len(my_lst) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_lst)):
            if i == 0:
                print(f"First I eat {my_lst[0]}")
            else:
                print(f"Next I eat {my_lst[i]}")


# Test that your file works by running it in your terminal.
# Remember, you need to call your functions in order for them to run.
# Make sure that all three functions run (please print the output of pack()) before submitting the file.


hello()
print(pack("a", "b", "c"))
print(pack(1, 2, 3))
eat_lunch([])
eat_lunch(["Sandwich"])
eat_lunch(["apple", "banana", "sandwich", "cookie"])
