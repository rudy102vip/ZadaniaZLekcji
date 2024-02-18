print("Witam w programie do obsługi ładowania paczek")

iloscPaczek = int(input("Wprowadz ilosc paczek do wysłania: "))

wagaPaczki = 0
najwiecejPustychKg = 0
numerPaczkiZNajwiekszailosciaKg = 0

for paczki in range(iloscPaczek):
    wagaPojedynczejPaczki = int(input(f"Podaj wagę paczki {paczki + 1} (1-10): "))
    while wagaPojedynczejPaczki < 1 or wagaPojedynczejPaczki > 10:
        print("Waga paczki musi być z zakresu 1-10 kg.")
        wagaPojedynczejPaczki = int(input(f"Podaj wagę paczki {paczki + 1} (1-10): "))

    wagaPaczki += wagaPojedynczejPaczki
    pusteKg = 20 - wagaPojedynczejPaczki

    if pusteKg > najwiecejPustychKg:
        najwiecejPustychKg = pusteKg
        numerPaczkiZNajwiekszailosciaKg = paczki + 1

print(f"Wysłano {iloscPaczek} paczek")
print(f"Wysłano {wagaPaczki} kg")
print(f"Suma pustych kilogramów: {najwiecejPustychKg} kg")
print(f"Najwięcej pustych kilogramów ma paczka {numerPaczkiZNajwiekszailosciaKg} ({najwiecejPustychKg} kg)")
