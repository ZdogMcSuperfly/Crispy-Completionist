from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.font as font
import os
 
#setup
root = Tk()
root.geometry("510x420")

#play button
playlevel = 0
playskill = 0
def PlayDoom():
    print("./crispy-doom -warp "+str(playlevel)+" -skill "+str(SkillVar.get())+" -levelstat")
    os.system("./crispy-doom -warp "+str(playlevel)+" -skill "+str(SkillVar.get())+" -levelstat")

PlayBtn = Button(root, text = "PLAY", command = PlayDoom)
PlayBtn.grid(row=0,column=0, sticky=N)

#skill level and parameter frame
SPframe = Frame(root)
SPframe.grid(row=0,column=1, sticky=N)

#Skill level selector 
MenuBttn = Menubutton(SPframe, text = "Skill level", relief = RAISED)
SkillVar = IntVar()
SkillMenu = Menu(MenuBttn, tearoff = 0)
SkillMenu.add_radiobutton(label = "I'm too young to die", variable = SkillVar, value = 1)
SkillMenu.add_radiobutton(label = "Hey, not too rough", variable = SkillVar, value = 2)
SkillMenu.add_radiobutton(label = "Hurt me plenty", variable = SkillVar, value = 3)
SkillMenu.add_radiobutton(label = "Ultra-Violence", variable = SkillVar, value = 4)
SkillMenu.add_radiobutton(label = "Nightmare!", variable = SkillVar, value = 5)
MenuBttn["menu"] = SkillMenu 
MenuBttn.grid(row=0,column=0, sticky=W)

#parameter selector
FastVar = IntVar()
FChkBttn = Checkbutton(SPframe, text = "Fast", width = 4, variable = FastVar)
FChkBttn.grid(row=0,column=1, sticky=W)

RespawnVar = IntVar()
RChkBtn = Checkbutton(SPframe, text = "Respawn", width = 8, variable = RespawnVar)
RChkBtn.grid(row=0,column=2, sticky=W)

#SPframe spacer (this is a dumb way)
label = Label(SPframe,text = "                                      ")  
label.grid(row=0,column=3, sticky=W)

#WAD name
WNlabel = Label(root,text = "")  
WNlabel.grid(row=1,column=1, sticky=W)

#WAD name progress bar
WADprogress = Progressbar(root, orient = HORIZONTAL, length = 200, mode = 'determinate')
WADprogress.grid_remove()

#WAD selector function
def wadnamechange1(event):
    WADprogress.grid(row=1,column=1, sticky=E)
    if W1listbox.get(W1listbox.curselection()) == "DOOM":
        WNlabel.config(text = "The Ultimate Doom")
    if W1listbox.get(W1listbox.curselection()) == "SIGIL_v1_21":
        WNlabel.config(text = "SIGIL")
    if W1listbox.get(W1listbox.curselection()) == "DOOM2":
        WNlabel.config(text = "Doom II")
    if W1listbox.get(W1listbox.curselection()) == "NERVE":
        WNlabel.config(text = "No Rest for the Living")
    if W1listbox.get(W1listbox.curselection()) == "TNT":
        WNlabel.config(text = "TNT: Evilution")
    if W1listbox.get(W1listbox.curselection()) == "PLUTONIA":
        WNlabel.config(text = "The Plutonia Experiment")
    if W1listbox.get(W1listbox.curselection()) == "MASTERLEVELS":
        WNlabel.config(text = "Master Levels for Doom II")
    WADlevelDrawButton()
    LVLlabel.config(text = "")
    WIframe.grid_remove()

def wadnamechange2(event):
    WADprogress.grid(row=1,column=1, sticky=E) 
    if W2listbox.get(W2listbox.curselection()) == "DBIMPACT":
        WNlabel.config(text = "Double Impact")
    if W2listbox.get(W2listbox.curselection()) == "NEIS":
        WNlabel.config(text = "No End in Sight")
    if W2listbox.get(W2listbox.curselection()) == "DEATHLESS":
        WNlabel.config(text = "Deathless")
    if W2listbox.get(W2listbox.curselection()) == "BTSX_e1":
        WNlabel.config(text = "Back to Saturn X episode 1")
    if W2listbox.get(W2listbox.curselection()) == "BTSX_e2":
        WNlabel.config(text = "Back to Saturn X episode 2")
    if W2listbox.get(W2listbox.curselection()) == "REKKRSA":
        WNlabel.config(text = "REKKR")
    if W2listbox.get(W2listbox.curselection()) == "DOOMZERO":
        WNlabel.config(text = "Doom Zero")
    WADlevelDrawButton()
    LVLlabel.config(text = "")
    #WNlabel.config(text = W2listbox.get(W2listbox.curselection()))

