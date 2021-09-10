"""
    This program is made by Gabro
    you can visit my YT channel https://www.youtube.com/channel/UCkGvbGqYzDi3lfgtbQ_pngg
    for more info or to make questions about.

    This code take a .csv file inside where there are
    time value for each break points of the day.
    In particular, I made 4 break points:

        -entry --> time at what the employee start to work
        -half --> time at what employee have launch
        -back --> time at what employee returns to work
        -exit --> time at what employee end to work

    Things you have to edit to run the program:
        -line 638
        -line 564
        -line 693 to 702

    NOTE:
        If you are interested into my program I can edit it
        and make it as you want for your purpose.
        I can acquire data:
            -via webcam or scanner using a QR code
            -card reader
            -whatever you want
        email me --> gabriaquila729@gmail.com
"""


# Install these package via pip no more file needed

# Libraries fot plotting and manipulating data
import matplotlib
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Time Libraries
from datetime import date
from datetime import datetime

# Graphics Libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk, Toplevel, messagebox, filedialog
from ttkthemes import ThemedStyle
from tkinter.ttk import *

# Other support libraries
from os import *
import os
from distutils.dir_util import copy_tree


# These are project variables, useful to work with .csv file
cols = ['entry', 'half', 'back', 'exit']
Cols = ['entry', 'half', 'back', 'exit', 'free']
my_col = {"entry": 0, "half": 1, "back": 2, "exit": 3, "free": 4}
employees = ["One", "Two", "Three", "Four"]
months_days = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31,
               "June": 30, "July": 31, "August": 31, "September": 30, "October": 31,
               "November": 30, "December": 31}
months_num = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
months_num_dict = {"January": '01', "February": '02', "March": '03', "April": '04', "May": '05',
                   "June": '06', "July": '07', "August": '08', "September": '09', "October": '10',
                   "November": '11', "December": '12'}
sort_months = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5,
               "June": 6, "July": 7, "August": 8, "September": 9, "October": 10,
               "November": 11, "December": 12}
my_themes = ["arc", "blue", "alt", "classic", "clam", "yaru", "aquativo", "clearlooks", "winxpblue"]
my_themes.sort()

# Set the App icon (The image must be .ico file)
icon = "icon.ico"

# Employees list

my_emplo = ["One", "Two", "Three", "Four"]

# Set password

my_pass = "1234"


# Some global variables let functions comunicate between them
# This is easy way, instead of making a class

global main_window
global label_graph
global dot
global count
global data_view
global lines
global mod_values
global my_input
global my_input_1
global emplo
global liness
global gg
global pass_text
global check_text
global var
global pass_try
global emplo_selection
global style_selection
global my_style


# Things to do at start
def on_start():
    """To do at start"""
    backup()
    clear_csv()
    global my_style
    my_style = "clearlooks"


def menu_option():
    """Insert a menu in the main window"""
    global main_window

    menubar = Menu(main_window)
    filemenu = Menu(menubar, tearoff=0, font=("Lucinda Console", 10))
    filemenu.add_command(label="Open...", command=open_file)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=main_window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    optionmenu = Menu(menubar, tearoff=0, font=("Lucinda Console", 10))
    optionmenu.add_command(label="Style", command=change_style_box)
    menubar.add_cascade(label="Options", menu=optionmenu)

    helpmenu = Menu(menubar, tearoff=0, font=("Lucinda Console", 10))
    helpmenu.add_command(label="Contact me", command=contact_me)
    helpmenu.add_separator()
    helpmenu.add_command(label="About...", command=info_app)
    menubar.add_cascade(label="Help", menu=helpmenu)

    main_window.config(menu=menubar)


def change_style_box():
    """Change the stile of the main window"""
    global my_style
    global style_selection

    style_window: Toplevel = Toplevel()
    style_window.geometry("450x100")
    style_window.pack_propagate(False)
    style_window.resizable(0, 0)
    style_window.iconbitmap(icon)

    label_stile = Label(style_window, text="Select a theme", font=("Lucinda Console", 15),
                        foreground="black").pack(pady=20, padx=20)

    style_selection = ttk.Combobox(style_window, values=my_themes,
                                   font=("Helvetica", 15),
                                   foreground="black", state="readonly")
    style_selection.pack()
    style_selection.bind("<<ComboboxSelected>>", change_style)
    style_selection.current(0)


