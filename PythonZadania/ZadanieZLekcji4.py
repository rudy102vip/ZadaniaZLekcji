print("\nWitamy w programie do obsługi bazy szkoły\n")
class Uczen:
    def __init__(self, imieUcznia, nazwiskoUcznia, nazwaKlasyUcznia):
        self.imie = imieUcznia
        self.nazwisko = nazwiskoUcznia
        self.nazwaKlasy = nazwaKlasyUcznia

    def __repr__(self):
        return f"Imię: {self.imie.title()}, Nazwisko: {self.nazwisko.title()}, Klasa: {self.nazwaKlasy}"

class Nauczyciel:
    def __init__(self, imieNauczyciela, nazwiskoNauczyciela, przedmiotProwadzony, zajeciaZKlasa):
        self.imie = imieNauczyciela
        self.nazwisko = nazwiskoNauczyciela
        self.przedmiot = przedmiotProwadzony
        self.zajecia = zajeciaZKlasa

    def __repr__(self):
        return f"Imię: {self.imie.title()}, Nazwisko: {self.nazwisko.title()}, " \
               f"Przedmot prowadzony przez nauczyciela: {self.przedmiot.title()}"

class Wychowawca:
    def __init__(self, imieWychowawcy, nazwiskoWychowawcy, prowadzonaKlasa):
        self.imieWychowawcySzkoly = imieWychowawcy
        self.nazwiskoWychowawcySzkoly = nazwiskoWychowawcy
        self.prowadzonaKlasa = prowadzonaKlasa

    def __repr__(self):
        return f"Imie: {self.imieWychowawcySzkoly.title()}, Nazwisko: {self.nazwiskoWychowawcySzkoly.title()}, " \
               f"Prowadzona klasa: {self.prowadzonaKlasa.title()}"

uczniowie = [Uczen(imieUcznia = "kamil", nazwiskoUcznia = "dudziński", nazwaKlasyUcznia = "7C"),
             Uczen(imieUcznia = "agnieszka", nazwiskoUcznia = "bury", nazwaKlasyUcznia = "5D"),
             Uczen(imieUcznia = "weronika", nazwiskoUcznia = "nowak", nazwaKlasyUcznia = "3A"),
             Uczen(imieUcznia = "KaroloNa", nazwiskoUcznia = "kwaśniewska", nazwaKlasyUcznia = "7C")]

nauczyciele = [
                Nauczyciel(imieNauczyciela ="Kazimierz", nazwiskoNauczyciela ="Nowakowski",
                        przedmiotProwadzony = "Przyroda", zajeciaZKlasa = "7C"),
                Nauczyciel(imieNauczyciela = "Joanna", nazwiskoNauczyciela = "Marzec",
                        przedmiotProwadzony = "Biologia", zajeciaZKlasa = "5D")]

wychowawca = [Wychowawca(imieWychowawcy ="Agnieszka", nazwiskoWychowawcy ="Wojciechowska", prowadzonaKlasa ="7C"),
              Wychowawca(imieWychowawcy = "Paweł", nazwiskoWychowawcy = "Burt", prowadzonaKlasa = "3A")]

def znajdzKlase(nazwaKlasy):
    pobierzListeKlas = []
    for listaKlas in uczniowie:
        if listaKlas.nazwaKlasy == nazwaKlasy:
            pobierzListeKlas.append(listaKlas)

    for imieWychowawcySzkoly in wychowawca:
        if imieWychowawcySzkoly.prowadzonaKlasa == nazwaKlasy:
            pobierzListeKlas.append(imieWychowawcySzkoly)
    return pobierzListeKlas

def znajdzNauczycielaProwadzacegoUcznia(imieUcznia, nazwiskoUcznia):
    for uczen in uczniowie:
        if uczen.imie == imieUcznia and uczen.nazwisko == nazwiskoUcznia:
            for nauczyciel in nauczyciele:
                if nauczyciel.zajecia == uczen.nazwaKlasy:
                    return nauczyciel

def znajdzKlasyKtoreProwadziNauczyciel(imieNauczyciela, nazwiskoNauczyciela):
    uczniowieProwadzeniPrzezNauczyciela = []
    for nauczyciel in nauczyciele:
        if nauczyciel.imie == imieNauczyciela and nauczyciel.nazwisko == nazwiskoNauczyciela:
            for uczen in uczniowie:
                if nauczyciel.zajecia in uczen.nazwaKlasy:
                    uczniowieProwadzeniPrzezNauczyciela.append(uczen)
    return uczniowieProwadzeniPrzezNauczyciela

def znajdzWychowawceKlasy(imieWychowawcy, nazwiskoWychowawcy):
    uczniowieProwadzeniPrzezWychowawce = []
    for wychowawcy in wychowawca:
        if wychowawcy.imieWychowawcySzkoly == imieWychowawcy \
            and wychowawcy.nazwiskoWychowawcySzkoly == nazwiskoWychowawcy:
            for uczen in uczniowie:
                if wychowawcy.prowadzonaKlasa in uczen.nazwaKlasy:
                    uczniowieProwadzeniPrzezWychowawce.append(uczen)
    return uczniowieProwadzeniPrzezWychowawce

