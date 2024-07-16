import random
ice_learned = False
fire_learned = False
lightning_learned = False
# monsters must be defined as variable at the top to ensure the item shop works
monster = ""
vilespawn = ""
ogre = ""
minotaur = ""
# the player and monsters have various stats
# note to self: create some template monsters from manual to put in
# streamlined monster abilities?

# monster gains
player_gold = 250
exp = 0
level = 1
level_bonus_2 = 0
level_bonus_3 = 0
level_bonus_4 = 0
# core abilities
strength = 0
dex = 0
con = 0
spellcast = 0
spellcast_ability = 0
proficiency_bonus = 0
player_spell_save_dc = 0
player_str_bonus = 0
player_dex_bonus = 0
player_con_bonus = 0
# combat
initiative_player = 0
initiative_monster = 0
player_condition = ""
monster_condition = ""
god = ""

# shop items defined
player_greatsword = ""
player_battleaxe = ""
player_shortsword = ""
player_focus = ""
player_shield = ""
player_plate_armor = ""
player_scale_armor = ""
player_leather_armor = ""

# equippables defined
greatsword = ""
battleaxe = ""
shortsword = ""
stick = ""
shield = ""

# game functions
def create_character():
    global strength
    global dex
    global con
    global spellcast
    global player_in_bonus
    global player_health
    global player_start_health
    global player_spell_save_dc
    global spellcast_ability
    global player_str_bonus
    global player_dex_bonus
    global player_con_bonus
    global proficiency_bonus
    global player_alive
    global god
    player_alive = True
    # tutorial
    print("First, let's design your character!")
    print("There are four abilities: Strength, Dexterity, Constitution," + 
          " and Spellcasting.")
    print("Would you like an explanation of any abilities? (y/n)")
    explain = input()
    if explain == "y":
      explaining = True
      while explaining:
        print("Which ability would you like explained?")
        ability_explanation = input()
        if ability_explanation == "Strength" or ability_explanation == "strength":
          print("Strength is your physical ability.  It affects your skill with most weapons and how much damage you deal with them.")
        elif ability_explanation == "Dexterity" or ability_explanation == "dexterity":
          print("Dexterity is how quickly and precisely you can move.  It affects the accuracy and damage of some weapons, as well as how easily you can evade most attacks.")
        elif ability_explanation == "Constitution" or ability_explanation == "constitution":
          print("Constitution is your hardiness.  It affects how much damage you can take, as well as how easily you can resist the effects of poisons.")
        elif ability_explanation == "Spellcasting" or ability_explanation == "spellcasting":
          print("Spellcasting is your magical aptitude.  It determines the effectiveness of all spells you cast.")
        else:
          print("Please enter a valid ability, listed above(Strength, Dexterity, Constitution, or Spellcasting)")
        print("")
        print("Would you like any other abilities explained? (y/n)")
        keep_explaining = input()
        if keep_explaining == "y":
          continue
        else:
          break

    rolls_num = 0
    # 4 6-sided dice are rolled 4 times.  
    # The lowest possible number is 2.  
    # The lowest value is subtracted from the total
    while rolls_num < 4:
        roll_a = random.randint(2, 6)
        roll_b = random.randint(2, 6)
        roll_c = random.randint(2, 6)
        roll_d = random.randint(2, 6)
        roll_total = (roll_a + roll_b + roll_c + 
                        roll_d - min(roll_a, roll_b, roll_c, roll_d))
        if rolls_num == 0:
            roll_1 = roll_total
        elif rolls_num == 1:
            roll_2 = roll_total
        elif rolls_num == 2:
            roll_3 = roll_total
        elif rolls_num == 3:
            roll_4 = roll_total
        rolls_num += 1
    print("Your rolls are as follows:")
    print("1: " + str(roll_1))
    print("2: " + str(roll_2))
    print("3: " + str(roll_3))
    print("4: " + str(roll_4))
    god = input()
    # god mode for ease of debugging
    if god != "god mode":
        # player picks strength score
        print("Which roll would you like to assign to strength?")
        while strength == 0 or strength == "":
            strength_issue = input()
            
            if strength_issue == "1":
                strength = roll_1
                roll_1 = ""
            elif strength_issue == "2":
                strength = roll_2
                roll_2 = ""
            elif strength_issue == "3":
                strength = roll_3
                roll_3 = ""
            elif strength_issue == "4":
                strength = roll_4
                roll_4 = ""
            else:
                print("Error.  Please enter the number (1, 2, 3, 4) " + 
                      "of a roll that has not already been used.")
        print("")
        print("Your strength score is: " + str(strength))
        print("")
        
        # player picks dexterity score
        print("Which roll would you like to assign to dexterity?")
        while dex == 0 or dex == "":
            dex_issue = input()
            
            if dex_issue == "1" and roll_1 != "":
                dex = roll_1
                roll_1 = ""
            elif dex_issue == "2" and roll_2 != "":
                dex = roll_2
                roll_2 = ""
            elif dex_issue == "3" and roll_3 != "":
                dex = roll_3
                roll_3 = ""
            elif dex_issue == "4" and roll_4 != "":
                dex = roll_4
                roll_4 = ""
            else:
                print("Error.  Please enter the number (1, 2, 3, 4) " + 
                      "of a roll that has not already been used.")
        print("")
        print("Your dexterity score is: " + str(dex))
        print("")
        
        # player picks constitution score
        print("Which roll would you like to assign to constitution?")
        while con == 0 or con == "":
            con_issue = input()
            
            if con_issue == "1" and roll_1 != "":
                con = roll_1
                roll_1 = ""
            elif con_issue == "2" and roll_2 != "":
                con = roll_2
                roll_2 = ""
            elif con_issue == "3" and roll_3 != "":
                con = roll_3
                roll_3 = ""
            elif con_issue == "4" and roll_4 != "":
                con = roll_4
                roll_4 = ""
            else:
                print("Error.  Please enter the number (1, 2, 3, 4) " + 
                      "of a roll that has not already been used.")
        print("")
        print("Your constitution score is: " + str(con))
        print("")
        
        # player picks spellcasting score
        print("Which roll would you like to assign to spellcasting?")
        while spellcast == 0 or spellcast == "":
            spell_issue = input()
            
            if spell_issue == "1" and roll_1 != "":
                spellcast = roll_1
                roll_1 = ""
            elif spell_issue == "2" and roll_2 != "":
                spellcast = roll_2
                roll_2 = ""
            elif spell_issue == "3" and roll_3 != "":
                spellcast = roll_3
                roll_3 = ""
            elif spell_issue == "4" and roll_4 != "":
                spellcast = roll_4
                roll_4 = ""
            else:
                print("Error.  Please enter the number (1, 2, 3, 4) " + 
                      "of a roll that has not already been used.")
        print("")
        print("Your spellcasting score is: " + str(spellcast))
        print("")
        print("Your final ability scores are as follows:")
        print("")
        print("Strength: " + str(strength))
        print("Dexterity: " + str(dex))
        print("Constitution: " + str(con))
        print("Spellcasting: " + str(spellcast))
        print("")
        #player stats are calculated
        spellcast_ability = (spellcast - 10) // 2
        proficiency_bonus = 2 + (level - 1) // 4
        player_spell_save_dc = 8 + proficiency_bonus + spellcast_ability
        player_str_bonus = (strength - 10) // 2
        player_dex_bonus = (dex - 10) // 2
        player_con_bonus = (con - 10) // 2
        player_health = (30 + player_con_bonus * level + level_bonus_2 + 
                    level_bonus_3 + level_bonus_4)
        print("You have " + str(player_health) + " Hit Points")
        player_start_health = player_health
        player_in_bonus = player_dex_bonus
    else:
        strength = 50
        dex = 50
        con = 50
        spellcast = 50
        spellcast_ability = (spellcast - 10) // 2
        print(str(spellcast_ability))
        proficiency_bonus = 2 + (level - 1) // 4
        player_spell_save_dc = 8 + proficiency_bonus + spellcast_ability
        print(str(player_spell_save_dc))
        player_str_bonus = (strength - 10) // 2
        player_dex_bonus = (dex - 10) // 2
        player_con_bonus = (con - 10) // 2
        player_health = (30 + player_con_bonus * level + level_bonus_2 + 
                    level_bonus_3 + level_bonus_4)
        print("You have " + str(player_health) + " Hit Points")
        player_start_health = player_health
        player_in_bonus = player_dex_bonus
