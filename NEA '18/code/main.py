import passGen as pGen
import password_check as pCheck

def menu():
    choice = input("----------------------------------------\nWelcome To 2Password\n1 - Check Password\n2 - Generate Password\n3 - Quit\n>>> ")
    while choice != '1' and choice != '2' and choice != '3': # data validation
        choice = input("ERROR\n>>> ")
    print("--------------------")
    # checking user choice and directing them to desired function
    if choice == '1':
        pCheck.password_check()
        end_of_task()
    elif choice == '2':
        pGen.final_pass_gen()
        end_of_task()
    elif choice == '3':
        print("\n\n--------------------\nThank you for using 2Password\n--------------------")
        quit() # quitting

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
        
menu()
