from tkinter import StringVar, messagebox
from customtkinter import N, S, W, E
from Spirit_types import options
import Spirit_GUI_Class as Ss
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def main():

    def summon_spirit(force, typ):
        try:
            force = int(force)
            tab = spirits.add(f"Force {force} {typ.capitalize()} Spirit")
            Ss.SpiritSummoner(typ, force, tab)
            spirits.set(f"Force {force} {typ.capitalize()} Spirit")
            remove_button = customtkinter.CTkButton(tab, text='Remove', command=lambda: spirits.delete(spirits.get()),
                                                    fg_color="red")
            remove_button.grid(column=0, row=0, sticky=N + E)
        except ValueError:
            messagebox.showerror('Missing Force', 'Please, enter the value for force.')

    #   The basic window itself
    app = customtkinter.CTk()
    app.title("Spirit Summoner")
    force_var = StringVar()
    type_var = StringVar()

    spirit_select_frame = customtkinter.CTkFrame(app)
    spirit_select_frame.grid(column=0, row=0, sticky=customtkinter.W, pady=10, padx=10)
    spirits_frame = customtkinter.CTkFrame(app)
    spirits_frame.grid(column=0, row=1, sticky=W + E, pady=5, padx=10)

    force_label = customtkinter.CTkLabel(spirit_select_frame, text='Force: ')
    force_label.grid(column=0, row=0)

    force_entry_field = customtkinter.CTkEntry(spirit_select_frame, textvariable=force_var, width=3)
    force_entry_field.grid(column=1, row=0, padx=5)
    force_entry_field.focus_set()

    spirit_type_dropdown = customtkinter.CTkOptionMenu(spirit_select_frame, variable=type_var, values=options)
    spirit_type_dropdown.grid(column=2, row=0, padx=5)
    spirit_type_dropdown.set(options[0])

    summon_button = customtkinter.CTkButton(spirit_select_frame, text="Summon",
                                            command=lambda: summon_spirit(force_var.get(), type_var.get()))
    summon_button.grid(column=3, row=0, padx=5)

    spirits = customtkinter.CTkTabview(spirits_frame)
    spirits.grid(column=0, row=0)

    app.mainloop()


if __name__ == "__main__":
    main()
