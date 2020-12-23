import random

chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()"     #available *characters* to be used

while 1:
    password_len = int(input("Comprimento da senha: "))                              #asking how many characters the password will have
    password_count = int(input("Quantas senhas você quer gerar: "))                  #quantity of different passwords going to be generated 
    for x in range(0, password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)                                     #choosing randomly between the *characters*
            password = password + password_char                                      #changing the previously created string (password) for the random character
        print("Here is your password: ", password)                                   #printing the passwords that were asked