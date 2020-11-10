import os
import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from MacroTracker import sql_data
from tkinter.ttk import Progressbar


class Welcome:
    def __init__(self, master):
        # Create Login/Register window
        self.login = master
        self.login.geometry("250x300+850+350")
        self.login.title("Account Login")
        self.login.configure(bg="white")
        self.login.iconbitmap("c:/users/Conor/OneDrive/Pictures/Camera Roll/food.ico")

        # Form Login/Register Label
        tk.Label(text="", height="1", bg="white").pack()
        tk.Label(text="Login or Register", bg="white", width=200, height="2", font=("Calibri", 13), fg="black").pack()
        tk.Label(text="", height="2", bg="white").pack()

        # Click to Login Button
        tk.Button(text="Login", height="2", width="30", bg="lightgreen", command=login_screen).pack()
        tk.Label(text="", bg="white").pack()

        # Click to Register Button
        tk.Button(text="Register", height="2", width="30", bg="#EBEB28", command=register_screen).pack()


def register_screen():
    # Create register window
    reg_screen = tk.Tk()
    reg_screen.geometry("300x290+830+420")
    reg_screen.title("Register")
    reg_screen.configure(bg="white")
    reg_screen.iconbitmap("c:/users/Conor/OneDrive/Pictures/Camera Roll/food.ico")

    # User instructions
    tk.Label(reg_screen, text="", bg="white").pack()
    tk.Label(reg_screen, text="Register", bg="white", height="1", font=("Calibri", 19), fg="black").pack()
    tk.Label(reg_screen, text="", bg="white").pack()

    # Username Label
    user_label = tk.Label(reg_screen, text="Username", font=("Calibri", 13), bg="white")
    user_label.pack()

    # Username Entry
    username = tk.Entry(reg_screen, width=30, bg="#e6f2ff")
    username.pack()

    # Password Label
    password_label = tk.Label(reg_screen, text="Password", font=("Calibri", 13), bg="white")
    password_label.pack()

    # Password Entry
    password = tk.Entry(reg_screen, show="*", width=30, bg="#e6f2ff")
    password.pack()

    tk.Label(reg_screen, text="", bg="white", height=1).pack()

    def register_user_onto_file():

        # Adds user to current user files
        file = open("Users/" + username.get(), "w")
        file.write(username.get())
        file.write("\n")
        file.write(password.get())
        file.close()
        print("User " + username.get() + " created.")

        # Show succes message upon complete registration then destroys register window
        tk.Label(reg_screen, text="Registration Success!", fg="green", font=("calibri", 11)).pack()
        reg_screen.after(1200, lambda: reg_screen.destroy())

    tk.Button(reg_screen, text="Register", width=15, height=2, font=("Calibri", 13), bg="white",
              command=register_user_onto_file).pack()


def login_screen():
    # Create login screen
    login_user = tk.Tk()
    login_user.title("Login")
    login_user.geometry("300x290+830+420")
    login_user.configure(bg="white")
    login_user.iconbitmap("c:/users/Conor/OneDrive/Pictures/Camera Roll/food.ico")

    tk.Label(login_user, text="", bg="white").pack()
    tk.Label(login_user, text="Login", bg="white", font=("Calibri", 19)).pack()
    tk.Label(login_user, text="", bg="white").pack()

    # Username Label
    user_label = tk.Label(login_user, text="Username", font=("Calibri", 13), bg="white")
    user_label.pack()

    # Username Entry
    username_login = tk.Entry(login_user, width=30, bg="#e6f2ff")
    username_login.pack()

    # Password Label
    password_label = tk.Label(login_user, text="Password", font=("Calibri", 13), bg="white")
    password_label.pack()

    # Password Entry
    password_login = tk.Entry(login_user, show="*", width=30, bg="#e6f2ff")
    password_login.pack()

    tk.Label(login_user, text="", bg="white", height=1).pack()

    def check_user_credentials():

        # check to see if user and pass match ones on file
        username_entry = username_login.get()
        password_entry = password_login.get()
        print(username_entry)
        print(password_entry)

        path = "C:/Users/Conor/PCNew/ctimprovements/MacroTracker/users"
        list_of_names = os.listdir(path)
        if username_entry in list_of_names:

            file = open("users/" + username_entry, "r")
            if password_entry in file:
                print("User Authenticated")
                tk.Label(login_user, text="Success!", fg="green").pack()
                login_user.destroy()
                main_screen()

            else:
                tk.Label(login_user, text="Incorrect username or password", bg="white").pack()
                password_login.delete(0, tk.END)
        else:
            print("Incorrect Username or Password")
            tk.Label(login_user, text="Incorrect Username or Password").pack()

    # Login Button
    tk.Button(login_user, text="Login", bg="white", width=15, font=("Calibri", 13), height=2,
              command=check_user_credentials).pack()


