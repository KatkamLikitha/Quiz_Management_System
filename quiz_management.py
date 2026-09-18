# QUIZ MANAGEMENT SYSTEM

quiz_list=['python','Java']
question_list=[[0,'what is python','A.Programming language','B.Operating sytsem','C.Database','D.language','A'],[1,'who invented java','A.James Gosling','B.Dennis','C.charles','D.Guido','A']]
score_list=[]
admin_user="admin"
admin_password="admin123"
students={}
student_scores = []
while True:
    print("="*20,"QUIZ MANAGEMNET SYTSEM","="*20)
    print("1.Admin")
    print("2.Student")
    print("3.Exit")
    role=input("Select Role:")
# ADMIN
    if role=='1':
        username=input("Enter username:")
        password=input("Enter password:")
        if username==admin_user and password==admin_password:
            print("!!Login Successful!!")
        else:
            print("Invalid password or password")
            continue
        while True:
            print("*"*27,"ADMIN MENU","*"*27)
            print("1.Add Quiz")
            print("2.Add Questions")
            print("3.View Quiz")
            print("4.Delete Question")
            print("5.Modify Question")
            print("6.View Student Scores")
            print("7.Back")
            choice=input("Enter choice:")
            if choice=='1':
                quiz=input("Enter Quiz Name:")
                found=False
                for q in quiz_list:
                    if q.lower()==quiz.lower():
                        found=True
                        break
                if found:
                    print("!!Quiz Already Exists!!")
                else:
                    quiz_list.append(quiz)
                    print("!!Quiz Added Successfully!!")
            elif choice=='2':
                if len(quiz_list)==0:
                    print("No Quiz is Available")
                else:
                    print("Available Quizzes:")
                    for i in range(len(quiz_list)):
                        print(i+1,'.',quiz_list[i])
                    qn=int(input("Select Quiz Number:"))-1
                    question=input("Enter Question:")
                    op1=input("Option A:")
                    op2=input("Option B:")
                    op3=input("Option C:")
                    op4=input("Option D:")
                    answer=input("Enter Correct Option(A/B/C/D):").upper()
                    question_list.append([qn,question,op1,op2,op3,op4,answer])
                    print("!!Question Added!!")
            elif choice=='3':
                if len(quiz_list)==0:
                    print("No Quizzes Are Available")
                else:
                    for i in range(len(quiz_list)):
                        print("QUIZ:",quiz_list[i])
                        for i in range(len(quiz_list)):
                                print("\nQUIZ :", quiz_list[i])

                                for q in question_list:
                                    if q[0] == i:
                                        print("Question :", q[1])
                                        print(q[2])
                                        print(q[3])
                                        print(q[4])
                                        print(q[5])
                                        print("Correct Option :", q[6])
                                        print("-"*30)
            elif choice=='4':
                if len(question_list)==0:
                    print("No Questions")
                else:
                    for i in range(len(question_list)):
                        print(i+1,question_list[i][1])
                    d=int(input("Enter Question Number To Delete:"))-1
                    question_list.pop(d)
                    print("!!Question Deleted!!")
            elif choice=='5':
                if len(question_list)==0:
                    print("No Questions Available")
                else:
                    print("Available Questions:")
                    for i in range(len(question_list)):
                        print(i+1,question_list[i][1],'->',question_list[i][2])
                    ch=int(input("Enter question number to modify:"))-1
                    if 0<=ch<len(question_list):
                        new_question=input("Enter new question:")
                        new_answer=input("Enter new correct answer:")
                        question_list[ch][1]=new_question
                        question_list[ch][2]=new_answer
                        print("!!Question Modified Successfully!!")
                    else:
                        print("Invalid Question Number")
            elif choice == '6':
                if len(student_scores) == 0:
                    print("No Student Attempted Quiz Yet")
                else:
                    print("{:<15} {:<15} {:<10}".format("Username", "Quiz", "Score"))
                    print("-"*40)
                for s in student_scores:
                    print("{:<15} {:<15} {:<10}".format(s[0], s[1], s[2]))
            elif choice=='7':
                break
            else:
                print("Invalid Choice")
    # STUDENT
    elif role == '2':
        username = input("Enter Username: ")
        if username in students:
            print("!!User Already Exists!!")
            password = input("Enter Password: ")
            if students[username] != password:
                print("Wrong Password")
                continue
        else:
            password = input("Create Password: ")
            students[username] = password
            print("Registration Successful!!")
        if len(quiz_list) == 0:
            print("No Quiz Available")
            continue
        print("\nAvailable Quizzes:")
        for i in range(len(quiz_list)):
            print(i+1, ".", quiz_list[i])
        qn = int(input("Select Quiz Number: ")) - 1
        score = 0
        print("*"*20, "QUIZ STARTED", "*"*20)
        for q in question_list:
            if q[0] == qn:
                print("\nQuestion:", q[1])
                print(q[2])
                print(q[3])
                print(q[4])
                print(q[5])
                ans = input("Enter Option (A/B/C/D): ").upper()
                if ans == q[6]:
                    score += 1
        print("*"*20, "QUIZ FINISHED", "*"*20)
        print("Your Score:", score)
        student_scores.append([username, quiz_list[qn], score])
    elif role=='3':
        print("Thank You!!")
        break
    else:
        print("Invalid Choice")
            
            
        
        
