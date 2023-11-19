# Program will open a text file called DOB.txt and display the information within this file in two seperate lists.

# Start program on new line
print("\n")


# Open the file.

info = open("DOB.txt", 'r')


# Read the contents into a list

Contents = []
for line in info:
    Contents.append(line)


# Close the file

info.close()


# Read first two words in each string and store them in a list
# Search each item in Contents list for white spaces. If its the second white space, store all characetrs up to that position in Name list. All characters after that position to be stored in Birthdate list

temp = "" # for storing each item in Content list as a string
white_space = 0 # to use for separating names from brithdates
List_Name = [] # list for names
List_Birthdate = [] # List for birthdates


for i in range(len(Contents)):                                  # For loop to run through each item in the list Contents
    temp = Contents[i]                                          # Store the current string into a temp string
    for c in range(len(temp)):                                  # For loop to run through each character of the current string
        if temp[c] == " ":                                      # Check if the current characetr is a white space
            white_space = white_space + 1
            if white_space == 2:                                # If its the second white space then
                List_Name.append(temp[0:c])                     # add all characters up to this position into the Name List
                List_Birthdate.append(temp[c+1:len(temp)-1])    # Add all characters from this point to the Birthdate list, minus the last two characters
                white_space = 0                                 # reset the white space checkign variable for the next item in the list Contents
                break


# Print the list of Names

print("\033[1mName\n \033[0m")
for i in range(len(List_Name)):
    print(List_Name[i])


# Print the list of Birthdates

print("\033[1m\n\nBirthdate\n\033[0m")
for i in range(len(List_Birthdate)):
    print(List_Birthdate[i])
