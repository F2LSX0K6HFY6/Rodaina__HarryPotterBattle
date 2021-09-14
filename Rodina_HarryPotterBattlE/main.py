# This is a sample Python script.

# This is a sample Python script.

class Voldmort:                                 #first class for voldmort
    health= 100                                 #class attribute for health
    energy= 500                                 #class attribute for energy
    sp = {"AvadaKedavra": ('A', 100),           #spells of voldmort
          "Crucio": ('A', 40),
          "Imperio": ('A', 20),
          "sheild": ('A', 0),
          "Taboo": ('V', 80),
          "Expulso": ('V', 60),
          "Confringo": ('V', 55)
          }
    def __init__(self,no1):                   #constructor that have one argument
      self.no1=no1                            #instantation


    def set_energy(self,no1):                 #first method that calculated the energy of voldmort

        self.no1 = no1

        k=int (Voldmort.sp[no1][1])           #to store the power value
        Voldmort.energy-=k                    #to calculate the energy

    def get_energy(self):                     #method to return the energy
        return Voldmort.energy

class Harry:                                  #second class for Harry
    health=100                                #class attribute for health
    energy=500                                #class attribute for energy
    sp = {"AvadaKedavra" : ('A',100),         #spells of Harry
          "Crucio"       : ('A', 40),
          "Imperio"      : ('A', 20),
          "sheild"       : ('A',  0),
          "Reducto"      : ('H', 60),
          "Fiendfyre"    : ('H', 50),
          "Nebulus"      : ('H', 40),
          }

    def __init__(self,no1):                  #constructor that have one argument
      self.no1=no1


    def set_energy(self,no1):                #first method that calculated the energy of voldmort

        self.no1 = no1

        k=int (Harry.sp[no1][1])            #to store the power value
        Harry.energy-=k                     #to calculate the energy

    def get_energy(self):                   #method to return the energy
        return Harry.energy




count1=0                                 #for number of usage of the shield
count2=0

while Voldmort.sp:                       #the battle
 print("Enter the two spells (Harry then Voldmort)")   #get the spells
 g=input()
 f=input()
 volta1 = Voldmort(f)                                  #call voldmort class
 volta1.set_energy(f)                                  #call method of energy
 print("Harry" "              " "Volta"  )

 harry1 = Harry(g)                                     #call class harry
 harry1.set_energy(g)                                  #call method of set energy
 print(f"Energy:={harry1.get_energy()}        Energy:={volta1.get_energy()}")  #print energy




 v= int(Voldmort.sp[f][1])                               #power of the choosen spells
 h = int(Harry.sp[g][1])

 if (v>h):                                               #in case power of spell voldmort>harry
    if (g == "sheild"):                                  #check that the spell is shiels so the health and energy doesn't affected
        Harry.health=Harry.health
        count1+=1
        if (count1 > 3):                                 #check that he didn't use the shield more than 3 times
            continue                                     #back to loop to choose another spell
    else:
     h = int(Harry.sp[g][1])
     Harry.health=Harry.health-(v-h)                      #set health
    if (Harry.health <= 0):
        Harry.health = 0
    print(f"Health:={Harry.health}        Health:={Voldmort.health}")

 else:                                                 #in case power of spell voldmort>harry
     if (f == "sheild"):                               #check that the spell is shiels so the health and energy doesn't affected
         Voldmort.health = Voldmort.health
         count2 += 1
         if (count2 >3):                              #check that he didn't use the shield more than 3 times
           continue                                   #back to loop to choose another spell
     else:
       v = int(Voldmort.sp[f][1])
       Voldmort.health = Voldmort.health - (h -v)     #set health
     if (Voldmort.health<=0):
        Voldmort.health=0
     print(f"Health:={Harry.health}        Health:={Voldmort.health}")
 if (Harry.health <=0):                              #checl who is the winner
     print( "     Volta is the winner ..")
     break
 elif(Voldmort.health <=0):
    print("     Harry is the winner ..")
    break

