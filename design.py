from tkinter import *
import os
from home import *


def login_register_screen():

    global login

    login = Tk()
    login.geometry("250x300+850+350")
    login.title("Account Login")
    login.configure(bg="white")
    login.iconbitmap("c:/users/Conor/OneDrive/Pictures/Camera Roll/food.ico")

    # Form Label
    Label(text="", height="1", bg="white").pack()
    Label(text="Login or Register", bg="white", width=200, height="2", font=("Calibri", 13), fg="black").pack()
    Label(text="", height="2", bg="white").pack()

    # Login Button
    Button(text="Login", height="2", width="30", bg="lightgreen", command=login_screen).pack()
    Label(text="", height="2", bg="white").pack()

    # Register Button
    # Register Button
    Button(text="Register", height="2", width="30", bg="#EBEB28", command=register_screen).pack()

    login.mainloop()


def register_screen():

    reg_screen = Tk()
    reg_screen.geometry("300x290+830+420")
    reg_screen.title("Register")
    reg_screen.configure(bg="white")
    reg_screen.iconbitmap("c:/users/Conor/OneDrive/Pictures/Camera Roll/food.ico")

    # User instructions
    Label(reg_screen, text="", bg="white").pack()
    Label(reg_screen, text="Register", bg="white", height="1", font=("verdana", 19)).pack()
    Label(reg_screen, text="", bg="white").pack()

    # Username Label
    user_label = Label(reg_screen, text="Username", font=("Times", 13), bg="white")
    user_label.pack()

    # Username Entry
    username = Entry(reg_screen, width=30, bg="#e6f2ff")
    username.pack()

    # Password Label
    password_label = Label(reg_screen, text="Password", font=("Times", 13), bg="white")
    password_label.pack()

    # Password Entry
    password = Entry(reg_screen, show="*", width=30, bg="#e6f2ff")
    password.pack()

    Label(reg_screen, text="", bg="white", height=1).pack()

    def register_user_onto_file():
        file = open("Usernames/" + username.get(), "w")
        file.write(username.get())
        file.write("\n")
        file.write(password.get())
        file.close()
        print("User " + username.get() + " created.")

        Label(reg_screen, text="Registration Success!", fg="green", font=("calibri", 11)).pack()
        reg_screen.after(1200, lambda: reg_screen.destroy())

    Button(reg_screen, text="Register", width=20, height=2, bg="white", command=register_user_onto_file).pack()


def login_screen():

    login_user = Tk()
    login_user.title("Login")
    login_user.geometry("300x290+830+420")
    login_user.configure(bg="white")
    login_user.iconbitmap("c:/users/Conor/OneDrive/Pictures/Camera Roll/food.ico")

    Label(login_user, text="", bg="white").pack()
    Label(login_user, text="Login", bg="white", font=("verdana", 19)).pack()
    Label(login_user, text="", bg="white").pack()

    user_label = Label(login_user, text="Username", font=("Times", 13), bg="white")
    user_label.pack()

    # Username Entry
    username_login = Entry(login_user, width=30, bg="#e6f2ff")
    username_login.pack()

    # Password Label
    password_label = Label(login_user, text="Password", font=("Times", 13), bg="white")
    password_label.pack()

    # Password Entry
    password_login = Entry(login_user, show="*", width=30, bg="#e6f2ff")
    password_login.pack()

    Label(login_user, text="", bg="white", height=1).pack()

    def check_user_credentials():
        username_entry = username_login.get()
        password_entry = password_login.get()
        print(username_entry)
        print(password_entry)

        path = "C:/Users/Conor/PycharmProjects/CalorieTracker/Usernames"
        list_of_names = os.listdir(path)
        if username_entry in list_of_names:

            file = open("Usernames/" + username_entry, "r")
            if password_entry in file:
                print("User Authenticated")
                Label(login_user, text="Success!", fg="green").pack()
                login.destroy()
                login_user.destroy()
                home_page()

            else:
                Label(login_user, text="Incorrect username or password", bg="white").pack()
                password_login.delete(0, END)
        else:
            print("Incorrect Username or Password")
            Label(login_user, text="Incorrect Username or Password").pack()

    # Login Button
    Button(login_user, text="Login", bg="white", width=20, height=2, command=check_user_credentials).pack()

    login_user.mainloop()

login_register_screen()