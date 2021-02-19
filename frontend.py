from tkinter import *
from tkinter.ttk import Progressbar
import tkinter.font as font
import os
 
#setup
root = Tk()
root.geometry("510x420")

#play button
playlevel = ""
playskill = 0
playwad = ""
playfast = ""
playrespawn = ""
playsolonet = ""
pickmaster = 0 #this is for picking the correct master level
def PlayDoom():
    playlevel = ''.join(i for i in LVLlabel.cget("text")[0:5] if i.isdigit())

    if WNlabel.cget("text") == "Master Levels for Doom II":
        #print("./crispy-doom"+playwad+playmaster[pickmaster]+".wad -warp "+playlevel+" -skill "+str(SkillVar.get())+playfast+playrespawn+playsolonet+" -levelstat")
        os.system("./crispy-doom"+playwad+playmaster[pickmaster]+".wad -warp "+playlevel+" -skill "+str(SkillVar.get())+playfast+playrespawn+playsolonet+" -levelstat")
    else:
        #print("./crispy-doom"+playwad+" -warp "+playlevel+" -skill "+str(SkillVar.get())+playfast+playrespawn+playsolonet+" -levelstat")
        os.system("./crispy-doom"+playwad+" -warp "+playlevel+" -skill "+str(SkillVar.get())+playfast+playrespawn+playsolonet+" -levelstat")
    print("doom closed")


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
def Fastfunc():
    global playfast
    if FastVar.get() == 1:
        playfast = " -fast"
    else:
        playfast = ""

def Respawnfunc():
    global playrespawn
    if RespawnVar.get() == 1:
        playrespawn = " -respawn"
    else:
        playrespawn = ""

def Solonetfunc():
    global playsolonet
    if SolonetVar.get() == 1:
        playsolonet = " -solo-net"
    else:
        playsolonet = ""

FastVar = IntVar()
FChkBttn = Checkbutton(SPframe, text = "Fast", width = 4, variable = FastVar, command = Fastfunc)
FChkBttn.grid(row=0,column=1, sticky=W)

RespawnVar = IntVar()
RChkBtn = Checkbutton(SPframe, text = "Respawn", width = 8, variable = RespawnVar, command = Respawnfunc)
RChkBtn.grid(row=0,column=2, sticky=W)

SolonetVar = IntVar()
SChkBtn = Checkbutton(SPframe, text = "Plus", width = 4, variable = SolonetVar, command = Solonetfunc)
SChkBtn.grid(row=0,column=3, sticky=W)

#SPframe spacer (this is a dumb way)
label = Label(SPframe,text = "                                      ")  
label.grid(row=0,column=4, sticky=W)

#WAD name
WNlabel = Label(root,text = "")  
WNlabel.grid(row=1,column=1, sticky=W)

#WAD name progress bar
WADprogress = Progressbar(root, orient = HORIZONTAL, length = 200, mode = 'determinate')
WADprogress.grid_remove()

levels = 0
mode = [0]

#WAD selector function
def wadnamechange1(event):
    global playwad
    global playlevel
    global playmaster
    global levels
    global mode
    WADprogress.grid(row=1,column=1, sticky=E)
    if W1listbox.get(W1listbox.curselection()) == "DOOM":
        WNlabel.config(text = "The Ultimate Doom")
        playwad = " -iwad doom.wad"
        levels = 36
        mode = [11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49]
    if W1listbox.get(W1listbox.curselection()) == "SIGIL_v1_21":
        WNlabel.config(text = "SIGIL")
        playwad = " -iwad doom.wad -file sigil_v1_21.wad"
        levels = 9
        mode = [51,52,53,54,55,56,57,58,59]
    if W1listbox.get(W1listbox.curselection()) == "DOOM2":
        WNlabel.config(text = "Doom II")
        playwad = " -iwad doom2.wad"
        levels = 32
        mode = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    if W1listbox.get(W1listbox.curselection()) == "NERVE":
        WNlabel.config(text = "No Rest for the Living")
        playwad = " -iwad doom2.wad -file nerve.wad"
        levels = 9
        mode = [1,2,3,4,5,6,7,8,9] 
    if W1listbox.get(W1listbox.curselection()) == "TNT":
        WNlabel.config(text = "TNT: Evilution")
        playwad = " -iwad tnt.wad"
        levels = 32
        mode = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    if W1listbox.get(W1listbox.curselection()) == "PLUTONIA":
        WNlabel.config(text = "The Plutonia Experiment")
        playwad = " -iwad plutonia.wad"
        levels = 32
        mode = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    if W1listbox.get(W1listbox.curselection()) == "MASTERLEVELS": #THIS IS GONNA BE A PAIN IN THE ASS TO GET WORKING SO ABRITRARY :O
        WNlabel.config(text = "Master Levels for Doom II")
        playwad = " -iwad doom2.wad -file masterlevels/"
        playmaster = ["ATTACK","BLACKTWR","BLOODSEA","CANYON","CATWALK","COMBINE","FISTULA","GARRISON","GERYON","MANOR","MEPHISTO","MINOS","NESSUS","PARADOX","SUBSPACE","SUBTERRA","TEETH","TEETH","TTRAP","VESPERAS","VIRGIL"] #picks the correct master levels wad
        levels = 21
        mode = [1,25,7,1,1,1,1,1,8,1,7,5,7,1,1,1,31,32,1,9,3]
    WADlevelDrawButton()
    LVLlabel.config(text = "")
    WIframe.grid_remove()
    playlevel = ""

