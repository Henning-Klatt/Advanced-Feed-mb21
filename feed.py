#! /usr/bin/python3
from urllib.request import *
import os
"""
===============================================================
Project Name:        Advanced Feed
Autor:               Fabian Geiselhart
Erstelldatum:        13.7.15
Zuletzt Bearbeitet:  16.7.15
Typ:                 Python 3 RSS Feed Klasse
Description:         Klasse zum Download und der auswertung eines RSS FEEDS
===============================================================
"""
#Download des Feed Codes
#---------------------------------------------------------------
def down(feed, profil):
    feed = check(feed) #Feed Kontrollieren
    text = str(urlopen(feed).read(), encoding="utf-8") #Text Downloaden
    feedfolder= "/usr/lib/Advanced-Feed/tmp/" #Pfad für Ordner Festlegen
    if os.isdir(feedfolder) == False: #Wennder Ordner nicht erstellt ist:
        os.mkdir(feedfolder)          #Erstelle ihn
    os.chdir(feedfolder) #Wechsle in Ordner
    file = open(feedfolder + "feed", "w")
    file = text
    

#Feed mit www. und http:// ausstatten
#---------------------------------------------------------------
def check(feed):
    if feed[0:6] == "http://" or feed[0:7] == "https://": #Probe ob Protokoll Angegeben
        if feed[7:11] != "www." or feed[8:12] != "www.": #Probe ob www. angegeben
            if feed[0:6] == "http://": #Wenn Link http hat...
                y = feed[7:]           #...dann ergenze www.
                feed = "http://www." + y 
            else:
                y = feed[8:]             #Wenn Link https hat...
                feed = "https://www." + y#...dann ergenze www.
                
        else: #Wenn www. angegeben
            if feed[0:6] == "http://": 
                zw = feed[7:]
                feed = "http://www." + zw #http hinzufügen
            else:
                zw = feed[8:]
                feed = "https://www." + zw #https hinzufügen

    elif feed[0:4] == "www.": #Wenn www. angegeben
        feed = "http://" + feed #http hinzufügen

    else: #sonst beides hinufügen
        feed = "http://www." + feed
    return feed


#Speichert Array mit Posts und Vergleicht welche Posts noch nicht Gezeigt wurden
#-----------------------------------------------------------------
def ComparePosts(path):
    pass
