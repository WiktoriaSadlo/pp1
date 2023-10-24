Peter_age = 17
Anna_age = 23

if Peter_age>=18 and Anna_age>=18:
    print('Peter and Anna are both adults')
elif Peter_age>=18 and Anna_age<18:
    print('Peter is adult, but Anna is not')
elif Peter_age<18 and Anna_age>=18:
    print('Anna is adult, but Peter is not')
else:
    print('Anna and Peter are nt adult.')