def wadnamechange2(event):
    global playwad
    global playlevel
    global levels
    global mode
    WADprogress.grid(row=1,column=1, sticky=E) 
    if W2listbox.get(W2listbox.curselection()) == "DBIMPACT":
        WNlabel.config(text = "Double Impact")
        playwad = " -iwad doom.wad -file dbimpact.wad"
        levels = 9
        mode = [11,12,13,14,15,16,17,18,19]
    if W2listbox.get(W2listbox.curselection()) == "NEIS":
        WNlabel.config(text = "No End in Sight")
        playwad = " -iwad doom.wad -file neis.wad -deh neis.deh"
        levels = 38
        mode = [11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,10,40]
    if W2listbox.get(W2listbox.curselection()) == "DEATHLESS":
        WNlabel.config(text = "Deathless")
        playwad = " -iwad doom.wad -file deathless.wad"
        levels = 36
        mode = [11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49]
    if W2listbox.get(W2listbox.curselection()) == "BTSX_e1":
        WNlabel.config(text = "Back to Saturn X episode 1")
        playwad = " -iwad doom2.wad -file btsx_e1a.wad btsx_e1b.wad -deh btsx_e1.deh"
        levels = 27
        mode = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,31,32]
    if W2listbox.get(W2listbox.curselection()) == "BTSX_e2":
        WNlabel.config(text = "Back to Saturn X episode 2")
        playwad = " -iwad doom2.wad -file btsx_e2a.wad btsx_e2b.wad -deh btsx_e2.deh"
        levels = 28
        mode = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,31]
    if W2listbox.get(W2listbox.curselection()) == "REKKR":
        WNlabel.config(text = "REKKR")
        playwad = " -iwad doom.wad -file rekkr.wad -deh rekkr.deh"
        levels = 36
        mode = [11,12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49]
    if W2listbox.get(W2listbox.curselection()) == "DOOMZERO":
        WNlabel.config(text = "Doom Zero")
        playwad = " -iwad doom2.wad -file DoomZero.wad -deh doomzero.deh" #this one is case senestive for whatever reason
        levels = 32
        mode = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
    WADlevelDrawButton()
    LVLlabel.config(text = "")
    WIframe.grid_remove()
    playlevel = ""

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
for i, wad in enumerate(["DBIMPACT", "NEIS", "DEATHLESS", "BTSX_e1", "BTSX_e2", "REKKR", "DOOMZERO"]): #thanks to akiyamn
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
nDOOM=["Hangar","Nuclear Plant","Toxin Refinery","Command Control","Phobos Lab","Central Processing","Computer Station","Phobos Anomaly","Military Base","Deimos Anomaly","Containment Area","Refinery","Deimos Lab","Command Center","Halls of the Damned","Spawning Vats","Tower of Babel","Fortress of Mystery","Hell Keep","Slough of Despair","Pandemonium","House of Pain","Unholy Cathedral","Mt. Erebus","Limbo","Dis","Warrens","Hell Beneath","Perfect Hatred","Sever the Wicked","Unruly Evil","They Will Repent","Against Thee Wickedly","And Hell Followed","Unto the Cruel","Fear"]
nSIGIL=["Baphomet's Demesne","Sheol","Cages of the Damned","Paths of Wretchedness","Abaddon's Void","Unspeakable Persecution","Nightmare Underworld","Halls of Perdition","Realm of Iblis"]
nDOOM2=["Entryway","Underhalls","The Gantlet","The Focus","The Waste Tunnels","The Crusher","Dead Simple","Tricks and Traps","The Pit","Refueling Base","'O' of Destruction!","The Factory","Downtown","The Inmost Dens","Industrial Zone","Suburbs","Tenements","The Courtyard","The Citadel","Gotcha!","Nirvana","The Catacombs","Barrels o' Fun","The Chasm","Bloodfalls","The Abandoned Mines","Monster Condo","The Spirit World","The Living End","Icon of Sin","Wolfenstein","Grosse"]
nNERVE=["The Earth Base","The Pain Labs","Canyon of the Dead","Hell Mountain","Vivisection","Inferno of Blood","Baron's Banquet","Tomb of Malevolence","March of the Demons"]
nTNT=["System Control","Human BBQ","Power Control","Wormhole","Hanger","Open Season","Prison","Metal","Stronghold","Redemption","Storage Facility","Crater","Nukage Processing","Steel Works","Dead Zone","Deepest Reaches","Processing Area","Mill","Shipping/Respawning","Central Processing","Administration Center","Habitat","Lunar Mining Project","Quarry","Baron's Den","Ballistyx","Mount Pain","Heck","River Styx","Last Call","Pharaoh","Caribbean"]
nPLUTONIA=["Congo","Well of Souls","Aztec","Caged","Ghost Town","Baron's Lair","Caughtyard","Realm","Abattoire","Onslaught","Hunted","Speed","The Crypt","Genesis","The Twilight","The Omen","Compound","Neurosphere","NME","The Death Domain","Slayer","Impossible Mission","Tombstone","The Final Frontier","The Temple of Darkness","Bunker","Anti-Christ","The Sewers","Odyssey of Noises","The Gateway of Hell","Cyberden","Go 2 It"]
nMASTER=["Attack","Black Tower","Bloodsea Keep","Canyon","The Catwalk","The Combine","The Fistula","The Garrison","Geryon","Titan Manor","Mephisto's Maosoleum","Minos' Judgement","Nessus","Paradox","Subspace","Subterra","The Express Elevator To Hell","Bad Dream","Trapped On Titan","Vesperas","Virgil's Lead",]

