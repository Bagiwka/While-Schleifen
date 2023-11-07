import re

def ist_gueltige_seriennummer(seriennummer):
    return bool(re.match(r'^[a-zA-Z0-9]{12}$', seriennummer))

    #re.match == compare
    #^ == Anfang vom String
    #[a-zA-Z0-9] == prüfe, ob inhalt des Stringes aus chracaters von a-z, A-Z oder 0-9 besteht
    #{10} == wiederhole 10 mal
    #$ == End vom String
    #, seriennummer == führe mit seriennummer aus

def prüfziffer_prüfer(seriennummer):
    i=0
    total = 0
    while i<11:
        if i<2:
            number = ord(seriennummer[i].lower()) - 96
        else:
            number = int(seriennummer[i])
        total = total + number
        i+=1
    total = total % 9
    total = 7 - total
    if total == 0:
        total = 9
    elif total == -1:
        total = 8
    if(int(seriennummer[11]) == total):
        returnvar = True
    else:
        returnvar = False
    return returnvar
    
        

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
    while seriennummer is None or not ist_gueltige_seriennummer(seriennummer) or not prüfziffer_prüfer(seriennummer):
        seriennummer = input("Geben Sie die Seriennummer eines Geldscheins ein: ")
        if not ist_gueltige_seriennummer(seriennummer):
            print("Ungültige Seriennummer. Die Seriennummer muss aus 10 alphanumerischen Zeichen bestehen.")
        elif not prüfziffer_prüfer(seriennummer):
            print("Ungültige Prüfziffer.")

    print("Eingaben sind korrekt!")

    end = input("Repeat (y/n)? ")
    if end == 'n':
        break