def player_equips():
    global greatsword
    global battleaxe
    global shortsword
    global stick
    global shield
    global fire_learned
    global ice_learned
    global lightning_learned
    equipping = "Yes"
    print("")
    print("What weapon will you equip?")
    print("You have the following equippable items in your inventory: ")
    if player_greatsword:
        print("Greatsword")
    if player_battleaxe:
        print("Battleaxe")
    if player_shortsword:
        print("Shortsword")
    if player_shield:
        print("Shield")
    print("Stick")
    while (equipping == "Yes" or equipping == "yes" or 
           equipping == "y" or equipping == "Y"):
        weapon = input()
        if ((weapon == "Greatsword" or weapon == "greatsword") 
                and player_greatsword):
            greatsword = "equipped"
            battleaxe = "unequipped"
            shortsword = "unequipped"
            stick = "unequipped"
            shield = "unequipped"
        elif ((weapon == "Battleaxe" or weapon == "battleaxe") 
                and player_battleaxe):
            greatsword = "unequipped"
            battleaxe = "equipped"
            shortsword = "unequipped"
            stick = "unequipped"
            shield = "unequipped"
        elif ((weapon == "Shortsword" or weapon == "shortsword") 
                and player_shortsword):
            greatsword = "unequipped"
            battleaxe = "unequipped"
            shortsword = "equipped"
        elif weapon == "stick" or weapon == "Stick":
            greatsword = "unequipped"
            battleaxe = "unequipped"
            stick = "equipped"
        elif weapon == "shield" or weapon == "Shield" and player_shield:
            greatsword = "unequipped"
            battleaxe = "unequipped"
            shield = "equipped"
        else:
            print("Please select a valid, owned item to equip.")
        if (shield == "equipped" and shortsword == "equipped" 
            and stick == "equipped"):
            stick = "unequipped"
        print("Would you like to continue equipping items?(y/n)")
        equipping = input()
        if (equipping != "Yes" and equipping != "yes" and 
            equipping != "y" and equipping != "Y"):
            print("You are currently wielding:")
            if greatsword == "equipped":
                print("Greatsword")
            elif battleaxe == "equipped":
                print("Battleaxe")
            elif shortsword == "equipped" and shield == "equipped":
                print("Shortsword and Shield")
            elif shortsword == "equipped" and stick == "equipped":
                print("Shortsword and Stick")
            elif stick == "Equipped" and shield == "equipped":
                print("Stick and Shield")
            elif shortsword == "equipped":
                print("Shortsword")
            else:
                print("Stick")
        else:
            print("What else would you like to equip?")