def change_style(styl_sel):
    """Effective change the theme"""
    global my_style
    my_style = style_selection.get()
    stile = ThemedStyle(main_window)
    stile.theme_use(my_style)


def contact_me():
    """Show the email address of the producer"""

    contact_window: Toplevel = Toplevel()
    contact_window.geometry("300x100")
    contact_window.pack_propagate(False)
    contact_window.resizable(0, 0)
    contact_window.title = "Mail contact"
    contact_window.iconbitmap(icon)
    stile_5 = ThemedStyle(contact_window)
    stile_5.theme_use(my_style)

    label_contact = Text(contact_window, height=3, font=("Spectral", 15))
    label_contact.insert(1.0,
                         "    You can contact the producer\n"
                         "                           at:\n          gabri729@gmail.com")
    label_contact.pack()
    label_contact.configure(state="disabled")


def info_app():
    """Terms and conditions"""

    terms_window: Toplevel = Toplevel()
    terms_window.geometry("720x140")
    terms_window.pack_propagate(False)
    terms_window.resizable(0, 0)
    terms_window.title = "Info App"
    terms_window.iconbitmap(icon)
    stile_6 = ThemedStyle(terms_window)
    stile_6.theme_use(my_style)

    info_label = Label(terms_window,
                       text="This program is made by Gabro for personal use.\n"
                            "If you want to use this App for business usage\n"
                            "please contact me at --> see HELP MENU",
                       font=("Spectral", 15),
                       foreground="black")

    info_label.pack(pady=20)


def check_dipe(dip):
    """See what is selected in the ComboBox"""

    if emplo_selection.get() == "":
        messagebox.showerror("Attention", "Empty selection")
    elif emplo_selection.get() != "" and dip == "mod" and emplo_selection.get() in employees:
        pop_pass()
    elif emplo_selection.get() != "" and dip == "histo" and emplo_selection.get() in employees:
        plot()
    else:
        messagebox.showerror("Attention", "Select something before go")


def read_CSV(employ):
    """ Read the .csv file by use the name of the employees
        and the current month
    """

    giorno, mese, anno = scandata()
    df = pd.read_csv(f'{employ}_{mese}.csv')
    return df


def media(dataf):
    """Return the average of all time value base on selected column"""
    mytuple = []
    for col in cols:
        mytuple.append(dataf[col].mean())
    return mytuple


def pop_pass():
    """Insert password"""

    global pass_text
    global var
    global pass_try

    pass_window: Toplevel = Toplevel()
    pass_window.geometry("280x280")
    pass_window.pack_propagate(False)
    pass_window.resizable(0, 0)
    pass_window.title = "Security check"
    pass_window.iconbitmap(icon)
    stile_4 = ThemedStyle(pass_window)
    stile_4.theme_use(my_style)

    passw = Label(pass_window, text="Insert the password\nbefore edit",
                  font=("Lucida Console", 15), foreground="black", relief="flat")
    passw.place(relx=0.03, rely=0.2)

    var = IntVar()
    show_pass = tk.Checkbutton(pass_window, text="Show", variable=var, onvalue=1, offvalue=0,
                               command=show_password, font=("Lucida Console", 17), relief="raised")
    show_pass.place(relx=0.55, rely=0.74)

    pass_text = StringVar()
    pass_try = Entry(pass_window, text=pass_text, font=("Lucida Console", 15), show='*')
    pass_try.place(relx=0.06, rely=0.6)

    button_conferma = tk.Button(pass_window, text='OK', fg="black", relief="raised",
                                command=pass_check, activebackground="light gray", font=("Lucida Console", 15))
    button_conferma.place(relx=0.12, rely=0.74)


def pass_check():
    """Check the typed password"""

    global pass_text
    global check_text

    if pass_text.get() == my_pass:
        stop()
        mod_entries()
    elif pass_text.get() == "":
        messagebox.showerror("Attention", "Type something!")
    else:
        messagebox.showerror("Attention", "Wrong password")


