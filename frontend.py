from tkinter import *
import tkinter.font as font
 
#setup
root = Tk()
root.geometry("530x420")

#play button
PlayBtn = Button(root, text = "PLAY", command = set)
PlayBtn.grid(row=0,column=0, sticky=N)

#skill level and parameter frame
SPframe = Frame(root)
SPframe.grid(row=0,column=1, sticky=N)


#Skill level selector 
MenuBttn = Menubutton(SPframe, text = "Skill level", relief = RAISED)
SkillVar = IntVar()
SkillMenu = Menu(MenuBttn, tearoff = 0)
SkillMenu.add_radiobutton(label = "I'm too young to die", variable = SkillVar, value = 0)
SkillMenu.add_radiobutton(label = "Hey, not too rough", variable = SkillVar, value = 1)
SkillMenu.add_radiobutton(label = "Hurt me plenty", variable = SkillVar, value = 2)
SkillMenu.add_radiobutton(label = "Ultra-Violence", variable = SkillVar, value = 3)
SkillMenu.add_radiobutton(label = "Nightmare!", variable = SkillVar, value = 4)
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

#WAD selector function
def wadnamechange1(event):
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

def wadnamechange2(event):
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

def wadnamechange3(event):
    WNlabel.config(text = W3listbox.get(W3listbox.curselection()))

#WAD selector
label = Label(root,text = "id WADs")  
label.grid(row=1,column=0, sticky=W)

W1listbox = Listbox(root, height = 7, width = 15)  
W1listbox.insert(1,"DOOM")  
W1listbox.insert(2, "SIGIL_v1_21")  
W1listbox.insert(3, "DOOM2")  
W1listbox.insert(4, "NERVE")
W1listbox.insert(5, "TNT")   
W1listbox.insert(6, "PLUTONIA")   
W1listbox.insert(7, "MASTERLEVELS")   
W1listbox.grid(row=2,column=0, sticky=W)
W1listbox.bind('<<ListboxSelect>>', wadnamechange1)

label = Label(root,text = "Add-ons WADs")  
label.grid(row=3,column=0, sticky=W)

W2listbox = Listbox(root, height = 7, width = 15)  
W2listbox.insert(1,"DBIMPACT")  
W2listbox.insert(2, "NEIS")  
W2listbox.insert(3, "DEATHLESS")  
W2listbox.insert(4, "BTSX_e1")
W2listbox.insert(5, "BTSX_e2")   
W2listbox.insert(6, "REKKRSA")   
W2listbox.insert(7, "DOOMZERO")   
W2listbox.grid(row=4,column=0, sticky=W)
W2listbox.bind('<<ListboxSelect>>', wadnamechange2)

label = Label(root,text = "Licenced WADs")  
label.grid(row=5,column=0, sticky=W)

W3listbox = Listbox(root, height = 3, width = 15)  
W3listbox.insert(1,"JPTR_V40")  
W3listbox.insert(2, "PERDGATE")  
W3listbox.insert(3, "HELL2PAY")    
W3listbox.grid(row=6,column=0, sticky=W)
W3listbox.bind('<<ListboxSelect>>', wadnamechange3)

#WAD button font
WADFont = font.Font(size=8)

#WAD level selector frame
WSframe = Frame(root)
WSframe.grid(row=2,column=1, sticky=NW)

#WAD level names
nDOOMSIGIL=["","","","","","","","","","","","Hangar","Nuclear Plant","Toxin Refinery","Command Control","Phobos Lab","Central Processing","Computer Station","Phobos Anomaly","Military Base","","Deimos Anomaly","Containment Area","Refinery","Deimos Lab","Command Center","Halls of the Damned","Spawning Vats","Tower of Babel","Fortress of Mystery","","Hell Keep","Slough of Despair","Pandemonium","House of Pain","Unholy Cathedral","Mt. Erebus","Limbo","Dis","Warrens","","Hell Beneath","Perfect Hatred","Sever the Wicked","Unruly Evil","They Will Repent","Against Thee Wickedly","And Hell Followed","Unto the Cruel","Fear","","Baphomet's Demesne","Sheol","Cages of the Damned","Paths of Wretchedness","Abaddon's Void","Unspeakable Persecution","Nightmare Underworld","Halls of Perdition","Realm of Iblis"]

#WAD level selector buttons
def WADlevelDrawButton():
    def ChangeLevelNameOnButtonClick(btxt,bnum):
        if WNlabel.cget("text") == "The Ultimate Doom" or WNlabel.cget("text") == "SIGIL":
            LVLlabel.config(text = btxt+": "+nDOOMSIGIL[bnum])
        
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
        LVbtn = Button(WSframe, text = "MAP32", width = 2, font=WADFont,  command = lambda txt="MAP32",num=32 : ChangeLevelNameOnButtonClick(txt,num))
        LVbtn.grid(row = 4, column = 1)

#WAD level info
LVLlabel = Label(root,text = "")  
LVLlabel.grid(row=3,column=1, sticky=W)

#WAD info frame
WIframe = Frame(root)
WIframe.grid(row=4,column=1, sticky=W)

#WAD goals frame
WGframe = Frame(WIframe)
WGframe.grid(row=0,column=0, sticky=W)

#WAD goal font
GoalFont = font.Font(size=34)

#WAD goal text
label = Label(WGframe, font=GoalFont, fg="red", text = "✔️")  
label.grid(row=0,column=0, sticky=NE)
label = Label(WGframe, font=GoalFont, fg="red", text = "🔫")  
label.grid(row=0,column=1, sticky=NW)
label = Label(WGframe, font=GoalFont, fg="red", text = "👿")  
label.grid(row=0,column=2, sticky=NW)
label = Label(WGframe, font=GoalFont, fg="red", text = "🔑")  
label.grid(row=0,column=3, sticky=NW)
label = Label(WGframe, font=GoalFont, fg="red", text = "?")  
label.grid(row=0,column=4, sticky=NW)
label = Label(WGframe, font=GoalFont, fg="red", text = "⏱️")  
label.grid(row=0,column=5, sticky=NW)
label = Label(WGframe, font=GoalFont, fg="red", text = "🏃")  
label.grid(row=0,column=6, sticky=NW)
label = Label(WGframe, font=GoalFont, fg="red", text = "🔄")  
label.grid(row=0,column=7, sticky=NW)
label = Label(WGframe, font=GoalFont, fg="red", text = "+")  
label.grid(row=0,column=8, sticky=NW)
#✔=exited,🔫=pistol start,🏃=fast,🔄=respawn,⏱️=par time,👿=kills,🔑=items,?=secrets,+=co-op monsters
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