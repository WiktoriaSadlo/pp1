godzina24 = input('Enter a time: ')
godzina12 = ""

if len(godzina24)==5:
    if int(godzina24[:2])>12:
        godzina12 = str(int(godzina24[:2])-12)
        godzina12 += godzina24[2:]
        print(godzina12 + " PM")
    elif int(godzina24[:2])==12:
        print(godzina24 + "PM")
    else:
        print(godzina24+" AM")
elif int(godzina24[:1])==0:
    godzina12 = '12'
    godzina12 += godzina24[1:]
    print(godzina12 + " AM")
else:
    print(godzina24 + " AM")