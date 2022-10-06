from tkinter import Tk, W, StringVar, ttk, N, E, messagebox
import Spirit_GUI_Class as Ss

TABS = []

options = ['Air', 'Earth', 'Fire', 'Water', 'Beast', 'Man', 'Guardian', 'Sage', 'Plant', 'Task']


def remove_spirit():
    i = spirits_tabs.index(spirits_tabs.select())
    spirits_tabs.forget(i)
    TABS[i].destroy()


def summon_spirit():
    try:
        new_tab = ttk.Frame(spirits_tabs, borderwidth=0)
        spirit = Ss.SpiritSummoner(type_var.get(), force_var.get(), new_tab)
        spirits_tabs.add(new_tab, text=f'Force {spirit.spirit.force} {spirit.spirit.typ.capitalize()} Spirit')
        TABS.append(new_tab)
        spirits_tabs.select(len(TABS) - 1)
        remove_button = ttk.Button(new_tab, text='Remove', command=remove_spirit)
        remove_button.grid(column=0, row=0, sticky=N + E)
    except ValueError:
        messagebox.showerror('Missing Force', 'Please, enter the value for force.')


#   The basic window itself
spirits_popup = Tk()
spirits_popup.title('Spirit Summoner')
force_var = StringVar()
type_var = StringVar()

selection_frame = ttk.Frame(spirits_popup)
selection_frame.grid(column=0, row=0, sticky=W, pady=10, padx=10)
main_tabs_frame = ttk.Frame(spirits_popup)
main_tabs_frame.grid(column=0, row=1, sticky=W, pady=5, padx=10)

force_label = ttk.Label(selection_frame, text='Force: ')
force_label.grid(column=0, row=0)

force_entry = ttk.Entry(selection_frame, textvariable=force_var, width=3)
force_entry.grid(column=1, row=0)
force_entry.focus_set()

type_menu = ttk.OptionMenu(selection_frame, type_var, options[0], *options)
type_menu.grid(column=2, row=0)

summon_button = ttk.Button(selection_frame, text='Summon', command=summon_spirit)
summon_button.grid(column=3, row=0)

spirits_tabs = ttk.Notebook(main_tabs_frame)
spirits_tabs.grid(column=0, row=0)

spirits_popup.mainloop()
