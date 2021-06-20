from random import randrange, randint
from os import system
from time import sleep

def welcome_ascii():
  print(",--.   ,--.       ,--.")
  print("|  |   |  | ,---. |  | ,---. ,---. ,--,--,--. ,---.")
  print("|  |.'.|  || .-. :|  || .--'| .-. ||        || .-. :")
  print("|   ,'.   |\   --.|  |\ `--.' '-' '|  |  |  |\   --.")
  print("'--'   '--' `----'`--' `---' `---' `--`--`--' `----'")
  print("  ,--.               ,--.  ,--.")
  print(",-'  '-. ,---.     ,-'  '-.|  ,---.  ,---.")
  print("'-.  .-'| .-. |    '-.  .-'|  .-.  || .-. :")
  print("  |  |  ' '-' '      |  |  |  | |  |\   --.")
  print("  `--'   `---'       `--'  `--' `--' `----'")
  print("  ,---.           ,--.                                ,--.")
  print(" /  O  \ ,--.--.,-'  '-. ,---.      ,--,--.,--,--,  ,-|  |")
  print("|  .-.  ||  .--''-.  .-'(  .-'     ' ,-.  ||      \' .-. |")
  print("|  | |  ||  |     |  |  .-'  `)    \ '-'  ||  ||  |\ `-' |")
  print("`--' `--'`--'     `--'  `----'      `--`--'`--''--' `---'")
  print(" ,-----.                ,---.  ,--.")
  print("'  .--./,--.--. ,--,--./  .-',-'  '-. ,---.")
  print("|  |    |  .--'' ,-.  ||  `-,'-.  .-'(  .-'")
  print("'  '--'\|  |   \ '-'  ||  .-'  |  |  .-'  `)")
  print(" `-----'`--'    `--`--'`--'    `--'  `----'                ,---.")
  print(",--.  ,--.                                                 |   |")
  print("|  '--'  | ,--,--.,--,--,  ,---. ,--,--,--. ,--,--.,--,--, |  .'")
  print("|  .--.  |' ,-.  ||      \| .-. ||        |' ,-.  ||      \|  |")
  print("|  |  |  |\ '-'  ||  ||  |' '-' '|  |  |  |\ '-'  ||  ||  |`--'")
  print("`--'  `--' `--`--'`--''--'.`-  / `--`--`--' `--`--'`--''--'.--.")
  print("                          `---'                            '--'")

#Printing format:
#prompt
#> |user input here
def get_input(prompt, check_acc_enter=True, to_lower=True):
  alphabet = "abcdefghijklmnopqrstuvwxyz_"

  print(prompt)
  need_to_reprompt = True
  while True:
    if to_lower:
      user_in = input("> ").lower()
    else:
      user_in = input("> ")

    if user_in:
      letter_idx = 0
      final_idx = len(user_in) - 1
      for letter in user_in:
        if letter not in alphabet:
          print("Heads up, I only accept input containing alphabetical characters. No ordinary spaces, numbers, funky characters, etc. (which means no non-alphabetical characters in the mystery phrases, since then it would be impossible to guess :D).")
          print(prompt)
          break
        
        if letter_idx == final_idx:
          need_to_reprompt = False

        letter_idx += 1
      
      if need_to_reprompt:
        continue  

      else:
        return user_in

    elif check_acc_enter:
      print("It looks like you accidentally pressed enter. Please try again.")
      print(prompt)
    
    else:
      return user_in

def get_user_info():
  user_name = get_input("First, I would like to get to know my opponent before we begin. What's your name (plz use an underline instead of a space if you need it)?", to_lower=False)
  fav_colour = get_input("Just for fun, what is your favourite colour (if you can't decide, just press enter)?", check_acc_enter=False)
  return (user_name, fav_colour)

