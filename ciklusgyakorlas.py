#Írjuk ki 0-tól 150-ig a páros számokat!
def feladat1():
    i:int=0
    while i!=150:
        i += 1
        print(i,end=",")
#Számold meg 10 bekért szám esetében a 3-mal osztható számokat!

def feladat2():
    szamlalo:int=0
    i:int=0
    while i != 10:
        szam:int=int(input("Kérem adjon meg egy számot"))
        if szam%3==0:
            szamlalo+=1
        i+=1

    print(szamlalo)
#Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*

def feladat3():
    szam: int = int(input("Kérem adjon meg egy számot"))
    while not(szam % 10==0):
        szam:int=int(input("Kérem adjon meg egy számot"))

#Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*

def feladat4():
    szam: int = int(input("Kérem adjon meg egy számot"))
    while not((szam>=10) and (szam<99) and (szam % 2 ==0)):
        szam: int = int(input("Kérem adjon meg egy számot"))
  #Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*

def feladat5():
    szam: int = int(input("Kérem adjon meg egy számot"))
    while not ((szam>=0) and (szam % 2 == 1)):
        szam: int = int(input("Kérem adjon meg egy számot"))
#Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.*

def feladat6():
    szam: int = int(input("Kérem adjon meg egy számot"))
    while not ( (szam%3==0) or ((szam **0.5) % 1==0) ):
        szam: int = int(input("Kérem adjon meg egy számot"))

#Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!
def feladat7():
    a: int = int(input("Kérem adjon meg egy számot"))
    b: int = int(input("Kérem adjon meg egy számot"))
    c: int = int(input("Kérem adjon meg egy számot"))


    while not(((a + b) > c) and ((b + c) > a) and ((c + a) > b)):
        a: int = int(input("Kérem adjon meg egy számot"))
        b: int = int(input("Kérem adjon meg egy számot"))
        c: int = int(input("Kérem adjon meg egy számot"))
    print("Jo szamokat adott meg!")
#Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*

def feladat8():
    szoveg: str = input("Kérem adjon meg egy szoveget")
    while  (len(szoveg)>=3):
        szoveg: str = input("Kérem adjon meg egy szoveget")
    print(szoveg.upper())
#Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*


def feladat9():
    szoveg: str = input("Kérem adjon meg egy szoveget")
    while  not((len(szoveg)==4) and (szoveg.islower()==True)):
        szoveg: str = input("Kérem adjon meg egy szoveget")
def feladat10():
    osszeg=0
    db=0
    szam: int = int(input("Kérem adjon meg egy számot"))
    osszeg+=szam
    db+=1
    while (szam!=0):
        szam: int = int(input("Kérem adjon meg egy számot"))
        osszeg+=szam
        db+=1
    print(osszeg/(db-1))
    #Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!
    #A fenti feladatot írd meg úgy, hogy csak pozitív számot fogadjon el (ha negatív, addig kérjen új számot, ameddig pozitív nem lesz), illetve ha 0-t ír, akkor legyen vége a bemeneteknek!

def feladat11():
    osszeg = 0
    db = 0

    szam: int = int(input("Kérem adjon meg egy számot"))
    while (szam != 0):
        while (szam < 0):
            szam: int = int(input("Kérem adjon meg egy számot"))
        osszeg += szam
        db += 1
        szam: int = int(input("Kérem adjon meg egy számot"))
    print(osszeg / (db))

