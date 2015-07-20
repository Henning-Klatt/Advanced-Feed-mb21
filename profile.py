#! /usr/bin/python3.2
import os
import pickle
"""
===============================================================
Project Name:        Advanced Feed
Autor:               Fabian Geiselhart
Erstelldatum:        13.7.15
Zuletzt Bearbeitet:  16.7.15
Typ:                 Python 3 Funktionen für Profile
Description:         Interagiert mit Profilen
===============================================================
"""

#Erstellt neues Profil in eine .profile-Datei
#--------------------------------------------------------------
"""
profile.create(name, feedset, hobbyset)
name = Späterer name des Profils
feedset = Liste mit ALLEN Feeds für dieses Profil
hobbyset = Liste mit ALLEN Hobbys in KLEINSCHREIBUNG
"""

def create(name, feedset, hobbyset, usenetset):
    #Datei neu erstellen. Modus w
    path = "/usr/lib/Advanced-Feed/profiles"
    os.chdir(path)
    #Neuen Profil Ordner Erstellen und hinein wechseln
    pp = path + "/" + name
    try:
        os.mkdir(pp)
    except:
        pass
    os.chdir(pp)
    #Dateien Öffnen
    ln = name + ".profile"
    ls = open(pp + "/" + name + ".profile", mode="wb") #Liste mit Pfad zu allen anderen Listen
    fs = open(pp + "/" + "feedset.advfed", mode="wb") #Feed Menge
    hs = open(pp + "/" + "hobbyset.advfed", mode="wb") #Hobby Menge
    us = open(pp + "/" + "usenetset.advfed", mode="wb") #Usenet menge
    #Mit Pickle in Dateien Schreiben
    i = [name, pp + "/" + "feedset.advfed", pp + "/" + "hobbyset.advfed", pp + "/" + "usenetset.advfed"]
    pickle.dump(i, ls)
    pickle.dump(feedset, fs)
    pickle.dump(hobbyset, hs)
    pickle.dump(usenetset, us)
    #Dateien Schließen
    ls.close()
    fs.close()
    hs.close()
    us.close()


#Lädt Daten aus .profile Datei in Variablen
#--------------------------------------------------------------
"""
profile.load(path, feedset, hobbyset)
path = Pfad zur .profile Datei
feedset = Ausgabe Variable für Feeds (Menge)
hobbyset = Ausgabe Variable für Hobbys (Menge)
usenetset = Ausgabe Variable für Unsenet Groups (Menge)
"""

def load(path, feedset, hobbyset, usenetset):
    #Ist die Datei eine .profile Datei
    if path[-8:] != ".profile":
        pass
    #Name der Datei Filtern
    zw = path.split("/") #Nach jedem "/" Teilen
    x = len(zw) #Länge von zw ermitteln
    fname = zw[x-1] #Letzter Teil der Liste ist Datei Name
    y = len(fname) #Länge des File Names
    pl = len(path) - y
    fpath = path[0:pl] #Der Ordner Pfad
    os.chdir(fpath) #Ins Profil Verzeichniss Wechseln
    profile = open(path, "rb") #Path im Modus "rb" öffnen
    #Einzelne Datei Pfade zu anderen Dateien Öffnen
    global __filelist
    __filelist = pickle.load(profile) #.profile Datei öffnen und Speichern
    ifeedset = __filelist[1] #feedset in ifeedset Speichern
    ihobbyset = __filelist[2] #hobbyset in ihobbyset speichern
    iusenetset = __filelist[3] #usenetset in iusenetset sepichern
    #.adfed Daten öffnen
    fs = open(ifeedset, "rb")
    hs = open(ihobbyset, "rb")
    us = open(iusenetset, "rb")
    #Daten rekonstruieren
    ifs = pickle.load(fs)
    ihs = pickle.load(hs)
    ius = pickle.load(us)
    #Daten in Parameter Listen Speichern
