height_cm = int(input('Enter your height in cm:'))
height_feet = int(height_cm*0.033)
height_inches = int((height_cm*0.033-height_feet)*12)
print(f'I am {height_cm} cm tall, i.e. {height_feet} feet and {height_inches} inches')