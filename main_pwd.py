txt = open('test.txt')                          # Add a variable with your document to open

def password():
    i = 1                                       # i variable is = to 1 try
    while i <= 3:                                # While i is less than or equal to 3 try, try again
        msg = input("Enter your password:\n") 
        with open('password.txt') as f:         # with the txt file, open the file where the password is saved, add it to f.
            for line in f:                      # for the 1st line in f (f is the file with the password now)
                password = line.strip()         # add a variable with value the line of the password file. (basiclly your password)
            if msg == password:                 # if you input is = to your password saved in your file
                print("Your device is unlocked") 
                print(txt.read())               # Your divice is unlocked and your file is open.
                break                           # Stop your script after unlocked your divice.

            else:                               # If your password in incorrected 
                i += 1                          # Add 1 more try to the i variable
                print("Password Incorected. Try again")
                if i == 4:                          # If you try more than 3 times, your divice is Locked Out. and the script stop without open your document.
                    print("You have been Locked Out.")
                    break
password()                                      # The define catagorie is print with the command. 

