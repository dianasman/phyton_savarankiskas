# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

def showObjectKeys(dict):
    print(dict.keys())
    print(dict.values())
    
showObjectKeys(audi)