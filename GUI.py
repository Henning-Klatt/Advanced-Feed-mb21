from tkinter import *
import os
from tkinter import messagebox
import time as sleep
import webbrowser
#import error
#import feed
#import profile
import pickle
"""
===============================================================
Project Name:        Advanced Feed
Autor:               Henning Klatt
Erstelldatum:        02.6.15
Zuletzt Bearbeitet:  21.7.15
Typ:                 Python 3 GUI zum Advanced Feed
Description:         GUI zum allgemeinem umgang mit dem Programm
===============================================================
"""
def end():
    os.chdir("/usr/lib/Advanced-Feed/tmp")
    os.system("rm -r *")
    quit()
feed = []# Leert die Globalen Variablen
hobby = []
usenet = []

#Globale Variablen:----------------------------
#(feedüb1 = [0:31]+"Die Normale Variable")  -> Einbau bei Bedarf
#feedüb1 = FeedGet(h1, Str)                 -> 1. (wahrscheinlich) beste Methode
feedüb1 = "Das ist die Überschriftsvariable 1"#Aktuelle Test Methode
feedinhalttext1 = "Das ist der genauere Inhalt vom 1. Feed,\nder auch die möglichkeit hat, bis ins unendliche lang zu sein!"
autor1var = "Autor: Fabian Geiselhart"
kategorie1var = "Raspberry Pi"
veröffentlichung1var = "13.05.2015"
link1 = "www.ardupi.de"
feedüb2 = "Das ist die Überschriftsvariable 2"
feedinhalttext2 = "Das ist der genauere Inhalt vom 2. Feed"
autor2var = "Autor: Fabian Geiselhart"
kategorie2var = "Raspberry Pi"
veröffentlichung2var = "13.05.2015"
link2 = "www.politik.de"
feedüb3 = "Das ist die Überschriftsvariable 3"
feedinhalttext3 = "Das ist der genauere Inhalt vom 3. Feed, \nder auch ruhig mal sehr lang werden kann, \nalso so lang, wie es uns passt!"
autor3var = "Autor: Fabian Geiselhart"
kategorie3var = "Raspberry Pi"
veröffentlichung3var = "13.05.2015"
link3 = "www.feed.de"
feedüb4 = "Die Wunderschöne not Merkel labert..."
feedinhalttext4 = "Die Bundeskanzlerin Angela Merkel hält mal \nwieder nicht ihre versprechen!"
autor4var = "Autor: Fabian Geiselhart"
kategorie4var = "Raspberry Pi"
veröffentlichung4var = "13.05.2015"
link4 = "http://henningswebsite.ddns.net"
feedüb5 = "Das neue iPhone 7 ist erschienen..."
feedinhalttext5 = "Das iPhone 7 soll viele neue Funktionen haben, \nzum einen auch ein Iris Scanner!"
autor5var = "Autor: Fabian Geiselhart"
kategorie5var = "Raspberry Pi"
veröffentlichung5var = "13.05.2015"
link5 = "http://apple.de"
feedüb6 = "Bla Bli Blub ist ein Schimpfwort!"
feedinhalttext6 = "Am Sonntag veröffentlichte die Bild Neuigkeiten! \nBli Bla Blub wird als Schimpfwort anerkannt!"
autor6var = "Autor: Fabian Geiselhart"
kategorie6var = "Raspberry Pi"
veröffentlichung6var = "13.05.2015"
link6 = "bild.de"
    
#Neues Profil erstellen
#-----------------------------------------------
def neuesprofil():
    print("Neues Profil wird erstellt!")
    pa.destroy()
#Neues Profil ertsellen Fenster-------------------------------
    npe = Tk()
    npe.title("Advanced Feed | Neues Profil erstellen")
    npe.geometry("450x100-300+300")
