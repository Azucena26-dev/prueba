decimal=int(input("ingrese el decimal:\n"))
binario = ''
while decimal // 2 != 0:
    binario = str(decimal % 2) + binario # mod para que sean numero entero
    print("binario",binario)
    decimal = decimal // 2
    print("decimal",decimal)
print( str(decimal) + binario)



