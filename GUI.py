from tkinter import *
import own
import os
from tkinter import messagebox
import time as sleep
#Definitionen
#-----------------------------------------------
def neuesprofil():
    print("Neues Profil wird erstellt!")
    pa.destroy()
#Neues Profil ertsellen Fenster-------------------------------
    npe = Tk()
    npe.title("Advanced Feed | Neues Profil erstellen")
    npe.geometry("600x500-600+600")
#NPE Aktionen-------------------------------------------------
    def fertig():
        print("Profil Name: %s" % (pne.get()))
        os.system("mkdir Advanced_Feed_profile") #Erstellt den profile ordner
        messagebox.showinfo("Advanced Feed", "Wähle bitte nun deinen Speicherort")
        s = filedialog.asksaveasfilename() #Sucht den Speicherort
        print("Speicherort:")
        print(s)
        npe.destroy()                       #Zerstört das neues Profil erstellen Fenster#

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

    def tierwelt():
        if CheckVar2.get() == 0:
            tierwelt=0
        else:
            print("Tierwelt")
            tierwelt=1

    def pflanzen():
        if CheckVar3.get() == 0:
            pflanzen=0
        else:
            print("Pflanzen")
            pflanzen=0
        
       

    profilname = Label(master=npe,
                    font=("Arial", 10),
                    text="Name des Profils:",
                    width = 20)

    interessen = Label(master=npe,
                      font=("Arial", 10),
                      text="Markiere deine Interessen!",
                      width = 30)
    
    pne = Entry(npe, width=30)
    
    fertig = Button(master=npe,
               text="Fertig",
               command=fertig,
               font=("Arial", 10), fg="green")

    abbrechen= Button(master=npe,
                text="Abbrechen",
                command=quit,
                font=("Arial", 10), fg="red")

    c0 = Checkbutton(npe, text = "Technik", variable = CheckVar0, onvalue = 1, offvalue = 0, height=3, width = 20, command = technik)
    c1 = Checkbutton(npe, text = "Sport", variable = CheckVar1, onvalue = 1, offvalue = 0, height=3, width = 20, command = sport)
    c2 = Checkbutton(npe, text = "Tierwelt", variable = CheckVar2, onvalue = 1, offvalue = 0, height=3, width = 20, command = tierwelt)
    c3 = Checkbutton(npe, text = "Pflanzen", variable = CheckVar3, onvalue = 1, offvalue = 0, height=3, width = 20, command = pflanzen)

    fertig.grid(column=3, row=7)
    abbrechen.grid(column=2, row=7)
    profilname.grid(column=1, row=1)
    pne.grid(column=2, row=1)
    interessen.grid(column=1, row=2)
    c0.grid(column=1, row=3)
    c1.grid(column=1, row=4)
    c2.grid(column=1, row=5)
    c3.grid(column=1, row=6)

#------------------------------------------------------------------------------------------------------------------------------

def altesprofil():
    print("Altes Profil wird geladen...")
    f = filedialog.askopenfilename() #Sucht den Dateiname
    print (f)
    pa.destroy()
    
    main = Tk()
    main.title("Advaned Feed | Projekt von Fabian & Henning")
    main.geometry('700x700-700+350')

    menu = Menu(master=main)
    scrollbar = Scrollbar(master=main)
    menubar = Menu(master=main)
    main.config(menu=menubar)

    def überuns():
        messagebox.showinfo("Advanced Feed | Über uns", "Advanced Feed 0.2 Alpha         produced by Fabian Geiselhart und Henning Klatt.                  Published: 17.7.2015                  More Information: advancedfeed.ddns.net")

    def feedüber1():
        messagebox.showinfo("Feedüberschrift 1", "Hier dann die genauere Beschreibung auch als Variable")

    
    feedüb1 = "Das ist die Überschriftsvariable 1"

    menubar.add_command(label="anderes Profil laden | ",
                    command=altesprofil)

    menubar.add_command(label="Über Uns | ",
                    command=überuns)

    menubar.add_command(label="Exit | ",
                    command=quit)

    headline = Label(master=main,
                font=("Arial", 17),
                text="Hier ist dein persönlicher Feed:",
                width = 30)

    akprüb = Label(master=main,
                   font=("Arial", 10),
                         text="geladenes Profil:",
                         width = 13,#Breite des Textfeldes
                         height = 3)#Abstand zum Textfeldes

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

    

    canvas_width = 100
    canvas_height = 100
    y = int(canvas_height / 15)
    w.create_line(0, y, 300, y, fill="#476042")
    w2.create_line(0, y, 300, y, fill="#476042")

    feedüberschrift1 = Button(master=main,
                              text=(feedüb1),
                              width = 30,
                              height = 1,
                              command=feedüber1,
                              font=("Arial", 15))



    headline.grid(column=1, row=1)
    scrollbar.grid(column=1, row=1)
    akprofil.grid(column=2,row=2)
    akprüb.grid(column=1, row=2)
    w.grid(column=1, row=3)
    w2.grid(column=1, row=5)
    feedüberschrift1.grid(column=1, row=4)

    
    
#Tkinter
#-----------------------------------------------
pa = Tk()
pa.title("Advaned Feed | Wähle!")
pa.geometry('480x100-700+350')

#Menüpunkte:

#Sonstiges
np=0
ap=0
x=0
own.error.FileDataError()
#Buttons
#----------------------------------------------
neues_profil = Button(master=pa,
                text="neues Profil erstellen",
                command=neuesprofil,
                font=("Arial", 10), fg="green")

altes_profil = Button(master=pa,
                     text="existierendes Profil laden",
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
             text="Bist du ein neuling?",
             width = 30)

#Das Layout
#------Profil-Auswahl-----------------------
frage.grid(column=1, row=1)
neues_profil.grid(column=1, row=2)
altes_profil.grid(column=2, row=2)#row -> Reihe
close2.grid(column=10, row=3)
