"""
Copeland’s Corporate Company has finalized what they want their username and temporary password creation to be and have enlisted your help, once again, to build the function to generate them. In this exercise, you will create two functions, username_generator and password_generator.
Let’s start with username_generator. Create a function called username_generator take two inputs, first_name and last_name and returns a username. The username should be a slice of the first three letters of their first name and the first four letters of their last name. If their first name is less than three letters or their last name is less than four letters it should use their entire names.
For example, if the employee’s name is Abe Simpson the function should generate the username AbeSimp.
"""
# Define a function that takes 2 inputs, first_name and last_name
def username_generator(first_name, last_name):
  # If the first_name is fewer than 4 characters, the resulting username should include the full first_name. Otherwise, the username should include only the first 3 characters
  if len(first_name) < 3:
    first = first_name
  else:
    first = first_name[:3]
  # If the last_name is fewer than 5 characters, the resulting username should include the full last_name. Otherwise, the username should include only the first 4 characters
  if len(last_name) < 4:
    last = last_name
  else:
    last = last_name[:4]
  username = first + last
  print(username)

"""
Now for the temporary password, they want the function to take the input user name and shift all of the letters by one to the right, so the last letter of the username ends up as the first letter and so forth. For example, if the username is AbeSimp, then the temporary password generated should be pAbeSim.
Start by defining the function password_generator so that it takes one input, username and in it define an empty string named password. Inside password_generator create a for loop that iterates through the indices username by going from 0 to len(username).
To shift the letters right, at each letter the for loop should add the previous letter to the string password.
"""
# Define a function that takes 1 input, username
def password_generator(username):
  password = ''
  # for each index in the length of username, subtract 1 to reference the letter to the right, and concatenate to the empty password string
  for i in range(len(username)):
    password = password + username[i-1]
  print(password)

username_generator('Sarah', 'May')
password_generator('SarMay')