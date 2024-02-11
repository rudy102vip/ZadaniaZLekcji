# Stwórz program, który generuje spersonalizowaną kartkę urodzinową. Program będzie prosił użytkownika o konkretne
# informacje, a następnie generował kartkę urodzinową na podstawie jego odpowiedzi. Wiek osoby powinien być obliczany
# na podstawie roku urodzenia podanego przez użytkownika.

print("Program do generowania życzeń urodzinowych\n")

imieOdbiorcy = input("Podaj swoje imię: ")
rokUrodzenia = int(input("Podaj swój rok urodzenia: "))

imieNadawcy = input("Podaj imie nadawcy: ")
aktualnyRok = int(2024)
oliczenieAktualnegoRokuUrodzenia = aktualnyRok - rokUrodzenia
spersonalizowanaWiadomość = "Niech Twoje urodziny będą jak najjaśniejsze gwiazdy na niebie – nie do przeoczenia i pełne magii. Sto lat!"
print()
print(f"{imieOdbiorcy} wszystkiego najlepszego z okazji {oliczenieAktualnegoRokuUrodzenia} urodzin!!")
print(spersonalizowanaWiadomość)
print("Życzy " + imieNadawcy)





