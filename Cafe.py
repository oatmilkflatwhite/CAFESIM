text_success = " did a great job!"
text_failure = " didn't do a very good job..."
text_assignedto = " assinged to "
text_noassigned = "**NONE ASSIGNED**"
text_invalid = "Invalid answer."
prompt_reply = "Input: "
text_pleaseent = "Please select tasks for each member of staff."
text_areuhap = "Are you happy with this?"
text_nofoh = "Nobody was there to see to customers..."
text_nokit = "Nobody was there to make food..."
text_nodrk = "Nobody was there to make drinks..."
text_shiftno = "Day "
tab = "     "
jobnames = ["Front of House", "Kitchen", "Bar/drinks"]
yesno = ["Yes", "No"]
foh = []
kit = []
drk = []
lives = 9
score = 0
shiftcount = 1

class Empl:
    def __init__(self, name, canfoh, cankit, candrk, fails, failq1, failq2, failq3):
        self.name = name 
        self.canfoh = canfoh
        self.cankit = cankit
        self.candrk = candrk
        self.fails = fails
        self.failq1 = failq1
        self.failq2 = failq2
        self.failq3 = failq3

lny = Empl("LENNY", True, True, True, 0, "LENNY gets lonely and sad if he works alone. \nAfter his shift, he looked up at you with his big brown eyes sadly, and said nothing.","He whimpered as he approached the rest of the staff after his shift. He seems to have missed being around others.","He refuses to meet your gaze.") # works poorly alone - kitchen and drinks
apo = Empl("APOLLO", True, False, True, 0, "APOLLO isn't very good in the kitchen. \nHe said, \"Oop! Drop!\"", "He said, \"Pour water!\"", "\"SHKSHKSHKSHKSHK... Suck!\"") # cant work in kitchen
bas = Empl("BASTI", True, True, True, 0,"BASTI doesn't get along with MR. STRIPEY. \nShe hissed at him so much she was struggling to breathe. You had to pick her up to comfort her...","She worked herself up so much that she had to lie down...", "She doesn't seem to like you.") # cant work w mr stripey
mrs = Empl("MR. STRIPEY", True, True, True, 0,"mr stripey dont fail cos hes perfect","failq2","failq3") #perfect
dge = Empl("DOGIE", False, True, True, 0,"DOGIE wasn't very good at serving customers.\nHe kept getting distracted, was sometimes rude to customers, tore up a bit of the carpet, but is otherwise in good spirits.","Customers have began complaining about DOGIE, and he is continuing to cause damage to the carpet.", "He has destroyed more of the carpet.") # wasnt good at serving customers

def failquote(x):
    if x.fails == 0:
        print(x.failq1)
    elif x.fails == 1:
        print(x.failq2)
    else:
        print(x.failq3)
    x.fails = x.fails + 1

def taskfail(x):
    print(" * " + f"{x.name}{text_failure}")

def tasksucc(x):
    print(" * " + f"{x.name}{text_success}")

def lny_compliance(): #IF ALONE IN KITCHEN OR BAR FAIL
    if len(kit) == 1 and kit[0] == lny or len(drk) == 1 and drk[0] == lny:
        taskfail(lny)
        failquote(lny)
        return 1
    else:
        tasksucc(lny)
        return 0
    
def apo_compliance(): # IF IN KITCHEN FAIL
    if apo in kit:
        taskfail(apo)
        failquote(apo)
        return 1
    else:
        tasksucc(apo)
        return 0

def bas_compliance(): ## IF ON TASK W MR STRIPEY FAIL
    f = [bas, mrs]
    jobs = [foh, kit, drk]
    s = 0
    for x in jobs:
        matching = list(filter(lambda y: y in f, x))
        if len(matching) == len(f):
            #print("basti and mr s are ont he same group")
            s = s + 1
        else:
            s = s + 0
            #print("basti and mrs s arent working together")
    if s == 1:
        taskfail(bas)
        failquote(bas)
    else:
        tasksucc(bas)    
    return s

def mrs_compliance(): # hes perfect
    tasksucc(mrs)
    return 0

def dge_compliance(): # IF IN KITCHEN FAIL
    if dge in foh:
        taskfail(dge)
        failquote(dge)
        return 1
    else:
        tasksucc(dge)
        return 0

def all_compliance():
    alljobs = []
    alljobs.extend(foh)
    alljobs.extend(kit)
    alljobs.extend(drk)
    total = []
    if apo in alljobs:
        x = apo_compliance()
        total.append(x)
    if bas in alljobs:
        x = bas_compliance()
        total.append(x)
    if dge in alljobs:
        x = dge_compliance()
        total.append(x)
    if lny in alljobs:
        x = lny_compliance()
        total.append(x)
    if mrs in alljobs:
        x = mrs_compliance()
        total.append(x)
    totalsum = sum(total)
    #print("* " + str(totalsum) + " deduction from personal foibles!")
    return totalsum


    #totalsum = sum(total)
    #return totalsum 

def show_tasksassigned(x):
    print(tab + x + ":")