#NPE Aktionen-------------------------------------------------
    
            
    def fertig():
        print("Profil Name: %s" % (pne.get()))
        npe.destroy()
        npe2 = Tk()
        npe2.title("Advanced Feed | Schritt 2")
        npe2.geometry("500x300-300+300")
         #--------------------------------
        userfeedsinfo = Label(master=npe2,
                              font=("Arail", 9),
                              text="Geben sie ihre RSS2 Feeds durch Leerzeichen getrennt ein!",
                              width = 45)

        feeds = Entry(npe2, width=30)
        
        feedbeispiele = Label(master=npe2,
                              font=("Arial", 9),
                              text="Falls sie keine RSS2 Feeds kennen, habe wir hier ein par Beispiele: \n \napple.com/rss/ -> Für Musik/Mac/Apple Infos\nwww.pcwelt.de/rss -> Für PC Infos",
                              width = 60)
                              
        def weiterlos():
                print("Eingetragene Feeds: %s" % (feeds.get()))
                npe2.destroy()
                npe3 = Tk()
                npe3.title("Advanced Feed | Schritt 3")
                npe3.geometry("500x500-300+300")
                
        
                CheckVar0 = IntVar()
                CheckVar1 = IntVar()
                CheckVar2 = IntVar()
                CheckVar3 = IntVar()

                def technik():
                    if CheckVar0.get() == 0:
                        technik=0
                        return 0
                    else:
                       technik=1
                       return 1

                def sport():
                    if CheckVar1.get() == 0:
                        sport=0
                        return 0
                    else:
                        sport=1
                        return 1

                def pflanzen():
                    if CheckVar3.get() == 0:
                        pflanzen=0
                        return 0
                    else:
                        pflanzen=1
                        return 1

                def tierwelt():
                    if CheckVar2.get() == 0:
                        tierwelt=0
                        return 0
                    else:
                        tierwelt=1
                        return 1

                def weiterlos2():
                    print("Deine Interessen:")
                    print("Technik: %s" % technik())
                    print("Sport: %s" % sport())
                    print("Pflanzen: %s" % pflanzen())
                    print("Tierwelt: %s" % tierwelt())
                    npe3.destroy()
                    npe4 = Tk()
                    npe4.title("Advanced Feed | Schritt 4")
                    npe4.geometry("300x300-300+300")

                weiter = Button(master=npe3,
                                text="Weiter",
                                command=weiterlos2,
                                font=("Arial", 10), fg="green")

                info = Label(master=npe3,
                             font=("Arial", 10),
                             text="Bitte markieren sie ihre Interessen",
                             width = 40)

                c0 = Checkbutton(npe3, text = "Technik", variable = CheckVar0, onvalue = 1, offvalue = 0, height=3, width = 20, command = technik)
                c1 = Checkbutton(npe3, text = "    Sport", variable = CheckVar1, onvalue = 1, offvalue = 0, height=3, width = 20, command = sport)
                c2 = Checkbutton(npe3, text = "Tierwelt", variable = CheckVar2, onvalue = 1, offvalue = 0, height=3, width = 20, command = tierwelt)
                c3 = Checkbutton(npe3, text = "Pflanzen", variable = CheckVar3, onvalue = 1, offvalue = 0, height=3, width = 20, command = pflanzen)

                
                info.grid(column=1, row=1)
                c0.grid(column=1, row=2)
                c1.grid(column=1, row=3)
                c2.grid(column=1, row=4)
                c3.grid(column=1, row=5)
                weiter.grid(column=2, row=6)

        weiter = Button(master=npe2,
                text="weiter",
                command=weiterlos,
                font=("Arial", 10), fg="green")

            
        userfeedsinfo.grid(column=1, row=1)
        feeds.grid(column=1, row=2)
        weiter.grid(column=2, row=3)
        feedbeispiele.grid(column=1, row=4)
        
       

    profilname = Label(master=npe,
                    font=("Arial", 10),
                    text="Name des neuen Profils:",
                    width = 25)
    
    fertig = Button(master=npe,
               text="Weiter",
               command=fertig,
               font=("Arial", 10), fg="green")

    abbrechen= Button(master=npe,
                text="Abbrechen",
                command=end,
                font=("Arial", 10), fg="red")
    pne = Entry(npe, width=30)
    

    fertig.grid(column=2, row=8)
    abbrechen.grid(column=1, row=8)
    profilname.grid(column=1, row=1)
    pne.grid(column=2, row=1)

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