def main_screen():

    global ent
    global value
    global left_frame
    global right_frame
    global daily_date
    global gram_amount
    global frame_bottom_left
    global frame_bottom_middle
    global frame_bottom_right

    main = tk.Tk()
    main.title("Macro Counter")
    main.iconbitmap("c:/users/Conor/OneDrive/Pictures/Camera Roll/food.ico")
    main.geometry("900x600+510+200")
    main.resizable(False, False)
    main.configure(bg="white")

    # Header
    header_frame = tk.Frame(main, width=900, height=100, bg="yellow")
    header_frame.pack(side="top", fill="both")
    tk.Label(header_frame, text="Macro Counter", font=("calibri", 21), bg="yellow").pack()

    # Set option frame
    left_frame = tk.Frame(main, width=390, height=100, bg="#e0e0d1")
    left_frame.pack(side="left", fill="both")
    tk.Label(left_frame, text="", bg="#e0e0d1").pack()
    tk.Label(left_frame, text="", bg="#e0e0d1").pack()
    tk.Label(left_frame, text="", bg="#e0e0d1").pack()
    tk.Label(left_frame, text="Add", font=("calibri", 14), bg="#e0e0d1").pack()

    # Create Option List
    value = tk.StringVar()
    i = sql_data.item_list()
    optionbox = tk.ttk.Combobox(left_frame, width=15, textvariable=value, font=("times", 12), foreground="black")
    optionbox['values'] = i
    optionbox.current(None)
    optionbox.pack(padx=10)
    tk.Label(left_frame, text="Enter grams", font=("calibri", 12), bg="#e0e0d1").pack(pady=1, padx=1)
    gram_amount = tk.Entry(left_frame, width=6)
    gram_amount.configure(bd=1.4, bg="white")
    gram_amount.pack(pady=5, padx=5)

    # Submit Food to Daily Database

    add_food_button = tk.Button(left_frame, text="Submit", command=success, bg="#b3cccc", width=20, height=2)
    add_food_button.configure(font=("calibri", 11), borderwidth=2)
    tk.Label(left_frame, text="", bg="#e0e0d1").pack()
    add_food_button.pack()
    tk.Label(left_frame, text="", bg="#e0e0d1").pack()
    tk.Label(left_frame, text="", bg="#e0e0d1").pack()

    # Create a new meal/food
    tk.Label(left_frame, text="", bg="#e0e0d1").pack()
    tk.Label(left_frame, text="New", font=("calibri", 14), bg="#e0e0d1").pack()

    create_food_button = tk.Button(left_frame, text="Create Meal", bg="#b3cccc",
                                   command=add_new_meal, width=20, height=2)
    create_food_button.configure(font=("calibri", 11))
    create_food_button.pack(padx=10)
    tk.Label(left_frame, text="Create a meal or individual food", bg="#e0e0d1").pack()
    tk.Label(left_frame, text="", height=4, bg="#e0e0d1").pack()

    def logout_user():
        main.destroy()
        print("Log out Successful.")

    tk.Button(left_frame, text="Update", command=set_macro).pack(padx=5, pady=5)
    tk.Button(left_frame, text="Logout", bg="#E9E090", command=logout_user).pack()

    right_frame = tk.Frame(main, width=510, height=200, bg="white")
    right_frame.pack(fill="both")

    tk.Label(right_frame, text="Select View Date", bg="white").pack(padx=2, pady=5)

    ent = DateEntry(right_frame,
                        width=15,
                        date_pattern='mm/dd/y',
                        background="grey")

    ent.pack(pady=5, padx=5)

    frame_bottom = tk.Frame(main, width=640, height=265, bg="white")
    frame_bottom.pack()

    frame_bottom_left = tk.Frame(frame_bottom, width=210, height=265, bg="white")
    frame_bottom_left.pack(side="left")
    frame_bottom_right = tk.Frame(frame_bottom, width=210, height=265, bg="white")
    frame_bottom_right.pack(side="right")
    frame_bottom_middle = tk.Frame(frame_bottom, width=220, height=265, bg="white")
    frame_bottom_middle.pack(side="top")

    display_daily_macros()


