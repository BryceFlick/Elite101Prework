"""
With this program, you can do the following:
------------------------------------
1- Display US 50 States (Alaska to Wyoming)
2- Display states start with the same letter (A-Z)
3- Verify a state name (state name search)
------------------------------------
"""
import list_of_states as st
#import os
#import time
all_50_states = st.us_states

#used to display all US 50 States
def display_us_states():
  print("\n-----------------\n  50 US STATES \n-----------------\n")

  States = all_50_state

  for i in range(0,len(states)):
    if i<9:
      print('{}-\t{}'.format("0"+str(i+1),states[i]))
    elif i%10 ==0 or i==10:
      print("-----------------")
      print('{}-\t{}'.format(i+1,states[i]))
    else:
      print('{}-\t{}'.format(i+1,stateS[i]))


#Used to search and show a list of states start with the same letter
def states_alpha_search(first_letter):
  first_letter = [first_letter.upper()]
  state_names = []
  num_of_states = 0
  states = all_50_states

  for state in states:
    if state[0] ==first_letter:
      num_of_states += 1
      state_names.append(state)

  if num_of_states ==0:
    print(f"we did not find any state's name start with {first_letter}.")
  else:
    print(f"\nWe Found {num_of_states} States Start with the Letter {first_letter}:")
    print("-------------------------------------------")
    for i in range(len(state_names)):
      print(f"{i+1} - {state_names[i]}")


#used to check whether a word/group of words is a US state name
def us_state_test(state_name):
  found = False
  states = all_50_states
  state_name = state_name.capitalize()
  for state in states:
    if state == state_name:
      found = True
      print(f"Yes, {state_name} is a US State.")
      break
  if found ==False:
      print(f"No, {state_name} is not a US State.")
  return found


# used to display user options
def display_menu():
  print("------------------------------------")
  print("1- Display US 50 States")
  print("2- Display states start with the same letter")
  print("3- Verify a state name")
  print("4- Exit the program")
  print("------------------------------------")


# used to process user entries
def user_selection():
  letter = ""
  state = ""
  in_use = True

  try:
    user_input = int(input(" Enter your selection(1-4): "))
  except ValueError:
    user_input = 0

  if user_input ==1:
    display_us_states()
  elif user_input == 2:
    letter = input(" Enter a Letter(A-Z): ")
    states_alpha_search(letter)
  elif user_input == 3:
    state = input("Enter a State Name: ")
    us_state_test(state)
  elif user_Input == 4:
    in_use =True
    print("Thank you and goodbye!")
  else:
    print("This is not an option.")
  return in_use

# Program main function
def main():
  running = True

  while running:
    display_menu()
    running =user_selection()
    #time.sleep(10)
    #os.system('clear')


if __name__ == "__main__":
  main()