from char_factory import CharFactory
import tkinter as tk

class RPGCharGen(): # RPG Character Generator
    def __init__(self):
        # root initialization
        self.__root = tk.Tk()
        self.__root.title("RPG Character Generator")
        self.__root.resizable(False, False)

        # Buttons
        self.__warrior_button = tk.Button(self.__root, text="Warrior", command=lambda: self.__generate("Warrior"))
        self.__warrior_button.grid(column=0, row=0, pady=5)

        self.__thief_button = tk.Button(self.__root, text="Thief", command=lambda: self.__generate("Thief"))
        self.__thief_button.grid(column=1, row=0, pady=5)

        self.__mage_button = tk.Button(self.__root, text="Mage", command=lambda: self.__generate("Mage"))
        self.__mage_button.grid(column=2, row=0, pady=5)

        # Strength
        self.__strength_label = tk.Label(self.__root, text="Strength")
        self.__strength_label.grid(column=0, row=1)

        self.__strength_entry = tk.Entry(self.__root)
        self.__strength_entry.grid(column=0, row=2, padx=10)

        # Endurance
        self.__endurance_label = tk.Label(self.__root, text="Endurance")
        self.__endurance_label.grid(column=0, row=3)

        self.__endurance_entry = tk.Entry(self.__root)
        self.__endurance_entry.grid(column=0, row=4, padx=10)

        # Agility
        self.__agility_label = tk.Label(self.__root, text="Agility")
        self.__agility_label.grid(column=1, row=1)

        self.__agility_entry = tk.Entry(self.__root)
        self.__agility_entry.grid(column=1, row=2, padx=10)

        # Speed
        self.__speed_label = tk.Label(self.__root, text="Speed")
        self.__speed_label.grid(column=1, row=3)

        self.__speed_entry = tk.Entry(self.__root)
        self.__speed_entry.grid(column=1, row=4, padx=10)

        # Intelligence
        self.__intelligence_label = tk.Label(self.__root, text="Intelligence")
        self.__intelligence_label.grid(column=2, row=1)

        self.__intelligence_entry = tk.Entry(self.__root)
        self.__intelligence_entry.grid(column=2, row=2, padx=10)

        # Willpower
        self.__willpower_label = tk.Label(self.__root, text="Willpower")
        self.__willpower_label.grid(column=2, row=3)

        self.__willpower_entry = tk.Entry(self.__root)
        self.__willpower_entry.grid(column=2, row=4, padx=10)

        # Quit Button
        self.__quit_button = tk.Button(self.__root, text="Quit", command=quit)
        self.__quit_button.grid(column=1, row=5, pady=5)

        # Switch off entries
        self.__switch_entries("readonly")

    def __generate(self, class_name):
        char = CharFactory.generate_char(class_name)

        self.__switch_entries("normal")
        self.__clear_entries()

        self.__strength_entry.insert(0, char.get_strength())
        self.__endurance_entry.insert(0, char.get_endurance())
        self.__agility_entry.insert(0, char.get_agility())
        self.__speed_entry.insert(0, char.get_speed())
        self.__intelligence_entry.insert(0, char.get_intelligence())
        self.__willpower_entry.insert(0, char.get_willpower())

        self.__switch_entries("readonly")

    def __switch_entries(self, param):
        self.__strength_entry.config(state=param)
        self.__endurance_entry.config(state=param)
        self.__agility_entry.config(state=param)
        self.__speed_entry.config(state=param)
        self.__intelligence_entry.config(state=param)
        self.__willpower_entry.config(state=param)

    def __clear_entries(self):
        self.__strength_entry.delete(0, tk.END)
        self.__endurance_entry.delete(0, tk.END)
        self.__agility_entry.delete(0, tk.END)
        self.__speed_entry.delete(0, tk.END)
        self.__intelligence_entry.delete(0, tk.END)
        self.__willpower_entry.delete(0, tk.END)

    def run(self):
        self.__root.mainloop()