#def wadnamechange3(event):
    #WNlabel.config(text = W3listbox.get(W3listbox.curselection()))

#WAD selector
label = Label(root,text = "id WADs")  
label.grid(row=1,column=0, sticky=W)

W1listbox = Listbox(root, height = 7, width = 15)  
for i, wad in enumerate(["DOOM", "SIGIL_v1_21", "DOOM2", "NERVE", "TNT", "PLUTONIA", "MASTERLEVELS"]): #thanks to akiyamn
    W1listbox.insert(i+1, wad) #thanks to akiyamn
W1listbox.grid(row=2,column=0, sticky=W)
W1listbox.bind('<<ListboxSelect>>', wadnamechange1)

label = Label(root,text = "Add-ons WADs")  
label.grid(row=3,column=0, sticky=W)

W2listbox = Listbox(root, height = 7, width = 15) 
for i, wad in enumerate(["DBIMPACT", "NEIS", "DEATHLESS", "BTSX_e1", "BTSX_e2", "REKKRSA", "DOOMZERO"]): #thanks to akiyamn
    W2listbox.insert(i+1, wad) #thanks to akiyamn  
W2listbox.grid(row=4,column=0, sticky=W)
W2listbox.bind('<<ListboxSelect>>', wadnamechange2)

#coming soon
#label = Label(root,text = "Licenced WADs")  
#label.grid(row=5,column=0, sticky=W)

#W3listbox = Listbox(root, height = 3, width = 15)  
#W3listbox.insert(1,"JPTR_V40")  
#W3listbox.insert(2, "PERDGATE")  
#W3listbox.insert(3, "HELL2PAY")    
#W3listbox.grid(row=6,column=0, sticky=W)
#W3listbox.bind('<<ListboxSelect>>', wadnamechange3)

#WAD button font
WADFont = font.Font(size=8)

#WAD level selector frame
WSframe = Frame(root)
WSframe.grid(row=2,column=1, sticky=NW)

#WAD level names
nDOOMSIGIL=["","","","","","","","","","","","Hangar","Nuclear Plant","Toxin Refinery","Command Control","Phobos Lab","Central Processing","Computer Station","Phobos Anomaly","Military Base","","Deimos Anomaly","Containment Area","Refinery","Deimos Lab","Command Center","Halls of the Damned","Spawning Vats","Tower of Babel","Fortress of Mystery","","Hell Keep","Slough of Despair","Pandemonium","House of Pain","Unholy Cathedral","Mt. Erebus","Limbo","Dis","Warrens","","Hell Beneath","Perfect Hatred","Sever the Wicked","Unruly Evil","They Will Repent","Against Thee Wickedly","And Hell Followed","Unto the Cruel","Fear","","Baphomet's Demesne","Sheol","Cages of the Damned","Paths of Wretchedness","Abaddon's Void","Unspeakable Persecution","Nightmare Underworld","Halls of Perdition","Realm of Iblis"]
nDOOM2=["","Entryway","Underhalls","The Gantlet","The Focus","The Waste Tunnels","The Crusher","Dead Simple","Tricks and Traps","The Pit","Refueling Base","'O' of Destruction!","The Factory","Downtown","The Inmost Dens","Industrial Zone","Suburbs","Tenements","The Courtyard","The Citadel","Gotcha!","Nirvana","The Catacombs","Barrels o' Fun","The Chasm","Bloodfalls","The Abandoned Mines","Monster Condo","The Spirit World","The Living End","Icon of Sin","Wolfenstein","Grosse"]
nNERVE=["","The Earth Base","The Pain Labs","Canyon of the Dead","Hell Mountain","Vivisection","Inferno of Blood","Baron's Banquet","Tomb of Malevolence","March of the Demons"]
nTNT=["","System Control","Human BBQ","Power Control","Wormhole","Hanger","Open Season","Prison","Metal","Stronghold","Redemption","Storage Facility","Crater","Nukage Processing","Steel Works","Dead Zone","Deepest Reaches","Processing Area","Mill","Shipping/Respawning","Central Processing","Administration Center","Habitat","Lunar Mining Project","Quarry","Baron's Den","Ballistyx","Mount Pain","Heck","River Styx","Last Call","Pharaoh","Caribbean"]
nPLUTONIA=["","Congo","Well of Souls","Aztec","Caged","Ghost Town","Baron's Lair","Caughtyard","Realm","Abattoire","Onslaught","Hunted","Speed","The Crypt","Genesis","The Twilight","The Omen","Compound","Neurosphere","NME","The Death Domain","Slayer","Impossible Mission","Tombstone","The Final Frontier","The Temple of Darkness","Bunker","Anti-Christ","The Sewers","Odyssey of Noises","The Gateway of Hell","Cyberden","Go 2 It"]

