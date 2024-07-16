from corefunc import create_character
from corefunc import shop
from corefunc import choose_monster
from corefunc import fight
print("Welcome to the land of Panga")
print("What is your name, traveler?")
# player chooses their name
choosing_name = True
while choosing_name:
  name = input()
  print("Your name is " + name + "? (y/n)")
  name_confirm = input()
  if name_confirm == "y":
    print("Welcome to Panga, " + name + "!")
    break
  else:
    print("Then what is your name?")
    print("")
create_character()
print("")
input()
print("Now, let's visit the local shop!")
input()
shop("Bilbo's Bits and Bobs")
# choose_monster only takes string answers
# if "playerpick" is entered, the player chooses the monster
print("As you exit the shop, you hear a strange chittering noise...")
print("Oh no!  A Vilespawn!")
input()
choose_monster("Vilespawn")
fight()
if player_alive:
  input()
  print("Good job fighting off that Vilespawn, " + name + ".")
  print("They've been a plague on these lands for quite some time")
else:
  print("A valiant effort")
  quit()