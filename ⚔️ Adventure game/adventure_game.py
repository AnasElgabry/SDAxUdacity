import time
import random
#areas = ['Dark forest', 'Ice land ', 'Wind land', 'Poison forest', 'Vlocano land']
#creatures = ['Dragon', 'Goblin', 'Zombie', 'Vampire', 'Beast']
#weapons = ['Blood Sowrd', 'Poison Sowrd', 'Fire Sowrd', 'Wind Sowrd', 'Freeze Sowrd'] << should move to def play game 

# To make print out slow or fast
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.5)

# Set an intro  
def intro(items, areas, creatures, weapons):
    print_pause("You find yourself standing in an open field, filled with "+ areas +".")
    print_pause("Rumor has it that a wicked fairie is somewhere around here and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty 'but not very effective' dagger.")
    #field (items) << not necessry and it will run error
    
# Here Where the Player start the game
def field (items, areas, creatures, weapons):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")  
    print_pause("What would you like to do?")
    # Set a while so the player can pick only 1 or 2 otherwhise she/he will get the same question
    while True: # Ask a user weather wants to enter house or cave
        PlayerEnter = input("Please enter 1 or 2\n")
        if PlayerEnter == "1": # press '1' to enter the house
            house(items, areas, creatures, weapons) # move to house here
            break
        elif PlayerEnter == "2": # press '2' to enter the cave
            cave(items, areas, creatures, weapons) # move to cave here
            break
            
# When Player Choose 1 to start adventure
def house(items, areas, creatures, weapons):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a "+ creatures +".")
    print_pause("Eep! This is the "+ creatures +"'s house!")
    print_pause("The gorgon attacks you!")
    #print_pause("Would you like to (1) fight or (2) run away?\n")
    #fight (items)
    if "weapon" not in items: # if a user did not bring a weapon from cave it will print out this 
        print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.")
        fight(items, areas, creatures, weapons) # move to fight def
    elif "weapon" in items: # if a user brought a weapon
        fight(items, areas, creatures, weapons) # move to fight def

# Once the Player enter the house and start fighting either want to fight or run away
def fight(items, areas, creatures, weapons):
    # Set a while so the player can pick only 1 or 2 otherwhise she/he will get the same question
    while True: # Ask a user weather want to fight or run away
        PlayerPick = input("Would you like to (1) fight or (2) run away?\n")
        if PlayerPick == "1": # if a user press '1' and did not have a weapon, she/he will fail fighting an enemy 
            if "weapon" not in items:
                print_pause("You do your best...")
                print_pause("but your dagger is no match for the wicked fairie.")
                print_pause("You have been defeated!")
                end_game() # move to end game goes here
                break
            elif "weapon" in items: # if a user press '1' and brought the weapon, she/he will win the fighting
                print_pause("As the "+ creatures +" moves to attack, you unsheath your new sword.")
                print_pause("The Sword of "+ weapons +" shines brightly in your hand as you brace yourself for the attack.")
                print_pause("But the "+ creatures +" takes one look at your shiny new toy and runs away!")
                print_pause("You have rid the town of the "+ creatures +". You are victorious!")
                end_game() # move to end game goes here
                break
        elif PlayerPick == "2": # if a user press '2', it will return to the main field
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.")
            field(items, areas, creatures, weapons) # return back to filed
            break
         
# When Player Choose 2 to pick up an item 
def cave(items, areas, creatures, weapons):
    #list = random.choice(creatures)
    #for i in range(2):
    #    list = random.choice(creatures)
        
    if "weapon" not in items: # if a user did not have amd will pick up a weapon
        items.append("weapon") 
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the "+ weapons +"!")
        print_pause("You discard your silly old dagger and take the sword with you.")
        print_pause("You walk back out to the field.")
        field (items, areas, creatures, weapons) # return back to filed
    elif "weapon" in items: # if a user came again and already had a weapon 
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field (items, areas, creatures, weapons) # return back to filed
            
# Ending the game goes here and ask the player weather want to play again or not
def end_game():
    # Set a while so the player can pick only n or y otherwhise she/he will get the same question
    while True: # ask a user weather want to play again or stop
        PlayerChoose = input("Would you like to play again? y/n\n")
        if PlayerChoose == "y": # Start game again goes here
            print_pause("Excellent! Restarting the game ...")
            play_game() # To start play again goes here
            break
        elif PlayerChoose == "n": #End game goes here
            print_pause("Thanks for playing! See you next time.") # here will exit the python
            break 
    
# Set a play game def 
def play_game():
    items = []
    areas = random.choice(['Dark forest', 'Ice land ', 'Wind land', 'Poison forest', 'Vlocano land'])
    creatures = random.choice(['Dragon', 'Goblin', 'Zombie', 'Vampire', 'Beast'])
    weapons = random.choice(['Blood Sowrd', 'Poison Sowrd', 'Fire Sowrd', 'Wind Sowrd', 'Freeze Sowrd'])
    intro(items, areas, creatures, weapons)
    field(items, areas, creatures, weapons)
play_game()