nDBIMPACT=["","","","","","","","","","","","Maintenance Area","Central Computing","Research Complex","Hydroponic Facility","Engineering Station","Command Center","Waste Treatment","Launch Bay","Operations"]
nNEIS=["","","","","","","","","","","Tom's Halls","Terminal","Slime Trails","Logistics Center","Abandoned Factory","Warehouse","Power Core","Biosphere","Enigma","Quarantine Silos","","Receiving Station","Proving Grounds","Contagion Engine","Derelict Vessel","Deep Storage","Poison Control","Gateway Labs","Rubicon","Castle of Illusion","","Gates of Hades","Emblem of Destruction","The Grinder","Fortuna Bridge","Forgotten Caverns","Anomaly Retribution","Netherworld Citadel","Requiem","Lake of Fire","RGC Alpha","Nexus","Parallels","Square Zero","Wartorn Precinct","The Blood Beneath","Sanctuary of Filth","Vacuum Consortium","No End In Sight","Vile Cross"]
nDEATHLESS=["","","","","","","","","","","","Contagion","Laid to Rust","Sluice Gate","Underflow","Outage","Burial Ground","Mainstay","Embolon","Gods","","Hydroelectrics","Snake Alley","Greenhouse","Virulent","Repugnant Gardens","The Mad Mistress","City of Coal","Dukes","Slain","","Open Wound","Salted Earth","Forlorn Morgue","Vestibule","Soul Drinker","Dire Prayers","Wormwood Cathedral","Ire","The Wastes","","Inhuman Remains","Fetid Site","Corroded","Incision","Serene Shadows","Vertigo","Sea of Entrails","Desecrators","Under"]
nBTSX1=["","Back to Saturn X Radio Report","Postal Blowfish","The Room Taking Shape","A Good Flying Bird","Total Exposure","Mix Up The Satellite","Metal Mothers","Get Out Of My Stations I","Some Drilling Implied","A Proud And Booming Industry","The Colossus Crawls West","Underground Initiations","I'll Replace You With Machines","Big Chief Chinese Restaurant","Tricyclic Looper","Get Out Of My Stations II","Navigating Flood Regions","Cyclone Utilities (Remember Your Birthday)","Bingo Pool Hall of Blood","U.S. Mustard Company","Failed Experiments and Trashed Aircraft","Gonna Never Have To Die","Get Out Of My Stations III","Tough Skin River","The Unsinkable Fats Domino","","","","","","Optical Hopscotch","The Hard Way"]
nBTSX2=["","Shadow Port","Underwater Explosions","Wings of Thorn","Dirty Water","Tower in the Fountain of Sparks I","Useless Inventions","Shrine to the Dynamic Years (Athens Time Change Riots)","A Blue Shadow","Adverse Wind","Eureka Signs","Tower in the Fountain of Sparks II","Demons Are Real","Nation Gone Dry","Shocker in Gloomtown","The Theory of Broken Circles","Tower in the Fountain of Sparks III","Steeple of Knives","Optional Bases Opposed","Unbaited Vicar of Scorched Earth","Speedtraps for the Bee Kingdom","Bulldog Skin","Bite","Tower in the Fountain of Sparks IV","Perhaps Now the Vultures","Unstable Journey","Beneath a Festering Moon","","","","","Fireking Says No Cheating"]
nREK=["","","","","","","","","","","","Sinking","Down","Flurrious","Blade Swamp","Fielding","Rampart","Dripstone Wharf","Hazardous Coast","Pop Some Hops","","On Fire","Drained","Sequester","Metal","Marketplace","Magnus Avenue","Mistory","Audience","Addle","","Isolation","Claustrophilia","Dungeon","Acrophobinox","Shine On","Seeing Red","Siege","Rok","Begin","","Village of Delusion","Ice Melt","Quick","Window Pain","Mal Arena","Cliffusion","Dance Macabre","EyeBrawl","home.wad"]
nZERO=["","High-Rise Roof","Toxic Tower","Marble Zone","Triple Town","The Pits","Echo Halls","Claustrophobia","Module Base","Ancient Archives","Leap Gates","Too Close To Home","Underland","Tease","Crust","Peak Facility","Natural Supply","The Testing Labs","Atom Transporter","Quantum Processing","Familiar Face","Starbourn","The Cracks","Atmos Caves","Booster Hub","Abandoned Compound","Fortification","The Junction","Suspension","The Rematch","The Sarcophagus","Meat","Dark Roof"]

