#! /usr/bin/python3.2
"""
===============================================================
Project Name:        Advanced Feed
Autor:               Fabian Geiselhart
Erstelldatum:        13.7.15
Zuletzt Bearbeitet:  13.7.15
Typ:                 Python 3 ERROR Klasse
Description:         Errors Anzeigen
===============================================================
"""
#Klasse für Errors
#---------------------------------------------------------------
class error:
    def FileDataError():
        print("File Data Error")
    def ProfileOpenError():
        print("ProfileOpenError\n Profil nicht verhanden")
    def ProfileCreateError():
        print("ProfileCreateError\n Profil schon verhanden")