def show_password():
    """Show or hide the password"""

    global var

    if var.get() == 1:
        pass_try.config(show='')
    elif var.get() == 0:
        pass_try.config(show='*')


def mod_entries():
    """Edit values in a specific day"""

    global my_input_1
    global my_input
    global lines
    global liness
    global mod_values

    edit_window: Toplevel = Toplevel()
    edit_window.geometry("540x540")
    edit_window.pack_propagate(False)
    edit_window.resizable(0, 0)
    edit_window.title = "Edit values"
    edit_window.iconbitmap(icon)
    stile_3 = ThemedStyle(edit_window)
    stile_3.theme_use(my_style)

    title = Label(edit_window, text="Edit values\nof a specific day\nof a selected employee",
                  font=("Lucida Console", 15), foreground="black", relief="raised")
    title.place(relx=0.15, rely=0.05)

    definizioni = Label(edit_window, text="Write the date\nexample\n24/05/2021",
                        font=("Lucida Console", 15), foreground="black", relief="raised")
    definizioni.place(relx=0.015, rely=0.25)

    liness = StringVar()
    my_input_1 = Entry(edit_window, text=liness, font=("Lucida Console", 15))
    my_input_1.place(relx=0.64, rely=0.31, width=150)

    definizioni_2 = Label(edit_window, text="Write the column value\nthen ',' and then the time"
                                            "\nexample:\nentry,7.43 or exit,20.03",
                          font=("Lucida Console", 15), foreground="black", relief="raised")
    definizioni_2.place(relx=0.015, rely=0.45)

    lines = StringVar()
    my_input = Entry(edit_window, text=lines, font=("Lucida Console", 18))
    my_input.place(relx=0.25, rely=0.65)

    mod_values = []
    button_ok = tk.Button(edit_window, text='OK', fg="black", relief="raised", command=queque_prev,
                          activebackground="light gray", font=("Lucida Console", 15))
    button_ok.place(relx=0.29, rely=0.75)

    button_canc = tk.Button(edit_window, text='Canc', fg="black", relief="raised",
                            command=clear_my_input,
                            activebackground="light gray", font=("Lucida Console", 15))
    button_canc.place(relx=0.55, rely=0.75)

    button_fatto = tk.Button(edit_window, text='Done', fg="black", relief="raised", command=mod_csv,
                             activebackground="light gray", font=("Lucida Console", 15))
    button_fatto.place(relx=0.43, rely=0.93)

    button_undo = tk.Button(edit_window, text='Undo', fg="black", relief="raised",
                            command=undo, activebackground="light gray", font=("Lucida Console", 15))
    button_undo.place(relx=0.58, rely=0.93)


def queque():
    """Verify if the inserted string is formatted"""

    global mod_values

    entry = my_input.get()

    entry_v = entry.split(",")

    if entry_v[0] not in Cols or len(entry_v) == 0:
        messagebox.showerror("Attention", "Writing error!")
    elif entry_v[0] in Cols and len(entry_v) != 0:
        try:
            orario = float(entry_v[1])
            if len(mod_values) == 0:
                mod_values.append(entry_v[0] + "," + str(orario))
            elif (entry_v[0] + "," + str(orario)) in mod_values:
                pass
            else:
                mod_values.append(entry_v[0] + "," + str(orario))
        except ValueError:
            messagebox.showerror("Attention", "Writing error!")
    elif entry_v[0] in Cols and len(entry_v) != 0 and type(entry_v[1]) == int:
        orario = int(entry_v[1])
        if len(mod_values) == 0:
            mod_values.append(entry_v[0] + "," + str(orario))
        elif (entry_v[0] + "," + str(orario)) in mod_values:
            pass
        else:
            mod_values.append(entry_v[0] + "," + str(orario))


def queque_prev():
    """Another function to verify if the string is formatted"""

    global gg

    oggi, mese, anno = scandata()
    entry_prev = my_input_1.get()

    entry_prev_data = entry_prev.split("/")

    if len(entry_prev_data) < 3 or entry_prev_data[1] not in months_num or entry_prev_data[1] != months_num_dict[mese] or \
            entry_prev_data[2] != str(anno):
        messagebox.showerror("Attention", "Wrong date format!")
    elif entry_prev_data[1] in months_num and len(entry_prev_data) == 3 and entry_prev_data[1] == months_num_dict[mese] and \
            entry_prev_data[2] == str(anno):
        try:
            gg = float(entry_prev_data[0])
            queque()
        except ValueError:
            messagebox.showerror("Attention", "Wrong date format!")


