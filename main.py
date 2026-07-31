from Player import Player
import math
BANK = Player("Bank", math.inf, input("BANK PIN (This lets you reset player pins): "))
print("\033[H\033[2J", end="")
STARTING_PRICE = int(input("What is the starting price? "))
player_count = int(input("How many players? ")) # TEMPORARY VARIABLE
players = []
names = []
for i in range(player_count):
    name = input("Player " + str(i+1) + "'s name: ")
    while name == "Bank" or name in players:
        name = input("Sorry, try again. Name: ")
    names.append(name)
    pin = input("Player " + str(i+1) + "'s PIN (4-Digit, Only Numbers): ")
    while len(pin) != 4 or pin.isdigit() != True:
        pin = input("Sorry, try again. PIN: ")
    if name != "Bank":
        players.append(name, STARTING_PRICE, pin)
del player_count
while len(players) > 1:
    for player in players:
        if player.balance <= 0:
            names.remove(player.name)
            players.remove(player)
    selected_player = players[names.index(input("Which player would you like to see? "))]
    menu_choice = int(input(
        f"""
        {selected_player.name}'s Balance: {selected_player.balance}
        You can:
        1. Transfer Money
        2. Reset PIN
        Choose an option:
        """
    ))
    if menu_choice == 1:
        recipient_choice_text = f"""
        What player would you, {selected_player.name}, like to transfer money to?\n
        0. BANK
        """
        for player in players:
            recipient_choice_text += f"\n{players.index(player)+1}. {player.name}\n"
        recipient_choice_text += f"\nRecipient (Input Name or Number): "
        recipient = input(recipient_choice_text)
        amount = int(input("How much money would you like to transfer? "))
        if recipient.isdigit():
            if int(recipient) == 0:
                selected_player.transfer(amount, BANK)
            else:
                selected_player.transfer(amount, recipient)
        else:
            selected_player.transfer(amount, players[names.index(recipient)])
    elif menu_choice == 2:
        selected_player.reset_pin(BANK)
    else:
        print("\033[H\033[2J", end="")
        continue