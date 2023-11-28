import re
txt = "To be, or not to be, that is the question"

vowels = re.findall("[aeiuoy]",txt)

sum = len(vowels)
print(sum)