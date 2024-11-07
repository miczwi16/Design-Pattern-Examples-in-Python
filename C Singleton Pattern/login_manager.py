import tkinter as tk

from session import Session
from singleton_exception import SingletonException

class LoginManager():
    def __init__(self):
        # root and passes initialization
        self.__root = tk.Tk()
        self.__root.title("Login Manager")
        self.__root.resizable(False, False)
        self.__user = "foo"
        self.__pass = "bar"

        # login entry
        self.__login_label = tk.Label(self.__root, text="Login:")
        self.__login_label.grid(column=0, row=0, sticky="e")

        self.__login_entry = tk.Entry(self.__root)
        self.__login_entry.grid(column=1, row=0)

        # password entry
        self.__password_label = tk.Label(self.__root, text="Password:")
        self.__password_label.grid(column=0, row=1, sticky="e")

        self.__password_entry = tk.Entry(self.__root, show="*")
        self.__password_entry.grid(column=1, row=1)

        # log entry
        self.__log_label = tk.Label(self.__root, text="Log:")
        self.__log_label.grid(column=0, row=2, sticky="e")

        self.__log_entry = tk.Entry(self.__root)
        self.__log_entry.grid(column=1, row=2)
        self.__log_entry.config(state="readonly")

        # login button
        self.__login_button = tk.Button(self.__root, text="LOGIN", command=lambda: self.__login())
        self.__login_button.grid(column=2, row=0, padx=5, sticky="nsew")

        # logout button
        self.__logout_button = tk.Button(self.__root, text="LOGOUT", command=lambda: self.__logout())
        self.__logout_button.grid(column=3, row=0, padx=5, sticky="nsew")

        # clear button
        self.__clear_button = tk.Button(self.__root, text="CLEAR", command=lambda: self.__clear())
        self.__clear_button.grid(column=2, row=1, padx=5, columnspan=2, sticky="nsew")

        # quit button
        self.__quit_button = tk.Button(self.__root, text="QUIT", command=quit)
        self.__quit_button.grid(column=2, row=2, padx=5, columnspan=2, sticky="nsew")

    def __login_successful(self):
        if self.__login_entry.get() == self.__user and self.__password_entry.get() == self.__pass:
            return True
        else:
            return False

    def __write_log(self, message):
        self.__log_entry.config(state="normal")
        self.__log_entry.delete(0, tk.END)
        self.__log_entry.insert(0, message)
        self.__log_entry.config(state="readonly")

    def __login(self):
        if self.__login_successful():
            try:
                Session.open()
                self.__write_log("Login successful!")
            except SingletonException as e:
                self.__write_log(e.args[0])
        else:
            self.__write_log("Login unsuccessful!")

    def __logout(self):
        if Session.exists():
            Session.close()
            self.__write_log("You've been logged out!")
        else:
            self.__write_log("You're not logged in!")

    def __clear(self):
        self.__login_entry.delete(0, tk.END)
        self.__password_entry.delete(0, tk.END)
        self.__write_log("")

    def run(self):
        self.__root.mainloop()