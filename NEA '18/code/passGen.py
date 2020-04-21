import score as pScore
import random

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
    score, pword = pScore.score_addsub(gen_p, p_split)
    while score < 20:
        p_split, gen_p = password_gen()
        score, pword = pScore.score_addsub(gen_p, p_split)
    print("Your password : ", pword,"\nYour password score is : ", score, "\nSTRONG")
