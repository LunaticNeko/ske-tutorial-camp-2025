import random
import time


# Game world - rooms and their properties
rooms = {
    'forest': {
        'description': 'You are in a dark, mysterious forest. Tall trees surround you.',
        'exits': {'north': 'cave', 'east': 'village', 'south': 'lake'},
        'items': ['stick', 'berries'],
        'protected_items': []
    },
    'cave': {
        'description': 'A damp cave with glowing crystals on the walls. You hear water dripping.',
        'exits': {'south': 'forest', 'east': 'mountain'},
        'items': ['torch', 'gold_coin'],
        'protected_items': []
    },
    'village': {
        'description': 'A small, peaceful village with cozy houses and friendly people.',
        'exits': {'west': 'forest', 'north': 'mountain'},
        'items': ['map'],
        'protected_items': ['bread']
    },
    'mountain': {
        'description': 'You stand atop a high mountain. The view is breathtaking!',
        'exits': {'west': 'cave', 'south': 'village'},
        'items': ['treasure_chest'],
        'protected_items': []
    },
    'lake': {
        'description': 'A serene lake with crystal-clear water. Fish swim peacefully below.',
        'exits': {'north': 'forest'},
        'items': ['fishing_rod'],
        'protected_items': ['fish']
    }
}


def display_location(player_location):
    """Show current location info"""
    current_room = rooms[player_location]
    print("\n" + "="*50)
    print(f"LOCATION: {player_location.upper()}")
    print("="*50)
    print(current_room['description'])
   
    # Show available exits
    exits = list(current_room['exits'].keys())
    print(f"\nExits: {', '.join(exits)}")
   
    # Show items in room
    if current_room['items']:
        print(f"You can see: {', '.join(current_room['items'] + current_room['protected_items'])}")
   
# Morning task
def move_player(direction, game_state):
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]


    # Where exactly I am right now
    current_location = game_state["player_location"]
    current_location_properties = rooms[current_location]


    # What are the allowable directions
    list_of_can_go_directions = list(current_location_properties['exits'].keys())


    # Is the direction supplied in the allowable directions
    # If so,  go to the room in that direction and update the game state
    if direction in list_of_can_go_directions:
        game_state["player_location"] = current_location_properties['exits'][direction]
        print(f"You moved {direction}.")
        if random.random() < 0.3:
            random_event(game_state)
    else:
        print(f"You cannot move {direction}.")


# Morning task
def take_item(item_name, game_state):
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]
    # Where exactly I am right now
    current_location = game_state["player_location"]
    current_location_properties = rooms[current_location]

    # What are the allowable items to take
    list_of_can_take_items = current_location_properties['items']

    # Is the item_name supplied in the allowable items to take
    # If so, take the item and remove that item from the current location
    if item_name in list_of_can_take_items:
        game_state["player_inventory"].append(item_name)
        current_location_properties['items'].remove(item_name)
    elif item_name in current_location_properties['protected_items']:
        print(f"You can't just take {item_name}!")


# Morning task
def check_win_condition(game_state):
    # Check if player has collected the treasure
    treasure_chest_in_inventory = 'treasure_chest' in game_state["player_inventory"]
    return treasure_chest_in_inventory

def display_stats(game_state):
    """Show HP, score, item count"""
    print(f"HP: {game_state['player_health']} | Score: {game_state['player_score']} | Items: {len(game_state['player_inventory'])}")

def show_inventory(game_state):
    """Show items"""
    print("Inventory:")
    if len(game_state["player_inventory"]) == 0:
        print("  Nothing")
    else:
        for item in game_state["player_inventory"]:
            print(f"* {item}")

def random_event(game_state):    
    events = [
        {
            'description': "You encounter a friendly squirrel!",
            'health_change': 5,
            'score_change': 5
        },
        {
            'description': "You trip over a root and hurt yourself.",
            'health_change': -10,
            'score_change': 0
        },
        {
            'description': "You find a shiny pebble on the ground!",
            'health_change': 0,
            'score_change': 15
        },
        {
            'description': "A cool breeze refreshes you.",
            'health_change': 10,
            'score_change': 0
        }
    ]
    triggered_event = random.choice(events)
    print(triggered_event['description'])
    if triggered_event['health_change'] > 0:
        restore_health(triggered_event['health_change'], game_state)
    elif triggered_event['health_change'] < 0:
        damage_health(-triggered_event['health_change'], game_state)
    game_state['player_score'] += triggered_event['score_change']


def restore_health(amount, game_state):
    game_state["player_health"] += amount
    if game_state["player_health"] > 100:
        game_state["player_health"] = 100
    print(f"Your health has increased by {amount}. It is now {game_state['player_health']}.")

def damage_health(amount, game_state):
    game_state["player_health"] -= amount
    if game_state["player_health"] < 0:
        game_state["game_lose"] = True
    print(f"Your health has decreased by {amount}. It is now {game_state['player_health']}.")

