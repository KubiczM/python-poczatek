# Obliczanie kcal mężczyźni

def men_kcal():
    print()
    print("PODSTAWOWE INFORMACJE")
    bodyweight = float(input("Jaka jest masa Twojego ciała [w kg]: "))
    heigh = float(input("Ile masz wzrostu [w cm]: "))
    age = float(input("Ile masz lat: "))
    print()
    print("WSPÓŁCZYNNIK AKTYWNOŚCI W TYGODNIU")
    low_activity = float(input("Niska aktywność (większość osób nietrenujących, PAL: 1.4-1.7): "))
    medium_activity = float(input("Średnia aktywność (3-5 treningów w tygodniu, PAL: 1.7-2.0): "))
    high_activity = float(input("Wysoka aktywność (praca fizyczna + regularne treningi, PAL: 2-2.4): "))
    print()
    ppm = (10 * bodyweight) + (6.25 * heigh) - (5 * age) + 5
    print("PODSTAWOWA PRZEMIANA MATERII")
    print(f"Wynik: {ppm} kcal")

    if low_activity > 1.4 and low_activity < 1.7:
        print()
        print("CAŁKOWITA PRZEMIANA MATERII")
        print(f"Wynik: {low_activity * ppm} kcal")
    elif medium_activity > 1.7 and medium_activity < 2.0:
        print()
        print("CAŁKOWITA PRZEMIANA MATERII")
        print(f"Wynik: {medium_activity * ppm} kcal")
    elif high_activity > 2 and high_activity < 2.4:
        print()
        print("CAŁKOWITA PRZEMIANA MATERII")
        print(f"Wynik: {high_activity * ppm} kcal")


# Obliczanie kcal kobiety

def women_kcal():
    print()
    print("PODSTAWOWE INFORMACJE")
    bodyweight = float(input("Jaka jest masa Twojego ciała [w kg]: "))
    heigh = float(input("Ile masz wzrostu [w cm]: "))
    age = float(input("Ile masz lat: "))
    print()
    print("WSPÓŁCZYNNIK AKTYWNOŚCI W TYGODNIU")
    low_activity = float(input("Niska aktywność (większość osób nietrenujących, PAL: 1.4-1.7): "))
    medium_activity = float(input("Średnia aktywność (3-5 treningów w tygodniu, PAL: 1.7-2.0): "))
    high_activity = float(input("Wysoka aktywność (praca fizyczna + regularne treningi, PAL: 2-2.4): "))
    print()
    print("PODSTAWOWA PRZEMIANA MATERII")
    ppm = (10 * bodyweight) + (6.25 * heigh) - (5 * age) - 161
    print(f"Wynik: {ppm} kcal")

    if low_activity > 1.4 and low_activity < 1.7:
        print()
        print("CAŁKOWITA PRZEMIANA MATERII")
        print(f"Wynik: {low_activity * ppm} kcal")
    elif medium_activity > 1.7 and medium_activity < 2.0:
        print()
        print("CAŁKOWITA PRZEMIANA MATERII")
        print(f"Wynik: {medium_activity * ppm} kcal")
    elif high_activity > 2 and high_activity < 2.4:
        print()
        print("CAŁKOWITA PRZEMIANA MATERII")
        print(f"Wynik: {high_activity * ppm} kcal")


# Obliczanie deficytu

def deficit (cpm):
    print()
    print(f"Twoja całkowita przemiana materii wynosi: {cpm} kcal")
    percentage = (float(input("Ile ma wynosić Twój deficyt? [10-20%]: ")))
    percentage_of_deficit = cpm * percentage / 100
    sum_of_deficit = cpm - percentage_of_deficit
    print(f"Twoja łączna ilość kcal przy {percentage}% deficycie będzie wynosić: {sum_of_deficit} kcal")


# Obliczanie nadwyżki

def plus(cpm):
    print()
    print(f"Twoja całkowita przemiana materii wynosi: {cpm} kcal")
    percentage = (float(input("Ile ma wynosić Twója nadwyżka? [10-20%]: ")))
    percentage_of_deficit = cpm * percentage / 100
    sum_of_deficit = cpm + percentage_of_deficit
    print(f"Twoja łączna ilość kcal przy {percentage}% nadwyżce będzie wynosić: {sum_of_deficit} kcal")



men_kcal()
women_kcal()









