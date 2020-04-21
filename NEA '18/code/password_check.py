import score as pScore

def password_check():
    # ---------- Variables ---------- #
    allowed_chars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","!","$","%","^","&","*","(",")","_","-","+","="]
    rejected = []
    pword = input("Please enter your password\n>>> ")

    # ---------- Checking length ---------- #
    if len(pword) < 8:
        print("Password must be longer that 8 characters")
        import main as m
        m.menu()
    elif len(pword) > 24:
        print("Password must be shorter that 24 characters")
        import main as m
        m.menu()

    # ---------- Checking for unallowed characters ---------- #
    p_list = list(pword)
    for char in p_list:
        if char not in allowed_chars:
            rejected.append(char)
    if len(rejected) > 0:
        print("Your password contains unallowed chars\nThese are : ",rejected)
        menu()

    score, pword = pScore.score_addsub(pword,p_list)

    # ---------- Printing score ---------- #
    print("Your password : ", pword)
    if score >= 20:
        print("Your password score is : ", score, "\nSTRONG")
    elif score <= 0:
        print("Your password score is : ", score, "\nWEAK")
    else:
        print("Your password score is : ", score, "\nMEDIUM")