def draw_hangman(remaining_lives):
# ┌─────────┬─────────┐
# │         │         │
# │         _         │
# │        |_|        │
# │       __|__       │
# │         |         │
# │         |         │
# │        / \        │
# │       /   \       │
# │                   │
# │                   │
# │      x     x      │
# │       x   x       │
# │  x     x x     x  │
# │  x      x      x  │
# │  x     x x     x  │
# │  x   xx   xx   x  │
# │ x x x x   x x x x │
# │  x   x     x   x  │
# └───────────────────┘
  print(" ┌─────────┬─────────┐")
  print(" │         │         │")
  if remaining_lives < 6:
    print(" │         _         │")
    print(" │        |_|        │")
    if remaining_lives == 5:
      print(" │                   │")
      print(" │                   │")
      print(" │                   │")
      print(" │                   │")
      print(" │                   │")
    elif remaining_lives == 4:
      print(" │         |         │")
      print(" │         |         │")
      print(" │         |         │")
      print(" │                   │")
      print(" │                   │")
    elif remaining_lives == 3:
      print(" │         |__       │")
      print(" │         |         │")
      print(" │         |         │")
      print(" │                   │")
      print(" │                   │")
    elif remaining_lives == 2:
      print(" │       __|__       │")
      print(" │         |         │")
      print(" │         |         │")
      print(" │                   │")
      print(" │                   │")
    elif remaining_lives == 1:
      print(" │       __|__       │")
      print(" │         |         │")
      print(" │         |         │")
      print(" │          \        │")
      print(" │           \       │")
    else:
      print(" │       __|__       │")
      print(" │         |         │")
      print(" │         |         │")
      print(" │        / \        │")
      print(" │       /   \       │")
  else:
    print(" │                   │")
    print(" │                   │")
    print(" │                   │")
    print(" │                   │")
    print(" │                   │")
    print(" │                   │")
    print(" │                   │")
  
  print(" │                   │")
  print(" │                   │")
  print(" │      x     x      │")
  print(" │       x   x       │")
  print(" │  x     x x     x  │")
  print(" │  x      x      x  │")
  print(" │  x     x x     x  │")
  print(" │  x   xx   xx   x  │")
  print(" │ x x x x   x x x x │")
  print(" │  x   x     x   x  │")
  print(" └───────────────────┘")

