#what is the score?
score = int(input("what is your test score?"))

#Nested If else statements below
#Determine the grade
#if score >= 90:
    #print('your grade is an A')
#else:
   #if score >= 80:
        #print('your grade is a B')
    #else:
        #if score >= 70:
            #print('your score is a C')
        #else:
            #if score >= 60:
                #print('your score is a D')
            #else:
               # print('your score is an F')

#if-elif-else statements

#determine the grade
if score >= 90:
    print('your grade is an A')
elif score >= 80:
    print('your score is a B')
elif score >= 70:
    print('your score is a C')
elif score >= 60:
    print('your score is a D')
else:
    print('your score is an F')