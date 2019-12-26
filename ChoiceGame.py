#defining the death function
def death():
    print """You died. Thanks for playing! If you would like to restart, please
    press the up arrow key, and then enter.\n"""

#Actual game function:
def game():
    print """\nYou find yourself on an alien ship, cruising in the outer reaches
     of the galaxy.You dont know where you are, but you can see a sign which says
     '%s WANTED, dead is preferred.' So, you start running to find a way out."""% username

    print """\n You run out of the room you were in and see three stairways.
    Which one do you take?
    1. Left Stairway.
    2. Middle Stairway.
    3. Right Stairway. """

    first_choice = raw_input("\nType 1, 2 or 3 below. \n")

    print "-"*90
    if first_choice == "1":
        print """\nYou run up the left stairway as fast as you can, but fail to
        notice a couple of steps missing. You fall through the crack to your
        demise."""
        death()

    elif first_choice == "2":
        print """\nYou run up the staircase and find yourself in another room.
        There are 3 doors in the room, each with different symbols on them. Which
        one will you go through?
        1. Red door with a crescent moon symbol.
        2. Blue door with a sun symbol.
        3. Yellow door with a star symbol."""

        second_choice = raw_input("Type 1, 2, or 3 below. \n")
        print "-"*90

        if second_choice == "1":
            print """\nYou open the door, and find yourself face to face with
            the alien'sleader. As he is surrouned by guards, you are immeditely
            captured, and imprisoned."""
            death()

        elif second_choice == "2":
            print """You walk up to the blue door, but before you can touch the
            doorknob, it swings open by itself. Intrigued, you walk in
            confidently, and accidentally step on a pressure plate on the ground.
            Two laser blasts shoot out from the wall and vaporize you on the spot."""
            death()

        elif second_choice == "3":
            print """You walk through the yellow door, and see a long walkway,
            with what seems to be a hangar at the end. However, in between you
            and the escape pods in the hangar, there is a locked steel door that
            has a lockpad on it. On the pad, it says "The code is 3 digits, and
            is equal to (5*22) + (3^2)"""

            third_choice = raw_input("You enter the following code into the pad:\n")

            print "-"*90
            if third_choice == "119":
                print """The lockpad lights up green, and you hear the lock open.
                You run through the door, and get into an escape pod. You see the
                alien mob running into the room, but you rocket out of the hangar
                before they catch you."""
                print "\nCongratulations! You have beat Space Escape! Thanks for playing."
                exit()

            else:
                print """You hear a buzzer noise and the lockpad lights up red.
                That wasn't the right code. You hear the cries of the alien mob
                behind you, and you know you're done for."""
                death()

        else:
            print "Im sorry, that is an invalid input."
            exit()

    elif first_choice == "3":
        print """You run up the staircase and find yourself in what seems to be
        a cafeteria for the aliens. Obviously, they see you and apprehend you on the spot."""
        death()

    else:
        print "Im sorry, that is an invalid input."
        exit()

#Intro sequence and defining username:
print "Welcome to Space Escape, a CLI python game made by Aadi Anjaria. Lets get into it."
username = raw_input("What would you like your username to be? \n > ")

print "So you want to be called %s?" % username
confirm = raw_input("Type Y if yes, type N if you would like to exit the game:\n")

if confirm == "Y" or confirm == "y":
    print "\nOk, lets start the game."
    game()
else:
    print "See ya."
    exit()
