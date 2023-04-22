shortSide=2
longSide=3

print("Enviroment: " , 2*(shortSide+longSide))
print("Field: " , shortSide*longSide)

s = "Hello World"
print("Last Character: " , s[-1])
print("Last Character: " , len(s))

celcius = int(input("Celcius: "))
fahrenheit=(celcius*9)/5+32
print("Fahrenheit: ", fahrenheit)

wovels = ["a" , "e", "ı" , "i" , "o" , "ö" , "u" , "ü"]
word = "TechProEducation"

found = {}

for x in word:
    if x in wovels:
        found.setdefault(x , 0)
        found[x] = found[x] + 1

for k, v in sorted(found.items()) :
    print(k , "wovels" , v , "founded")

def hello() :
    print("Hello World")

hello()
print(hello())

for i in range(1,5) :
    hello()