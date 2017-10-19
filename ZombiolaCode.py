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


'''
#How to add and remove from Infected and Susceptible (infected example below)
IP = [Infected(pops) for pops in range(4)] # creates objects in the list

IP.append(Infected(len(IP))) #always appends to the end of the list
for i in range(len(IP)):
    print(IP[i])

#IP.pop(-1) for the last object in list
'''
IP = [Infected(pops) for pops in range(4)] # creates objects in the list

IP.append(Infected(len(IP))) #always appends to the end of the list
for i in range(len(IP)):
    print(IP[i])

print(IP[0].Kill())