def mod_csv():
    """Edit and update the csv"""

    global gg
    global emplo_selection

    df = read_CSV(emplo_selection.get())
    giorno, mese, anno = scandata()

    for v in mod_values:
        col = ""
        value = ""
        for letter in v:
            if str(letter) == ",":
                pass
            elif str(letter).isalpha():
                col += letter
            elif str(letter).isnumeric() or str(letter) == ".":
                value += letter
        df.iat[int(gg) - 1, my_col[col]] = value
        df.to_csv(f'{emplo_selection.get()}_{mese}.csv', index=False)

    stop()
    load_csv_data()
    plot()


def clear_my_input():
    """Clear input boxes"""

    if my_input.get() != "":
        lines.set("")
    try:
        liness.set("")
    except NameError:
        pass


def undo():
    """Undo the editing"""

    global mod_values
    try:
        mod_values.clear()
    except NameError:
        pass
    stop()


def make_time(ti_me):
    """Take a string and get the time value"""

    global dot

    Time = str(ti_me)
    hours, mins = Time.split(".")

    try:
        minutes = mins[0] + mins[1]
    except IndexError:
        minutes = mins[0] + "0"

    if len(str(int(minutes) % 60)) == 1:
        zero = 0
    else:
        zero = ''
    timE = float(str(int(hours) + int(int(minutes) / 60)) + '.' + str(zero) + str(int(minutes) % 60))
    return round(timE, 2)


def view_data(my_dipe):
    """Display the dataframe on the screen"""

    load_csv_data()


def plot():
    """Make a bar graph for the selected employee"""

    global label_graph
    global count

    matplotlib.use("TkAgg")
    plt.style.use('ggplot')
    clearFrame()
    dipendente = emplo_selection.get()
    dataf = read_CSV(dipendente)
    df_e_u = dataf[['entry', 'half', 'back', 'exit']]
    df_m = dataf[["free"]]
    df_e_u.columns = ['entry', 'half', 'back', 'exit']

    mylist = media(df_e_u)
    new_list = []
    for tim in mylist:
        new_list.append(make_time(tim))
    try:
        new_list.append(df_m.value_counts()[1] + 20)
        mezze = df_m.value_counts()[1]
    except KeyError:
        mezze = 0
        new_list.append(30)

    mydict = {0: "Entry", 1: "Half", 2: "Back", 3: "Exit", 4: "Free"}
    count = 0

    # Histo label
    my_data = pd.Series(new_list)
    figure = plt.Figure(figsize=(6, 5), dpi=100)
    bar_plot = FigureCanvasTkAgg(figure, label_graph)
    ax = figure.add_subplot(111)
    bar_plot.get_tk_widget().pack()
    my_data.plot(kind='bar', legend=False, ax=ax, color=["royalblue", "orange", "green", "red", "purple"])
    ax.set_title(f'Summary {dipendente}')
    ax.set(xlabel='Average time (HH:MM)')

    for bar, frequency in zip(ax.patches, new_list):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        if count == 4:
            text = f'{mydict[count]}\n{mezze}\n'
            ax.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
        else:
            text = f'{mydict[count]}\n{frequency:.2f}\n'
            count += 1
            ax.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

    toolbar = NavigationToolbar2Tk(bar_plot, main_window)
    toolbar.place(relx=0.76, rely=0.83)
    toolbar.update()


def clearFrame():
    """Clear the graph label"""

    global label_graph

    for widget in label_graph.winfo_children():
        widget.destroy()


