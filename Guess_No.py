# Guess Lucky No

sec_no = 7
i=0

while i < 3:
    guess_no = int(input("plese enter any decimal No:"))
    i+=1
    if guess_no == sec_no:
        
        print("You Win...!")
        break
    else:
        print("please try..")
        print(" your limit is remaining:",3-i)
else:
    print('your limit is over\n')
    print('\tTry it next time............')