#WAD level selector buttons
def WADlevelDrawButton():
    def ChangeLevelNameOnButtonClick(btxt,bnum):
        WIframe.grid(row=4,column=1, sticky=W)
        global playlevel 
        playlevel = bnum
        if WNlabel.cget("text") == "The Ultimate Doom" or WNlabel.cget("text") == "SIGIL":
            LVLlabel.config(text = btxt+": "+nDOOMSIGIL[bnum])
        if WNlabel.cget("text") == "Doom II" or WNlabel.cget("text") == "SIGIL":
            LVLlabel.config(text = btxt+": "+nDOOM2[bnum])
        if WNlabel.cget("text") == "No Rest for the Living" or WNlabel.cget("text") == "SIGIL":
            LVLlabel.config(text = btxt+": "+nNERVE[bnum])
        if WNlabel.cget("text") == "TNT: Evilution" or WNlabel.cget("text") == "SIGIL":
            LVLlabel.config(text = btxt+": "+nTNT[bnum])
        if WNlabel.cget("text") == "The Plutonia Experiment" or WNlabel.cget("text") == "SIGIL":
            LVLlabel.config(text = btxt+": "+nPLUTONIA[bnum])

        if WNlabel.cget("text") == "Double Impact":
            LVLlabel.config(text = btxt+": "+nDBIMPACT[bnum])
        if WNlabel.cget("text") == "No End in Sight":
            LVLlabel.config(text = btxt+": "+nNEIS[bnum])
        if WNlabel.cget("text") == "Deathless":
            LVLlabel.config(text = btxt+": "+nDEATHLESS[bnum])
        if WNlabel.cget("text") == "Back to Saturn X episode 1":
            LVLlabel.config(text = btxt+": "+nBTSX1[bnum])
        if WNlabel.cget("text") == "Back to Saturn X episode 2":
            LVLlabel.config(text = btxt+": "+nBTSX2[bnum])
        if WNlabel.cget("text") == "REKKR":
            LVLlabel.config(text = btxt+": "+nREK[bnum])
        if WNlabel.cget("text") == "Doom Zero":
            LVLlabel.config(text = btxt+": "+nZERO[bnum])
        
    x=0
    y=0
    i = 0
    levels = 0
    mode = -1 #0 is doom 1s exm1, 1 is doom 2s map04, 2 is sigil start at e5, 3 is NEIS m0s, 4 for btsx1, 5 for btsx2
    #sets the ammount of levels the WAD has
    if WNlabel.cget("text") == "The Ultimate Doom":
        mode = 0; levels = 36
    if WNlabel.cget("text") == "SIGIL":
        mode = 2; levels = 9
    if WNlabel.cget("text") == "Doom II":
        mode = 1; levels = 32
    if WNlabel.cget("text") == "No Rest for the Living":
        mode = 1; levels = 9
    if WNlabel.cget("text") == "TNT: Evilution":
        mode = 1; levels = 32
    if WNlabel.cget("text") == "The Plutonia Experiment":
        mode = 1; levels = 32
    if WNlabel.cget("text") == "Master Levels for Doom II":
        mode = 1; levels = 21
    if WNlabel.cget("text") == "Double Impact":
        mode = 0; levels = 9
    if WNlabel.cget("text") == "No End in Sight":
        mode = 3; levels = 36
    if WNlabel.cget("text") == "Deathless":
        mode = 0; levels = 36
    if WNlabel.cget("text") == "Back to Saturn X episode 1": #1-25 skips to 31,32
        mode = 4; levels = 25
    if WNlabel.cget("text") == "Back to Saturn X episode 2": #1-27 skips to 31,32
        mode = 5; levels = 27
    if WNlabel.cget("text") == "REKKR":
        mode = 0; levels = 36
    if WNlabel.cget("text") == "Doom Zero":
        mode = 1; levels = 32
    #clears the frame the buttons are in ...
    for LVbtn in WSframe.winfo_children():
        LVbtn.destroy()
    #then draws the buttons again so their are no duplicates
    while i < levels:
        if mode == 0 or mode == 3:
            LVbtn = Button(WSframe, text = "E"+str(y+1)+"M"+str(x+1), width = 2, font=WADFont,  command = lambda txt="E"+str(y+1)+"M"+str(x+1),num=((y+1)*10)+(x+1) : ChangeLevelNameOnButtonClick(txt,num))
        if mode == 2:
            LVbtn = Button(WSframe, text = "E"+str(y+5)+"M"+str(x+1), width = 2, font=WADFont,  command = lambda txt="E"+str(y+5)+"M"+str(x+1),num=((y+5)*10)+(x+1) : ChangeLevelNameOnButtonClick(txt,num))
        elif mode == 1 or mode == 4 or mode == 5:
            if i < 9:
                LVbtn = Button(WSframe, text = "MAP0"+str(i+1), width = 2, font=WADFont,  command = lambda txt="MAP0"+str(i+1),num=i+1 : ChangeLevelNameOnButtonClick(txt,num))
            else:
                LVbtn = Button(WSframe, text = "MAP"+str(i+1), width = 2, font=WADFont,  command = lambda txt="MAP"+str(i+1),num=i+1 : ChangeLevelNameOnButtonClick(txt,num))
        LVbtn.grid(row = y, column = x)
        x+=1
        if x == 9:
            x = 0
            y += 1
        i += 1
    
    if mode == 3:
        LVbtn = Button(WSframe, text = "E1M0", width = 2, font=WADFont,  command = lambda txt="E1M0",num=10 : ChangeLevelNameOnButtonClick(txt,num))
        LVbtn.grid(row = 5, column = 0)
        LVbtn = Button(WSframe, text = "E4M0", width = 2, font=WADFont,  command = lambda txt="E4M0",num=40 : ChangeLevelNameOnButtonClick(txt,num))
        LVbtn.grid(row = 5, column = 1)
    if mode == 4:
        LVbtn = Button(WSframe, text = "MAP31", width = 2, font=WADFont,  command = lambda txt="MAP31",num=31 : ChangeLevelNameOnButtonClick(txt,num))
        LVbtn.grid(row = 2, column = 7)
        LVbtn = Button(WSframe, text = "MAP32", width = 2, font=WADFont,  command = lambda txt="MAP32",num=32 : ChangeLevelNameOnButtonClick(txt,num))
        LVbtn.grid(row = 2, column = 8)
    if mode == 5:
        LVbtn = Button(WSframe, text = "MAP31", width = 2, font=WADFont,  command = lambda txt="MAP31",num=31 : ChangeLevelNameOnButtonClick(txt,num))
        LVbtn.grid(row = 4, column = 0)

