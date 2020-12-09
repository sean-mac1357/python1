count = 0
user_input = input("How high should we count? ")

try:
    MAX = int(user_input)
    # while(count < MAX:) will count 0-9
    while(count <= MAX): # counts 0-10
        print(count)
        # The following line means, "add 1 to the value of count"
        count += 1
except ValueError:
    print("Please run the program again, this time with a number")
