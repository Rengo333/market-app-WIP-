from tkinter import *

def main():
    app = Tk()

    # root window title and dimension
    app.title("Market App")

    app_width = 750
    app_height = 500
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    # Set geometry (widthxheight)

    # centering the app
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    app.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    app.resizable(False, False)

    # frame for username and password
    login_pass_frame = Canvas(app, height=300, width=300,bg="lightblue")
    login_pass_frame.place(anchor="c", relx=.5, rely=.5)

    login_pass_frame.create_text(150, 40, text="Username:",)
    login_pass_frame.pack()

    login_pass_frame.create_text(150, 100, text="Password:", )
    login_pass_frame.pack()

    # username and password entry fields
    user_login_entry = StringVar()
    user_login_entry = Entry(login_pass_frame, bg="white")
    user_login_entry.place(anchor="c", relx=.5, rely=.4)

    user_password_entry = StringVar()
    user_password_entry = Entry(login_pass_frame, bg ="white")
    user_password_entry.place(anchor="c", relx=.5, rely=.2)


    app.mainloop()

if __name__ == "__main__":
    main()