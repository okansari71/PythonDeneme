import re

str = "Python kursu: Python programlama Rehberi | 40 saat"

# result = re.findall("Python", str)
# result =len(result)

# result = re.split(" ", str)
# result = re.split("R", str)

# result = re.sub(" ","-",str) #boşluklara - getiriliyor
# result = re.sub("\s","-",str) #yukarıdakinin aynısı

result = re.search("Python", str)
# result = result.span()
# result = result.start()
# result = result.end()
# result = result.string()

print(result)


