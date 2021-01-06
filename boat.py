class Ship:
    def __init__(self, type, length, number_of_hits_taken = 0, destroyed = False):
        self.type = type
        self.length = length
        self.number_of_hits_taken = number_of_hits_taken
        self.destroyed = destroyed

    #accessor methods
    def get_type(self):
        return self.type

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
  
    #mutator methods

class Destroyer(Ship):
    #inherit attributes
    def __init__(self, owner):
        super().__init__("Destroyer", 4)
        self.owner = owner

    #accessor methods
    def get_owner(self):
        return self.owner

    #mutator methods

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
    
    #accessor methods
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_ship(self):
        return self.ship
    
    #mutator methods

    def set_ship(self, ship):
        self.ship = ship

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
            #self.sea is an array of arrays, can be accessed using self.sea[y][x] not the other way around

    #accessor methods
    def show_sea(self):
        for row in self.sea:
            thisrow = ""
            for location in row:
                #replaces locations with either ~ for empty or a letter for a ship
                ship = location.get_ship()
                
                if ship == "None":
                    thisrow += "~" + " "
                
                else: print(ship.get_type())

                #elif ship.get_type() == "Submarine":
                #    thisrow += "S" + " "
                
                #elif ship.get_type() == "Battleship":
                #    thisrow += "B" + " "
                
                #elif ship.get_type() == "Destroyer":
                #    thisrow += "D" + " "
                
                #elif ship.get_type() == "Aircraft Carrier":
                #    thisrow += "A" + " "
            print(thisrow)

    #mutator methods

    def add_ship(self, ship):
        l = 0
        if ship.get_type == "Submarine":
            l = 2
        elif ship.get_type == "Battleship":
            l = 3
        elif ship.get_type == "Destroyer":
            l = 4
        elif ship.get_type == "Aircraft Carrier":
            l = 5

        orientation = input("Horizontal or vertical? (h/v)")
        while not(orientation == "h" or orientation == "v"):
            print("Enter either h or v (case sensitive)")
            orientation = input()

        x = int(input("Enter the column you want the ship to be in (left most part of the ship)"))
        while not(x > 0 and x < 11):
            print("Thats not between 1 and 10, try again")
            x = input()

        y = int(input("Enter the row you want the ship to be in (top most part of the ship)"))
        while not(y > 0 and y < 11):
            print("Thats not between 1 and 10, try again")
            y = input()

        if orientation == "h":
            for i in range(l):
                try:
                    self.sea[y+i][x].set_ship(ship) #sets the length number of the row after the input to the ship
                except: 
                    pass
            
        elif orientation == "v":
            for i in range(l):
                try:
                    self.sea[y][x+i].set_ship(ship) #sets the length number of the row after the input to the ship
                except: 
                    pass


class Player():
    def __init__(self, name):
        self.name = name
        self.sea = Sea(self.name)
        self.ships = []

    def get_name(self):
        return self.name

    def get_sea(self):
        return self.sea

    def add_ships(self):
        ship = Submarine(self.name)
        print("Adding submarine (1 tile)")
        self.sea.add_ship(ship)
        self.ships.append(ship)
        

player1 = Player("Jimmy")
player1.add_ships()
sea = player1.get_sea()
sea.show_sea()