def process_correct_single_word_guess(lst_words_in_mys_phrase_in_mys_phrase, curr_word_placeholder, idx_found_word, lst_slots_known_or_n):
  reformatted = ""
  iter_word_idx = 0
  word_placeholder_idx = 0
  for word in lst_words_in_mys_phrase_in_mys_phrase:
    if iter_word_idx == idx_found_word:
      for letter in word:
        reformatted += letter + " "
        lst_slots_known_or_n[word_placeholder_idx//2] = 1

        word_placeholder_idx += 2
    else:
      idx_after_word_end = word_placeholder_idx + 2*len(word)
      for character in curr_word_placeholder[word_placeholder_idx:idx_after_word_end]:
        reformatted += character
      
      word_placeholder_idx = idx_after_word_end
        
    reformatted += "  "
    word_placeholder_idx += 2

    iter_word_idx += 1
  
  return (reformatted, lst_slots_known_or_n)

def init_round_data(word_lst):
  mys_word_hint_idx = randrange(0, len(word_lst), 1)
  mys_word_hint = word_lst[mys_word_hint_idx]
  word_lst = word_lst[:mys_word_hint_idx] + word_lst[mys_word_hint_idx+1:]

  indiv_words = mys_word_hint[0].split(" ")

  slots_found = []
  placeholded_word = ""
  for charcter in mys_word_hint[0]:
    if charcter == " ":
      slots_found.append(1)
      placeholded_word += "  "
    else:
      slots_found.append(0)
      placeholded_word += "_ "


  mys_word_last_idx = len(mys_word_hint[0]) - 1
  
  return (indiv_words, mys_word_hint, mys_word_last_idx, placeholded_word, slots_found, word_lst)

def print_wrong_guesses(x_guesses_lst):
  to_print = "Your wrong guesses:  "
  for guess in x_guesses_lst:
    to_print += guess + ", "
  
  to_print = to_print[:-2]
  print(to_print)

#returns True if the round was won, and False otherwise
def play_a_round(word_lst, remaining_lives):
  lst_words_in_mys_phrase, actve_word_hint, actve_word_last_idx, word_placeholder, rec_known_slots, updated_word_lst = init_round_data(word_lst)

  wrong_guesses = []
  words_guessed = []
  
  while remaining_lives >= 0:
    system("clear")
    print(actve_word_hint[1])
    draw_hangman(remaining_lives)
    print("What you know about the mystery phrase: ", word_placeholder)
    print_wrong_guesses(wrong_guesses)

    need_to_reprompt_guess = True
    while need_to_reprompt_guess:#This while loop is for catching erronous entries
      user_guess = get_input("What letter, or single word, do you think is in the mystery phrase?")
      user_guess_len = len(user_guess)
      
      guess_not_prev_found = True

      if user_guess in wrong_guesses:
        print("Oops! You already guessed that, and it was wrong. Please try again.")
        continue
      elif user_guess_len == 1:
        #Code block for character guesses
        for idx in range(len(actve_word_hint[0])):
          #Code block for each character

          if user_guess == actve_word_hint[0][idx]:
            if rec_known_slots[idx]:
              #The user re-guessed a correct character marked as found
              print("Oops! You either:\n - Guessed that already, it being correct.\n - Entered a space character.\nPlease try again.")
              need_to_reprompt_guess = True
              break
            else:
              need_to_reprompt_guess = False

            if guess_not_prev_found:
              guess_not_prev_found = False
              system("clear")
              print("The letter {} is in the mystery phrase!".format(user_guess))
            
            #Updating the [0, 1, 0, etc.] list of which chars are known
            rec_known_slots[idx] = 1
            #Checking if all the chars have been found
            if all(x for x in rec_known_slots):
              return (True, updated_word_lst)

            try:
              word_placeholder = word_placeholder[:2*idx] + user_guess + " " + word_placeholder[2*idx+2:]
            except IndexError:
              if idx == 0:
                word_placeholder = user_guess + word_placeholder[idx+1:]
              else:
                word_placeholder[:2*idx] + user_guess
            
            sleep(2)

          #If the entire phrase has been looped through (currently at the end of the last index), so a user re-guessing a correct letter has not been caught, the reprompt flag needs to be lowered
          if idx == actve_word_last_idx:
            need_to_reprompt_guess = False

        if need_to_reprompt_guess:
          #The for loop was just broken; redirecting to the top of the while loop to reprompt the user
          continue

        if guess_not_prev_found:
          if remaining_lives > 0:
            system("clear")
            print("Sorry, your guess was incorrect. The poor Stick Man has moved closer to death.")
            remaining_lives -= 1
            sleep(3)
            if user_guess not in wrong_guesses:
              wrong_guesses.append(user_guess)
              wrong_guesses.sort()
          else:
            return (False, updated_word_lst)

      else:
        #Code block handling single-word guesses
        if user_guess in words_guessed:
          print("Oops! You already guessed that word. Please try again.")
          continue
        else:
          words_guessed.append(user_guess)

        iter_idx = 0
        word_match_not_found = True
        for word in lst_words_in_mys_phrase:
          if word == user_guess:
            word_match_not_found = False

            word_placeholder, rec_known_slots = process_correct_single_word_guess(lst_words_in_mys_phrase, word_placeholder, iter_idx, rec_known_slots)

            system("clear")
            print("Indeed,", word, "is within that mystery phrase.")
            if all(x for x in rec_known_slots):
              return (True, updated_word_lst)
            else:
              sleep(1)
          
          iter_idx += 1

        if word_match_not_found:
          if remaining_lives > 0:
            system("clear")
            print("Sorry, your guess was incorrect. The poor stick man has moved closer to death.")
            remaining_lives -= 1
            sleep(3)
            if user_guess not in wrong_guesses:
              wrong_guesses.append(user_guess)
              wrong_guesses.sort()
          else:
            return (False, updated_word_lst)

      #If continue was not called, then there is no need to reprompt.
      break

def victory_screen(user_name, fav_colour):
  system("clear")
  if fav_colour:
    print("The Stick Man sends {} a very grateful note, written in {} ink. Unfortunately, the electronic display is too weak to comprehend such a wonderful hue.".format(user_name, fav_colour))
  else:
    print("The Stick Man sends", user_name, "a very grateful note.")

  print("               _   _   _   _   _   _   _   _   _")
  print("              / \ / \ / \ / \ / \ / \ / \ / \ / \\")
  print("             ( C | O | N | G | R | A | T | S | ! )")
  print("              \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/")
  print("           _   _   _                   _   _   _   _")
  print("          / \ / \ / \                 / \ / \ / \ / \\")
  print("         ( Y | o | u )               ( B | E | A | T )")
  print("          \_/ \_/ \_/                 \_/ \_/ \_/ \_/")
  print("       _   _   _                           _   _   _   _")
  print("      / \ / \ / \                         / \ / \ / \ / \\")
  print("     ( t | h | e )                       ( A | r | t | s )")
  print("      \_/ \_/ \_/                         \_/ \_/ \_/ \_/")
  print("   _   _   _                           _   _   _   _   _   _")
  print("  / \ / \ / \                         / \ / \ / \ / \ / \ / \\")
  print(" ( a | n | d )                       ( C | r | a | f | t | s )")
  print("  \_/ \_/ \_/                         \_/ \_/ \_/ \_/ \_/ \_/")
  print(" ")
  print(" ")
  print(" ")
  print(" ")
  print("                   _   _   _   _   _   _   _")
  print("                  / \ / \ / \ / \ / \ / \ / \\")
  print("                 ( H | a | n | g | m | a | n )")
  print("                  \_/ \_/ \_/ \_/ \_/ \_/ \_/")
  print("                       _   _   _   _   _")
  print("                      / \ / \ / \ / \ / \\")
  print("                     ( G | a | m | e | ! )")
  print("                      \_/ \_/ \_/ \_/ \_/")

def won_round_screen(past_round_num):
  system("clear")
  print("Come on! T_T You won round " + str(past_round_num) + "!")
  for second in ("5", "4", "3", "2", "1"):
    print("Moving to the next round in " + second + "...")
    sleep(1)
  
  if past_round_num == 1:
    print(" >======>                                       >=>")
    print(" >=>    >=>                                     >=>        >=>>=>")
    print(" >=>    >=>      >=>     >=>  >=> >==>>==>      >=>       >>   >=>")
    print(" >> >==>       >=>  >=>  >=>  >=>  >=>  >=>  >=>>=>           >=>")
    print(" >=>  >=>     >=>    >=> >=>  >=>  >=>  >=> >>  >=>          >=>")
    print(" >=>    >=>    >=>  >=>  >=>  >=>  >=>  >=> >>  >=>        >=>")
    print(" >=>      >=>    >=>       >==>=> >==>  >=>  >=>>=>       >======>")
  elif past_round_num == 2:
    print(" >======>                                       >=>")
    print(" >=>    >=>                                     >=>       >=>>=>")
    print(" >=>    >=>      >=>     >=>  >=> >==>>==>      >=>          >=>")
    print(" >> >==>       >=>  >=>  >=>  >=>  >=>  >=>  >=>>=>        >=>")
    print(" >=>  >=>     >=>    >=> >=>  >=>  >=>  >=> >>  >=>           >=>")
    print(" >=>    >=>    >=>  >=>  >=>  >=>  >=>  >=> >>  >=>            >=>")
    print(" >=>      >=>    >=>       >==>=> >==>  >=>  >=>>=>       >====>")
  elif past_round_num == 3:
    print(" >======>                                       >=>")
    print(" >=>    >=>                                     >=>            >=>")
    print(" >=>    >=>      >=>     >=>  >=> >==>>==>      >=>           >>=>")
    print(" >> >==>       >=>  >=>  >=>  >=>  >=>  >=>  >=>>=>          > >=>")
    print(" >=>  >=>     >=>    >=> >=>  >=>  >=>  >=> >>  >=>        >=> >=>")
    print(" >=>    >=>    >=>  >=>  >=>  >=>  >=>  >=> >>  >=>       >===>>=>>=>")
    print(" >=>      >=>    >=>       >==>=> >==>  >=>  >=>>=>            >=>")
  elif past_round_num == 4:
    print(" >======>                                       >=>")
    print(" >=>    >=>                                     >=>       >=>>==>")
    print(" >=>    >=>      >=>     >=>  >=> >==>>==>      >=>       >=>")
    print(" >> >==>       >=>  >=>  >=>  >=>  >=>  >=>  >=>>=>       >==>")
    print(" >=>  >=>     >=>    >=> >=>  >=>  >=>  >=> >>  >=>          >=>")
    print(" >=>    >=>    >=>  >=>  >=>  >=>  >=>  >=> >>  >=>            >=>")
    print(" >=>      >=>    >=>       >==>=> >==>  >=>  >=>>=>       >==>>=>")
  
  sleep(2)

def lose_screen(user_name, fav_colour):
  zero_or_one = randint(0, 1)
 
  if zero_or_one:
    print(user_name + ", good game! I enjoyed that very much.")
    print("In fact, I'm in such a good mood that I'll give you my new pair of scissors as a thank-you-for-playing present, instead of sending it to the Stick Man's nemesis.")
  else:
    print(user_name + ", good game!")

  if fav_colour:
    print("Tut tut tut... now where did I put the {} wrapping paper and ribbon...".format(fav_colour))
  else:
    print("Tut tut tut... now where did I put the wrapping paper and ribbon...")

  sleep(2)
  print("Ah!")
  sleep(1)
  if zero_or_one:
    print("Here you go! Thank you for your time! Come again another day!")
  else:
    print("Behold, the perfect reconciliation present for the Stick Man's nemesis!")
    if fav_colour:
      print("I even topped it off with a", fav_colour, "bow.")

  print("")
  print("      xxxxx    xxxxxx")
  print("      x  xxxxxxx     x")
  print("      xxx   xxxxxxxxxx")
  print("        xxxxxxx xxxxx")
  print("      xxxxxx  xxxxxxxx")
  print("     xx xxxxxxxxxxxxxxx")
  print("    x   x┌─────────┐x xx")
  print("  xx    x│ x     x │x  xx")
  print(" xx     x│  x   x  │x   xxx")
  print("        x│   \ /   │x     x")
  print("        x│    |    │x")
  print("        x│   / \   │x")
  print("        x│ x/   \\x │x")
  print("        x│x x   x x│x")
  print("        x│ x     x │x")
  print("        x└─────────┘x")
  print("        xxxxxxxxxxxxx")

def main():
  avalble_words = [("double sided tape", "This is used in putting things together or for placing something somewhere."), ("thread", "This is used in felt or fabric-related crafts."), ("construction paper", "This material is a thicker and colour-varying version of a material used by artists as well as all sorts of work."), ("glitter", "This can be sprinkled onto anything, or it can be applied within another material, and it adds a particular aesthetic quality."), ("paint", "This medium is classic for art."), ("scissors", "In crafts, this tool is invaluable for working with materials."), ("needle", "You don't work with fabric without this."), ("digital camera", "This is a main tool for creating something that imitates vision of a scene."), ("paintbrush", "This tool is used to apply various mediums to a surface."), ("apron", "The arts-and-crafts-er bears this on themselves at all times while working with messy stuff."), ("sewing machine", "This is a big help to doing projects involving a larger amount of fabric."), ("pencil crayon", "A colourful art medium")]
  user_won = False
  lives_left = 6

  welcome_ascii()
  print("Muahahaaaaaaa. I have captured the Stick Man. *playfully* I would be happy to let him go... IF you can figure out 5 of my mystery phrases. Otherwise, Your beloved Stick Man will be magically transformed into a pair of scissors.")
  user_name_colour = get_user_info()

  round_counter = 1
  while round_counter <= 5:
    round_won_bool_and_new_word_lst = play_a_round(avalble_words, lives_left)
    avalble_words = round_won_bool_and_new_word_lst[1]
    if round_won_bool_and_new_word_lst[0]:
      if round_counter == 5:
        victory_screen(user_name_colour[0], user_name_colour[1])
      else:
        won_round_screen(round_counter)

      round_counter += 1
    else:
      lose_screen(user_name_colour[0], user_name_colour[1])
      break
  

if __name__ == "__main__":
  main()