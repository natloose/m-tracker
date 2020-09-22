from tkinter import ttk
from tkinter.ttk import Progressbar
import sqlite3
from tkinter import *
from tkcalendar import *
import pandas as pd


def create_database():
    # Create a database or connect to one
    conn = sqlite3.connect('meals.db')
    print("Connected to SQLite")
    # Create Cursor
    c = conn.cursor()
    # Create table
    c.execute("""CREATE TABLE IF NOT EXISTS meal (
        Food text,
        Protein int,
        Carbs int,
        Fats int,
        Total_Weight int
    )""")
    # Commit Changes
    conn.commit()
    # Close Connection (optional, will close anyway)
    conn.close()

create_database()


def daily_database():
    conn = sqlite3.connect('daily.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS day (
        Meal text,
        Protein real,
        Carbs real,
        Fats real,
        Total_Weight int,
        sqltime TEXT DEFAULT (strftime('%Y-%m-%d','now', 'localtime'))
    )""")
    conn.commit()
daily_database()


def macro_database():
    conn = sqlite3.connect('macro.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS target (
        Protein real,
        Carbs real,
        Fats,
        sqltime TEXT DEFAULT (strftime('%Y-%m-%d','now', 'localtime'))        
    )""")


def gather_data():
    global final_p
    global final_c
    global final_f
    macro_date = "2020-09-17"
    day = sqlite3.connect('macro.db')
    data = pd.read_sql_query("Select * from target", day)
    data_time = data[data['sqltime'] == macro_date]
    all_info = data_time.sum()
    macro_p = all_info['Protein']
    macro_c = all_info['Carbs']
    macro_f = all_info['Fats']
    final_p = float(prott.get()) / float(macro_p) * 100
    final_c = float(carbss.get()) / float(macro_c) * 100
    final_f = float(fatss.get()) / float(macro_f) * 100

macro_database()


def addNewMeal():
    top = Tk()
    top.geometry("420x325+675+350")
    top.title("Create")
    top.iconbitmap("C:/Users/Conor/OneDrive/Pictures/Camera Roll/pluss.ico")
    Label(top, text="     CREATE", font=("courier", 20)).grid(row=0, column=0)
    Label(top, text="MEAL", font=("courier", 20)).grid(row=0, column=1)

    # Create Entry Boxes

    four = Label(top)
    four.grid(row=2, column=1)

    item = StringVar()
    item = Entry(top, borderwidth="1")
    item.grid(row=3, column=1)

    protein = int()
    protein = Entry(top, borderwidth="1")
    protein.grid(row=4, column=1)

    carbs = int()
    carbs = Entry(top, borderwidth="1")
    carbs.grid(row=5, column=1)

    fats = int()
    fats = Entry(top, borderwidth="1")
    fats.grid(row=6, column=1)

    grams = int()
    grams = Entry(top, borderwidth="1")
    grams.grid(row=7, column=1)

    # Create text boxes
    item_text = Label(top, text="Food:", font=('calibri', 17, 'bold'))
    item_text.grid(row=3, column=0)

    protein_text = Label(top, text="Protein(g):", font=('calibri', 17, 'bold'))
    protein_text.grid(row=4, column=0)

    carb_text = Label(top, text="Carbs(g):", font=('calibri', 17, 'bold'))
    carb_text.grid(row=5, column=0)

    fats_text = Label(top, text="Fats(g):", font=('calibri', 17, 'bold'))
    fats_text.grid(row=6, column=0)

    gram_text = Label(top, text="Total Weight(g):", font=('calibri', 17, 'bold'))
    gram_text.grid(row=7, column=0)

    empty = Label(top)
    empty.grid(row=8, column=8)

    # Submit button
    def savedata():
        conn = sqlite3.connect('meals.db')
        c = conn.cursor()
        c.execute('INSERT INTO meal(Food,Protein,Carbs,Fats,Total_Weight) VALUES(?,?,?,?,?)',
                  (item.get(), protein.get(), carbs.get(), fats.get(), grams.get()))
        conn.commit()
        print("Saved.")

        successful = Label(top, text="Meal Saved!", fg="green")
        successful.grid(row=10, column=1)
        top.after(1000, lambda: top.destroy())

    submit_btn = Button(top, text="Add", fg="black", width=20, bg="#ebebe0", font=("times", 12), command=savedata)
    submit_btn.grid(row=9, column=1, pady=10, padx=10)