nDBIMPACT=["Maintenance Area","Central Computing","Research Complex","Hydroponic Facility","Engineering Station","Command Center","Waste Treatment","Launch Bay","Operations"]
nNEIS=["Terminal","Slime Trails","Logistics Center","Abandoned Factory","Warehouse","Power Core","Biosphere","Enigma","Quarantine Silos","Receiving Station","Proving Grounds","Contagion Engine","Derelict Vessel","Deep Storage","Poison Control","Gateway Labs","Rubicon","Castle of Illusion","Gates of Hades","Emblem of Destruction","The Grinder","Fortuna Bridge","Forgotten Caverns","Anomaly Retribution","Netherworld Citadel","Requiem","Lake of Fire","Nexus","Parallels","Square Zero","Wartorn Precinct","The Blood Beneath","Sanctuary of Filth","Vacuum Consortium","No End In Sight","Vile Cross","Tom's Halls","RGC Alpha"]
nDEATHLESS=["Contagion","Laid to Rust","Sluice Gate","Underflow","Outage","Burial Ground","Mainstay","Embolon","Gods","Hydroelectrics","Snake Alley","Greenhouse","Virulent","Repugnant Gardens","The Mad Mistress","City of Coal","Dukes","Slain","Open Wound","Salted Earth","Forlorn Morgue","Vestibule","Soul Drinker","Dire Prayers","Wormwood Cathedral","Ire","The Wastes","Inhuman Remains","Fetid Site","Corroded","Incision","Serene Shadows","Vertigo","Sea of Entrails","Desecrators","Under"]
nBTSX1=["Back to Saturn X Radio Report","Postal Blowfish","The Room Taking Shape","A Good Flying Bird","Total Exposure","Mix Up The Satellite","Metal Mothers","Get Out Of My Stations I","Some Drilling Implied","A Proud And Booming Industry","The Colossus Crawls West","Underground Initiations","I'll Replace You With Machines","Big Chief Chinese Restaurant","Tricyclic Looper","Get Out Of My Stations II","Navigating Flood Regions","Cyclone Utilities (Remember Your Birthday)","Bingo Pool Hall of Blood","U.S. Mustard Company","Failed Experiments and Trashed Aircraft","Gonna Never Have To Die","Get Out Of My Stations III","Tough Skin River","The Unsinkable Fats Domino","Optical Hopscotch","The Hard Way"]
nBTSX2=["Shadow Port","Underwater Explosions","Wings of Thorn","Dirty Water","Tower in the Fountain of Sparks I","Useless Inventions","Shrine to the Dynamic Years (Athens Time Change Riots)","A Blue Shadow","Adverse Wind","Eureka Signs","Tower in the Fountain of Sparks II","Demons Are Real","Nation Gone Dry","Shocker in Gloomtown","The Theory of Broken Circles","Tower in the Fountain of Sparks III","Steeple of Knives","Optional Bases Opposed","Unbaited Vicar of Scorched Earth","Speedtraps for the Bee Kingdom","Bulldog Skin","Bite","Tower in the Fountain of Sparks IV","Perhaps Now the Vultures","Unstable Journey","Beneath a Festering Moon","","Fireking Says No Cheating"]
nREK=["Sinking","Down","Flurrious","Blade Swamp","Fielding","Rampart","Dripstone Wharf","Hazardous Coast","Pop Some Hops","On Fire","Drained","Sequester","Metal","Marketplace","Magnus Avenue","Mistory","Audience","Addle","Isolation","Claustrophilia","Dungeon","Acrophobinox","Shine On","Seeing Red","Siege","Rok","Begin","Village of Delusion","Ice Melt","Quick","Window Pain","Mal Arena","Cliffusion","Dance Macabre","EyeBrawl","home.wad"]
nZERO=["High-Rise Roof","Toxic Tower","Marble Zone","Triple Town","The Pits","Echo Halls","Claustrophobia","Module Base","Ancient Archives","Leap Gates","Too Close To Home","Underland","Tease","Crust","Peak Facility","Natural Supply","The Testing Labs","Atom Transporter","Quantum Processing","Familiar Face","Starbourn","The Cracks","Atmos Caves","Booster Hub","Abandoned Compound","Fortification","The Junction","Suspension","The Rematch","The Sarcophagus","Meat","Dark Roof"]

