import tkinter as tk

from low_level_enemy_fact import LowLevelEnemyFact
from medium_level_enemy_fact import MediumLevelEnemyFact
from high_level_enemy_fact import HighLevelEnemyFact

class EnemyGenerator():
    def __init__(self):
        # root initialization
        self.__root = tk.Tk()
        self.__root.title("Enemy Generator")
        self.__root.resizable(False, False)

        # Buttons
        self.__low_level_button = tk.Button(self.__root, text="Low level", command=lambda: self.__generate("low"))
        self.__low_level_button.grid(column=0, row=0, pady=5)

        self.__medium_level_button = tk.Button(self.__root, text="Medium level", command=lambda: self.__generate("medium"))
        self.__medium_level_button.grid(column=1, row=0, pady=5)

        self.__high_level_button = tk.Button(self.__root, text="High level", command=lambda: self.__generate("high"))
        self.__high_level_button.grid(column=2, row=0, pady=5)

        #Entries
        self.__entry_1 = tk.Entry(self.__root)
        self.__entry_1.grid(column=0, row=1)

        self.__entry_2 = tk.Entry(self.__root)
        self.__entry_2.grid(column=1, row=1)

        self.__entry_3 = tk.Entry(self.__root)
        self.__entry_3.grid(column=2, row=1)

        self.__entry_4 = tk.Entry(self.__root)
        self.__entry_4.grid(column=0, row=2)

        self.__entry_5 = tk.Entry(self.__root)
        self.__entry_5.grid(column=1, row=2)

        self.__entry_6 = tk.Entry(self.__root)
        self.__entry_6.grid(column=2, row=2)

        self.__entry_7 = tk.Entry(self.__root)
        self.__entry_7.grid(column=0, row=3)

        self.__entry_8 = tk.Entry(self.__root)
        self.__entry_8.grid(column=1, row=3)

        self.__entry_9 = tk.Entry(self.__root)
        self.__entry_9.grid(column=2, row=3)

        # switch off entries
        self.__switch_entries("readonly")

    def __generate(self, param):
        generator = 0

        if param == "low":
            generator = LowLevelEnemyFact()
        elif param == "medium":
            generator = MediumLevelEnemyFact()
        elif param == "high":
            generator = HighLevelEnemyFact()

        if generator:
            self.__switch_entries("normal")
            self.__clear_entries()

            self.__entry_1.insert(0, generator.generate().get_name())
            self.__entry_2.insert(0, generator.generate().get_name())
            self.__entry_3.insert(0, generator.generate().get_name())
            self.__entry_4.insert(0, generator.generate().get_name())
            self.__entry_5.insert(0, generator.generate().get_name())
            self.__entry_6.insert(0, generator.generate().get_name())
            self.__entry_7.insert(0, generator.generate().get_name())
            self.__entry_8.insert(0, generator.generate().get_name())
            self.__entry_9.insert(0, generator.generate().get_name())

            self.__switch_entries("readonly")

    def __switch_entries(self, param):
        self.__entry_1.config(state=param)
        self.__entry_2.config(state=param)
        self.__entry_3.config(state=param)
        self.__entry_4.config(state=param)
        self.__entry_5.config(state=param)
        self.__entry_6.config(state=param)
        self.__entry_7.config(state=param)
        self.__entry_8.config(state=param)
        self.__entry_9.config(state=param)

    def __clear_entries(self):
        self.__entry_1.delete(0, tk.END)
        self.__entry_2.delete(0, tk.END)
        self.__entry_3.delete(0, tk.END)
        self.__entry_4.delete(0, tk.END)
        self.__entry_5.delete(0, tk.END)
        self.__entry_6.delete(0, tk.END)
        self.__entry_7.delete(0, tk.END)
        self.__entry_8.delete(0, tk.END)
        self.__entry_9.delete(0, tk.END)

    def run(self):
        self.__root.mainloop()
