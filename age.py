def question():
    answer = None
    while answer is None:
        print ("Welcome to AGE\n please enter your age.")
        answer = input("How old are you?\nEnter a number from 0 to 99  ")
        try:
            answer = int(answer) 
            if answer >99 or answer < 0:
                answer = None
                
        except:
            answer = None
    if answer is 1:
        print("You are 1 year old")
    else:
        print("You are " + str(answer)  + " years old")

    if answer > -1 and answer < 3 :
       print ("This makes you a baby or a toddler")



    if answer > 3 and answer < 13 :
       print ("This makes you a child")
    if answer > 13 and answer < 19 :
       print ("This makes you a teenager")
    if answer > 19 and answer < 60 :
       print ("This makes you an adult")
    if answer > 60 and answer < 99 :
       print ("This makes you an elder")

    answer2= None
    while answer2 is None:
        answer2 = input("try again(yes/no) ")
        if answer2  in ["yes" , "y" , "Y" , "YES"]:
            answer = None 
            question()
        if answer2 in ["no" , "n" , "N" , "NO"]:
            pass
            print("thank you" )       
        else:
            print("I do not understand")
            answer2= None
  
    return None

question()