def shop(shop_name):
    global player_gold
    global player_greatsword
    global player_battleaxe
    global player_shortsword
    global player_focus
    global player_shield
    global player_plate_armor
    global player_scale_armor
    global player_leather_armor
    global player_armor
    global fire_learned
    global ice_learned
    global lightning_learned
    print("Welcome to " + shop_name + "!")
    print("You have " + str(player_gold) + " gold.")
    print("What would you like to buy?")
    print("")
    print("Greatsword - 150 Gold")
    print("Battleaxe - 150 Gold")
    print("Shortsword - 100 Gold")
    print("")
    print("Shield - 50 Gold")
    print("Plate Armor - 150 Gold")
    print("Scale Armor - 100 Gold")
    print("Leather Armor - 50 Gold")
    print("")
    print("Arcane focus - 50 Gold")
    print("Fire Bolt Scroll - 100 Gold")
    print("Ice Spike Scroll - 100 Gold")
    print("Summon Lightning Scroll - 100 Gold")
    shop = True
    # shop loop continues until player says they are done shopping
    while shop != "n":
        buy_item = input("")
        if buy_item == "Greatsword" or buy_item == "greatsword":
            if player_gold >= 150:
                print("Greatsword added")
                player_greatsword = True
                player_gold -= 150
                print("You have " + str(player_gold) + " gold remaining.")
            else:
                print("You do not have enough gold for that item.")
        elif buy_item == "Battleaxe" or buy_item == "battleaxe":
            if player_gold >= 150:
                print("Battleaxe added")
                player_battleaxe = True
                player_gold -= 150
                print("You have " + str(player_gold) + " gold remaining.")
            else:
                print("You do not have enough gold for that item.")
        elif buy_item == "Shortsword" or buy_item == "shortsword":
            if player_gold >= 100:
                print("Shortsword added")
                player_shortsword = True
                player_gold -= 100
                print("You have " + str(player_gold) + " gold remaining.")
            else:
                print("You do not have enough gold for that item.")
        elif buy_item == "Arcane focus" or buy_item == "Arcane Focus":
            if player_gold >= 50:
                print("Arcane focus added")
                player_focus = True
                player_gold -= 50
                print("You have " + str(player_gold) + " gold remaining.")
            else:
                print("You do not have enough gold for that item.")
        elif buy_item == "Shield" or buy_item == "shield":
            if player_gold >= 50:
                print("Shield added")
                player_shield = True
                player_gold -= 50
                print("You have " + str(player_gold) + " gold remaining.")
            else:
                print("You do not have enough gold for that item.")
        elif buy_item == "Plate armor" or buy_item == "Plate Armor" or buy_item == "plate armor":
            if player_gold >= 150:
                print("Plate armor added")
                player_plate_armor = True
                player_gold -= 150
                print("You have " + str(player_gold) + " gold remaining.")
            else:
                print("You do not have enough gold for that item.")
        elif buy_item == "Scale armor" or buy_item == "Scale Armor" or buy_item == "scale armor":
            if player_gold >= 100:
                print("Scale armor added")
                player_scale_armor = True
                player_gold -= 100
                print("You have " + str(player_gold) + " gold remaining.")
            else:
                print("You do not have enough gold for that item.")
        elif buy_item == "Leather armor" or buy_item == "Leather Armor" or buy_item == "leather armor":
            if player_gold >= 50:
                print("Leather armor added")
                player_leather_armor = True
                player_gold -= 50
                print("You have " + str(player_gold) + " gold remaining.")
            else:
                print("You do not have enough gold for that item.")
        elif buy_item == "Fire Bolt Scroll" or buy_item == "fire bolt scroll" or buy_item == "firebolt scroll" or buy_item == "Firebolt Scroll":
            if player_gold >= 100:
              print("Fire Bolt Scroll added")
              player_gold -= 100
              fire_learned = True
              print("You have " + str(player_gold) + " gold remaining.")
            else:
              print("You do not have enough gold for that item.")
        elif buy_item == "Ice Spike Scroll" or buy_item == "ice spike scroll":
            if player_gold >= 100:
              print("Ice Spike Scroll added")
              player_gold -= 100
              ice_learned = True
              print("You have " + str(player_gold) + " gold remaining.")
            else:
              print("You do not have enough gold for that item.")
        elif buy_item == "Summon Lightning Scroll" or buy_item == "summon lightning scroll":
            if player_gold >= 100:
              print("Summon Lightning Scroll added")
              player_gold -= 100
              lightning_learned = True
              print("You have " + str(player_gold) + " gold remaining.")
            else:
              print("You do not have enough gold for that item.")
        else:
            print("Please enter a valid item name")
        print("Do you want to continue shopping? (y/n)")
        shop = input("")
        if shop != "n":
            print("")
            print("What else would you like to buy?")
        else:
            print("Thank you for shopping at " + shop_name + "!")
            print("You've purchased: ")
            if player_greatsword:
                print("Greatsword")
            if player_battleaxe:
                print("Battleaxe")
            if player_shortsword:
                print("Shortsword")
            if player_shield:
                print("Shield")
            if player_plate_armor:
                print("Plate armor")
            if player_scale_armor:
                print("Scale armor")
            if player_leather_armor:
                print("Leather armor")
            if player_focus:
                print("Arcane focus")
            if fire_learned:
                print("Fire Bolt Scroll")
            if ice_learned:
                print("Ice Spike Scroll")
            if lightning_learned:
                print("Summon Lightning Scroll")
            player_equips()
            if player_plate_armor:
                player_armor = 18
            elif player_scale_armor:
                player_armor = 14 + min(player_dex_bonus, 2)
            elif player_leather_armor:
                player_armor = 11 + player_dex_bonus
            else:
                player_armor = 10 + player_dex_bonus
            if player_shield:
                player_armor += 2
 # the player actions are defined in their respective functions here
