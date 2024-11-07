from email_not_factory import EmailNotFactory
from sms_not_factory import SMSNotFactory
from push_not_factory import PushNotFactory
import tkinter as tk

class NotCreator(): # notification creator
    def __init__(self):
        # root initialization
        self.__root = tk.Tk()
        self.__root.title("Notification Creator")
        self.__root.resizable(False, False)

        # Buttons
        self.__push_button = tk.Button(self.__root, text="Push", command=lambda: self.__create_not("Push"))
        self.__push_button.grid(column=0, row=0, pady=5)

        self.__sms_button = tk.Button(self.__root, text="SMS", command=lambda: self.__create_not("SMS"))
        self.__sms_button.grid(column=1, row=0, pady=5)

        self.__email_button = tk.Button(self.__root, text="Email", command=lambda: self.__create_not("Email"))
        self.__email_button.grid(column=2, row=0, pady=5)

        # Message
        self.__message_label = tk.Label(self.__root, text="Message")
        self.__message_label.grid(column=1, row=1)

        self.__message_entry = tk.Entry(self.__root)
        self.__message_entry.grid(column=0, row=2, columnspan=3)
        self.__message_entry.config(state="readonly")

        # Quit button
        self.__quit_button = tk.Button(self.__root, text="Quit", command=quit)
        self.__quit_button.grid(column=1, row=3, pady=5)

    def __create_not(self, not_type): # create notification
        message_fact = 0

        if not_type == "Push":
            message_fact = PushNotFactory()
        elif not_type == "SMS":
            message_fact = SMSNotFactory()
        elif not_type == "Email":
            message_fact = EmailNotFactory()

        if message_fact:
            self.__message_entry.config(state="normal")
            self.__message_entry.delete(0, tk.END)
            self.__message_entry.insert(0, message_fact.create_not().send())
            self.__message_entry.config(state="readonly")

    def run(self):
        self.__root.mainloop()