
# Question 1 : Python Basics
# A- If you have two lists, L1=[‘HTTP’,’HTTPS’,’FTP’,’DNS’] L2=[80,443,20,53],
# convert it to generate this dictionary d={‘HTTP’:80,’HTTPS’:443,’FTP’:20,’DNS’:53 }

#  \\\\\\\\\ Solution :
L1 = ['HTTP' , 'HTTPS' ,'FTP' , 'DNS']
L2 = [80,443,20,53]
d= {}
for i in range(len(L1)):
    d.__setitem__(L1[i], L2[i])
print(d)



# B- Generate and print a list of primary numbers from 1 to 1000.
#  \\\\\\\\\ Solution :
Primary =[x for x in range(1, 1000) if all(x % y for y in range(2, x))]
print(Primary)




# C-  L=[‘Network’ , ’Math’ , ’Programming’, ‘Physics’ , ‘Music’]
#  In this exercise, you will implement a Python program that reads the items of the previous list and identifies 
#  the items that starts with ‘Ph’ letter, then print it on screen
# Tips: using loop, ‘len ()’ , startswith() methods.    
# \\\\\\\\\ Solution :
L=['Network' , 'Math' , 'Programming' , 'Physics' , 'Music']
for i  in range(len(L)) :
    if L[i].startswith("Ph"):
        print(L[i] , ':' , L[i][0:2]," /////////// ", 'The Right one' ,sep=" ")
        continue
    print(L[i] , ':' , L[i][0:2] ,sep=" ")




# D- Using Dictionary comprehension, Generate this dictionary 
# d={1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10,10:11} 
#  \\\\\\\\\ Solution :
d ={x:x+1 for x in range(1,11)}
print(d)







# Question 2: Convert from Binary to Decimal
#  Write a Python program that converts a Binary number into its equivalent Decimal number.
# The program should start reading the binary number from the user. Then the decimal equivalent number must be 
# calculated. Finally, the program must display the equivalent decimal number on the screen.
# Tips: solve input errors
# \\\\\\\\\ Solution :
try :
    Check = False
    Binary = (input('enter Your Binary Nuber To Convert to Decimal Number'))
    for i in Binary :
        if (int(i) != 0 ) and (int(i) !=1):
            Check = False
            break
        else:
            Check = True
    if Check ==  True:
     print('Good Binary Number!')
     Length= len(Binary)
     Result = 0
     for i in Binary:
      Result += int(i)*(2**(Length-1))
      Length -=1
     print(f'the Result is :  {Result}')
    else:
        print('Sorry You Should  Add just Zero / One')
except:
    print('Sorry You Have to Write Only Number! // Only : Zero Or One')
    print('Note : You should not add Any Type of Symbol Or left a Space Between Your Binary Code')



# Question 3: Working with Files” Quiz Program” :
# Type python quiz program that takes a text or json or csv file as input for (20 (Questions, Answers)).
# It asks the questions and finally computes and prints user results 
# and store user name and result in separate file csv or json file.



quiz = open(".\quiz.txt","w")
name = input('Enter Your Name')
Age = input('Enter Your Age')
Number = input('Enter Your Number')
quiz.write('Student Info : \n ')
quiz.write(f'Name : {name}  \n ')
quiz.write(f'Age : {Age}  \n ')
quiz.write(f'Number : {Number}  \n ')
quiz.write(f'Time : 1.5 H \n \n')
quiz.write(f'G O O D  L U C K !  \n \n ')
question = [
'q_1: 3 x 9 = ?','q_2: 2 x 12 = ? ','q_3: 3 x 3 = ? ','q_4: 4 x 4 = ? ','q_5: 5 x 20 = ? ',
'q_6: 10 x 12 = ? ','q_7: 7 x 6 = ? ','q_8: 9 x 9 = ? ','q_9: 15 x 2 = ? ','q_10: 2 x 8 = ? ',
'q_11: 11 x 3 = ? ','q_12: 3 x 10 = ? ','q_13: 4 x 6 = ? ','q_14: 8 x 4 = ? ','q_15: 6 x 6 = ? ',
'q_16: 40 x 2 = ? ','q_17: 43 x 2 = ? ','q_18: 60 x 3 = ? ','q_19: 20 x 100 = ? ','q_20: 14 x 3 = ? '
]

Answers = []

Check_Answers = [
'27' ,'24' ,'9' ,'16' ,'100' ,'120' ,'42' ,'81' ,'30' ,'16',
'33' ,'30' , '24' ,'32' ,'36' ,'80' ,'86' ,'180' ,'2000' ,'42',
]

Resut = 0
evaluation = 'F'

for i in range(0,20):
    quiz.write(f'{question[i]} \n')
    Answers.append(input(f'{question[i]}'))
    quiz.write(f'A_{i+1} : {Answers[i]}')
    quiz.write("\n")
    quiz.write("\n")

for i in range(20) :
    if Answers[i] == Check_Answers[i]:
        Resut +=0.5

if Resut<=5:
 evaluation = 'F'
elif (Resut>5) and (Resut<7) :
    evaluation = 'A'
elif (Resut >=7) and (Resut<=9) :
    evaluation = 'B'
else:
    evaluation= 'C'

import json
Details = {"Name":name,"Age":Age , "Number":Number, "result":Resut,"evaluation":evaluation}
with open(".\Result.json","w") as file:
    json.dump(Details, file)

