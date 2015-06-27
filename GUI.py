from tkinter import *


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
    fertig = Button(master=npe,
               text="Fertig",
               command=quit,
               font=("Arial", 10), fg="green")

    fertig.grid(column=1, row=1)
     
#------------------------------------------------------------

def altesprofil():
    print("Altes Profil wird geladen...")
    f = filedialog.askopenfilename() #Sucht den Dateiname
    print (f)
    pa.destroy()
#Main Fenster-------------------------------------------------
    main = Tk()
    main.title("Advaned Feed | Projekt von Fabian & Henning")
    main.geometry('700x700-700+350')

#Main Menü----------------------------------------------------
    menu = Menu(master=main)
    scrollbar = Scrollbar(master=main)
    menubar = Menu(master=main)
    main.config(menu=menubar)

    menubar.add_command(label="anderes Profil laden |",
                    command=altesprofil)

    menubar.add_command(label="Exit |",
                    command=quit)

#Main Gadgets------------------------------------------------
    headline = Label(master=main,
                font=("Arial", 17),
                text="Hier ist dein persönlicher Feed:",
                width = 30)

    akprüb = Label(master=main,
                   font=("Arial", 10),
                         text="geladenes Profil:",
                         width = 30)

    akprofil = Label(master=main,
                 font=("Arial", 10),
                 text=(f),
                 width = 30)

    headline.grid(column=1, row=1)
    scrollbar.grid(column=1, row=1)
    akprofil.grid(column=2,row=2)
    akprüb.grid(column=1, row=2)

    
    
#Tkinter
#-----------------------------------------------
pa = Tk()
pa.title("Advaned Feed | Wähle!")
pa.geometry('450x100-700+350')

#Menüpunkte:

#Sonstiges
np=0
ap=0
x=0

#Buttons
#----------------------------------------------
neues_profil = Button(master=pa,
                text="neues Profil erstellen",
                command=neuesprofil,
                font=("Arial", 10), fg="green")

altes_profil = Button(master=pa,
                     text="altes Profil laden",
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
