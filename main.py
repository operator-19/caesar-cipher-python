alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import logo
from art import logo
print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text: # if encode is selected skip if statement above
      if char in alphabet:
          position = alphabet.index(char) # grabs the position inputted 'text' then puts into 'positon' varibale
          new_position = position + shift_amount # figures out new position by adding inputted 'shift_amount' then into new variable
          end_text += alphabet[new_position] # append encoded to empty string
      else:
          end_text += char # if special character then just append with no chages
  print(f"Here's the {cipher_direction}d result: {end_text}")

shouldContinue = True
while shouldContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # takes remainder of inputted shift and moves it to fit within the alphabet
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Type 'no' to quit\n").lower()
    if result == 'no':
        shouldContinue = False
        print('You quit.')