#Wad button colors used for filtering when enabled will color buttons to show which have been completed or not
BtnColor = ["#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD","#DDD"] 

#WAD level selector buttons
def WADlevelDrawButton():
    def ChangeLevelNameOnButtonClick(btxt,bnum):
        global pickmaster #this is for picking the write wad for the master levels
        pickmaster = bnum

        WIframe.grid(row=4,column=1, sticky=W)
        if WNlabel.cget("text") == "The Ultimate Doom":
            LVLlabel.config(text = btxt+": "+nDOOM[bnum])
        if WNlabel.cget("text") == "SIGIL":
            LVLlabel.config(text = btxt+": "+nSIGIL[bnum])
        if WNlabel.cget("text") == "Doom II":
            LVLlabel.config(text = btxt+": "+nDOOM2[bnum])
        if WNlabel.cget("text") == "No Rest for the Living":
            LVLlabel.config(text = btxt+": "+nNERVE[bnum])
        if WNlabel.cget("text") == "TNT: Evilution":
            LVLlabel.config(text = btxt+": "+nTNT[bnum])
        if WNlabel.cget("text") == "The Plutonia Experiment":
            LVLlabel.config(text = btxt+": "+nPLUTONIA[bnum])
        if WNlabel.cget("text") == "Master Levels for Doom II":
            LVLlabel.config(text = btxt+": "+nMASTER[bnum])

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

    global levels
    global mode    
    x=0
    y=0
    i = 0
    mapORmap0 = "MAP0"
    #clears the frame the buttons are in ...
    for LVbtn in WSframe.winfo_children():
        LVbtn.destroy()
    #then draws the buttons again so their are no duplicates
    while i < levels:
        if mode[0] == 11 or mode[0] == 51:
            LVbtn = Button(WSframe, text = "E"+str(mode[i])[0]+"M"+str(mode[i])[1], width = 2, font=WADFont, bg=BtnColor[i], command = lambda txt="E"+str(mode[i])[0]+"M"+str(mode[i])[1],num=i : ChangeLevelNameOnButtonClick(txt,num))   
        if mode[0] == 1:
            if mode[i] > 9:
                mapORmap0 = "MAP"
            else:
                mapORmap0 = "MAP0" 
            LVbtn = Button(WSframe, text = mapORmap0+str(mode[i]), width = 2, font=WADFont, bg=BtnColor[i], command = lambda txt=mapORmap0+str(mode[i]),num=i : ChangeLevelNameOnButtonClick(txt,num))
        LVbtn.grid(row = y, column = x)
        x+=1
        if x == 9:
            x = 0
            y += 1
        i += 1

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
GoalFont = font.Font(size=30)

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

#turns the labels into selectable buttons so you click on em to filter what levels youve done the selected goal of
def FLTRreset():
    for label in WGframe.winfo_children():
        label.configure(relief="flat")

