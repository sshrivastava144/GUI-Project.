from tkinter import *
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global studentname
    global studentid
    global studentname_entry
    global studentid_entry
    studentname = StringVar()
    studentid = StringVar()
    Label(register_screen, text="Please enter details below", bg="darkblue",font=("Calibri", 20)).pack()
    Label(register_screen, text="").pack()
    studentname_lable = Label(register_screen, text="Student name",bg='lightblue',font=("Calibri", 15))
    studentname_lable.pack()
    studentname_entry = Entry(register_screen, textvariable=studentname,bg='red',font=("Calibri", 20),fg='white')
    studentname_entry.pack()
    studentid_lable = Label(register_screen, text="Student Id",bg='lightblue',font=("Calibri", 15))
    studentid_lable.pack()
    studentid_entry = Entry(register_screen, textvariable=studentid,bg='red',fg='white',font=("Calibri", 20))
    studentid_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=13, height=1, bg="blue", command=register_user).pack()

def retrive():

    global retrive_screen
    retrive_screen = Toplevel(main_screen)
    retrive_screen.title("retrive")
    retrive_screen.geometry("300x250")
    Label(retrive_screen, text="enter the student details",bg='blue',font=("Calibri", 15)).pack()
    Label(retrive_screen, text="").pack()
    global studentname_verify
    global studentid_verify
    studentname_verify = StringVar()
    studentid_verify = StringVar()
    global studentname_retrive_entry
    global studentid_retrive_entry
    Label(retrive_screen, text="student name",bg='lightblue',font=("Calibri", 15)).pack()
    studentname_retrive_entry = Entry(retrive_screen, textvariable=studentname_verify,bg='red',fg='white',font=("Calibri", 20))
    studentname_retrive_entry.pack()
    Label(retrive_screen, text="").pack()
    Label(retrive_screen, text="student id",bg='lightblue',font=("Calibri", 15)).pack()
    studentid_retrive_entry = Entry(retrive_screen, textvariable=studentid_verify,bg='red',fg='white',font=("Calibri", 20))
    studentid_retrive_entry.pack()
    Label(retrive_screen, text="").pack()
    Button(retrive_screen, text="Retrive", width=13, height=1, command=retrive_verify,bg='blue').pack()

def register_user():
    studentname_info = studentname.get()
    studentid_info = studentid.get()
    file = open('info.txt', "w")
    file.write(studentname_info+'\n')
    file.write(studentid_info)
    file.close()
    studentname_entry.delete(0, END)
    studentid_entry.delete(0, END)
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 15)).pack()
def retrive_verify():
    global studentid1
    studentname1 = studentname_verify.get()
    studentid1 = studentid_verify.get()
    studentname_retrive_entry.delete(0, END)
    studentid_retrive_entry.delete(0, END)
    file1 = open('info.txt', "r")
    verify = file1.read()
    print(verify)
    # verify1 = file1.read()
    # print(verify1)
    while verify !='':
            if verify == studentname1:
                # var1=file1.readline()
                var1 = file1.read()
                print(var1)
                break
            verify = file1.read()
def retrive_sucess():
    global retrive_success_screen
    retrive_success_screen = Toplevel(retrive_screen)
    retrive_success_screen.title("Success")
    retrive_success_screen.geometry("150x100")
    Label(retrive_success_screen, text="Retrive Success",bg='green',font=("Calibri", 15)).pack()

def studentid_not_recognised():
    global studentid_not_recog_screen
    studentid_not_recog_screen = Toplevel(retrive_screen)
    studentid_not_recog_screen.title("Success")
    studentid_not_recog_screen.geometry("150x100")
    Label(studentid_not_recog_screen, text="Invalid Student Id",bg='red').pack()

def student_user_not_found():
    global student_user_not_found_screen
    student_user_not_found_screen = Toplevel(retrive_screen)
    student_user_not_found_screen.title("Success")
    student_user_not_found_screen.geometry("150x100")
    Label(student_user_not_found_screen, text="student User Not Found",bg='red').pack()

#
def delete_retrive_success():
    retrive_success_screen

def delete_studentid_not_recognised():
    studentid_not_recog_screen

def delete_student_user_not_found_screen():
    student_user_not_found_screen


def main_account_screen():

    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("enter the Student details")
    Label(text="choose the register and retrive", bg="blue", width="300", height="2", font=("Calibri", 15)).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register,bg='darkblue',fg='red',font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Retrive", height="2", width="30", command=retrive,bg='darkblue',fg='red',font=("Calibri", 13)).pack()
    main_screen.mainloop()
main_account_screen()