def load_csv_data():
    """Populate the Tree View"""

    oggi, mese, anno = scandata()
    global data_view
    global count

    # Select your path for csv file
    file_path = fr"C:/Users/gabri/Desktop/YT/{emplo_selection.get()}_{mese}.csv"

    try:
        csv_filename = r"{}".format(file_path)
        if csv_filename[-4:] == ".csv":
            df = pd.read_csv(csv_filename)
        else:
            df = pd.read_excel(csv_filename)

    except ValueError:
        tk.messagebox.showerror("Info", "Cannot open the selected file")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Info", f"File {file_path} not found")
        return None

    clear_data()
    temp_list = list(df.columns)
    temp_list.insert(0, "giorno")
    data_view["column"] = temp_list
    temp_list.clear()
    data_view["show"] = "headings"

    for column in data_view["columns"]:
        data_view.heading(column, text=column)
        data_view.column(column, anchor=tk.CENTER, width=200)

    df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists

    count = 1
    for row in df_rows:
        row.insert(0, count)
        count += 1

    for row in df_rows:
        data_view.insert("", "end", values=row, tags=('even',))

    # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert

    for col in data_view['columns']:
        data_view.heading(col, text=f"{col}", anchor=tk.CENTER)
        data_view.column(col, anchor=tk.CENTER, width=100)

    return None


def clear_data():
    """Clean the TreeView"""

    global data_view
    data_view.delete(*data_view.get_children())
    return None


def clear_csv():
    """Reset every month the csv file"""

    oggi, mese, anno = scandata()
    nome_mese_file = sort_months[mese] - 1
    reversed_mesi_ordine = {value: key for (key, value) in sort_months.items()}
    prev_mese = reversed_mesi_ordine[nome_mese_file]

    for empl in my_emplo:
        try:
            os.rename(f"{empl}_{prev_mese}.csv", f"{empl}_{mese}.csv")
        except FileNotFoundError:
            pass