def use_item(item_name, game_state):
    """Use an item"""

    # check if the player has item
    # if not, display message and stop
    if item_name not in game_state["player_inventory"]:
        print(f"You don't have {item_name}.")
        return

    # actual item use logic
    if item_name == "berries":
        print("You eat the berries.")
        game_state["player_score"] += 10
        restore_health(10, game_state)
    if item_name == "fish":
        print("You eat the fish. You feel regret. You should have cooked it ...")
        damage_health(20, game_state)
    if item_name == "gold_coin":
        if game_state['player_location'] != 'village':
            print("The gold coin shines in your hand.")
            print("Obviously, it's used for trading.")
            print("You should use it where there are people.")
            print("Of course, not the Internet.")
            return
        if 'bread' not in rooms['village']['protected_items']:
            print("You hold up the gold coin in your hand, looking for traders.")
            print("There's nothing you can buy.")
            return
        print("You approach a baker and bought a bread using the gold coin.")
        rooms['village']['protected_items'].remove('bread')
        game_state['player_inventory'].append('bread')
    if item_name == "fishing_rod":
        if game_state['player_location'] != 'lake':
            print("You try to cast the fishing rod. But nothing happens ...")
            print("Maybe you should fish in a place where there's fish.")
            return
        if 'fish' not in rooms['lake']['protected_items']:
            print("There's water, but there's no fish.")
            return
        print("You cast the fishing rod.")
        time.sleep(1)
        print(" ... ")
        time.sleep(1)
        print(" ... ")
        print("You caught a fish!")
        rooms['lake']['protected_items'].remove('fish')
        game_state['player_inventory'].append('fish')

    # when everything is done, remove the item from the player
    # but if it's a fishing_rod, don't!
    if item_name != "fishing_rod":
        game_state["player_inventory"].remove(item_name)

def check_lose_condition(game_state):
    return game_state["player_health"] <= 0


def show_help():
    """Display available commands"""
    print("\n=== AVAILABLE COMMANDS ===")
    print("go <direction>     - Move in a direction (north, south, east, west)")
    print("                     (you can also use 'move' instead of 'go')")
    print("take <item>        - Pick up an item")
    print("use <item>         - Use an item from your inventory")
    print("inventory          - Show your items")
    print("look               - Look around current location")
    print("stats              - Check your stats")
    print("help               - Show this help message")
    print("quit               - Exit the game")


def process_command(command, game_state):
    # game_state = [player_location, player_health, player_score, player_inventory, game_quit]
    parts = command.lower().split()
    if not parts:
        return
   
    action = parts[0]
   
    if (action == 'go' or action == 'move') and len(parts) > 1:
        move_player(parts[1], game_state)
    elif action == 'take' and len(parts) > 1:
        take_item(parts[1], game_state)
    elif action == 'use' and len(parts) > 1:
        use_item(parts[1], game_state)
    elif action == 'inventory':
        show_inventory(game_state)
    elif action == 'look':
        display_location(game_state["player_location"])
    elif action == 'stats':
        display_stats(game_state)
    elif action == 'help':
        show_help()
    elif action == 'quit':
        print("\nThanks for playing!")
        game_state[4] = True
    else:
        print("\nI don't understand that command. Type 'help' for available commands.")


def main():
   
    # Player state
    player_location = 'forest'
    player_inventory = []
    player_health = 100
    player_score = 0
    game_win = False
    game_lose = False
    game_quit = False
    #current_game_state = [player_location, player_health, player_score, player_inventory, game_quit]
    current_game_state = {
        "player_location": player_location,
        "player_health" : player_health,
        "player_score" : player_score,
        "player_inventory" : player_inventory,
        "game_quit": game_quit,
        "game_lose": game_lose
    }


    print("="*60)
    print("         WELCOME TO THE ADVENTURE GAME!")
    print("="*60)
    print("\nYour goal is to explore the world and find the treasure!")
    print("Type 'help' at any time to see available commands.")
   
    display_location(player_location)
   
    while not (game_win or game_lose):
        command = input("\n> What do you want to do? ")
        process_command(command, current_game_state)
       
        # Check win conditions
        game_win = check_win_condition(current_game_state)

        # Check lose conditions
        game_lose = check_lose_condition(current_game_state)
       
        game_quit = current_game_state['game_quit']
        if game_quit:
            break
   
    # Game end messages
    print("\n" + "="*50)
    if game_win:
        print("🎉 CONGRATULATIONS! YOU WON! 🎉")
        print("You found the treasure and completed your adventure!")
    elif game_lose:
        print("💀 GAME OVER 💀")
        print("Your health reached zero. Better luck next time!")
   
    print(f"\nFinal Score: {player_score}")
    print(f"Items Collected: {len(player_inventory)}")
    print("="*50)


# Run the game
if __name__ == "__main__":
    main()


