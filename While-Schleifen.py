import re

def ist_gueltige_seriennummer(seriennummer):
    return bool(re.match(r'^[a-zA-Z0-9]{10}$', seriennummer))

    #re.match == compare
    #^ == Anfang vom String
    #[a-zA-Z0-9] == prüfe, ob inhalt des Stringes aus chracaters von a-z, A-Z oder 0-9 besteht
    #{10} == wiederhole 10 mal
    #$ == End vom String
    #, seriennummer == führe mit seriennummer aus

while True:
    zahl = None
    while zahl is None:
        zahl_str = input("Geben Sie eine Zahl ein: ")
        if zahl_str.isdigit():
            zahl = int(zahl_str)
        else:
            print("Ungültige Eingabe. Bitte geben Sie eine positive, ganze Zahl ein.")

    passwort = None
    while passwort is None or len(passwort) < 8:
        passwort = input("Geben Sie ein Passwort (mindestens 8 Zeichen) ein: ")
        if len(passwort) < 8:
            print("Das Passwort muss mindestens 8 Zeichen lang sein.")

    seriennummer = None
    while seriennummer is None or not ist_gueltige_seriennummer(seriennummer):
        seriennummer = input("Geben Sie die Seriennummer eines Geldscheins ein: ")
        if not ist_gueltige_seriennummer(seriennummer):
            print("Ungültige Seriennummer. Die Seriennummer muss aus 10 alphanumerischen Zeichen bestehen.")

    print("Eingaben sind korrekt!")

    end = input("Repeat (y/n)? ")
    if end == 'n':
        break