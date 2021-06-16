# IT 140 Module 7 Project Two by Gwen Virtue
# FIXME - Add documentation. This project satisfies the requirements of the class, but it is pretty simple. I hope to expand it a bit more.

def show_instructions():
    print("Welcome to Deep Space Hunt!")
    print("Scavenge the derelict space freighter for 6 items before confronting the alien")
    print("Move commands: North, South, East, West")
    print("Pickup item: Get 'item name'")
    print("Type 'Exit' at any time to leave the simulation")


def show_status(player_loc, player_inventory, rooms):
    # show_status(player_loc, player_inventory, rooms)
    print('Your current location is {}'.format(player_loc))
    print("Your current inventory is: ", end = " ")
    for i in player_inventory:
        print('{}'.format(i), end = " ")
    # print('Your current inventory is {}'.format(player_inventory))
    if 'item' in rooms[player_loc]:
        print('\nYou see a: {}'.format(rooms[player_loc]['item']))
    else:
        print('\nNothing in room')


def move_player(player_choice, player_loc, rooms, player_inventory):
    if player_choice == 'North' or player_choice == 'South' or player_choice == 'East' or player_choice == 'West':
        if player_choice in rooms[player_loc]:
            player_loc = rooms[player_loc][player_choice]
        else:
            print('There is no room in that direction.')
        # If the player chooses Exit then let them know that the game is over by printing something.
    elif player_choice == 'Exit':
        print('Thank you for playing!')
        exit()
        # Throw out all other commands and bring them back to the beginning of the while loop.
    elif player_choice == 'Get':
        if 'item' in rooms[player_loc]:
            player_inventory.append(rooms[player_loc]['item'])
            item = rooms[player_loc]['item']
            # print(item)
            del (rooms[player_loc]['item'])
        else:
            print("Nothing to get here!")
    else:
        print('Invalid choice, friend!')
    return player_loc

def check_win(player_loc, player_inventory, rooms):
    if player_loc == 'Barracks':
        if ('Grenade' in player_inventory) and ('Med-Pack' in player_inventory) and ('Fire Extinguisher' in player_inventory) and ('Food' in player_inventory) and ('Harpoon' in player_inventory) and ('Flashlight' in player_inventory):
            print('Congratulations! You have defeated the alien!')
            print('All of the treasures of this ship are yours to take.')
            exit()
        else:
            print('Argh! You were not prepared for the alien menace!')
            print('Try again!')
            exit()

def main():
    # Set starting place of player and initialize the player_choice variable.
    player_loc = 'Player Spawn'
    player_choice = 0
    player_inventory = []
    rooms = {
            'Armory': {'South': 'Med-Bay', 'item': 'Grenade'},
            'Med-Bay': {'North': 'Armory', 'West': 'Freight Storage', 'item': 'Med-Pack'},
            'Freight Storage': {'West': 'Tool Storage', 'South': 'Leisure Room', 'North': 'Galley', 'East': 'Med-Bay',
                                'item': 'Fire Extinguisher'},
            'Leisure Room': {'North': 'Freight Storage', 'East': 'Player Spawn', 'item': 'Flashlight'},
            'Galley': {'East': 'Barracks', 'South': 'Freight Storage', 'item': 'Food'},
            'Tool Storage': {'East': 'Freight Storage', 'item': 'Harpoon'},
            'Player Spawn': {'West': 'Leisure Room'},
            'Barracks': {'West': 'Galley'}
        }

    while player_choice != 'Exit':
        show_status(player_loc, player_inventory, rooms)
        player_choice = input('\nPlease choose a direction, Get an item, or Exit: ')
        player_loc = move_player(player_choice, player_loc, rooms, player_inventory)
        check_win(player_loc, player_inventory, rooms)

show_instructions()
main()
