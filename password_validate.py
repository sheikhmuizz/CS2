#this function checks password strength (uppercase,lowercase,8,specialcharacters)
def check_password_strength(password):
  counter = 0
  #this part will check to see if my password is > 8 characters
  if len(password) >= 8:
    counter += 1
  #this part will check for uppercase
  for letter in password:
    if ord(letter) >= 65  and ord(letter) <= 90:
      counter = counter + 1
      break 
  #this part will check for lowercase 
  for letter in password:
    if ord(letter) >= 97  and ord(letter) <= 122:
      counter = counter + 1
      break 


  if counter == 3:
    return True 
  else:
    return False 
