time = str(input("what time is it?").lower().strip())

def replacesymbol(x ,y , z):
      return x.replace(y,z)
stringtime = replacesymbol(time, ":", ".")


print(stringtime)
