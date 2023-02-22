from tkinter import *


def main():
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
    username_lbl.place(anchor="c", relx=.3, rely=.3)

    # username entry field
    user_login_entry = StringVar()
    user_login_entry = Entry(bg="white")
    user_login_entry.place(anchor="c", relx=.5, rely=.3)

    # password txt label
    password_lbl = Label(app, text="Password:", font=("Courier", 10))
    password_lbl.place(anchor="c", relx=.3, rely=.4)

    # password entry field
    user_password_entry = StringVar()
    user_password_entry = Entry(bg="white")
    user_password_entry.place(anchor="c", relx=.5, rely=.4)



    # sign up txt label
    sign_lbl = Label(app, text="Please sign in to the Market App:", font=("Courier", 13))
    sign_lbl.place(anchor="c", relx=.5, rely=.2)

    # no acc txt label
    no_acc_lbl = Label(app, text="Dont have an account yet?", font=("Courier", 10))
    no_acc_lbl.place(anchor="c", relx=.5, rely=.5)

    # sign in button
    register_button = Button(app, text="Sign In", font=("Courier", 10))
    register_button.place(anchor="c", relx=.7, rely=.35)

    # register button
    register_button = Button(app, text="Register here", font=("Courier", 10))
    register_button.place(anchor="c", relx=.5, rely=.6)
    app.mainloop()

if __name__ == "__main__":
    main()