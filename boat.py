import random

class Ship:
    def __init__(self, shipType, length, number_of_hits_taken = 0):
        self.shipType = shipType
        self.length = length
        self.number_of_hits_taken = number_of_hits_taken
        self.destroyed = False

    #accessor methods
    def get_type(self):
        return self.shipType

    def get_length(self):
        return self.length

    def get_hits(self):
        return self.number_of_hits_taken
    
    def get_destroyed(self):
        return self.destroyed
    
    #mutator methods
    def add_hit(self, hits = 1): #default one hit but allowing for multiple to be entered
        self.number_of_hits_taken += hits
    
    def destroy(self):
        self.destroyed = True

class Submarine(Ship):
    #inherit attributes from ship class
    def __init__(self, owner):
        super().__init__("Submarine", 2)
        self.owner = owner

    #accessor methods
    def get_owner(self):
        return self.owner

    #mutator methods

class Battleship(Ship):
    #inherit attributes
    def __init__(self, owner):
        super().__init__("Battleship", 3)
        self.owner = owner
    
    #accessor methods
    def get_owner(self):
        return self.owner

class Destroyer(Ship):
    #inherit attributes
    def __init__(self, owner):
        super().__init__("Destroyer", 4)
        self.owner = owner

    #accessor methods
    def get_owner(self):
        return self.owner

class Aircraft_Carrier(Ship):
    #inherit attributes
    def __init__(self, owner):
        super().__init__("Aircraft Carrier", 5)
        self.owner = owner

    #accessor methods
    def get_owner(self):
        return self.owner
    #mutator methods

class Location():
    def __init__(self, x, y, ship = "None"): 
        self.x = x
        self.y = y
        self.ship = ship
        self.isHit = False
    
    #accessor methods
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_ship(self):
        return self.ship

    def hit_state(self):
        return self.isHit
    
    #mutator methods

    def set_ship(self, newship):
        self.ship = newship

    def del_ship(self):
        self.ship = "None"

class Sea():
    def __init__(self, owner):
        self.sea = []
        self.owner = owner
        for i in range(10):                  #makes rows
            row = []
            for ii in range(10):             #makes columns
                location = Location(i, ii)
                row.append(location)        #adds columns to rows
            self.sea.append(row)            #adds rows to self.sea
            #self.sea is an array of arrays

    #accessor methods
    def show_sea(self):
        for row in self.sea:
            thisrow = ""
            for location in row:
                #replaces locations with either ~ for empty or a letter for a ship
                ship = location.get_ship()
                
                if ship == "None":
                    thisrow += "~" + " "

                elif ship.get_type() == "Submarine":
                    thisrow += "S" + " "
                
                elif ship.get_type() == "Battleship":
                    thisrow += "B" + " "
                
                elif ship.get_type() == "Destroyer":
                    thisrow += "D" + " "
                
                elif ship.get_type() == "Aircraft Carrier":
                    thisrow += "A" + " "
            print(thisrow)

    #mutator methods
    def add_ship(self, ship):
        #check if owner is "Computer"
        if ship.get_owner() == "Computer":
            computer = True
        else:
            computer = False

        l = 0
        if ship.get_type() == "Submarine":
            l = 2
        elif ship.get_type() == "Battleship":
            l = 3
        elif ship.get_type() == "Destroyer":
            l = 4
        elif ship.get_type() == "Aircraft Carrier":
            l = 5

        if computer:
            orientation = random.randint(1, 2) #can stay as ints as its random
            x = random.randint(0,9)
            y = random.randint(0,9)


        elif not computer:
            orientation = validateString("Horizontal or vertical? (h/v)")
            while not(orientation == "h" or orientation == "v"):
                print("Enter either h or v (case sensitive)")
                orientation = validateString(" ", 1)

            x = validateInt("Enter the column you want the ship to be in (left most part of the ship)") - 1
            while not(x >= 0 and x < 11):
                print("Thats not between 1 and 10, try again")
                x = validateInt() - 1

            y = validateInt("Enter the row you want the ship to be in (top most part of the ship)") - 1
            while not(y >= 0 and y < 11):
                print("Thats not between 1 and 10, try again")
                y = validateInt() - 1

        if orientation == "h" or orientation == 1:
            #tests input to see if any issues occur
            failed = True
            while failed:
                failed = False
                for i in range(l):                  
                    try:
                        if self.sea[y][x+i].get_ship() == "None":
                            pass

                        elif not failed:
                            failed = True
                            if not computer:
                                print("That overlaps on another ship")

                    except:
                        if not failed:
                            failed = True
                            if not computer:
                                print("That goes outside the map")    

                if failed and not computer:    
                    x = validateInt("Enter the column you want the ship to be in (left most part of the ship)") - 1
                    while not(x >= 0 and x < 11):
                        x = validateInt("Thats not between 1 and 10, try again") - 1

                    y = int(input("Enter the row you want the ship to be in (top most part of the ship)")) - 1
                    while not(y >= 0 and y < 11):
                        y = validateInt("Thats not between 1 and 10, try again") - 1
                    
                elif failed and computer:
                    orientation = random.randint(1, 2) #can stay as ints as its random
                    x = random.randint(0,9)
                    y = random.randint(0,9)

            #commits changes
            for i in range(l):                  
                self.sea[y][x+i].set_ship(ship) #sets the length number of the row after the input to the ship

        elif orientation == "v" or orientation == 2:
            #tests input to see if any issues occur
            failed = True
            while failed:
                failed = False
                for i in range(l):
                    try:
                        if self.sea[y+i][x].get_ship() == "None":
                            pass

                        elif not failed:
                            failed = True
                            if not computer:
                                print("That overlaps on another ship")

                    except:
                        if not failed:
                            failed = True
                            if not computer:
                                print("That goes outside the map")  

                if failed and not computer:    
                    x = int(input("Enter the column you want the ship to be in (left most part of the ship)")) - 1
                    while not(x >= 0 and x < 11):
                        x = validateInt("Thats not between 1 and 10, try again") - 1

                    y = int(input("Enter the row you want the ship to be in (top most part of the ship)")) - 1
                    while not(y >= 0 and y < 11):
                        y = validateInt("Thats not between 1 and 10, try again") - 1
                    
                elif failed and computer:
                    orientation = random.randint(1, 2) #can stay as ints as its random
                    x = random.randint(0,9)
                    y = random.randint(0,9)

            #commits changes to sea
            for i in range(l):                  
                self.sea[y+i][x].set_ship(ship)