def player_magic():
    if player_focus:
        choosing_spell = True
        print("What spell will you cast?")
        if fire_learned:
            print("Fire Bolt")
        if ice_learned:
            print("Ice Spike")
        if lightning_learned:
            print("Summon Lightning")
        while choosing_spell:
            choosing_spell = False
            spell = input("")
            if (spell == "Fire Bolt" or spell == "fire bolt" or 
                spell == "Fire bolt" or spell == "Firebolt") and fire_learned:
                player_fire_magic()
            elif (spell == "Ice Spike" or spell == "ice spike" 
                or spell == "Ice spike") and ice_learned:
                player_ice_magic()
            elif (spell == "Summon lightning" or 
                  spell == "summon lightning" or spell == "Summon Lightning" 
                  or spell == "lightning") and lightning_learned:
                player_lightning_magic()
            else:
                print("Please select a valid, prepared spell.")
                choosing_spell = True
            print("")
    else:
        print("You don't have an Arcane focus and can't cast spells!")
        print("You waste your action making hand motions at the " + 
            monster + ".")
def player_fire_magic():
  global monster_health
  print("You lob a ball of scorching flame at the " + monster + ".")
    # monster makes a save, takes damage on fail
  monster_saving_throw = (random.randint(1, 20) + monster_save)
  if monster_saving_throw <= player_spell_save_dc:
      print("The " + monster + " failed to dodge your honing flame.")
      damage = (random.randint(1, 10) + spellcast_ability)
      # fire resistant monsters take less damage from fire
      if monster_fire_resist:
          damage = damage // 2
          print("The " + monster + " doesn't seem very " +
          "damaged by your flames")
      monster_health -= damage
      if monster_health > 0:
          print("The " + monster + " has " + str(monster_health) + 
                    " Hit Points left.")
  else:
      print("The " + monster + " dodged your spell!")