def open_file():
    """Open a .csv file and make a bar graph to compare different month logs"""

    matplotlib.use("TkAgg")
    global count

    # Set your initial path
    file = filedialog.askopenfilename(initialdir=r"C:\Users\gabri\Desktop", title="Select a file",
                                      filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    giorno, mese, anno = scandata()
    dataf = pd.read_csv(file)
    dipendente = file.split("/")
    df_e_u = dataf[['entry', 'half', 'back', 'exit']]
    df_m = dataf[["free"]]
    df_e_u.columns = ['entry', 'half', 'back', 'exit']

    mylist = media(df_e_u)
    new_list = []
    for tim in mylist:
        new_list.append(make_time(tim))

    try:
        new_list.append(df_m.value_counts()[1] + 20)
        mezze = df_m.value_counts()[1]
    except KeyError:
        mezze = 0
        new_list.append(30)

    mydict = {0: "Entry", 1: "Half", 2: "Back", 3: "Exit", 4: "Free"}

    figure = plt.figure('Summary')
    sns.set_style('whitegrid')
    # Titolo del grafico
    axes = sns.barplot(x=new_list, y=np.arange(1, 6))
    axes.set_title(f'Summary {dipendente[-1]}')
    axes.set(xlabel='Average time (HH:MM)')
    axes.set_ylim(top=int(max(mylist)) * 0.3, bottom=0)
    count = 0

    for bar, frequency in zip(axes.patches, new_list):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        if count == 4:
            text = f'{mydict[count]}\n{mezze}\n'
            axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
        else:
            text = f'{mydict[count]}\n{frequency:.2f}\n'
            count += 1
            axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')

    plt.show(block=False)


def backup():
    """Backup of the csv files every day"""

    giorno, mese, anno = scandata()

    # Set your dir
    my_dir = "Registro_Ingressi_" + anno
    my_dir_month = "Registro_Ingressi_" + mese

    try:
        os.mkdir(fr"C:\Users\gabri\OneDrive\Desktop\lavori gabri\Registro Ingressi Backup\{my_dir}")
    except FileExistsError:
        pass
    finally:
        my_dir_path = r"C:\Users\gabri\OneDrive\Desktop\Registro Ingressi"
        new_dir_path = fr"C:\Users\gabri\OneDrive\Desktop\lavori gabri\Registro Ingressi Backup\{my_dir}\{my_dir_month}"

    copy_tree(my_dir_path, new_dir_path)


def stop():
    """End a python process by pid"""
    system(f"TASKKILL /PID {os.getpid()}")


def scanora():
    """Take actual time"""
    orap = datetime.now()
    orari = orap.strftime("%H.%M")
    return float(orari)


def scandata():
    """Return today date DD/MM/YYYY"""
    oggi = date.today()
    mese = oggi.strftime("%B")
    dat = (oggi.strftime("%d"), mese, oggi.strftime("%Y"))

    return dat


def tk_stuffs():
    """Main program"""

    global main_window
    global emplo_selection
    global label_graph
    global data_view
    global screen

    progress.stop()
    screen.destroy()

    # Main window

    main_window = Tk()
    main_window.title("Access Log")
    main_window.geometry("1300x708")
    main_window.pack_propagate(False)
    main_window.resizable(False, False)
    main_window.grid_columnconfigure(4, weight=3)
    credit = tk.Label(main_window, text="Gabro©")
    credit.place(relx=0.475, rely=0.97)
    credit.configure(background="gray", fg="dark red", font=("Times", 10), relief="ridge")

    # Icon
    main_window.iconbitmap(icon)

    # Label window

    label_principale = tk.LabelFrame(main_window, text="Employee Access Register", font=("Spectral", 15),
                                     foreground="black")
    label_principale.place(height=250, width=600, relx=0.03, rely=0.15)

    button_modifica = tk.Button(text="Editing", fg="black", bg="LightYellow3", relief="raised",
                                activebackground="light gray", command=lambda m="mod": check_dipe(m),
                                font=("Spectral", 15))
    button_modifica.place(relx=0.13, rely=0.55)

    button_histo = tk.Button(text="See Graph", fg="black", bg="sandy brown", relief="raised",
                             activebackground="light gray", font=("Spectral", 15),
                             command=lambda m="histo": check_dipe(m))
    button_histo.place(relx=0.3, rely=0.55)

    # ComboBox

    emplo_selection = ttk.Combobox(main_window, values=my_emplo,
                                   font=("Lucinda Console", 15),
                                   foreground="black", state="readonly")
    emplo_selection.place(relx=0.17, rely=0.05)

    emplo_selection.bind("<<ComboboxSelected>>", view_data)
    emplo_selection.current()

    # Style
    stile = ThemedStyle(main_window)
    stile.theme_use(my_style)

    stile.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
    stile.configure("Treeview", background="white", foreground="black", fieldbackground="silver")
    stile.map("Treeview", background=[('selected', 'gray')])

    # Treeview Widget
    data_view = ttk.Treeview(label_principale)
    data_view.place(relheight=1, relwidth=1)

    treescrolly = tk.Scrollbar(label_principale, orient="vertical",
                               command=data_view.yview)  # command means update the yaxis view of the widget
    treescrollx = tk.Scrollbar(label_principale, orient="horizontal",
                               command=data_view.xview)  # command means update the xaxis view of the widget
    data_view.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
    treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

    # Plot label frame

    label_graph = tk.LabelFrame(main_window, text="Bar Graph", font=("Spectral", 15),
                                foreground="black")
    label_graph.place(height=540, width=540, relx=0.53, rely=0.05)

    label_scan = tk.LabelFrame(main_window, text="Most recent scan", font=("Spectral", 15),
                               foreground="black")
    label_scan.place(height=80, width=600, relx=0.03, rely=0.715)

    scan_text = Text(label_scan, height=1, font=("Times", 18))
    scan_text.insert(1.0, "No login has taken place yet")
    scan_text.pack()

    fig_graph = plt.Figure(figsize=(6, 5), dpi=100)
    bar_plot_1 = FigureCanvasTkAgg(fig_graph, label_graph)
    ax_1 = fig_graph.add_subplot(111)
    bar_plot_1.get_tk_widget().pack()

    menu_option()

    if __name__ == "__main__":
        main_window.mainloop()


on_start()

# Loading Screen
screen = tk.Tk()
screen.title("Loading")
screen.geometry("300x90")
stile_screen = ThemedStyle(screen)
stile_screen.theme_use(my_style)
screen.iconbitmap(icon)

progress = ttk.Progressbar(screen, orient=HORIZONTAL, length=200, mode='determinate')
progress.pack(pady=20)
screen_label = Label(screen, text='Loading...')
screen_label.pack(pady=1)
progress.start(45)
screen.after(5400, tk_stuffs)
screen.mainloop()
