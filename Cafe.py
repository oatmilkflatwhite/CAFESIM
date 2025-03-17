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
tab = "     "
jobnames = ["Front of House", "Kitchen", "Bar/drinks"]
yesno = ["Yes", "No"]
foh = []
kit = []
drk = []
jobs = [foh,kit,drk]
lives = 9
score = 0

class Empl:
    def __init__(self, name, canfoh, cankit, candrk):
        self.name = name 
        self.canfoh = canfoh
        self.cankit = cankit
        self.candrk = candrk

lny = Empl("LENNY", True, True, True) # works poorly alone - kitchen and drinks
apo = Empl("APOLLO", True, False, True) # cant work in kitchen
bas = Empl("BASTI", True, True, True) # cant work w mr stripey
mrs = Empl("MR. STRIPEY", True, True, True) #perfect
dge = Empl("DOGIE", False, True, True ) # wasnt good at serving customers

#def lny_compliance:
###IF ALONE IN KITCHEN OR BAR FAIL
#   return 0

#def apo_compliance:
### IF IN KITCHEN FAIL
#    return 0

#def bas_compliance:
### IF ON TASK W MR STRIPEY
#    return 0

#def dge_compliance:
### IF ON FOH
#    return 0

#def all_compliance:
#### PUT ALL THE NUMBERS IN A TUPLE THEN TOTAL AND RETURN FOR MEGA DESTRUCTION

def stafflist(x):
    names = []
    for y in x:
        names.append(y.name)
    names.sort()
    if len(names) == 1:
        print(*names)
    elif len(names) == 0:
        print(text_noassigned)
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

def show_tasksassigned(x):
    jobdex = jobs.index(x)
    job_name = jobnames[jobdex]
    print(job_name + ":")
    stafflist(x)

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
    lives = 9

def taskempty():
    if len(foh) == 0:
        print(text_nofoh)
        return 9
    if len(kit) == 0:
        print(text_nokit)
        return 4
    if len(drk) == 0:
        print(text_nodrk)
        return 9
    else:
        return 0

def solobar():
    if len(drk) == 0:
        victim = drk[0]
        print(f"{victim.name} needed more help making drinks...")
        return 2
    else:
        return 0

lnyfail = "%s gets lonely if he works alone. \nAfter his shift, he looked up at you with his big brown eyes sadly, and said nothing." % (lny.name) ###COUNT FAILURES AND SHIFT TEXT IF SO
lnyfail2 = "LENNY whimpered as he approached the rest of the staff after his shift. He seems to have missed them."
lnyfail3 = "LENNY refuses to meet your gaze."
apofail = "%s isn't good in the kitchen. \nHe said, \"Oop! Drop!\"" % (apo.name)
apofail2 = "APOLLO said, \"Pour water!\""
apofail3 = "\"SHKSHKSHKSHKSHK... Suck!\""
basfail ="%s doesn't get along with %s. \nShe hissed at him so much she was struggling to breathe. You had to pick her up to comfort her..." % (bas.name, mrs.name)
basfail2 = "BASTI worked herself up so much that she had to lie down..."
basfail3 = "BASTI doesn't want to speak to you."
dgefail ="%s wasn't very good at serving customers. \nHe kept getting distracted, was sometimes rude to customers, tore up a bit of the carpet, but is otherwise in good spirits." % (dge.name)
dgefail2 = "Customers have began complaining about DOGIE, and he is continuing to cause damage to the carpet"
dgefail3 = "DOGIE has destroyed more of the carpet."


staff = []
staff.append(apo)
staff.append(bas)
staff.append(dge)
staff.append(lny)
staff.append(mrs)


print("**PET CAFE SIMULATOR**")
while True:
    assigned = False
    while assigned == False:
        print("Employees for today's shift:")
        stafflist(staff)
        print(text_pleaseent)
        show_jobs(jobnames)
        assigntasks()
        show_tasksassigned(foh)
        show_tasksassigned(kit)
        show_tasksassigned(drk)
        print(text_areuhap)
        show_jobs(yesno)
        answer = inputreply(2)
        if answer == 2:
            print("That's okay, we can start again.")
            resettasks()
            continue
        elif answer == 1:
            print("Great!")
            assigned = True
    
    print("score before" + str(lives))
    deduction = taskempty()
    lives = lives - deduction
    print("score after taskempty" + lives)
    deduction = solobar()
    lives = lives - deduction
    print("score after solobar" + lives)

    if lives == 9:
        print("Today's shift went really well!")
    else:
        print("Today's shift didn't go well at all...")
    

    