def player_ice_magic():
    global monster_health
    print("Your ice spirals towards the " + monster + "!")
    # player rolls to hit against monster AC
    attack = (random.randint(1, 20) + spellcast_ability + proficiency_bonus)
    if attack >= monster_armor:
      damage = (random.randint(1, 10) + spellcast_ability)
      print("You spear the "+ monster + " with your spike")
        # if monster is resistant to ice damage, damage is halved
      if monster_ice_resist:
          damage = damage // 2
          print("It doesn't seem to have much effect.")
      monster_health -= damage
      
      if monster_health > 0:
          print("The " + monster + " has " + str(monster_health) + 
                    " Hit Points left.")
    else:
      print("The " + monster + " dodged your spell!")
def player_lightning_magic():
    global monster_health
    print("An arc of lightning jumps at the " + monster + "!")
    # player rolls to hit against monster AC
    attack = (random.randint(1, 20) + spellcast_ability + proficiency_bonus)
    if attack >= monster_armor:
      damage = (random.randint(1, 6) + spellcast_ability)
      print("The " + monster + " was struck by the bolt of lightning")
        # if monster is resistant to lightning damage, damage is halved
        # and the additional affect is negated
      if monster_lightning_resist:
          damage = damage // 2
          print("It doesn't seem to have much effect.")
      else:
            save = random.randint(1, 20) + monster_save
            if save < player_spell_save_dc:
                monster_condition = "stunned"
                print("The monster was stunned!")
      monster_health -= damage
      
      if monster_health > 0:
          print("The " + monster + " has " + str(monster_health) + 
                    " Hit Points left.")
    else:
      print("The " + monster + " dodged your spell!")
def player_greatsword_attack():
  global monster_health
  print("You swing at the " + monster + " with your greatsword")
  attack_roll = (random.randint(1, 20) + 
                  player_str_bonus + proficiency_bonus)
  if attack_roll >= monster_armor:
      print("And you hit!")
      damage = (random.randint(1, 6) + 
                random.randint(1, 6) + player_str_bonus)
      monster_health -= damage
      if monster_health > 0:
              print("The " + monster + " has " + str(monster_health) + 
                    " Hit Points left.")
  else:
      print("But you miss.")
