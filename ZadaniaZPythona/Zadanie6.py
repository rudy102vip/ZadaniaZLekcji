print("Program liczący pole i obwód prostokąta")

bokProstokataA = float(input("Podaj długość boku A prostokąta: "))
bokProstokataB = float(input("Podaj długość boka B prostokąta: "))

poleProstokata = bokProstokataA * bokProstokataB
pole = bokProstokataA * bokProstokataB
obwod = 2 * (bokProstokataA + bokProstokataB)

print(f"Prostokąt o bokach {bokProstokataA} i {bokProstokataB} ma obwód wynoszący {obwod} j. i pole wynoszące {pole} j.kw")