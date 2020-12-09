day = int(input("Day (0-6)? "))
if day == 0 or day == 6:
   print("\nSleep In")
elif 1 <= day <= 5:
   print("\nGo To Work")

else:
    print("\nPlease enter weekday number between 0-6.")
