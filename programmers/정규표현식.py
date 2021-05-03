import re

expression = str(100-200*300-500+20)
p = re.compile('\d')

m = p.match("+")
result = p.findall(str(100-200*300-500+20))

print(m)
print(result)