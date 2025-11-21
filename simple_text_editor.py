# Making Simple Text Editor Using Only Python

import os
from os.path import exists

def read_file(filename):
  with open(filename, "r")as file:
    return file.read()
# Read a text file and return its content as a string

def write_file(filename, content):
  with open(filename, "w")as file:
    file.write(content)
# Write a string to a text file

def get_user_input():
  print("\nEnter your text (type SAVE on a new line to save and exit):")

  lines = []
   # Read lines from user until they type "SAVE"
  while True:
    line = input()
    if line == "SAVE":  
      break
    lines.append(line)
     # Join lines into a single string with newline characters
  return "\n".join(lines)

def main():
  filename = input('Enter the filename to open or create: ').strip()
  try:
    if os.path.exists(filename):
      print(read_file(filename))
    else:
      write_file(filename, "")
      # Get user input and write it to the file

    content = get_user_input()
     # Write the content to the file
    write_file(filename, content)
     # Confirm that the file has been saved
    print(f"File '{filename}' has been saved.")
  except OSError:
     # Handle any errors that occur while reading or writing the file
    print(f"{filename} could not be opened.")

if __name__ == "__main__":
  main()
# Run the main function if this script is executed directly

