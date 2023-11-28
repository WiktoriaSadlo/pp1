import re

txt = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

temperatures = re.findall('\d{2}',txt)

sum = 0
for x in temperatures:
    sum+=int(x)

print(sum/len(temperatures))