def success():
    # Create connection & Cursor

    daily = sqlite3.connect('database/daily.db')
    meals = sqlite3.connect('database/meals.db')
    m = meals.cursor()
    d = daily.cursor()
    # Read from DB

    click = value.get()
    alphanumeric = ""
    for character in click:
        if character.isalnum() or " ":
            alphanumeric += character
    m.execute("SELECT * FROM meal WHERE Food = ?", (alphanumeric,))
    all_data = m.fetchall()

    def strip():

        for data in all_data:
            n = data[0]
            p = data[1]/data[4]*int(gram_amount.get())
            c = data[2]/data[4]*int(gram_amount.get())
            f = data[3]/data[4]*int(gram_amount.get())
            t = data[4]/data[4]*int(gram_amount.get())
            date = list((n, p, c, f, t))
            print(date)
            return date

    d.execute("INSERT INTO day (Meal,Protein,Carbs,Fats,Total_Weight) VALUES (?,?,?,?,?)", (strip()),)
    daily.commit()
    print("Meal added to daily.")

    itemadded = tk.Label(left_frame, text="Great! Added", bg="#e0e0d1", fg="green")
    itemadded.pack()
    itemadded.after(1000, lambda: itemadded.destroy())


def set_macro():
    global pro
    global fats
    global carb
    global macro

    macro = tk.Tk()
    macro.title("Macro Selector")
    macro.geometry("450x300+710+350")
    tk.Label(macro, text="Here you can enter your dialy macro targets. \nPlease note all input is in grams (g)",
                font=("calibri", 10)).pack()
    tk.Label(macro, text="", bg="#F0ECEC").pack()

    pro_lab = tk.Label(macro, text="Protein", bg="#F0ECEC", font=("calibiri", 18))
    pro_lab.pack()
    pro = int()
    pro = tk.Entry(macro, borderwidth="1")
    pro.pack()
    carb_lab = tk.Label(macro, text="Carbs", bg="#F0ECEC", font=("calibiri", 18))
    carb_lab.pack()
    carb = int()
    carb = tk.Entry(macro, borderwidth="1")
    carb.pack()
    fats_lab = tk.Label(macro, text="Fats", bg="#F0ECEC", font=("calibiri", 18))
    fats_lab.pack()
    fats = int()
    fats = tk.Entry(macro, borderwidth="1")
    fats.pack()
    tk.Label(macro, text="", bg="#F0ECEC").pack()

    submit_entry = tk.Button(macro, text="Submit", bg="white", command=savemacro)
    submit_entry.pack(padx=5, pady=10)


def savemacro():
    conn = sqlite3.connect('database/macro.db')
    c = conn.cursor()
    c.execute('INSERT INTO target(Protein,Carbs,Fats) VALUES (?,?,?)',
                  (pro.get(), carb.get(), fats.get()))
    conn.commit()
    print("Saved.")

    successful = tk.Label(macro, text="Meal Saved!", fg="green")
    successful.pack()
    macro.after(1000, lambda: macro.destroy())


def add_new_meal():
    top = tk.Tk()
    top.geometry("420x325+675+350")
    top.title("Create")
    top.iconbitmap("C:/Users/Conor/OneDrive/Pictures/Camera Roll/pluss.ico")
    tk.Label(top, text="     CREATE", font=("courier", 20)).grid(row=0, column=0)
    tk.Label(top, text="MEAL", font=("courier", 20)).grid(row=0, column=1)

    # Create Entry Boxes

    four = tk.Label(top)
    four.grid(row=2, column=1)

    item = tk.StringVar()
    item = tk.Entry(top, borderwidth="1")
    item.grid(row=3, column=1)

    protein = int()
    protein = tk.Entry(top, borderwidth="1")
    protein.grid(row=4, column=1)

    carbs = int()
    carbs = tk.Entry(top, borderwidth="1")
    carbs.grid(row=5, column=1)

    fats = int()
    fats = tk.Entry(top, borderwidth="1")
    fats.grid(row=6, column=1)

    grams = int()
    grams = tk.Entry(top, borderwidth="1")
    grams.grid(row=7, column=1)

    # Create text boxes
    item_text = tk.Label(top, text="Food:", font=('calibri', 17, 'bold'))
    item_text.grid(row=3, column=0)

    protein_text = tk.Label(top, text="Protein(g):", font=('calibri', 17, 'bold'))
    protein_text.grid(row=4, column=0)

    carb_text = tk.Label(top, text="Carbs(g):", font=('calibri', 17, 'bold'))
    carb_text.grid(row=5, column=0)

    fats_text = tk.Label(top, text="Fats(g):", font=('calibri', 17, 'bold'))
    fats_text.grid(row=6, column=0)

    gram_text = tk.Label(top, text="Total Weight(g):", font=('calibri', 17, 'bold'))
    gram_text.grid(row=7, column=0)

    empty = tk.Label(top)
    empty.grid(row=8, column=8)

    # Submit button
    def savedata():
        conn = sqlite3.connect('database/meals.db')
        c = conn.cursor()
        c.execute('INSERT INTO meal(Food,Protein,Carbs,Fats,Total_Weight) VALUES(?,?,?,?,?)',
                  (item.get(), protein.get(), carbs.get(), fats.get(), grams.get()))
        conn.commit()
        print("Saved.")

        successful = tk.Label(top, text="Meal Saved!", fg="green")
        successful.grid(row=10, column=1)
        top.after(1000, lambda: top.destroy())

    submit_btn = tk.Button(top, text="Add", fg="black", width=20, bg="#ebebe0", font=("times", 12), command=savedata)
    submit_btn.grid(row=9, column=1, pady=10, padx=10)


