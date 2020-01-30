from _overlapped import NULL

from random import randint

class Flight:
    
    def __init__(self, idL, start, end, distance):
        self.idL = idL
        self.start = start
        self.end = end
        self.distance = distance
    
    def toString(self):
        return "Let " + self.idL + ", relacija: " + self.start + " - " + self.end + ", udaljenost: " + str(self.distance)
    
    def toStringReverse(self):
        return "Let " + self.idL + ", relacija: " + self.end + " - " + self.start + ", udaljenost: " + str(self.distance)
    
    def toStringJustDestRev(self):
        return self.end + " - " + self.start
    
    def getIDL(self):
        return self.idL
    
    def toStringJustDest(self):
        return self.start + " - " + self.end
    
    def returnPriceReverseBussines(self):
        return self.distance * 0.50
    
    def returnPriceReverseEconomic(self):
        return self.distance * 0.25
    
    def returnPriceOneWayBussines(self):
        return self.distance * 0.6
    
    def returnPriceOneWayEconomic(self):
        return self.distance * 0.28

    
flights = []
data = []
price = 0

def loadFlights():
    
    fajl = open("letovi.txt", "r")
    for line in fajl:
        idl, druga, distance= line.split(",")
        start, end = druga.split("-")
        let = Flight(idl.strip(), start.strip(), end.strip(), int(distance.strip()))
        flights.append(let)    
    fajl.close()
    
def sortFlights():
    flights.sort(key = lambda k: k.getIDL(), reverse = False)

def printFlights():
    
    for line in flights:
        print(line.toString())
    print("*******udaljenost je izrazena u km****** \n")

def findFlight(ide):
    
    for line in flights:
        if str(line.idL) == str(ide):
            return line
    return NULL
  
def reserveFlight():
    
    print("Usli ste u meni za rezervaciju avio karte.")
    print("Vodite racuna o tacnosti podataka koje uzimate od klijenata.")
    ide = input("Unesite ID leta -> ")
    flight = findFlight(ide)
    if flight != NULL:
        data.insert(0, flight)
        print("Zelite rezervisati kartu za let " + ide + ", " + flight.toStringJustDest() + "\n")
        print("*datume unosite u formatu DD-M-GG*")
        datP = input("Unesite datum polaska -> ")
        data.insert(1, datP)
        way = eval(input("Povratno(1) / jednosmerno(2) putovanje -> "))
        if way == 1:
            data.insert(2, "Povratno putovanje")
            datPov = input("Unesite datum povratka -> ")
            d, m, g = datP.split("-")
            d1, m1, g1 = datPov.split("-")
            if int(g) < 2018 or int(g1) < 2019:
                print("Neispravan format datuma. Unesite ponovo!!! \n")
                reserveFlight()      
            data.insert(3, datPov)
            klasa = input("Klasa putovanja (b)Bussines, (e)Economic -> ")
            if klasa == "b":
                price = flight.returnPriceReverseBussines()
                data.insert(4, "Biznis klasa")
            elif klasa == "e":
                price = flight.returnPriceReverseEconomic()
                data.insert(4, "Ekonomska klasa")
            else:
                print("Pogresan unos!!! \n")
                reserveFlight()
            
            kol = eval(input("Koliko osoba putuje -> "))
            if kol < 0 or kol > 10:
                print("Broj osoba nije ispravno unesen \n")
                reserveFlight()
            else:
                data.insert(5, kol)
                price *= kol
                data.insert(6, price)
                dataReturn()
                
        else:
            klasa = input("Klasa putovanja (b)Bussines, (e)Economic -> ")
            data.insert(2, "Jednosmerno putovanje")
            if klasa == "b":
                price = flight.returnPriceOneWayBussines()
                data.insert(3, "Biznis klasa")
            elif klasa == "e":
                price = flight.returnPriceOneWayEconomic()
                data.insert(3, "Ekonomska klasa")
            else:
                print("Pogresan unos \n")
                reserveFlight()
            
            kol = eval(input("Koliko osoba putuje -> "))
            if kol < 0 or kol > 10:
                print("Broj osoba nije ispravno unesen \n")
                reserveFlight()
            else:
                data.insert(4, kol)
                price *= kol
                data.insert(5, price)
                dataOneWay()
    else:
        print("Unesen pogresan broj leta \n")
        reserveFlight()       

            