#WAD level info
LVLlabel = Label(root,text = "")  
LVLlabel.grid(row=3,column=1, sticky=W)

#WAD info frame
WIframe = Frame(root)
WIframe.grid_remove()

#WAD goals frame
WGframe = Frame(WIframe)
WGframe.grid(row=0,column=0, sticky=W)

#WAD goal font
GoalFont = font.Font(size=32)

#WAD goal tool tip functions
def TT(event):
    TTlabel["text"] = ""

def TTexit(event):
    TTlabel["text"] = "Level exited"

def TTpistolstart(event):
    TTlabel["text"] = "Level pistol started"

def TT100kills(event):
    TTlabel["text"] = "100% Kills"

def TT100items(event):
    TTlabel["text"] = "100% Items"

def TT100secrets(event):
    TTlabel["text"] = "100% Secrets"

def TTpartime(event):
    TTlabel["text"] = "Par time beaten"

def TTfast(event):
    TTlabel["text"] = "Fast monsters on"

def TTrespawn(event):
    TTlabel["text"] = "Respawning monsters on"

def TTplus(event):
    TTlabel["text"] = "Co-op monsters on"

#WAD goal text
Glabel = Label(WGframe, font=GoalFont, fg="red", text = "✔️")
Glabel.grid(row=0,column=0, sticky=NE)
Glabel.bind("<Enter>", TTexit)
Glabel.bind("<Leave>", TT)  