# Print daily carbs to right_frame
def display_daily_macros():
    global get_daily_date
    global protein_day
    global carbs_day
    global fats_day
    global protein_label
    global fats_label
    global carb_label
    global p_progress
    global c_progress
    global f_progress
    global prott
    global carbss
    global fatss

    prott = tk.StringVar()
    carbss = tk.IntVar()
    fatss = tk.IntVar()
    date = str(ent.get_date())

    daily = sqlite3.connect('database/daily.db')
    data = pd.read_sql_query("Select * from day", daily)
    data_time = data[data['sqltime'] == date]
    all_info = data_time.sum()
    p = all_info['Protein']
    c = all_info['Carbs']
    f = all_info['Fats']
    prott.set(p)
    carbss.set(c)
    fatss.set(f)
    protein_label = tk.Label(frame_bottom_left, text="Protein(g)", bg="white")
    protein_label.pack(padx=10, pady=5)
    protein_day = tk.Label(frame_bottom_left, textvariable=prott, bg="white", font=("TkDefaultFont", 8))
    protein_day.pack(padx=10, pady=5)
    carb_label = tk.Label(frame_bottom_middle, text="Carbs(g)", bg="white")
    carb_label.pack(padx=10, pady=5)
    carbs_day = tk.Label(frame_bottom_middle, textvariable=carbss, bg="white", font=("TkDefaultFont", 8))
    carbs_day.pack(padx=10, pady=5)
    fats_label = tk.Label(frame_bottom_right, text="Fats(g)", bg="white")
    fats_label.pack(padx=10, pady=5)
    fats_day = tk.Label(frame_bottom_right, textvariable=fatss, bg="white", font=("TkDefaultFont", 8))
    fats_day.pack(padx=10, pady=5)

    # call function to recieve daily macro data
    gather_data()

    p_progress = Progressbar(frame_bottom_left, mode='determinate', length=200, value="10")
    p_progress.pack(padx=5, pady=5)
    c_progress = Progressbar(frame_bottom_middle, mode='determinate', length=200, value="15")
    c_progress.pack(padx=5, pady=5)
    f_progress = Progressbar(frame_bottom_right, mode='determinate', length=200, value="10")
    f_progress.pack(padx=5, pady=5)

    def refresh():
        protein_label.destroy()
        protein_day.destroy()
        carb_label.destroy()
        carbs_day.destroy()
        fats_label.destroy()
        fats_day.destroy()
        p_progress.destroy()
        c_progress.destroy()
        f_progress.destroy()
        display_daily_macros()

    sbt_button_date = tk.Button(right_frame, text="Submit", command=refresh)
    sbt_button_date.pack(padx=5, pady=5)

    tk.Label(right_frame, text="Daily Information", bg="white", font=("calibri", 20, "underline")).pack(pady=10,
                                                                                                         padx=10)
    tk.Label(right_frame, text="", bg="white").pack()


def gather_data():
    global final_p
    global final_c
    global final_f

    if prott and carbss and fatss != 0:
        day = sqlite3.connect('database/macro.db')
        data = pd.read_sql_query("Select * from target", day)
        macro_date = data['sqltime'].max()
        data_time = data[data['sqltime'] == macro_date]
        all_info = data_time.sum()
        macro_p = all_info['Protein']
        macro_c = all_info['Carbs']
        macro_f = all_info['Fats']
        final_p = float(prott.get()) / float(macro_p) * 100
        final_c = float(carbss.get()) / float(macro_c) * 100
        final_f = float(fatss.get()) / float(macro_f) * 100
    else:
        pass


if __name__ == "__main__":
    root = tk.Tk()
    h = Welcome(root)
    root.mainloop()
