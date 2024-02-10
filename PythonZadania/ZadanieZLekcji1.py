# Stwórz program, który generuje spersonalizowaną kartkę urodzinową. Program będzie prosił użytkownika o konkretne
# informacje, a następnie generował kartkę urodzinową na podstawie jego odpowiedzi. Wiek osoby powinien być obliczany
# na podstawie roku urodzenia podanego przez użytkownika.

print("Program do generowania życzeń urodzinowych")

imieOdbiorcy = input("Podaj swoje imię: ")
rokUrodzenia = int(input("Podaj swój rok urodzenia: "))
# wiadomosc = "Wszystkiego najlepszego z okazji urodzin"
imieNadawcy = input("Podaj imie nadawcy: ")
aktualnyRok = 2024
oliczenieAktualnegoRokuUrodzenia = aktualnyRok - rokUrodzenia

print(f"{imieOdbiorcy} wszystkiego najlepszego z okazji {oliczenieAktualnegoRokuUrodzenia} urodzin!!")


