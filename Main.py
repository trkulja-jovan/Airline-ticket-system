from Seminarski.sluzbenici import loadEmployee, preglednik, choice

def main():
    print("==================================================")
    print("=           REZERVACIJE AVIO KARATA              =")
    loadEmployee()
    preglednik()
    try:
        n = eval(input("Unesite opciju -> "))
        while n < 1 or n > 5:
            n = eval(input("Unesite opciju -> "))
        choice(n)
    except:
        print("Uneli ste slovo umesto cifre")
        
    
if __name__ == '__main__':
    main()