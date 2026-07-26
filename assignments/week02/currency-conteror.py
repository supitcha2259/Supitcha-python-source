#1 Dollar = 33.70 Bath
#1 Yuan = 4.98 Bath
#1 Dong = 0.0013 Bath
#1 Yen = 0.21 Bath

Dollar = 33.70
Yuan = 4.98
Dong = 0.0013
Yen = 0.21

print("=" *50)
Currency = int(input("Select the currency you wish to convert as follows: \n1.Dollar\n2.Yuan\n3.Dong\n4.Yen\n"))

if Currency <= 5 and Currency > 0:
    while True:
        if Currency == 1:
            print("=" *50)
            Dol = float(input("Dollar you want: "))
            sum = Dol/33.70
            print(Dol,"Dollar =",sum,"Bath.")
            break
        elif Currency == 2:
            print("=" *50)
            Yu = float(input("Yuan you want: "))
            sum = Yu/0.21
            print(Yu,"Yuan =",sum,"Bath.")
            break
        elif Currency == 3:
            print("=" *50)
            Don = float(input("Dong you want: "))
            sum = Don/0.0013
            print(Don,"Dong =",sum,"Bath.")
            break
        elif Currency == 4:
            print("=" *50)
            yen = float(input("Yen you want: "))
            sum = yen/0.0013
            print(yen,"Yen =",sum,"Bath.")
            break
        else:
            break
print("=" *50)