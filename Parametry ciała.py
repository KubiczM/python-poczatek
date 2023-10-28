

def body():
    print()
    print("PODSTAWOWE INFORMACJE")
    heigh = float(input("Wzrost [w cm]: "))
    legs = float(input("Długość kończyny dolnej (mierzona od pachwiny) [w cm]: "))
    tibia = float(input("Długość piszczela (mierzona od kolana do kostki) [w cm]: "))
    femur = float(input("Długość uda (mierzona od pachwiny do kolana) [w cm]: "))
    wingspan = float(input("Rozpiętość ramion (mierzona od opuszka palca do opuszka palca) [w cm]: "))
    arm = float(input("Długość ramienia [w cm]: "))
    forearm = float(input("Długość przedramienia (mierzona od łokcia do nadgarstka) [w cm]: "))
    print()

    percentage_legs = 100 * legs / heigh

    if percentage_legs <= 43:
        print("Kończyny dolne: krótkie")
    elif percentage_legs >= 44 and percentage_legs <= 47:
        print("Kończyny dolne: średnie")
    elif percentage_legs >= 47:
        print("Kończyny dolne: długie")

    percentage_tibia = 100 * tibia / femur

    if percentage_tibia <= 78:
        print("Piszczel: krótki")
    elif percentage_tibia >= 79 and percentage_tibia <= 84:
        print("Piszczel: średni")
    elif percentage_tibia >= 85:
        print("Piszczel: długi")

    if wingspan < heigh:
        print("Kończyny górne: krótkie")
    elif wingspan == heigh or wingspan - heigh < 4:
        print("Kończyny górne: średnie")
    elif wingspan - heigh > 4:
        print("Konczyny górne: długie")

    percentage_forearm = 100 * forearm / arm

    if percentage_forearm <= 75 and percentage_forearm <= 78:
        print("Przedramię: krótkie")
    elif percentage_forearm >= 79 and percentage_forearm <= 84:
        print("Przedramię: średnie")
    elif percentage_forearm >= 85:
        print("Przedramię: długie")





body()





