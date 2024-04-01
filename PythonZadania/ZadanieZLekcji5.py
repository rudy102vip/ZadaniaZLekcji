
print("Witam w naszym programie do wypożyczanie kaset VHS")
saldo = 1000
konto = []
film = [
    {
    "tytulFilmu" : "Potop",
    "rezyser" : "Hoffman",
    "produkcja" : "Zespół Filmowy 'X'",
    "iloscSztuk" : 10,
    "iloscDostepnychSztuk" : 5,
    }
]

zakonczProgram = False
while not zakonczProgram:
    menuWyboru = input("Wybierz z listy operację do wykonania:\n1. Saldo, \n2. Sprzedaż, \n3. Zakup, \n4. Konto, \n5. "
                       "Lista, \n6. Magazyn, \n7. Przegląd, \n8. Koniec programu\n\nWpisz wybraną opcję: ")
    if menuWyboru == "1":
        dodajDoSalda = float(input("Podaj kwotę jaką chcesz dodać do salda: "))
        saldo = float(saldo)
        noweSaldo = saldo + dodajDoSalda
        with open("plik.txt", "r") as plik:
            dodajDoSalda = str(plik.readline())
        if noweSaldo < 0:
            print("Nie możesz mieć ujemniego salda")
        else:
            saldo = noweSaldo
            konto.append(f"Twoje aktualne saldo po operacji wynosi: {saldo}")
            with open("plik.txt", "a+") as plik:
                plik.write(str(saldo))

    if menuWyboru == "2":
        tytulFilmu = input("Podaj tytuł filmu jaki chcesz wypożyczyć: ")
        podajRezysera = input("Podaj reżysera filmu: ")
        znalezionoFilm = False
        wypozyczonoFilm = False
        for filmoteka in film:
            if filmoteka["tytulFilmu"] == tytulFilmu and filmoteka["rezyser"] == podajRezysera:
                znalezionoFilm = True
                if filmoteka["iloscDostepnychSztuk"] > 0:
                    filmoteka["iloscDostepnychSztuk"] -= 1
                    wypozyczonoFilm = True
                    saldo += 20
                    print(f"Wypożyczono film {tytulFilmu}")

        if not znalezionoFilm:
            print("Nie znaleziono filmu o podanych danych")
            konto.append("Próba wypożyczenia filmu, którego nie mamy")
        elif znalezionoFilm and not wypozyczonoFilm:
            print("Niestety ten film nie jest dostępny")
            konto.append(f"Próba wypożyczenia {tytulFilmu}, brak dostępności")
    print()

    if menuWyboru == "3":
        tytulFilmuZakup = input("Podaj tytuł filmu jaki chcesz kupić: ")
        rezyserZakup = input("Podaj nazwisko reżysera filmu jaki chcesz kupić: ")
        produkcjaZakup = input("Podaj producenta filmu jaki chcesz zakupić: ")
        iloscSztukZakup = int(input("Podaj ilość sztuk jakią chcesz zakupić: "))
        cenaZakup = float(input("Podaj cen zakupu filmu: "))
        if saldo >= iloscSztukZakup * cenaZakup:
            film.append(
            {
            "tytulFilmu" : tytulFilmuZakup.title(),
            "rezyser" : rezyserZakup.title(),
            "produkcja" : produkcjaZakup.title(),
            "iloscSztuk" : iloscSztukZakup,
            "iloscDostepnychSztuk" : iloscSztukZakup
            })
            saldo = saldo - (iloscSztukZakup * cenaZakup)
        else:
            print("Nie możemy dokonać zakupu filmu")

    elif menuWyboru == "4":
        with open("plik.txt", "r") as plik:
            saldo = plik.readline()
            print(f"Na twoim koncie aktualnie masz do dyspozycji {saldo} środków PLN")

    if menuWyboru == "5":
        for filmyNaPolce in film:
            print("Filmy dostępne do wypożyczenia: ")
            for klucz, wartosc in filmyNaPolce.items():
                print(f"{klucz} : {wartosc}")
                print()

    if menuWyboru == "6":
        tytulFilmuMagazyn = input("Podaj nazwę filmu: ")
        znalezionoFilm = False
        for stanMagazynowy in film:
            if stanMagazynowy["tytulFilmu"] == tytulFilmuMagazyn:
                znalezionoFilm = True
                iloscSztuk = stanMagazynowy.get("iloscSztuk")
                iloscDostepnychSztuk = stanMagazynowy.get("iloscDostepnychSztuk")
                print(f"Ilość sztuk: {iloscSztuk}")
                print(f"Ilość dostępnych sztuk: {iloscDostepnychSztuk}")
                break
        if not znalezionoFilm:
            print("Nie mamy w bazie takiego filmu")

    if menuWyboru == "7":
        od = input("Podaj mi wartość początkową: ")
        do = input(("Podaj mi wartość końcową: "))
        if od != "" and do != "":
            print(film[int(od) : int(do)])
        elif od != "" and do != "":
            print(film[int(od):])
        with open("przeglad.txt", "a+") as plik:
            plik.write(str(film) + "\n")

    if menuWyboru == "8":
        zakonczProgram = True
        print("Dziękujemy za skorzystanie z naszego programu")

