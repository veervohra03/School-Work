def score_addsub(pword,p_list):
    # ---------- Variables ---------- #
    triplet_in_p = []
    digits, symbols, score, letters, bonus, upcase, lowcase = 0, 0, len(pword), 0, 0, 0, 0
    upcase, lowcase, number, symbol = False, False, False, False
    triplets = ["qwe", "wer", "ert", "rty", "tyu", "yui", "uio", "iop","asd", "sdf", "dfg", "fgh", "ghj", "hjk", "jkl","zxc", "xcv", "cvb", "vbn","bnm"]

    # ---------- Adding points for having uppercase/lowercase/numbers/symbols ---------- #
    for char in p_list:
        if 65 <= ord(char) <= 90 and not upcase: # if it is an uppercase letter
            score += 5
            bonus += 1
            upcase = True
        elif 97 <= ord(char) <= 122 and not lowcase: # if it is a lowercase letter
            score += 5
            bonus += 1
            lowcase = True
        elif char.isdigit() and not number: # if its a number
            score += 5
            bonus += 1
            number = True
        elif char in p_list and char.isdigit() == False and char.isalpha() == False and not symbol: # if it is a symbol
            score += 5
            symbol = True
    if bonus == 4: # checking if they have achieved the bonus
        score += 10

    # ---------- Subtracting points for having only symbols/letters/numbers ---------- #
    for char in p_list: # iterating through password
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
            if char.upper() == char:
                upcase += 1
            elif char.lower() == char:
                lowcase += 1
        elif char in p_list and char.isdigit() == False and char.isalpha() == False:
            symbols += 1
    if letters == len(pword) or symbols == len(pword) or digits == len(pword): # if there are only numbers/letters/symbols
        score -= 5
    if symbols == 0 and digits == 0 and upcase > 0 and lowcase == 0 or symbols == 0 and digits == 0 and upcase > 0 and lowcase > 0 or symbols == 0 and digits == 0 and upcase == 0 and lowcase > 0:
        # if there are only uppercase or only lowercase
        score -= 5

    # ---------- Subtracting points for keyboard patterns ---------- #
    for triplet in triplets:
        if triplet in pword.lower():
            triplet_in_p.append(triplet)
    score -= (len(triplet_in_p) * 5)

    return score, pword