def altesprofil():
    print("Altes Profil wird geladen...")
    f = filedialog.askopenfilename() #Sucht den Dateiname
    print (f)
    #profile.load(f, feed, hobby, usenet)
    pa.destroy()
    
    main = Tk()
    main.title("Advaned Feed | Projekt von Henning & Fabian")
    main.geometry('900x700-700+350')

    menu = Menu(master=main)
    scrollbar = Scrollbar(master=main)
    menubar = Menu(master=main)
    main.config(menu=menubar)

    def überuns():
        messagebox.showinfo("Advanced Feed | Über uns", "Advanced Feed 0.2 Alpha         produced by Henning Klatt und Fabian Geiselhart.                  Published: 17.7.2015                  More Information: advancedfeed.ddns.net")

    def weiterlesen1():
        def kill1():
            wl1.destroy()

        def openlink1():
            webbrowser.open(link1)
            
        wl1 = Tk()
        wl1.title("Advanced Feed | Feed 1")
        wl1.geometry("550x500-500+500")

        fertig1 = Button(master=wl1,
                        text="Fertig",
                        command=kill1,
                        font=("Arial", 10), fg="green")

        open1 = Button(master=wl1,
                       text="Öffnen",
                       command=openlink1,
                       font=("Arial", 10), fg="blue")

        text1 = Label(master=wl1,
                     font=("Arial", 10),
                     text=(feedinhalttext1),
                     width = 60)

        autor1 = Label(master=wl1,
                       font=("Arial", 10),
                       text=(autor1var),
                       width = 20)

        text1.grid(column=1, row=1)
        fertig1.grid(column=3, row=2)
        open1.grid(column=2, row=2)
        autor1.grid(column=1, row=3)

    def weiterlesen2():
        def kill2():
            wl2.destroy()

        def openlink2():
            webbrowser.open(link2)

        wl2 = Tk()
        wl2.title("Advanced Feed | Feed 2")
        wl2.geometry("550x500-500+500")

        
        fertig2 = Button(master=wl2,
                        text="Fertig",
                        command=kill2,
                        font=("Arial", 10), fg="green")

        open2 = Button(master=wl2,
                       text="Öffnen",
                       command=openlink2,
                       font=("Arial", 10), fg="blue")

        text2 = Label(master=wl2,
                     font=("Arial", 10),
                     text=(feedinhalttext2),
                     width = 60)

        autor2 = Label(master=wl2,
                       font=("Arial", 10),
                       text=(autor2var),
                       width = 60)

        text2.grid(column=1, row=1)
        autor2.grid(column=1, row=3)
        fertig2.grid(column=3, row=2)
        open2.grid(column=2, row=2)

    def weiterlesen3():
        def kill3():
            wl3.destroy()

        def openlink3():
            webbrowser.open(link3)
            

        wl3 = Tk()
        wl3.title("Advanced Feed | Feed 3")
        wl3.geometry("550x500-500+500")

        
        fertig3 = Button(master=wl3,
                        text="Fertig",
                        command=kill3,
                        font=("Arial", 10), fg="green")

        open3 = Button(master=wl3,
                       text="Öffnen",
                       command=openlink3,
                       font=("Arial", 10), fg="blue")

        text3 = Label(master=wl3,
                     font=("Arial", 10),
                     text=(feedinhalttext3),
                     width = 60)

        autor3 = Label(master=wl3,
                       font=("Arial", 10),
                       text=(autor3var),
                       width = 60)

        text3.grid(column=1, row=1)
        autor3.grid(column=1, row=3)
        fertig3.grid(column=3, row=2)
        open3.grid(column=2, row=2)

    def weiterlesen4():
        def kill4():
            wl4.destroy()

        def openlink4():
            webbrowser.open(link4)

        wl4 = Tk()
        wl4.title("Advanced Feed | Feed 4")
        wl4.geometry("550x500-500+500")

        fertig4 = Button(master=wl4,
                        text="Fertig",
                        command=kill4,
                        font=("Arial", 10), fg="green")

        open4 = Button(master=wl4,
                       text="Öffnen",
                       command=openlink4,
                       font=("Arial", 10), fg="blue")

        text4 = Label(master=wl4,
                      font=("Arial", 10),
                      text=(feedinhalttext4),
                      width = 60)

        autor4 = Label(master=wl4,
                       font=("Arial", 10),
                       text=(autor4var),
                       width = 60)

        text4.grid(column=1, row=1)
        autor4.grid(column=1, row=3)
        fertig4.grid(column=3, row=2)
        open4.grid(column=2, row=2)

    def weiterlesen5():
        def kill5():
            wl5.destroy()

        def openlink5():
            webbrowser.open(link5)

        wl5 = Tk()
        wl5.title("Advanced Feed | Feed 5")
        wl5.geometry("550x500-500+500")

        fertig5 = Button(master=wl5,
                        text="Fertig",
                        command=kill5,
                        font=("Arial", 10), fg="green")

        open5 = Button(master=wl5,
                       text="Öffnen",
                       command=openlink5,
                       font=("Arial", 10), fg="blue")

        text5 = Label(master=wl5,
                      font=("Arial", 10),
                      text=(feedinhalttext5),
                      width = 60)

        autor5 = Label(master=wl5,
                       font=("Arial", 10),
                       text=(autor5var),
                       width = 60)

        text5.grid(column=1, row=1)
        autor5.grid(column=1, row=3)
        fertig5.grid(column=3, row=2)
        open5.grid(column=2, row=2)

    def weiterlesen6():
        def kill6():
            wl6.destroy()

        def openlink6():
            webbrowser.open(link6)

        wl6 = Tk()
        wl6.title("Advanced Feed | Feed 6")
        wl6.geometry("550x500-500+500")

        fertig6 = Button(master=wl6,
                        text="fertig",
                        command=kill6,
                        font=("Arial", 10), fg="green")

        open6 = Button(master=wl6,
                       text="Öffnen",
                       command=openlink6,
                       font=("Arial", 10), fg="blue")

        text6 = Label(master=wl6,
                      font=("Arial", 10),
                      text=(feedinhalttext6),
                      width = 60)

        autor6 = Label(master=wl6,
                       font=("Arial", 10),
                       text=(autor6var),
                       width = 60)

        text6.grid(column=1, row=1)
        autor6.grid(column=1, row=3)
        fertig6.grid(column=3, row=2)
        open6.grid(column=2, row=2)
