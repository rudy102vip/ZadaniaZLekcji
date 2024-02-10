print("Witaj w naszym programie do sprawdzenia czy dany wyraz znajduje się w innym wyrazie")

pierwszyWyraz = input("Podaj wyraz, który ma znaleźć się w innnym wyrazie: ")
drugiWyraz = input("Podaj wyraz w którym chcesz szukać: ")

czyJestPodWyrazem = pierwszyWyraz in drugiWyraz

print(czyJestPodWyrazem)