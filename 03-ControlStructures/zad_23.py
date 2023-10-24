dog_age = int(input('Enter your dogs age:'))


if dog_age == 1:
    print("The dog's age in dog’s years is 10.5 years.")
elif  dog_age == 2:
    print("The dog's age in dog’s years is 21 years.")
else:
    print(f"The dog's age in dog’s years is {21+4*(dog_age-2)} years.")