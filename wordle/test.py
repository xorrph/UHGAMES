f = open("wordle.txt", "r")
z = open("newWordle.txt", "w")
content = f.readlines()
for x in content:
    x= x.strip()
    x = x + " "
    z.write(x)
    z.flush()
    print("going")
  

