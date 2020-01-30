from Seminarski.avioKarte import printFlights, loadFlights, reserveFlight, sortFlights

class Sluzbenik:
   
    def __init__(self, ide, ime, prez,user,sifra):
        self.id = ide
        self.ime = ime
        self.prez = prez
        self.user = user
        self.sifra = sifra
    
    def toString(self):
        return "Sluzbenik: ID -> " + str(self.id) + ", " + self.ime + " " + self.prez
    
    def getId(self):
        return int(self.id)


employee = []

def loadEmployee():
    
    fajl = open("sluzbenici.txt", "r")
    for line in fajl:
        ide, ime, prez, user, sifra = line.split(",")
        sluzbenik = Sluzbenik(ide.strip(),ime.strip(),prez.strip(),user.strip(),sifra.strip())
        employee.append(sluzbenik)
    fajl.close()

def printEmployee():
    
    for line in employee:
        print(line.toString())

def sortEmployee():
    
    employee.sort(key = lambda k: k.getId(), reverse = False)
        
def preglednik():
    print("================================================== \n")
    print("Izaberite opciju:")
    print("1. Uloguj se")
    print("2. Dodaj sluzbenika")
    print("3. Pregled (sortiranje) zaposlenih")
    print("4. Zaboravljeno korisnicko ime i lozinka")
    print("5. Kraj \n")
    print("================================================== \n")
    
def choice(n):
    if(n == 1):
        user = input("Unesite korisnicko ime -> ")
        sifra = input("Unesite lozinku -> ")
        if login(user,sifra):
            print("Uspesno ulogovan sluzbenik: ")
            printWorker(user,sifra)
            nextJob()
        else:
            print("Pogresno korisnicko ime i lozinka. Da li ste zaboravili?")
            x = input("Unesite da ili ne -> ")
            if x == 'da':
                choice(4)
            else:
                choice(1)
    elif n == 2:
        addEmployee()
    elif n == 3:
        sortEmployee()
        printEmployee()
    elif n == 4:
        forgotUserOrPassword()
    else:
        print("Program je zavrsio sa radom")
        return

def forgotUserOrPassword():
    n = input("Unesite Vas ID -> ")
    for x in employee:
        if n == x.id:
            print("Vase korisnicko ime -> " , x.user)
            print("Vasa lozinka -> " , x.sifra)
            print("Vodite racuna o ovakvim stvarima!!! Sada se mozete ulogovati normalno \n")
            choice(1)
            return
    else:
        print("Uneti ID je pogresan. Obratite se Vasem sefu radi dobijanja novog ID-a \n")
        return
        
def tempMeni():
    print("1. Stampaj red letenja (red letenja je sortiran) \n")
    print("2. Rezervisi let \n")
    print("3. Promeni sluzbenika \n")
    
def nextJob():
    print("Dobrodosli u meni. Izaberite opciju i nastavite dalji rad. \n")
    tempMeni()
    x = eval(input("Unesite broj -> "))
    while x < 1 or x > 3:
        x = eval(input("Unesite broj -> "))
    choiceFlights(x)
    
def choiceFlights(x):
    if x == 1:
        loadFlights()
        sortFlights()
        printFlights()
        tempMeni()
        x = eval(input("Unesite opciju -> "))
        print("\n")
        choiceFlights(x)
    elif x == 2:
        loadFlights()
        reserveFlight()
    else:
        preglednik()
        n = eval(input("Unesite opciju -> "))
        choice(n)
               
def login(user, sifra):
    
    for x in employee:
        if x.user == user and x.sifra == sifra:
            return True
    return False

def printWorker(user, sifra):
    
    for x in employee:
        if x.user == user and x.sifra == sifra:
            print("***************************************************")
            print(x.toString())
            print("***************************************************")

def addEmployee():
    print("Usli ste u Meni za dodavanje novog radnika. ")
    print("Za dalji rad Vam je neophodna sifra administratora sistema. \n")
    try:
        a = input("Unesite administratorsku lozniku -> ")
        if a == 'administratorAvioKarte9822':
            print("Uspesno ulogovan administrator. Sledite dalje korake. \n")
            ide = eval(input("Dodelite id novom radniku -> "))
            if findWorker(ide) == True:
                print("Zaposleni sa unetim id-om vec postoji!")
            else:
                ime = input("Unesite ime novog radnika -> ")
                prez = input("Unesite prezime novog radnika -> ")
                user = input("Dodelite mu korisnicko ime -> ")
                sifra = input("Dodelite mu lozinku -> ")
                novi = Sluzbenik(ide,ime,prez,user,sifra)
                addInFile(novi)
                employee.append(novi)
                print("Uspesno upisan nov radnik. Srecan pocetak posla. \n")
                sortEmployee()
                printEmployee()
            
        else:
            print("Greska u prijavi administratora.")
    except:
        print("Nesto je krenulo po zlu")
        addEmployee()

def findWorker(ide):
    for x in employee:
        if x.getId() == ide:
            return True
    return False

def addInFile(novi):
    fajl = open("sluzbenici.txt", "r+")
    fajl.read()
    fajl.write("\n" + toString(novi))
    fajl.close()
    
def toString(novi):
    return str(novi.id)+","+novi.ime+","+novi.prez+","+ novi.user+"," + novi.sifra

                    