def player_battleaxe_attack():
  global monster_health
  print("You swing you battleaxe in a wide arc at the " + monster)
  attack_roll = (random.randint(1, 20) + 
                  player_str_bonus + proficiency_bonus)
  if attack_roll >= monster_armor:
      print("You hit!")
      damage = (random.randint(1, 10) + player_str_bonus)
      monster_health -= damage
      if monster_health > 0:
              print("The " + monster + " has " + str(monster_health) + 
                    " Hit Points left.")
  else:
      print("But you miss.")
def player_shortsword_attack():
  global monster_health
  print("You slash at the " + monster + " with your shortsword")
  attack_roll = (random.randint(1, 20) + 
                  max(player_dex_bonus, player_str_bonus) + 
                  proficiency_bonus)
  if attack_roll >= monster_armor:
      print("You hit!")
      damage = (random.randint(1, 6) + 
                max(player_dex_bonus, player_str_bonus))
      monster_health -= damage
      if monster_health > 0:
              print("The " + monster + " has " + str(monster_health) + 
                    " Hit Points left.")
  else:
      print("But you miss.")
def player_stick_attack():
  global monster_health
  print("You haphazardly bash the " + monster + " with a stick")
  attack_roll = (random.randint(1, 20) + player_str_bonus 
                              + proficiency_bonus)
  if attack_roll >= monster_armor:
      print("You hit!")
      damage = (random.randint(1, 4) + player_str_bonus)
      monster_health -= damage
      if monster_health > 0:
              print("The " + monster + " has " + str(monster_health) + 
                    " Hit Points left.")
  else:
      print("The " + monster + " ignores your effort.")
def player_heal():
        global player_health
        print("You use your healing abilities!")
        healing = (random.randint(1, 6) + spellcast_ability)
        player_health += healing
        if player_health > player_start_health:
            player_health = player_start_health
        print("You have " + str(player_health) + " Hit Points left.")