def FLTRexit(event):
    FLTRreset(); Glabelexit.configure(relief="sunken")

def FLTRpistolstart(event):
    FLTRreset(); Glabelpistolstart.configure(relief="sunken")

def FLTR100kills(event):
    FLTRreset(); Glabel100kills.configure(relief="sunken")

def FLTR100items(event):
    FLTRreset(); Glabel100items.configure(relief="sunken")

def FLTR100secrets(event):
    FLTRreset(); Glabel100secrets.configure(relief="sunken")

def FLTRpartime(event):
    FLTRreset(); Glabelpartime.configure(relief="sunken")

def FLTRfast(event):
    FLTRreset(); Glabelfast.configure(relief="sunken")

def FLTRrespawn(event):
    FLTRreset(); Glabelrespawn.configure(relief="sunken")

def FLTRplus(event):
    FLTRreset(); Glabelplus.configure(relief="sunken")

#WAD goal text, #666 not beaten, #A00 for beaten
Glabelexit = Label(WGframe, font=GoalFont, fg="#666", bd = 2, relief="flat", text = "✔️")
Glabelexit.grid(row=0,column=0, sticky=N)
Glabelexit.bind("<Button-1>", FLTRexit)
Glabelexit.bind("<Enter>", TTexit)
Glabelexit.bind("<Leave>", TT)  

Glabelpistolstart = Label(WGframe, font=GoalFont, fg="#666", bd = 2, relief="flat", text = "🔫")  
Glabelpistolstart.grid(row=0,column=1, sticky=N)
Glabelpistolstart.bind("<Button-1>", FLTRpistolstart)
Glabelpistolstart.bind("<Enter>", TTpistolstart)
Glabelpistolstart.bind("<Leave>", TT)

Glabel100kills = Label(WGframe, font=GoalFont, fg="#666", bd = 2, relief="flat", text = "👿")  
Glabel100kills.grid(row=0,column=2, sticky=N)
Glabel100kills.bind("<Button-1>", FLTR100kills)
Glabel100kills.bind("<Enter>", TT100kills)
Glabel100kills.bind("<Leave>", TT)

Glabel100items = Label(WGframe, font=GoalFont, fg="#666", bd = 2, relief="flat", text = "🔑")  
Glabel100items.grid(row=0,column=3, sticky=N)
Glabel100items.bind("<Button-1>", FLTR100items)
Glabel100items.bind("<Enter>", TT100items)
Glabel100items.bind("<Leave>", TT)

Glabel100secrets = Label(WGframe, font=GoalFont, fg="#666", bd = 2, relief="flat", text = "?")  
Glabel100secrets.grid(row=0,column=4, sticky=N)
Glabel100secrets.bind("<Button-1>", FLTR100secrets)
Glabel100secrets.bind("<Enter>", TT100secrets)
Glabel100secrets.bind("<Leave>", TT)

Glabelpartime = Label(WGframe, font=GoalFont, fg="#666", bd = 2, relief="flat", text = "⏱️")  
Glabelpartime.grid(row=0,column=5, sticky=N)
Glabelpartime.bind("<Button-1>", FLTRpartime)
Glabelpartime.bind("<Enter>", TTpartime)
Glabelpartime.bind("<Leave>", TT)

Glabelfast = Label(WGframe, font=GoalFont, fg="#666", bd = 2, relief="flat", text = "🏃")  
Glabelfast.grid(row=0,column=6, sticky=N)
Glabelfast.bind("<Button-1>", FLTRfast)
Glabelfast.bind("<Enter>", TTfast)
Glabelfast.bind("<Leave>", TT)

Glabelrespawn = Label(WGframe, font=GoalFont, fg="#666", bd = 2, relief="flat", text = "🔄")  
Glabelrespawn.grid(row=0,column=7, sticky=N)
Glabelrespawn.bind("<Button-1>", FLTRrespawn)
Glabelrespawn.bind("<Enter>", TTrespawn)
Glabelrespawn.bind("<Leave>", TT)

Glabelplus = Label(WGframe, font=GoalFont, fg="#666", bd = 2, relief="flat", text = "+")  
Glabelplus.grid(row=0,column=8, sticky=N)
Glabelplus.bind("<Button-1>", FLTRplus)
Glabelplus.bind("<Enter>", TTplus)
Glabelplus.bind("<Leave>", TT)
#✔=exited,🔫=pistol start,👿=kills,🔑=items,?=secrets,⏱️=par time,🏃=fast,🔄=respawn+=co-op monsters spawning

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