def main():
    while True:
        opcje = input(f"Wybierz opcję do wyboru:\n 1. Utwórz\n 2. Zarządzaj\n 3. Koniec\n\nPodaj swój wybór: ")
        if opcje == "1":
            while True:
                wyborUtworz = input("Wybierz jedną z opcji:\n 1. Utwórz nowego ucznia\n "
                                    "2. Utwórz nowego nauczyciel\n 3. Utwórz nowego wychowawca\n "
                                    "4. Wróc do menu głównego\n\nPodaj swój wybór: ")

                if wyborUtworz == "1":
                    imieUcznia = input("Podaj imie ucznia szkoły: ")
                    nazwiskoUcznia = input("Podaj nazwisko ucznia szkoły: ")
                    nazwaKlasy = input("Podaj nazwę klasy ucznia: ")
                    uczniowie.append(Uczen(imieUcznia.title(), nazwiskoUcznia.title(), nazwaKlasy))
                    print(uczniowie)

                elif wyborUtworz == "2":
                    imieNauczyciela = input("Podaj imię nauczyciela szkoły: ")
                    nazwiskoNauczyciela = input("Podaj nazwisko nauczyciela szkoły: ")
                    nazwaPrzedmiotu = input("Podaj nazwę przedmiotu jaki nauczyciel prowadzi: ")
                    zajeciaZKlasa = input("Podaj nazwę klasy, którą nauczyciel prwadzi: ")
                    nauczyciele.append(Nauczyciel(imieNauczyciela, nazwiskoNauczyciela, nazwaPrzedmiotu, zajeciaZKlasa))
                    print(nauczyciele)

                elif wyborUtworz == "3":
                    imieWychowawcy = input("Podaj imię wychowawcy klasy: ")
                    nazwiskoWychowawcy = input("Podaj nazwisko wychowawcy klasy: ")
                    klasaProwadzona = input("Podaj klasę którą prowadzi wychowawca: ")
                    wychowawca.append(Wychowawca(imieWychowawcy, nazwiskoWychowawcy, klasaProwadzona))
                    print(wychowawca)

                elif wyborUtworz == "4":
                    break

                else:
                    print("\nWybrałeś niewłaściwą opcję, spróbuj ponownie\n")
                    continue

        elif opcje == "2":
            while True:
                opcje = input("Wybierz jedną z opcji: \n1. Zarządzaj klasami \n2. Zarządzań uczniami "
                              "\n3. Zarządzaj nauczycielami \n4. Zarządzaj wychowawcami "
                              "\n5. Wróc do menu głównego\n\n Podaj swój wybór: ")

                if opcje == "1":
                    podajNazweKlasy = input("Podaj nazwę klasy: ")
                    podajNazweKlasyWSzkole = znajdzKlase(nazwaKlasy = podajNazweKlasy)
                    for wypiszNazweKlasWSzkole in podajNazweKlasyWSzkole:
                        print(wypiszNazweKlasWSzkole)
                    else:
                        print("Nie ma takiego ucznia")

                elif opcje == "2":
                    imieUcznia = input("Podaj imię ucznia: ")
                    nazwiskoUcznia = input("Podaj nazwisko ucznia: ")
                    nauczycielUczacy = znajdzNauczycielaProwadzacegoUcznia(imieUcznia, nazwiskoUcznia)
                    if nauczycielUczacy:
                        print(f"Nauczyciel, który uczy ucznia {imieUcznia.title()} {nazwiskoUcznia.title()}: "
                              f"{nauczycielUczacy}")
                    else:
                        print(f"Nie znaleziono nauczyciela uczącego ucznia o "
                              f"imieniu {imieUcznia} i nazwisku {nazwiskoUcznia}.")

                elif opcje == "3":
                    imieNauczyciela = input("Podaj imie nauczyciela: ")
                    nazwiskoNauczyciela = input("Podaj nazwisko nauczyciela: ")
                    nauczycielProwadzacyKlase = znajdzKlasyKtoreProwadziNauczyciel(imieNauczyciela, nazwiskoNauczyciela)
                    if nauczycielProwadzacyKlase:
                        for uczen in nauczycielProwadzacyKlase:
                            print(f"Nauczyciel {imieNauczyciela} {nazwiskoNauczyciela} prowadzi następujące klasy {uczen}")
                    else:
                        print("Brak uczniów prowadzonych przez tego nauczyciela.")

                elif opcje == "4":
                    imieWychowawcy = input("Podaj imie wychowawcy: ")
                    nazwiskoWychowawcy = input("Podaj nazwisko wychowawcy: ")
                    wychowawcaProwadzacyKlase = znajdzWychowawceKlasy(imieWychowawcy, nazwiskoWychowawcy)
                    if wychowawcaProwadzacyKlase:
                        for uczen in wychowawcaProwadzacyKlase:
                            print(uczen)
                    else:
                        print("Brak uczniów prowadzonych przez tego wychowawcę")

                elif opcje == "5":
                    break

                else:
                    print("\nWybrałeś niewłaściwą opcję, spróbuj ponownie\n")
                    continue


        elif opcje == "3":
            print("Koniec programu")
            break
        else:
            print("Wybrałeś nieprawidłową opcję, spróbuj ponownie")

if __name__ == "__main__":
    main()