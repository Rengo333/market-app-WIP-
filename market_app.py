from tkinter import *
import matplotlib.pyplot as plt

#TODO after database is created
def registration():
    pass

# log in button for now leads to a main menu without a username and password check
def main_menu():
    for widgets in app.winfo_children():
        widgets.destroy()

    # MIDDLE BUTTONS

    chart_button = Button(app, text="Chart", font=("Courier", 10), command=display_chart)
    chart_button.place(relx=.45, rely=.2)

    table_button = Button(app, text="Table", font=("Courier", 10), command=main_menu)
    table_button.place(relx=.45, rely=.3)

    buy_or_sell_button = Button(app, text="Buy or Sell", font=("Courier", 10), command=main_menu)
    buy_or_sell_button.place(relx=.42, rely=.4)

    app_settings_button = Button(app, text="App Settings", font=("Courier", 10), command=main_menu)
    app_settings_button.place(relx=.415, rely=.5)

    deposit_or_withdraw_button = Button(app, text="Deposit or Withdraw", font=("Courier", 10), command=main_menu)
    deposit_or_withdraw_button.place(relx=.37, rely=.6)

    log_out_button = Button(app, text="Log out", font=("Courier", 10), command=main_menu)
    log_out_button.place(relx=.44, rely=.7)

    # TOP RIGHT BUTTONS

    profile_settings_button = Button(app, text="Profile\nSettings", font=("Courier", 10), command=main_menu)
    profile_settings_button.place(relx=.88, rely=.0)

    transaction_history_button = Button(app, text="Transaction\nHistory", font=("Courier", 10), command=main_menu)
    transaction_history_button.place(relx=.72, rely=.0)

    premium_button = Button(app, text="Premium", font=("Courier", 10), command=main_menu)
    premium_button.place(relx=.605, rely=.0)

    # TOP LEFT BUTTON

    balance_button = Button(app, text="Balance", font=("Courier", 10), command=main_menu)
    balance_button.place(relx=.0, rely=.0)

#TODO: make a page where user can choose 2 currencies and display the chart using test data(api data later)
def display_chart():

    for widgets in app.winfo_children():
        widgets.destroy()
    # temp currencies
    options = [
        "EUR",
        "USD"
    ]

    clicked = StringVar()

    # datatype of menu text
    clicked_currency1 = StringVar()
    clicked_currency2 = StringVar()
    # initial menu text
    clicked_currency1.set("EUR")
    clicked_currency2.set("USD")

    currency_dropmenu1 = OptionMenu(app, clicked_currency1, *options)
    currency_dropmenu1.pack()

    currency_dropmenu2 = OptionMenu(app, clicked_currency2, *options)
    currency_dropmenu2.pack()



#TODO make a page where user can choose 2 currencies and display the table using test data(api data later)
def display_table():
    pass

#TODO make a page where user can buy and sell his currencies
def buy_or_sell():
    pass


if __name__ == "__main__":
    app = Tk()

    # root window title and dimension
    app.title("Market App")

    # variables used to calculate the center of a screen
    app_width = 600
    app_height = 400
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    # centering the app
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    # creating app window
    app.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    app.resizable(False, False)

    # username txt label
    username_lbl = Label(app, text="Username:", font=("Courier", 10))
    username_lbl.place( relx=.25, rely=.3)

    # username entry field
    user_login_entry = StringVar()
    user_login_entry = Entry(bg="white")
    user_login_entry.place( relx=.4, rely=.3)

    # password txt label
    password_lbl = Label(app, text="Password:", font=("Courier", 10))
    password_lbl.place( relx=.25, rely=.4)

    # password entry field
    user_password_entry = StringVar()
    user_password_entry = Entry(bg="white")
    user_password_entry.place( relx=.4, rely=.4)

    # sign up txt label
    sign_lbl = Label(app, text="Please log in:", font=("Courier", 13))
    sign_lbl.place(relx=.37, rely=.2)

    # no acc txt label
    no_acc_lbl = Label(app, text="Dont have an account yet?", font=("Courier", 10))
    no_acc_lbl.place(relx=.33, rely=.5)

    # sign in button
    log_in_button = Button(app, text="Log In", font=("Courier", 10), command=main_menu)
    log_in_button.place(relx=.65, rely=.35)

    # register button
    register_button = Button(app, text="Register", font=("Courier", 10))
    register_button.place(relx=.43, rely=.6)
    app.mainloop()