def dataOneWay():
    ime = input("Ime vlasnika karte -> ")
    prez = input("Prezime vlasnika karte -> ")
    broj = randint(100, 1000)
    print("Jedinstveni broj karte -> " + str(broj))
    data.insert(6, ime)
    data.insert(7, prez)
    data.insert(8, broj)
    readData()
   
def dataReturn():
    ime = input("Ime vlasnika karte -> ")
    prez = input("Prezime vlasnika karte -> ")
    broj = randint(100, 1000)
    print("Jedinstveni broj karte -> " + str(broj))
    data.insert(7, ime)
    data.insert(8, prez)
    data.insert(9, broj)
    readData()

    
def readData():
    print("Proverite da li ste uneli sve podatke ispravno: \n")
    if data != NULL:
        if data[2] == "Povratno putovanje":
            print(data[0].toString())
            print(data[0].toStringReverse() + "\n")
            print("Tip putovanja -> Povratno putovanje")
            print("Datum polaska -> " + data[1])
            print("Datum povratka -> " + data[3])
            print("Klasa -> " + data[4])
            print("Putnika -> " + str(data[5]))
            print("Ukupna cena -> " + str(data[6]) + " $")
            print("Karta se rezervise na klijenta -> " + data[7] + " " + data[8])
            print("Jedinstveni broj karte -> " + str(data[9]) + "\n")
            confrim()
        else:
            print(data[0].toString() + "\n")
            print("Tip putovanja -> Jednosmerno putovanje")
            print("Datum polaska -> " + data[1])
            print("Klasa -> " + data[3])
            print("Putnika -> " + str(data[4]))
            print("Ukupna cena -> " + str(data[5]) + " $")
            print("Karta se rezervise na klijenta -> " + data[6] + " " + data[7])
            print("Jedinstveni broj karte -> " + str(data[8]) + "\n")
            confrim()
    
def prepareToWriting(data):
    string = "Relacija: "
    if data[2] == "Povratno putovanje":
        string += "Jedinstveni broj karte -> " + str(data[9]) + "\n"
        string += "Ime i prezime klijenta -> " + data[7] + " " + data[8] + "\n"
        string += data[0].toStringJustDest() + " < - > "
        string += data[0].toStringJustDestRev() + "\n"
        string += "Tip putovanja -> Povratno putovanje \n"
        string += "Datum polaska -> " + data[1] + "\n"
        string += "Datum povratka -> " + data[3] + "\n"
        string += "Klasa -> " + data[4] + "\n"
        string += "Karta se rezervise za -> " + str(data[5]) + " putnika \n"
        string += "Ukupna cena -> " + str(data[6]) + " $ \n"
        string += "********************************** \n"
        return string
    else:
        string += "Jedinstveni broj karte -> " + str(data[8]) + "\n"
        string += "Ime i prezime klijenta -> " + data[6] + " " + data[7] + "\n"
        string += data[0].toStringJustDest() + "\n"
        string += "Tip putovanja -> Jednosmerno putovanje \n"
        string += "Datum polaska -> " + data[1] + "\n"
        string += "Klasa -> " + data[3] + "\n"
        string += "Karta se rezervise za -> " + str(data[4]) + " putnika \n"
        string += "Ukupna cena -> " + str(data[5]) + " $ \n"
        string += "********************************** \n"
        return string
        
def printInFile(data):
    
    fajl = open("rezervacije.txt", "r+")
    fajl.read()
    stri = prepareToWriting(data)
    fajl.write(stri)
    fajl.close()
          
def confrim():

    n = input("Da li potvrdjujete rezervaciju karte -> ")
    if n == 'da':
        print("Uspesno rezervisana karta. Rezervaciju proverite u fajlu 'rezervacije.txt' \n")
        printInFile(data)
    else:
        print("Kraj programa")
        return
