#! /usr/bin/python3
from urllib.request import *
import os
import pprint
"""
===============================================================
Project Name:        Advanced Feed
Autor:               Fabian Geiselhart
Erstelldatum:        13.7.15
Zuletzt Bearbeitet:  21.7.15
Typ:                 Python 3 RSS Feed Klasse
Description:         Klasse zum Download und der auswertung eines RSS FEEDS
===============================================================
"""
#Download des Feed Codes
#---------------------------------------------------------------
def down(feed, z):
    feed = check(feed) #Feed Kontrollieren
    text = str(urlopen(feed).read(), encoding="utf-8") #Text Downloaden
    tmpfolder= "/usr/lib/Advanced-Feed/tmp/" #Pfad für Ordner Festlegen
    if os.isdir(tmpfolder) == False: #Wennder Ordner nicht erstellt ist:
        os.mkdir(tmpfolder)          #Erstelle ihn
    os.chdir(tmpfolder) #Wechsle in Ordner
    file = open(feedfolder + "/" + z, "w")
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


#Läd alle Feeds in Dateien im tmp Ordner
#---------------------------------------------------------------
def GetAllFeeds(feedset):
    y = 0 #Zähler = 0
    for i in feedset:  #Alle Downloaden und Speichern
        down(i, y)
        y+=1
    f = open("/usr/lib/Advanced-Feed/tmp/feedz", "w") #Anzahl Speichern
    f.write(y) #Schreiben
    f.close() #Schliesen
    

#Wertet alle in tmp Ordner gespeicherten Feeds aus und 
#-----------------------------------------------------------------
def MakeOneFeedScript
    f = open("/usr/lib/Advanced-Feed/tmp/feedz", "r") #Feedanzahl laden
    z = f.read() #Feedanzahl auslesen
    f.close() #Datei Schliesen
    CFeedList = list(range(z))
    #Listen Für 1. 2. 3. Post, usw,
    1FeedList = [[0]*z]*6 #Liste für Posttime des 1. posts pro feed
    for i in z: #Alle Daten aus Dateien Lesen
        s = "/usr/lib/Advanced-Feed/tmp/" + i 'Speicherort Speichern
        f = open(s, "r") #Öffnen
        CFeedList[i] = f.read() #In Liste Speichern
        f.close() #Schließen
    y = 0 #Zähler auf 0
    for i in CFeedList:
        zw = i
        x = zw.find("<item>") #Schauen wo interressanter Teil anfängt
        zw = zw[x:] #Alles andere Wegschneiden
        CFeedList[i] = zw
    SnipList = CFeedList #Liste Kopieren
    y = 0 #Zähler auf 0
    zz1 = 0 #Zähjler 2 auf 0
    #Nach dem 1. Post in JEDEM Feed suchen
    for i in range(6):
        for i in SnipList: #Alles einmal durchlaufen
            try:
                x = SnipList.find("<pubDate>") #Neustes Pub Date Finden
                1FeedList[zz1][y] = i[x:(x-50)] #In Liste für post Time Sepichern
                zw = i[8:] #Erstes <item> abschneiden
                zw = zw.find("<item>") #Nächstes Item finden
                SnipList[y] = zw #In SnipList Schreiben
            except:
                print("Str. ", y ,"Leer")
            y+=1
        zz1+=1
    y = 0 #Zähler 1 auf 0
    zz1 = 0 #Zähler 2 auf 0
    neuePosts = [0]*6 #Liste für Text mit neusetm Post
    zwlist = [0]*6 #Zwischen Speicher für PubDates
    for i in 1FeedList[y]: #Alle Posts Durchgehen
        for i in 1FeedList[y][zz1]: #
            zwlist[zz1] = i
        zz1+=1
    y+=1
        
