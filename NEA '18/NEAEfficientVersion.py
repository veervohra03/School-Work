import random

def menu():
    choice = input("----------------------------------------\nWelcome To 2Password\n1 - Check Password\n2 - Generate Password\n3 - Quit\n>>> ")
    while choice != '1' and choice != '2' and choice != '3':
        choice = input("ERROR\n>>> ")
    print("--------------------")
    if choice == '1':
        password_check()
    elif choice == '2':
        final_pass_gen()
    elif choice == '3':
        print("\n\n--------------------\nThank you for using 2Password\n--------------------")
        quit()

def end_of_task():
    # ---------- Menu/Exit ---------- #
    now_what = input("\n----------------------------------------\n1 - Exit\n2 - Main Menu\n>>> ")
    while now_what != '1' and now_what != '2':
        now_what = input("ERROR\n>>> ")
    print("--------------------")
    if now_what == '1':
        print("\n\n--------------------\nThank you for using 2Password\n--------------------")
        quit()
    else:
        menu()

def score_addsub(pword,p_list):
    # ---------- Variables ---------- #s
    triplet_in_p = []
    digits, symbols, score, letters, bonus = 0, 0, len(pword), 0, 0
    upcase, lowcase, number, symbol = False, False, False, False
    triplets = ["qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop","asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl","zxc", "xcv", "cvb", "vbn"]

    # ---------- Adding points for having uppercase/lowercase/numbers/symbols ---------- #
    for char in p_list:
        if 65 <= ord(char) <= 90 and not upcase:
            score += 5
            bonus += 1
            upcase = True
        elif 97 <= ord(char) <= 122 and not lowcase:
            score += 5
            bonus += 1
            lowcase = True
        elif char.isdigit() and not number:
            score += 5
            bonus += 1
            number = True
        elif char in p_list and char.isdigit() == False and char.isalpha() == False and not symbol:
            score += 5
            symbol = True
    if bonus == 4:
        score += 10

    # ---------- Subtracting points for having only symbols/letters/numbers ---------- #
    for char in p_list:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        elif char in p_list and char.isdigit() == False and char.isalpha() == False:
            symbols += 1
    if digits == len(pword):
        score -= 5
    if letters == len(pword):
        score -= 5
    if symbols == len(pword):
        score -=5

    # ---------- Subtracting points for keyboard patterns ---------- #
    for triplet in triplets:
        if triplet in pword.lower():
            triplet_in_p.append(triplet)
    score -= (len(triplet_in_p) * 5)

    return score, pword

def password_check():
    # ---------- Variables ---------- #
    allowed_chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","!","$","%","^","&","*","(",")","_","-","+","="]
    rejected = []

    pword = input("Please enter your password\n>>> ")

    # ---------- Checking length ---------- #
    while len(pword) < 8:
        pword = input("Password must be longer that 8 characters\n>>> ")
    while len(pword) > 24:
        pword = input("Password must be shorter that 24 characters\n>>> ")

    # ---------- Checking for unallowed characters ---------- #
    p_list = list(pword)
    for char in p_list:
        if char not in allowed_chars:
            rejected.append(char)
    while len(rejected) > 0:
        print("Your password contains unallowed chars\nThese are : ",rejected)
        pword = input(">>> ")
        p_list = pword.split()
        rejected = []
        for char in p_list:
            if char not in allowed_chars:
                rejected.append(char)

    score, pword = score_addsub(pword,p_list)

    # ---------- Printing score ---------- #
    print("Your password : ", pword)
    if score >= 20:
        print("Your password score is : ", score, "\nSTRONG")
    elif score <= 0:
        print("Your password score is : ", score, "\nWEAK")
    else:
        print("Your password score is : ", score, "\nMEDIUM")

    end_of_task()

def password_gen():
    gen_p = ""
    p_length = random.randint(8,12)
    allowed_chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","!","$","%","^","&","*","(",")","_","-","+","="]
    for i in range(p_length):
        gen_p += random.choice(allowed_chars)
        p_split = list(gen_p)
    return p_split, gen_p

def final_pass_gen():
    p_split, gen_p = password_gen()
    score, pword = score_addsub(gen_p, p_split)
    while score < 20:
        p_split, gen_p = password_gen()
        score, pword = score_addsub(gen_p, p_split)
    print("Your password : ", pword,"\nYour password score is : ", score, "\nSTRONG")
    end_of_task()
    

menu()