def success():
    # Create connection & Cursor
    global gram_amount

    daily = sqlite3.connect('daily.db')
    meals = sqlite3.connect('meals.db')
    m = meals.cursor()
    d = daily.cursor()
    # Read from DB

    click = value.get()
    alphanumeric = ""
    for character in click:
        if character.isalnum():
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

    itemadded = Label(left_frame, text="Great! Added", bg="#e0e0d1", fg="green")
    itemadded.pack()
    itemadded.after(1000, lambda: itemadded.destroy())


def set_macro():
    macro = Tk()
    macro.title("Macro Selector")
    macro.geometry("450x300+710+350")
    Label(macro, text="Here you can enter your dialy macro targets. \nPlease note all input is in grams (g)",
        font=("calibri", 10)).pack()
    Label(macro, text="", bg="#F0ECEC").pack()

    pro_lab = Label(macro, text="Protein", bg="#F0ECEC", font=("calibiri", 18))
    pro_lab.pack()
    pro = int()
    pro = Entry(macro, borderwidth="1")
    pro.pack()
    carb_lab = Label(macro, text="Carbs", bg="#F0ECEC", font=("calibiri", 18))
    carb_lab.pack()
    carb = int()
    carb = Entry(macro, borderwidth="1")
    carb.pack()
    fats_lab = Label(macro, text="Fats", bg="#F0ECEC", font=("calibiri", 18))
    fats_lab.pack()
    fats = int()
    fats = Entry(macro, borderwidth="1")
    fats.pack()
    Label(macro, text="", bg="#F0ECEC").pack()

    def savemacro():
        conn = sqlite3.connect('macro.db')
        c = conn.cursor()
        c.execute('INSERT INTO target(Protein,Carbs,Fats) VALUES (?,?,?)',
            (pro.get(), carb.get(), fats.get()))
        conn.commit()
        print("Saved.")

        successful = Label(macro, text="Meal Saved!", fg="green")
        successful.pack()
        macro.after(1000, lambda: macro.destroy())

    submit_entry = Button(macro, text="Submit", bg="white", command=savemacro)
    submit_entry.pack(padx=5, pady=10)


def item_list():
    conn = sqlite3.connect('meals.db')
    c = conn.cursor()
    items = c.execute("SELECT Food FROM meal")
    food_list = [it[0] for it in items.fetchall()]
    return food_list


def logout_user():
    root.destroy()
    print("Log out Successful.")


