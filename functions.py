global_var = "help me"
names = ["ayna forger", "mahiro oyama", "momiji hozuki", "mahari oyama"]
def name():
    print("Etienne Hanzon")
def golvar():
    print (global_var)
def inp():
    w3chools=input("what are you ")
    print (w3chools)

def Oyama_filt(x):
  if "oyama" in x:
    return True
  else:
    return False

oyama = filter(Oyama_filt, names)

for x in oyama:
  print(x)

y = "hello Ayna"
x = list(y)
print(x)


def ito_fun(z):
   return z + "ito"

ito = map (ito_fun, ("Burr", "mosqu", "incogn"))
print (list(ito))

for j in range(1,10):
    print (j)

loid = ['s', 'e', 'c', 'o', 'n', 'd']

x = sorted(loid)
print (x)

print (int ("8576309"))

print(str(104.36))

name()
golvar()
inp()