def stafflist(x):
    names = []
    if len(x) == 0:
        print(text_noassigned)
    else:
        for y in x:
            names.append(y.name)
            names.sort()
        if len(names) == 1:
            print(names[0])
        elif len(names) == 2:
            print(names[0] +" and "+ names[1])
        else:
            p = len(names)
            cutoff = p-2
            enddex = p-1
            print (*names[0:cutoff], sep = ", ",end=", ")
            print (names[cutoff] + " and " + names[enddex])

def show_jobs(x): #x must be list
    y = 1
    for z in x:
        print(tab + str(y) + ": " + z)
        y = y + 1

def assigntasks():
    x = jobnames    
    while not len(staff) == 0:
        for y in staff[:]: #### adding this extra : here worked. lol ??? ohhh its cos removing stuff affects the index. right.
            while y in staff[:]:
                rawinput = input("Enter job for " + y.name + ": ")
                inputted = rawinput.strip() ######hwhy is every second one being skipped....?
                try:
                    inty = int(inputted)
                    if inty == 1:
                        staff.remove(y)
                        foh.append(y)
                        print(y.name + text_assignedto + x[0])
                    elif inty == 2:
                        staff.remove(y)
                        kit.append(y)
                        print(y.name + text_assignedto + x[1])
                    elif inty == 3:
                        staff.remove(y)
                        drk.append(y)
                        print(y.name + text_assignedto + x[2])
                    else:
                        print(text_invalid)
                        
                except:
                    print(text_invalid)

def inputreply(x): #x must be +ve integer (number of poss options)
    doneflag = False
    while doneflag == False:
        rawinput = input(prompt_reply)
        inputted = rawinput.strip()
        if inputted.isdigit():
            try:
                inty = int(inputted)
            except TypeError:
                print(text_invalid)
            except:
                print(text_invalid)
            if inty > 0 and inty != 0 and inty <= x:
                doneflag = True
                return inty
            else:
                print(text_invalid)
        else:
            print(text_invalid)

def resettasks():
    foh.clear()
    kit.clear()
    drk.clear()
    staff.clear()
    staff.append(apo)
    staff.append(bas)
    staff.append(dge)
    staff.append(lny)
    staff.append(mrs)

def hardreset():
    apo.fails = 0
    bas.fails = 0
    dge.fails = 0
    lny.fails = 0
    mrs.fails = 0
    global shiftcount 
    shiftcount = 1

def taskempty():
    if len(foh) == 0:
        print(text_nofoh)
        return 9
    if len(drk) == 0:
        print(text_nodrk)
        return 9
    if len(kit) == 0:
        print(text_nokit)
        return 3
    else:
        return 0

def solobar():
    if len(drk) == 1:
        victim = drk[0]
        print(f"{victim.name} needed more help making drinks on the bar. It took time for drinks to be made and sent out to customers.")
        return 2
    else:
        return 0
    
def score(x):
    if x == 9:
        print("Today's shift went perfectly! Everyone did really well!")
    elif x == 8:
        print("Today's shift went almost perfectly!")
    elif x == 7: 
        print("Today's shift went okay.")
    elif x == 6 or x == 5 or x == 4:
         print("Today's shift could've gone a lot better...")
    elif x == 0:
         print("Because of that, the cafe couldn't be opened...")
    else:
        print("Today's shift didn't go well at all...")

staff = []
staff.append(apo)
staff.append(bas)
staff.append(dge)
staff.append(lny)
staff.append(mrs)

print("**********************")
print("**PET CAFE SIMULATOR**")
print("**********************")
print("Can you make the perfect shift happen in the cafe?")
print("\n")
while True:
    print(text_shiftno + str(shiftcount))
    assigned = False
    shift = False
    while assigned == False:
        print("Employees for today's shift:")
        stafflist(staff)
        print(text_pleaseent)
        print("\n")
        show_jobs(jobnames)
        print("\n")
        assigntasks()
        print("\n")
        show_tasksassigned(jobnames[0])
        stafflist(foh)
        show_tasksassigned(jobnames[1])
        stafflist(kit)
        show_tasksassigned(jobnames[2])
        stafflist(drk)
        print("\n")
        print(text_areuhap)
        show_jobs(yesno)
        answer = inputreply(2)
        if answer == 2:
            print("That's okay, we can start again.")
            resettasks()
            continue
        elif answer == 1:
            print("Great! Let's see how it goes.")
            assigned = True
            shift = True
    
    while shift == True:
        lives = 9
        #print("**score before " + str(lives))
        deduction = taskempty()
        lives = lives - deduction
        if lives == 0:
            score(lives)
            shift = False
        else: 
            #print("**score after taskempty " + str(lives))
            deduction = solobar()
            lives = lives - deduction
            #print("**score after solobar " + str(lives))
            deduction = all_compliance()
            lives = lives - deduction

            score(lives)
            shift = False
    if lives == 9:
        print ("** WELL DONE! You did a great job :) **")
        print ("It took you " + str(shiftcount) + " shifts to become a fantastic cafe manager!")
        hardreset()
        resettasks()
        input("Press any key to play from the beginning. ")
    else:   
        input("Press any key to play again. ")
        shiftcount = shiftcount + 1
        resettasks()
        print("\n**********************")
        assigned = False

        
    