def home_page():

    global root
    global value
    global daily_date
    global left_frame
    global right_frame
    global success_refresh
    global sum_amount
    global gram_amount
    global item_added_text

    root = Tk()
    root.title("Macro Counter")
    root.iconbitmap("c:/users/Conor/OneDrive/Pictures/Camera Roll/food.ico")
    root.geometry("900x600+510+200")
    root.resizable(False, False)
    root.configure(bg="white")

    # Header
    header_frame = Frame(root, width=900, height=100, bg="yellow")
    header_frame.pack(side="top", fill="both")
    Label(header_frame, text="Macro Counter", font=("calibri", 21), bg="yellow").pack()

    # Set option frame
    left_frame = Frame(root, width=390, height=100, bg="#e0e0d1")
    left_frame.pack(side="left", fill="both")
    Label(left_frame, text="", bg="#e0e0d1").pack()
    Label(left_frame, text="", bg="#e0e0d1").pack()
    Label(left_frame, text="", bg="#e0e0d1").pack()
    Label(left_frame, text="Add", font=("calibri", 14), bg="#e0e0d1").pack()

    # Create Option List
    value = StringVar()
    i = item_list()
    optionbox = ttk.Combobox(left_frame, width=15, textvariable=value, font=("times", 12), foreground="black")
    optionbox['values'] = i
    optionbox.current(0)
    optionbox.pack(padx=10)
    Label(left_frame, text="Enter grams", font=("calibri", 12), bg="#e0e0d1").pack(pady=1, padx=1)
    gram_amount = Entry(left_frame, width=6)
    gram_amount.configure(bd=1.4, bg="white")
    gram_amount.pack(pady=5, padx=5)

    # Submit Food to Daily Database

    add_food_button = Button(left_frame, text="Submit", command=success, bg="#b3cccc", width=20, height=2)
    add_food_button.configure(font=("calibri", 11), borderwidth=2)
    Label(left_frame, text="", bg="#e0e0d1").pack()
    add_food_button.pack()
    Label(left_frame, text="", bg="#e0e0d1").pack()
    Label(left_frame, text="", bg="#e0e0d1").pack()

    # Create a new meal/food
    Label(left_frame, text="", bg="#e0e0d1").pack()
    Label(left_frame, text="New", font=("calibri", 14), bg="#e0e0d1").pack()

    create_food_button = Button(left_frame, text="Create Meal", bg="#b3cccc", command=addNewMeal, width=20, height=2)
    create_food_button.configure(font=("calibri", 11))
    create_food_button.pack(padx=10)
    Label(left_frame, text="Create a meal or individual food", bg="#e0e0d1").pack()
    Label(left_frame, text="", height=4, bg="#e0e0d1").pack()

    Button(left_frame, text="Update", command=set_macro).pack(padx=5, pady=5)
    Button(left_frame, text="Logout", bg="#E9E090", command=logout_user).pack()

    right_frame = Frame(root, width=510, height=200, bg="white")
    right_frame.pack(fill="both")

    Label(right_frame, text="Select View Date", bg="white").pack(padx=2, pady=5)

    global daily_date
    global ent
    ent = DateEntry(right_frame,
                    width=15,
                    date_pattern='mm/dd/y',
                    background="grey")
    ent.pack(pady=5, padx=5)

    frame_bottom = Frame(root, width=640, height=265, bg="white")
    frame_bottom.pack()

    frame_bottom_left = Frame(frame_bottom, width=210, height=265, bg="white")
    frame_bottom_left.pack(side="left")
    frame_bottom_right = Frame(frame_bottom, width=210, height=265, bg="white")
    frame_bottom_right.pack(side="right")
    frame_bottom_middle = Frame(frame_bottom, width=220, height=265, bg="white")
    frame_bottom_middle.pack(side="top")

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

        prott = StringVar()
        carbss = IntVar()
        fatss = IntVar()
        date = str(ent.get_date())

        daily = sqlite3.connect('daily.db')
        data = pd.read_sql_query("Select * from day", daily)
        data_time = data[data['sqltime'] == date]
        all_info = data_time.sum()
        p = all_info['Protein']
        c = all_info['Carbs']
        f = all_info['Fats']
        prott.set(p)
        carbss.set(c)
        fatss.set(f)
        protein_label = Label(frame_bottom_left, text="Protein(g)", bg="white")
        protein_label.pack(padx=10, pady=5)
        protein_day = Label(frame_bottom_left, textvariable=prott, bg="white", font=("TkDefaultFont", 8))
        protein_day.pack(padx=10, pady=5)
        carb_label = Label(frame_bottom_middle, text="Carbs(g)", bg="white")
        carb_label.pack(padx=10, pady=5)
        carbs_day = Label(frame_bottom_middle, textvariable=carbss, bg="white", font=("TkDefaultFont", 8))
        carbs_day.pack(padx=10, pady=5)
        fats_label = Label(frame_bottom_right, text="Fats(g)", bg="white")
        fats_label.pack(padx=10, pady=5)
        fats_day = Label(frame_bottom_right, textvariable=fatss, bg="white", font=("TkDefaultFont", 8))
        fats_day.pack(padx=10, pady=5)
        gather_data()

        p_progress = Progressbar(frame_bottom_left, mode='determinate', length=200, value=final_p)
        p_progress.pack(padx=5, pady=5)
        c_progress = Progressbar(frame_bottom_middle, mode='determinate', length=200, value=final_c)
        c_progress.pack(padx=5, pady=5)
        f_progress = Progressbar(frame_bottom_right, mode='determinate', length=200, value=final_f)
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

    sbt_button_date = Button(right_frame, text="Submit", command=refresh)
    sbt_button_date.pack(padx=5, pady=5)

    Label(right_frame, text="Daily Information", bg="white", font=("calibri", 20, "underline")).pack(pady=10, padx=10)
    Label(right_frame, text="", bg="white").pack()

    display_daily_macros()

    root.mainloop()
    root.mainloop()
home_page()