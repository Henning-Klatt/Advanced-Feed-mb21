from tkinter import *
import os
from tkinter import messagebox
import time as sleep
#import error
#import feed
#import profile
import pickle
"""
===============================================================
Project Name:        Advanced Feed
Autor:               Henning Klatt
Erstelldatum:        02.6.15
Zuletzt Bearbeitet:  16.7.15
Typ:                 Python 3 GUI zum Advanced Feed
Description:         GUI zum allgemeinem umgang mit dem Programm
===============================================================
"""
feed = []# Leert die Globalen Variablen
hobby = []
usenet = []

#Globale Variablen:----------------------------
feedüb1 = "Das ist die Überschriftsvariable 1"
feedinhalttext1 = """Das ist der genauere Inhalt vom 1. Feed,
der auch die möglichkeit hat, bis ins unendliche lang zu sein!"""
feedüb2 = "Das ist die Überschriftsvariable 2"
feedinhalttext2 = "Das ist der genauere Inhalt vom 2. Feed"
feedüb3 = "Das ist die Überschriftsvariable 3"
feedinhalttext3 = """Das ist der genauere Inhalt vom 3. Feed,
der auch ruhig mal sehr lang werden kann,
also so lang, wie es uns passt!"""
    
#Definitionen
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
        npe2.geometry("450x100-300+300")
         #--------------------------------
        userfeedsinfo = Label(master=npe2,
                              font=("Arail", 9),
                              text="Geben sie ihre RSS2 Feeds durch Leerzeichen getrennt ein!",
                              width = 45)

        feeds = Entry(npe2, width=30)
        
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
                    else:
                       print("Technik")
                       technik=1

                def sport():
                    if CheckVar1.get() == 0:
                        sport=0
                    else:
                        print("Sport")
                        sport=1

                def pflanzen():
                    if CheckVar3.get() == 0:
                        pflanzen=0
                    else:
                        print("Pflanzen")
                        pflanzen=0

                def tierwelt():
                    if CheckVar2.get() == 0:
                        tierwelt=0
                    else:
                        print("Tierwelt")
                        tierwelt=1

                def weiterlos2():
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
                command=quit,
                font=("Arial", 10), fg="red")
    pne = Entry(npe, width=30)
    

    fertig.grid(column=2, row=8)
    abbrechen.grid(column=1, row=8)
    profilname.grid(column=1, row=1)
    pne.grid(column=2, row=1)

#------------------------------------------------------------------------------------------------------------------------------

def altesprofil():
    print("Altes Profil wird geladen...")
    f = filedialog.askopenfilename() #Sucht den Dateiname
    print (f)
    #profile.load(f, feed, hobby, usenet)
    pa.destroy()
    
    main = Tk()
    main.title("Advaned Feed | Projekt von Henning & Fabian")
    main.geometry('700x700-700+350')

    menu = Menu(master=main)
    scrollbar = Scrollbar(master=main)
    menubar = Menu(master=main)
    main.config(menu=menubar)

    def überuns():
        messagebox.showinfo("Advanced Feed | Über uns", "Advanced Feed 0.2 Alpha         produced by Henning Klatt und Fabian Geiselhart.                  Published: 17.7.2015                  More Information: advancedfeed.ddns.net")

    def weiterlesen1():
        def kill1():
            wl1.destroy()
            
        wl1 = Tk()
        wl1.title("Advanced Feed | Feed 1")
        wl1.geometry("500x500-500+500")

        fertig1 = Button(master=wl1,
                        text="fertig",
                        command=kill1,
                        font=("Arial", 10), fg="green")

        text1 = Label(master=wl1,
                     font=("Arial", 10),
                     text=(feedinhalttext1),
                     width = 60)

        text1.grid(column=1, row=1)
        fertig1.grid(column=2, row=2)
        

    def feedweiterlesen():
        messagebox.showinfo("Feedüberschrift 2", "Hier dann die genauere Beschreibung auch als Variable")
    
    
    menubar.add_command(label="anderes Profil laden  ",
                    command=altesprofil)

    menubar.add_command(label="Über Uns  ",
                    command=überuns)

    menubar.add_command(label="Exit  ",
                    command=quit)

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
    

    canvas_width = 100
    canvas_height = 100
    y = int(canvas_height / 15)
    w.create_line(0, y, 300, y, fill="#476042")
    w2.create_line(0, y, 300, y, fill="#476042")
    w3.create_line(0, y, 300, y, fill="#476042")

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

    feedüberschrift3 = Label(master=main,
                              font=("Arial", 13),
                              text=(feedüb3),
                              width = 30,)

    
    feedinhalt3 = Label(master=main,
                             font=("Arial", 10),
                             text=(feedinhalttext3),
                             width = 50)

    headline.grid(column=1, row=1)
    scrollbar.grid(column=1, row=1)
    akprofil.grid(column=1,row=2)
    w.grid(column=1, row=3)
    w2.grid(column=1, row=7)
    w3.grid(column=1, row=10)
    w4.grid(column=1, row=13)
    feedüberschrift1.grid(column=1, row=4)
    feedinhalt1.grid(column=1, row=5)
    weiterlesen1.grid(column=1, row=6)
    feedüberschrift2.grid(column=1, row=8)
    feedinhalt2.grid(column=1, row=9)
    feedüberschrift3.grid(column=1, row=11)
    feedinhalt3.grid(column=1, row=12)
    
#Tkinter
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
               command=quit,

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
