
print("\nWitamy w programie do obsługi bazy szkoły\n")
class Uczen:
    def __init__(self, imieUcznia, nazwiskoUcznia, nazwaKlasyUcznia):
        self.imie = imieUcznia
        self.nazwisko = nazwiskoUcznia
        self.nazwaKlasy = nazwaKlasyUcznia

    def __repr__(self):
        return f"Imię: {self.imie.title()}, Nazwisko: {self.nazwisko.title()}, Klasa: {self.nazwaKlasy.title()}"

class Nauczyciel:
    def __init__(self, imieNauczyciela, nazwiskoNauczyciela, przedmiotProwadzony):
        self.imie = imieNauczyciela
        self.nazwisko = nazwiskoNauczyciela
        self.przedmiot = przedmiotProwadzony

    def __repr__(self):
        return f"Imię: {self.imie.title()}, Nazwisko: {self.nazwisko.title()}, Przedmot prowadzony przez nauczyciela: {self.przedmiot.title()}"


spolecznoscSzkoly = {
    "uczniowie" : [],
    "nauczyciele" : [],
    "wychowawcy" : []
}

uczniowie = [Uczen(imieUcznia = "kamil", nazwiskoUcznia = "dudziński", nazwaKlasyUcznia = "7C\n"),
             Uczen(imieUcznia = "agnieszka", nazwiskoUcznia = "bury", nazwaKlasyUcznia = "5D\n"),
             Uczen(imieUcznia = "weronika", nazwiskoUcznia = "nowak", nazwaKlasyUcznia = "3A\n")]

nauczyciel = [Nauczyciel(imieNauczyciela = "Kazimierz", nazwiskoNauczyciela = "Nowakowski",
                         przedmiotProwadzony = "Przyroda")]





def dodajUcznia():
    print("uczeń")


def main():
    while True:
        opcje = input(f"Wybierz opcję do wyboru:\n 1. Utwórz\n 2. Zarządzaj\n 3. Koniec\n\nPodaj swój wybór: ")
        if opcje == "1":
            while True:
                wyborUtworz = input("Wybierz jedną z opcji:\n 1. Uczeń\n 2. Nauczyciel\n 3. Wychowawca\n "
                                    "4. Wróc do menu głównego\n\nPodaj swój wybór: ")
                if wyborUtworz == "1":
                    imieUcznia = input("Podaj imie ucznia szkoły: ")
                    nazwiskoUcznia = input("Podaj nazwisko ucznia szkoły: ")
                    nazwaKlasy = input("Podaj nazwę klasy ucznia: ")
                    uczniowie.append(Uczen(imieUcznia.title(), nazwiskoUcznia.title(), nazwaKlasy.title()))
                    print(uczniowie)
                elif wyborUtworz == "2":
                    imieNauczyciela = input("Podaj imię nauczyciela szkoły: ")
                    nazwiskoNauczyciela = input("Podaj nazwisko nauczyciela szkoły: ")
                    nazwaPrzedmiotu = input("Podaj nazwę przedmiotu jaki nauczyciel prowadzi: ")
                    nauczyciel.append(Nauczyciel(imieNauczyciela, nazwiskoNauczyciela, nazwaPrzedmiotu))
                    print(nauczyciel)

                elif wyborUtworz == "3":
                    pass
                elif wyborUtworz == "4":
                    break
                else:
                    print("\nWybrałeś niewłaściwą opcję, spróbuj ponownie\n")
                    continue



        elif opcje == "2":
            pass
        elif opcje == "3":
            print("Koniec programu")
            break
        else:
            print("Wybrałeś nieprawidłową opcję, spróbuj ponownie")

if __name__ == "__main__":
    main()