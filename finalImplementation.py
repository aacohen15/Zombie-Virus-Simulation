import random

class Person(object):
    def __init__(self, ID):
        self.ID = ID

    def extraConditions(self):
        self.extraIssues = random.randint(0, 1)
        if self.extraIssues == 0:
            return False
        else:
            return True

    def Kill(self):
        self.attack = random.randint(0, 1)
        if self.attack == 0:
            return False
        else:
            return True
    def Bite(self):
        self.bitten = random.randint(0,1)
        if self.bitten ==0:
            return False
        else:
            return True


class Susceptible(Person):
    def healthLow(self):
        self.health = random.randint(0, 1)
        if self.health == 0:
            return False
        else:
            return True

    def healthRecovered(self):
        self.recovery = random.randint(0, 1)
        if self.recovery == 0:
            return False
        else:
            return True

    def __str__(self):
        return "Susceptible ID Number: " + str(self.ID)


class Infected(Person):
    def __init__(self, ID):
        super(Infected, self).__init__(ID)

    def __str__(self):
        return "Infected ID Number: " + str(self.ID)

def populationCheck(sP,iP,sListPop,iListPop,dead):
    totalPopulation = sP + iP
    simPopulation = len(sListPop) + len(iListPop) + dead
    if simPopulation != totalPopulation:
        return False
    else:
        return True

    

def Zombiola():
    SUSCEPTIBLE = 0
    INFECTED = 1
    REMOVED = 2
    BREAK_FROM_LOOP = 3
    currentState = SUSCEPTIBLE
    
    dayCount = 0  # incremented when new occurrence of currentState == Susceptible
    removedTotal = 0

    susPop = int(input("Initial Susceptible Population: "))
    infPop = int(input("Initial Infected Population: "))

    susceptiblePop = [Susceptible(susPop) for susPop in range(susPop)] # makes list of suscpetible
    infectedPop = [Infected(infPop) for infPop in range(infPop)]  # makes list of infected
    print("")
    print("Simulation Population: ", susPop)
    print("Infected Population: ", infPop)
    print("Total Dead: ", removedTotal)
    print("Running Zombiola Simulation . . .")
    
    print("") #provides a gap between the start output and the end output

    while len(susceptiblePop) > 0 and len(infectedPop) > 0:
        
        if currentState == SUSCEPTIBLE:
            if susceptiblePop[-1].healthLow() == True: 
                if susceptiblePop[-1].healthRecovered() == True:
                    if populationCheck(susPop,infPop,susceptiblePop,infectedPop,removedTotal) == True:
                        dayCount += 1
                        continue
                    else:
                        currentState = BREAK_FROM_LOOP
                        continue #Error found
                else:
                    dayCount+=1
                    continue

            elif susceptiblePop[-1].extraConditions() == True:
                currentState = REMOVED
                susceptiblePop.pop(-1) #Removes one susceptible object
                removedTotal += 1
                continue #Same Susceptible
            
            elif susceptiblePop[-1].Kill() == True:
                if susceptiblePop[-1].Bite() == True:
                    currentState = INFECTED
                    susceptiblePop.pop(-1)
                    infectedPop.append(Infected(len(infectedPop)))
                    continue #Susceptble now Infected
                else:
                    infectedPop.pop(-1)
                    removedTotal += 1
                    currentState = REMOVED
                    continue
                    
            else:
                if populationCheck(susPop,infPop,susceptiblePop,infectedPop,removedTotal) == True:
                    dayCount += 1
                    currentState = SUSCEPTIBLE
                    continue #Next Susceptible
                else:
                    currentState = BREAK_FROM_LOOP
                    continue #Error found

        if currentState == INFECTED:
            if infectedPop[-1].Kill() == True:
                if infectedPop[-1].Bite() == True:
                    if populationCheck(susPop,infPop,susceptiblePop,infectedPop,removedTotal) == True:
                        susceptiblePop.pop(-1)
                        removedTotal += 1
                        dayCount += 1
                        currentState = SUSCEPTIBLE
                        continue # new susceptible
                    else:
                        currentState = BREAK_fROM_LOOP
                        continue #Error Found
                else:
                    dayCount += 1
                    continue #new Susceptible
            elif infectedPop[-1].extraConditions() == True:
                    currentState = REMOVED
                    infectedPop.pop(-1)
                    removedTotal += 1
                    continue #Infected Kill
            else:
                if populationCheck(susPop,infPop,susceptiblePop,infectedPop,removedTotal) == True:
                    dayCount += 1
                    currentState = SUSCEPTIBLE
                    continue #new Suceptible
                else:
                    currentState = BREAK_FROM_LOOP
                    continue #Error Found

        if currentState == REMOVED:
            if populationCheck(susPop,infPop,susceptiblePop,infectedPop,removedTotal) == True:
                dayCount += 1
                currentState = SUSCEPTIBLE
                continue #new susceptible
            else:
                currentState = BREAK_FROM_LOOP
                continue # Error Found

        if currentState == BREAK_FROM_LOOP:
            print("Total Population Error: Restart Simulation")
            break

    if populationCheck(susPop,infPop,susceptiblePop,infectedPop,removedTotal) == True:
        if len(susceptiblePop) == 0: #returns only if all susceptibles are dead
            print("No Susceptibles Left...\n Total Infected: " + str(len(infectedPop)) + "\n Total Dead: " + str(removedTotal)+ "\n The Simulation Lasted: " + str(dayCount))
        else: #returns only if all infected are dead
            print("No Infected Left..." + "\n Total Susceptible: " + str(len(susceptiblePop)) + "\n Total Dead: " + str(removedTotal)+ "\n The Simultion Lasted: " + str(dayCount))
    else:
        print("Total Population Error: Restart Simulation")

if __name__ == "__main__":
    Zombiola()
