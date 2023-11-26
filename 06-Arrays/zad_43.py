import re

def NumOfWords(a):
    x = re.split('\s',a)
    return len(x)

txt='The rain in Spain'
print(NumOfWords(txt))