def fight():
        global first
        global player_health
        global monster_health
        global player_condition
        global monster_condition
        global player_gold
        global exp
        global level
        global level_bonus_2
        global level_bonus_3
        global level_bonus_4
        global player_alive
        print("You've encountered the " + monster + "!  Roll for initiative!")
        # whoever has the higher total initiative goes first
        initiative_player = (random.randint(1, 20) + player_in_bonus)
        initiative_monster = (random.randint(1, 20) + monster_in_bonus)
        if initiative_player >= initiative_monster:
            first = "player"
            print("You make the first move.")
            
        elif initiative_player < initiative_monster:
            print("The " + monster + " strikes first.")
            first = "monster"
            monster_agency()
            input()
    #actual fight code
    
        while (monster_health > 0 and player_health > 0):
                #player can attack with sword, use magic, or heal
            if player_condition != "prone":
                action = input("Are you going to attack, use magic," + 
                               " heal, or equip? ")
            else:
                print("You spend your action getting up.")
                player_condition = ""
            if (action != "attack" and action != "magic" and 
                action != "heal" and player_condition != "prone" and 
                action != "equip"):
                    print("You're wracked by indecision!")
                    print("(please enter 'attack', 'magic', or 'heal')")
                #sword attack
            elif action == "attack":
            # the player will be presented with all weapons in their inventory
                if greatsword == "equipped":
                    player_greatsword_attack()
                elif battleaxe == "equipped":
                    player_battleaxe_attack()
                elif shortsword == "equipped" and stick != "equipped":
                    player_shortsword_attack()
                elif shortsword == "equipped" and stick == "equipped":
                    player_shortsword_attack()
                    player_stick_attack()
                elif stick == "equipped":
                    player_stick_attack()
                input()
                #fire attack
            elif action == "magic":
                player_magic()
                input()
                #heal
            elif action == "heal":
                player_heal()
                input()
                #the monster will attack after the player action
            elif action == "equip":
                print("You hastily reach into you pack!")
                player_equips()
            if monster_health > 0 and monster_condition != "stunned":         
                monster_agency()
            elif monster_condition == "stunned":
              print("The " + monster + " is stunned and cannot act!")
              monster_condition = ""
            print("")
            if player_health <= 0:
              print("You died.")
              player_alive = False
            elif monster_health <= 0:
              player_alive = True
              print("You've slain the " + monster + "!")
              if monster == "Vilespawn":
                  player_gold += 100
                  vilespawn = "Dead"
                  exp += 500
                  print("You gained 100 Gold!")
              elif monster == "Ogre":
                  player_gold += 200
                  ogre = "Dead"
                  exp += 2500
                  print("You gained 200 Gold!")
              elif monster == "Minotaur":
                  player_gold += 1000
                  minotaur = "Dead"
                  exp += 4500
                  print("You gained 1000 Gold!")
              input()
              if exp >= 500 and level == 1:
                  level += 1
                  print("You leveled up!  You are now level " + str(level) + ".")
                  level_bonus_2 += random.randint(1, 8)
                  player_health = (30 + player_con_bonus * level + level_bonus_2 + 
                          level_bonus_3 + level_bonus_4)
                  print("")
                  print("Your new Hit Point Maximum is:")
                  print(str(player_health))
                  exp -= 500
                  level_up()
              if exp >= 2000 and level == 2:
                  level += 1
                  print("You leveled up!  You are now level " + str(level) + ".")
                  level_bonus_3 += random.randint(1, 8)
                  player_health = (30 + player_con_bonus * level + level_bonus_2 + 
                          level_bonus_3 + level_bonus_4)
                  print("")
                  print("Your new Hit Point Maximum is:")
                  print(str(player_health))
                  exp -= 2000
                  level_up()
              if exp >= 5000 and level == 3:
                  level += 1
                  print("You leveled up!  You are now level " + str(level) + ".")
                  level_bonus_4 += random.randint(1, 8)
                  player_health = (30 + player_con_bonus * level + level_bonus_2 + 
                          level_bonus_3 + level_bonus_4)
                  print("")
                  print("Your new Hit Point Maximum is:")
                  print(str(player_health))
                  exp -= 5000
                  level_up()