class Player():
    def __init__(self, name):
        self.name = name
        self.sea = Sea(self.name)
        self.ships = []

    def get_name(self):
        return self.name

    def get_sea(self):
        return self.sea

#   this is to save time when testing inputs // not part of program
#    def add_ship(self):
#        self.sea.show_sea()
#        ship = Submarine(self.name)
#        print("Adding submarine (2 tiles)")
#        self.sea.add_ship(ship)
#        self.ships.append(ship)

    def add_ships(self):
        if self.name == "Computer":
            ship = Submarine(self.name)
            self.sea.add_ship(ship)
            self.ships.append(ship)

            ship = Aircraft_Carrier(self.name)
            self.sea.add_ship(ship)
            self.ships.append(ship)

            for i in range(2):
                ship = Destroyer(self.name)
                self.sea.add_ship(ship)
                self.ships.append(ship)
            
            for i in range(3):
                ship = Battleship(self.name)
                self.sea.add_ship(ship)
                self.ships.append(ship)  

        else:
            self.sea.show_sea()
            ship = Submarine(self.name)
            print("Adding submarine (2 tiles)")
            self.sea.add_ship(ship)
            self.ships.append(ship)

            self.sea.show_sea()
            ship = Aircraft_Carrier(self.name)
            print("Adding aircraft carrier (5 tiles)")
            self.sea.add_ship(ship)
            self.ships.append(ship)

            for i in range(2):
                self.sea.show_sea()
                ship = Destroyer(self.name)
                print("Adding destroyer (4 tiles)")
                self.sea.add_ship(ship)
                self.ships.append(ship)
            
            for i in range(3):
                self.sea.show_sea()
                ship = Battleship(self.name)
                print("Adding battleship (3 tiles)")
                self.sea.add_ship(ship)
                self.ships.append(ship)   

def getPlayerName():
    choice = int(input("1) Play against the computer\n2)Play against a friend"))
    if choice == 1:
        name = input("Enter your name:")
        return name, "Computer
    
    else:
        name = input("Enter player 1's name:")
        name2 = input("Enter player 2's name:")
        return name, name2

#validates string //prevents crash in case of bad input
def validateString(prompt = " ", length = 0):
    failed = True
    while failed:
        failed = False
        string = input(prompt)
        try:
            string = int(string)
            failed = True
            print("That is an integer")
        except:
            if length != 0:
                if len(string) > length:
                    failed = True
                    print("That is longer than", str(length), "letters long")
                else:
                    return string
            else:
                return string

#validates integer //prevents crash
def validateInt(prompt = " "):
    failed = True
    while failed:
        failed = False
        num = input(prompt)
        try:
            num = int(num)
            return num
        except:
            print("That isn't an integer")
            failed = True

#get player names
name1, name2 = getPlayerName()

#make seas and add ships
player1 = Player(name1)
player1.add_ships()

player2 = Player(name2)
player2.add_ships()

#showing seas
sea = player1.get_sea()
print(player1.get_name(), "sea:")
sea.show_sea()

sea = player2.get_sea()
print(player2.get_name(), "sea:")
sea.show_sea()