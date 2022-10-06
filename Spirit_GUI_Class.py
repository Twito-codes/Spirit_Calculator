import Spirit_Class as Spirit
from tkinter import W, NO, E, CENTER, END, ttk


class SpiritSummoner(ttk.Frame):
    def __init__(self, typ, force, master):
        super().__init__(master)
        self.spirit = Spirit.Spirit(typ=typ, force=int(force))

        self.tab = ttk.Frame(master)
        self.tab.grid(column=0, row=1, pady=10, padx=10)

        self.stats_and_pools = ttk.Frame(self.tab)
        self.stats_and_pools.grid(column=0, row=0, sticky=W)

        self.initiative_frame = ttk.Frame(self.tab)
        self.initiative_frame.grid(column=1, row=0, sticky=W)

        self.stat_table = ttk.Treeview(self.stats_and_pools, columns=('stat', 'stat_val'), show='tree', height=11)
        self.stat_table.grid(column=0, row=0)
        self.place_stats()

        self.pools_table = ttk.Treeview(self.stats_and_pools, columns=('pool_name', 'pool_val'), show='tree', height=11)
        self.pools_table.grid(column=1, row=0)
        self.place_pools()

        self.initiative_label = ttk.Label(self.initiative_frame, text='')
        self.initiative_label.grid(column=1, row=0, padx=5, pady=10)
        self.initiative_button = ttk.Button(self.initiative_frame, text='Roll Initiative', command=self.roll_initiative)
        self.initiative_button.grid(column=0, row=0, pady=10)

        self.astral_initiative_label = ttk.Label(self.initiative_frame, text='')
        self.astral_initiative_label.grid(column=1, row=1, sticky=W, padx=5, pady=10)
        self.astral_initiative_button = ttk.Button(self.initiative_frame, text='Roll Astral Initiative',
                                                   command=self.roll_astral_initiative)
        self.astral_initiative_button.grid(column=0, row=1, sticky=W, pady=10)

        self.powers_and_services = ttk.Frame(self.tab)
        self.powers_and_services.grid(column=0, row=1, columnspan=2, sticky=W)

        self.powers_table = ttk.Treeview(self.powers_and_services, columns=('powers', 'optional_powers'), show='tree')
        self.powers_table.grid(column=0, row=0, sticky=W)
        self.place_powers()

    def place_stats(self):
        self.stat_table.column('#0', width=0, stretch=NO)
        self.stat_table.column('stat', anchor=W, width=60)
        self.stat_table.column('stat_val', anchor=E, width=40)

        self.stat_table.insert(parent='', index='end', iid='0', text='',
                               values=('Body', self.spirit.stats['body']))
        self.stat_table.insert(parent='', index='end', iid='1', text='',
                               values=('Agility', self.spirit.stats['agility']))
        self.stat_table.insert(parent='', index='end', iid='2', text='',
                               values=('Reaction', self.spirit.stats['reaction']))
        self.stat_table.insert(parent='', index='end', iid='3', text='',
                               values=('Strength', self.spirit.stats['strength']))
        self.stat_table.insert(parent='', index='end', iid='4', text='',
                               values=('Willpower', self.spirit.stats['willpower']))
        self.stat_table.insert(parent='', index='end', iid='5', text='',
                               values=('Logic', self.spirit.stats['logic']))
        self.stat_table.insert(parent='', index='end', iid='6', text='',
                               values=('Intuition', self.spirit.stats['intuition']))
        self.stat_table.insert(parent='', index='end', iid='7', text='',
                               values=('Charisma', self.spirit.stats['charisma']))

    def place_pools(self):
        self.pools_table.column('#0', width=0, stretch=NO)
        self.pools_table.column('pool_name', anchor=CENTER, width=150)
        self.pools_table.column('pool_val', anchor=CENTER, width=40)

        self.pools_table.insert(parent='', index='end', iid='0', text='',
                                values=('Defense', self.spirit.dice_pools['defense']))
        self.pools_table.insert(parent='', index='end', iid='1', text='',
                                values=('Astral Defense', self.spirit.dice_pools['astral_defense']))
        self.pools_table.insert(parent='', index='end', iid='2', text='',
                                values=('Armor', self.spirit.dice_pools['armor']))
        self.pools_table.insert(parent='', index='end', iid='3', text='',
                                values=('Assensing', self.spirit.dice_pools['assensing']))
        self.pools_table.insert(parent='', index='end', iid='4', text='',
                                values=('Astral Combat', self.spirit.dice_pools['astral_combat']))
        if self.spirit.dice_pools['blades']:
            self.pools_table.insert(parent='', index='end', iid='5', text='',
                                    values=('Blades', self.spirit.dice_pools['blades']))
        if self.spirit.dice_pools['clubs']:
            self.pools_table.insert(parent='', index='end', iid='6', text='',
                                    values=('Clubs', self.spirit.dice_pools['clubs']))
        if self.spirit.dice_pools['counterspelling']:
            self.pools_table.insert(parent='', index='end', iid='7', text='',
                                    values=('Counterspelling', self.spirit.dice_pools['counterspelling']))
        self.pools_table.insert(parent='', index='end', iid='8', text='',
                                values=('Exotic Ranged Weapons', self.spirit.dice_pools['exotic_ranged_weapons']))
        if self.spirit.dice_pools['flight']:
            self.pools_table.insert(parent='', index='end', iid='9', text='',
                                    values=('Flight', self.spirit.dice_pools['flight']))
        self.pools_table.insert(parent='', index='end', iid='10', text='',
                                values=('Perception', self.spirit.dice_pools['perception']))
        self.pools_table.insert(parent='', index='end', iid='11', text='',
                                values=('Unarmed Combat', self.spirit.dice_pools['unarmed_combat']))

    def place_powers(self):
        self.powers_table.column('#0', width=0, stretch=NO)
        self.powers_table.column('powers', anchor=W, width=150)
        self.powers_table.column('optional_powers', anchor=W, width=650)

        self.powers_table.insert(parent='', index='end', iid='0', values=('Core Powers', self.spirit.core_powers))
        self.powers_table.insert(parent='', index='end', iid='1', values=('Powers', self.spirit.powers))
        self.powers_table.insert(parent='', index=END, iid='2',
                                 values=('Optional Powers Count', int(self.spirit.optional_powers_count)))
        self.powers_table.insert(parent='', index='end', iid='3',
                                 values=('Optional Powers', self.spirit.optional_powers))
        if self.spirit.special:
            for special in self.spirit.special:
                self.powers_table.insert(parent='', index=END, values=special)

    def roll_initiative(self):
        initiative = self.spirit.roll_initiative()
        self.initiative_label.config(text=f'Initiative: {initiative}')

    def roll_astral_initiative(self):
        initiative = self.spirit.roll_astral_initiative()
        self.astral_initiative_label.config(text=f'Astral Initiative: {initiative}')
