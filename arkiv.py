class Game:
    def __init__(self):
        # Constructor for Game class. This is where you would
        # initialize any variables that the game needs.
        self.name = "The Casino"

    def start(self):
        # Method that starts the game. This is where you would
        # introduce the story and the game world, and let the
        # player know what they need to do.
        print(f"Welcome to {self.name}!")
        print("In this game, you are a brave adventurer exploring a dangerous cave.")
        print("Your goal is to collect as much treasure as you can before time runs out.")

    def show_menu(self):
        # Method that shows the game menu. This is where you would
        # present the player with a list of options they can choose
        # from, such as moving to a different location, picking up
        # an item, or checking their inventory.
        print("Main Menu:")
        print("1. Move to a different location")
        print("2. Pick up an item")
        print("3. Check your inventory")

    # Other methods for handling game settings, saving and loading
    # game progress, and so on could go here.

# To create an instance of the Game class and start playing,
# you would do something like this:


game = Game()
game.start()
game.show_menu()


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)

    def __str__(self):
        return self.name


class Game:
    def __init__(self):
        self.current_room = None
        self.rooms = {}

    def add_room(self, room):
        self.rooms[room.name] = room

    def start(self):
        self.current_room = self.rooms["Entrance"]
        print(f"Du er i {self.current_room}.")
        print(self.current_room.description)

    def move(self, direction):
        new_room = self.current_room.get_exit(direction)
        if new_room is None:
            print("Det er ingen vei i den retningen.")
        else:
            self.current_room = new_room
            print(f"Du er nå i {self.current_room}.")
            print(self.current_room.description)


# Opprette rom og legg dem til spillet
entrance = Room(
    "Entrance", "Du står i en stor hall med en dør i nord og en i sør.")
kitchen = Room("Kitchen", "Du er i et kjøkken med en dør i vest.")