#-------------------------------------
        
    menubar.add_command(label="anderes Profil laden  ",
                    command=altesprofil)

    menubar.add_command(label="Über Uns  ",
                    command=überuns)

    menubar.add_command(label="Exit  ",
                    command=end)

    headline = Label(master=main,
                font=("Arial", 17),
                text="Hier ist ihr persönlicher Feed:",
                width = 30)

    akprofil = Label(master=main,
                 font=("Arial", 10),
                 text=(f),
                 width = 50)
    w = Canvas(master=main,
               width=500,#Länge der Linie
               height=30)#Abstand zum Textfeld

    w2 = Canvas(master=main,
               width=500,#Länge der Linie
               height=20)#Abstand zum Textfeld
    
    w3 = Canvas(master=main,
               width=500,#Länge der Linie
               height=20)#Abstand zum Textfeld

    w4 = Canvas(master=main,
                width=500,
                height=20)

    w5 = Canvas(master=main,
                width=500,
                height=20)

    w6 = Canvas(master=main,
               width=500,#Länge der Linie
               height=20)#Abstand zum Textfeld

    w7 = Canvas(master=main,
                width=500,
                height=20)

    w8 = Canvas(master=main,
                width=500,
                height=20)
    

    canvas_width = 100
    canvas_height = 100
    y = int(canvas_height / 15)
    w.create_line(0, y, 300, y, fill="#476042")
    w2.create_line(0, y, 300, y, fill="#476042")
    w3.create_line(0, y, 300, y, fill="#476042")
    w4.create_line(0, y, 300, y, fill="#476042")
    w5.create_line(0, y, 300, y, fill="#476042")
    w6.create_line(0, y, 300, y, fill="#476042")
    w7.create_line(0, y, 300, y, fill="#476042")
    w8.create_line(0, y, 300, y, fill="#476042")

    feedüberschrift1 = Label(master=main,
                              font=("Arial", 13),
                              text=(feedüb1),
                              width = 30,)

    feedinhalt1 = Label(master=main,
                             font=("Arial", 10),
                             text=(feedinhalttext1),
                             width = 50)

    weiterlesen1 = Button(master=main,
                          text="Weiterlesen",
                          command=weiterlesen1,
                          font=("Arial", 10), fg="black")
                          
                            
    feedüberschrift2 = Label(master=main,
                             font=("Arial", 13),
                             text=(feedüb2),
                             width = 30)

    feedinhalt2 = Label(master=main,
                             font=("Arial", 10),
                             text=(feedinhalttext2),
                             width = 50)

    weiterlesen2 = Button(master=main,
                          text="Weiterlesen",
                          command=weiterlesen2,
                          font=("Arial", 10), fg="black")

    feedüberschrift3 = Label(master=main,
                              font=("Arial", 13),
                              text=(feedüb3),
                              width = 30,)

    
    feedinhalt3 = Label(master=main,
                             font=("Arial", 10),
                             text=(feedinhalttext3),
                             width = 50)

    weiterlesen3 = Button(master=main,
                          text="Weiterlesen",
                          command=weiterlesen3,
                          font=("Arial", 10), fg="black")

    feedüberschrift4 = Label(master=main,
                             font=("Arial", 13),
                             text=(feedüb4),
                             width = 30)

    feedinhalt4 = Label(master=main,
                        text=(feedinhalttext4),
                        width = 50)

    weiterlesen4 = Button(master=main,
                          text="Weiterlesen",
                          command=weiterlesen4,
                          font=("Arial", 10), fg="black")

    feedüberschrift5 = Label(master=main,
                             font=("Arial", 13),
                             text=(feedüb5),
                             width = 30)

    feedinhalt5 = Label(master=main,
                        text=(feedinhalttext5),
                        width = 50)

    weiterlesen5 = Button(master=main,
                          text="Weiterlesen",
                          command=weiterlesen5,
                          font=("Arial", 10), fg="black")

    feedüberschrift6 = Label(master=main,
                             font=("Arial", 13),
                             text=(feedüb6),
                             width = 30)

    feedinhalt6 = Label(master=main,
                        text=(feedinhalttext6),
                        width = 50)

    weiterlesen6 = Button(master=main,
                          text="Weiterlesen",
                          command=weiterlesen6,
                          font=("Arial", 10), fg="black")
    
    headline.grid(column=1, row=1)
    scrollbar.grid(column=1, row=1)
    akprofil.grid(column=1,row=2)
    w.grid(column=1, row=3)
    w2.grid(column=1, row=7)
    w3.grid(column=1, row=11)
    w4.grid(column=1, row=15)
    feedüberschrift1.grid(column=1, row=4)
    feedinhalt1.grid(column=1, row=5)
    weiterlesen1.grid(column=1, row=6)
    feedüberschrift2.grid(column=1, row=8)
    feedinhalt2.grid(column=1, row=9)
    weiterlesen2.grid(column=1, row=10)
    feedüberschrift3.grid(column=1, row=12)
    feedinhalt3.grid(column=1, row=13)
    weiterlesen3.grid(column=1, row=14)
    feedüberschrift4.grid(column=2, row=4)
    feedinhalt4.grid(column=2, row=5)
    weiterlesen4.grid(column=2, row=6)
    w5.grid(column=2, row=7)
    feedüberschrift5.grid(column=2, row=8)
    feedinhalt5.grid(column=2, row=9)
    weiterlesen5.grid(column=2, row=10)
    w6.grid(column=2, row=11)
    feedüberschrift6.grid(column=2, row=12)
    feedinhalt6.grid(column=2, row=13)
    weiterlesen6.grid(column=2, row=14)
    w7.grid(column=2, row=15)
    
#Anfangsfrage
#-----------------------------------------------
pa = Tk()
pa.title("Advaned Feed | Wähle!")
pa.geometry('400x100-700+350')

#Menüpunkte:

#Sonstiges
np=0
ap=0
x=0
#error.FileDataError()
#Buttons
#----------------------------------------------
neues_profil = Button(master=pa,
                text="Nein",
                command=neuesprofil,
                font=("Arial", 10), fg="green")

altes_profil = Button(master=pa,
                     text="Ja",
                     command=altesprofil,
                     font=("Arial", 10), fg="blue")

close2 = Button(master=pa,
               text="Schliessen",
               command=end,

               font=("Arial", 10), fg="red")


#Labels
#--------------------------------------------
frage = Label(master=pa,
             font=("Arial", 10),
             text="Wollen sie ein existierendes Profil laden?",
             width = 34)

#Das Layout
#------Profil-Auswahl-----------------------
frage.grid(column=1, row=1)
neues_profil.grid(column=1, row=2)
altes_profil.grid(column=2, row=2)#row -> Reihe
close2.grid(column=10, row=3)