def choose_monster(choice):
  global monster_health
  global monster_armor
  global monster_save
  global monster_attack_bonus
  global monster_pb
  global monster_in_bonus
  global monster_attack_1
  global monster_attack_2
  global monster_agency
  global monster
  global monster_fire_resist
  global monster_ice_resist
  global monster_lightning_resist
  choosing_monster = True
  while choosing_monster:
    choosing_monster = False
    print("")
    if choice == "playerpick":
      print("Which monster would you like to fight?")
      if vilespawn != "Dead":
        print("Vilespawn (Level 1)")
      if ogre != "Dead":
        print("Ogre (Level 2)")
      if minotaur != "Dead":
        print("Minotaur (Level 3)")
      monster = input()
    else:
      monster = choice
        # Vilespawn stats
    if monster == "Vilespawn" and vilespawn != "Dead":
      monster_health = 15
      monster_armor = 13
      monster_save = 0
      monster_attack_bonus = 3
      monster_pb = 1
      monster_in_bonus = 0
      monster_fire_resist = False
      monster_ice_resist = False
      monster_lightning_resist = False
      #monster actions in combat
      def monster_attack_1():
          global player_health
          print("The Vilespawn spews acid at you!")
          save = random.randint(1, 20) + player_in_bonus
          if save < 13:
              print("It burns!")
              damage = random.randint(1, 6) + monster_attack_bonus
              player_health -= damage
              if player_health > 0:
                  print("You have " + str(player_health) + 
                        " Hit Points left.")
          else:
              print("But you dodged!")
      def monster_attack_2():
          global player_health
          print("It attempts to bite you!")
          attack = (random.randint(1, 20) + monster_attack_bonus 
          + monster_pb)
          if attack >= player_armor:
              damage = random.randint(1, 4) + monster_attack_bonus
              player_health -= damage
              if player_health > 0:
                print("You have " + str(player_health) + 
                    " Hit Points left.")
          else:
              print("But it misses")
          # monsters with multiple attacks have respective conditions 
          # that decide which attack they are going to use.
          # these conditions are located in "monster_agency()"
      def monster_agency():
          if player_armor >= 14:
              monster_attack_1()
          elif player_in_bonus <= 1:
              monster_attack_2()
          else:
              choice = random.randint(1, 3)
              if choice == 1 or choice == 2:
                  monster_attack_1()
              else:
                  monster_attack_2()
    # Ogre stats
    elif monster == "Ogre" and ogre != "Dead":
      monster_health = 59
      monster_armor = 11
      monster_save = -1
      monster_attack_bonus = 4
      monster_pb = 2
      monster_in_bonus = -1
      monster_fire_resist = False
      monster_ice_resist = False
      monster_lightning_resist = False
      #monster actions in combat
      def monster_attack_1():
          print("The Ogre swings at you with its greatclub.")
          attack = (random.randint(1, 20) + monster_attack_bonus + 
                    monster_pb)
          if attack >= player_armor:
              damage = (random.randint(1, 8) + random.randint(1, 8) 
                        + monster_attack_bonus)
              global player_health 
              player_health -= damage 
              
              if player_health > 0:
                      print("You were hit!  You have " + 
                            str(player_health) + " Hit Points left")
          
          else:
              print("But it missed.")
      def monster_agency():
          monster_attack_1()
    # Minotaur stats
    elif monster == "Minotaur" and minotaur != "Dead":
      monster_health = 76
      monster_armor = 14
      monster_save = 0
      monster_attack_bonus = 4
      monster_pb = 2
      monster_in_bonus = 0
      monster_fire_resist = False
      monster_ice_resist = False
      monster_lightning_resist = False
      def monster_attack_1():
          print("The Minotaur charges at you with its horns!")
          attack = (random.randint(1, 20) + monster_attack_bonus + 
                    monster_pb)
          global player_health 
          global player_condition
          global first
          if attack >= player_armor:
              damage = (random.randint(1, 8)  + random.randint(1, 8) 
                        + monster_attack_bonus)
              # currently broken, not sure why tbh
              if first == "monster":
                  print("The Minotaur charges rapidly!")
                  damage += random.randint(1, 8) + random.randint(1, 8)
                  save = random.randint(1, 20) + strength
                  if save < 14:
                      player_condition = "prone"
                      player_health -= damage
                      if player_health > 0:
                          print("You were knocked prone.")
                          print("(You must spend your next action " + 
                                "getting up)")
                          print("You have " + str(player_health) + 
                            " Hit Points left.")
                  
                  else:
                      player_health -= damage
                      if player_health > 0:
                          print("You were hit hard!  You have " + 
                            str(player_health) + " Hit Points left")
                  first = ""
                  
              
              elif player_health > 0:
                  player_health -= damage
                  if player_health > 0:
                      print("You were hit!  You have " + 
                            str(player_health) + " Hit Points left")
              
              
          
          else:
              print("But it missed.")
      def monster_agency():
          monster_attack_1()
    else:
      print("Please select a valid monster.")
      print("Slain monsters cannot be refought.")
      choosing_monster = True
def level_up():
            global strength
            global dex
            global con
            global spellcast
            level_up = ""
            leveling = True
            print("")
            print("What ability score will you increase by 1?")
            print("Your current scores are as follows:")
            print("Strength = " + str(strength))
            print("Dexterity = " + str(dex))
            print("Constitution = " + str(con))
            print("Spellcasting = " + str(spellcast))
            while leveling:
                level_up = input()
                leveling = False
                if level_up == "strength" or level_up == "Strength":
                    strength += 1
                    print("Your new strength score is " + str(strength))
                elif level_up == "dexterity" or level_up == "Dexterity":
                    dex += 1
                    print("Your new dexterity score is " + str(dex))
                elif level_up == "constitution" or level_up == "Constitution":
                    con += 1
                    print("Your new constitution score is " + str(con))
                elif level_up == "spellcasting" or level_up == "Spellcasting":
                    spellcast += 1
                    print("Your new spellcasting score is " + 
                          str(spellcast))
                else:
                    print("Error.  Please select a valid ability score.")
                    leveling = True