Glabel = Label(WGframe, font=GoalFont, fg="red", text = "🔫")  
Glabel.grid(row=0,column=1, sticky=NW)
Glabel.bind("<Enter>", TTpistolstart)
Glabel.bind("<Leave>", TT)

Glabel = Label(WGframe, font=GoalFont, fg="red", text = "👿")  
Glabel.grid(row=0,column=2, sticky=NW)
Glabel.bind("<Enter>", TT100kills)
Glabel.bind("<Leave>", TT)

Glabel = Label(WGframe, font=GoalFont, fg="red", text = "🔑")  
Glabel.grid(row=0,column=3, sticky=NW)
Glabel.bind("<Enter>", TT100items)
Glabel.bind("<Leave>", TT)

Glabel = Label(WGframe, font=GoalFont, fg="red", text = "?")  
Glabel.grid(row=0,column=4, sticky=NW)
Glabel.bind("<Enter>", TT100secrets)
Glabel.bind("<Leave>", TT)

Glabel = Label(WGframe, font=GoalFont, fg="red", text = "⏱️")  
Glabel.grid(row=0,column=5, sticky=NW)
Glabel.bind("<Enter>", TTpartime)
Glabel.bind("<Leave>", TT)

Glabel = Label(WGframe, font=GoalFont, fg="red", text = "🏃")  
Glabel.grid(row=0,column=6, sticky=NW)
Glabel.bind("<Enter>", TTfast)
Glabel.bind("<Leave>", TT)

Glabel = Label(WGframe, font=GoalFont, fg="red", text = "🔄")  
Glabel.grid(row=0,column=7, sticky=NW)
Glabel.bind("<Enter>", TTrespawn)
Glabel.bind("<Leave>", TT)

#Does crispy-doom have a command for co-op monsters?
#Glabel = Label(WGframe, font=GoalFont, fg="red", text = "+")  
#Glabel.grid(row=0,column=8, sticky=NW)
#Glabel.bind("<Enter>", TTplus)
#Glabel.bind("<Leave>", TT)
#✔=exited,🔫=pistol start,🏃=fast,🔄=respawn,⏱️=par time,👿=kills,🔑=items,?=secrets,+=co-op monsters spawning
TTlabel = Label(WIframe, text = "")  
TTlabel.grid(row=1,column=0, sticky=E)

label = Label(WIframe, text = "Fastest time:")  
label.grid(row=1,column=0, sticky=NW)
label = Label(WIframe, text = "Total deaths:")  
label.grid(row=2,column=0, sticky=NW)
label = Label(WIframe, text = "Total time:")  
label.grid(row=3,column=0, sticky=NW)

#Total wad stats
#label = Label(root,text = "TOTAL PROGRESS              ")  
#label.grid(row=5,column=1, sticky=N)

#draw window
root.title("Crispy Compleationist")
root.resizable(False, False) 
root.mainloop()