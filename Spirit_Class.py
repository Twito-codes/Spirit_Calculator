import numpy


class Spirit:
    def __init__(self, typ, force):
        self.typ = typ.lower()
        self.force = int(force)
        self.optional_powers_count = numpy.floor(self.force / 3)
        self.optional_powers = ''
        self.core_powers = 'Astral combat, Materialisation, Sapience, Astral form'
        self.powers = ''
        self.stats = {
            'body': 0,
            'strength': 0,
            'agility': 0,
            'reaction': 0,
            'willpower': 0,
            'logic': 0,
            'intuition': 0,
            'charisma': 0
        }
        self.special = []
        self.make_stats(self.force)
        self.dice_pools = {
            'defense': self.stats['reaction'] + self.stats['intuition'],
            'astral_defense': self.stats['intuition'] * 2,
            'armor': self.force * 2,
            'assensing': self.stats['intuition'] + self.force,
            'astral_combat': self.stats['willpower'] + self.force,
            'exotic_ranged_weapons': self.stats['agility'] + self.force,
            'perception': self.stats['intuition'] + self.force,
            'blades': None,
            'clubs': None,
            'counterspelling': None,
            'flight': None,
            'unarmed_combat': self.stats['agility'] + self.force,
            'initiative': f'{(self.force * 2) + 4} + 2d6',
            'astral_initiative': f'{self.force * 2} + 3d6'
        }
        self.modify_dice_pools(self.force)
        self.initiative = 0

    def __del__(self):
        pass

    def modify_dice_pools(self, force):
        if self.typ == 'fire' or 'man':
            self.dice_pools['flight'] = self.stats['strength'] + force
        elif self.typ == 'guardian':
            self.dice_pools['blades'] = self.stats['agility'] + force,
            self.dice_pools['clubs'] = self.stats['agility'] + force,
            self.dice_pools['counterspelling'] = force * 2

    def make_stats(self, force):
        def air(sila):
            self.stats['body'] = sila - 2
            self.stats['agility'] = sila + 3
            self.stats['reaction'] = sila + 4
            self.stats['strength'] = sila - 3
            self.stats['willpower'] = sila
            self.stats['intuition'] = sila
            self.stats['charisma'] = sila
            self.stats['logic'] = sila
            self.optional_powers = 'Elemental attack, Energy Aura, Fear, Guard, Noxious breath, Psychokinesis'
            self.powers = 'Accident, Concealment, Confusion, Engulf, Movement, Search'
            self.special.append(('Sprint', 'Spirits of air move +10m per hit when sprinting.'))

        def earth(sila):
            self.stats['body'] = sila + 4
            self.stats['agility'] = sila - 2
            self.stats['reaction'] = sila - 1
            self.stats['strength'] = sila + 4
            self.stats['willpower'] = sila
            self.stats['logic'] = sila - 1
            self.stats['intuition'] = sila
            self.stats['charisma'] = sila
            self.optional_powers = 'Concealment, Confusion, Engulf, Elemental attack, Fear'
            self.powers = 'Binding, Guard, Movement, Search'

        def beast(sila):
            self.stats['body'] = sila + 2
            self.stats['agility'] = sila + 1
            self.stats['reaction'] = sila
            self.stats['strength'] = sila + 2
            self.stats['willpower'] = sila
            self.stats['logic'] = sila
            self.stats['intuition'] = sila
            self.stats['charisma'] = sila
            self.optional_powers = f'Concealment, Confusion, Guard, Natural weapon ({force}P),' \
                                   f' Noxious Breath, Search, Venom'
            self.powers = 'Animal control, Enhanced senses (Hearing, Low light vision, Smell), Fear, Movement'

        def fire(sila):
            self.stats['body'] = sila + 1
            self.stats['agility'] = sila + 2
            self.stats['reaction'] = sila + 3
            self.stats['strength'] = sila - 2
            self.stats['willpower'] = sila
            self.stats['logic'] = sila
            self.stats['intuition'] = sila + 1
            self.stats['charisma'] = sila
            self.optional_powers = 'Fear, Guard,Noxious breath, Search'
            self.powers = 'Accident, Confusion, Elemental attack, Energy aura, Engulf'
            self.special.append(('Allergy', 'Water (Severe)'))
            self.special.append(('Sprint', 'Spirits of air move + 5m per hit when sprinting'))

        def man(sila):
            self.stats['body'] = sila + 1
            self.stats['agility'] = sila
            self.stats['reaction'] = sila + 2
            self.stats['strength'] = sila - 2
            self.stats['willpower'] = sila
            self.stats['logic'] = sila
            self.stats['intuition'] = sila + 1
            self.stats['charisma'] = sila
            self.optional_powers = 'Fear, Innate spell (Known by summoner), Movement, Psychokinesis'
            self.powers = 'Accident, Concealment, Confusion, Enhanced senses (Low light, Thermographic vision), ' \
                          'Guard, Influence, Search'

        def water(sila):
            self.stats['body'] = sila
            self.stats['agility'] = sila + 1
            self.stats['reaction'] = sila + 2
            self.stats['strength'] = sila
            self.stats['willpower'] = sila
            self.stats['logic'] = sila
            self.stats['intuition'] = sila
            self.stats['charisma'] = sila
            self.optional_powers = 'Accident, Binding, Elemental attack, Energy aura, Guard, Weather control'
            self.powers = 'Concealment, Confusion, Engulf, Movement, Search'
            self.special.append(('Allergy', 'Fire(Severe)'))
            self.special.append(('Sprint', 'Spirits of water move twice as fast when in water'))

        def guardian(sila):
            self.stats['body'] = sila + 1
            self.stats['agility'] = sila + 2
            self.stats['reaction'] = sila + 3
            self.stats['strength'] = sila + 2
            self.stats['willpower'] = sila
            self.stats['logic'] = sila
            self.stats['intuition'] = sila
            self.stats['charisma'] = sila
            self.optional_powers = f'Animal control, Concealment'
            f'Elemental attack (Summoners choice), Natural weapon (DV = {sila + 2})'
            f'Psychokinesis, Skill (Combat skill)'

            self.powers = 'Fear, Guard, Magical guard, Movement'

        def sage(sila):
            self.stats['body'] = sila + 3
            self.stats['agility'] = sila - 1
            self.stats['reaction'] = sila + 2
            self.stats['strength'] = sila + 1
            self.stats['willpower'] = sila
            self.stats['logic'] = sila
            self.stats['intuition'] = sila
            self.stats['charisma'] = sila
            self.optional_powers = 'Engulf, Enhanced Senses (Hearing, Low light, Thermographic, Smell), Fear, Influence'
            self.powers = 'Confusion, Divining, Guard, Magical Guard, Search, Shadow Cloak'

        def plant(sila):
            self.stats['body'] = sila + 2
            self.stats['agility'] = sila - 1
            self.stats['reaction'] = sila
            self.stats['strength'] = sila + 1
            self.stats['willpower'] = sila
            self.stats['logic'] = sila - 1
            self.stats['intuition'] = sila
            self.stats['charisma'] = sila
            self.optional_powers = 'Accident, Confusion, Movement, Noxious Breath, Search'
            self.powers = 'Concealment, Engulf, Fear, Guard, Magical guard, Silence'

        def task(sila):
            self.stats['body'] = sila
            self.stats['agility'] = sila
            self.stats['reaction'] = sila + 2
            self.stats['strength'] = sila + 2
            self.stats['willpower'] = sila
            self.stats['logic'] = sila
            self.stats['intuition'] = sila
            self.stats['charisma'] = sila
            self.optional_powers = 'Concealment, Enhanced Senses (Hearing, Low-Light, Thermographic, Smell), ' \
                                   'Influence, Psychokinesis, Skill (Technical or Physical)'
            self.powers = 'Accident, Binding, Movement, Search'

        if self.typ == 'air':
            air(force)
        elif self.typ == 'earth':
            earth(force)
        elif self.typ == 'beast':
            beast(force)
        elif self.typ == 'fire':
            fire(force)
        elif self.typ == 'man':
            man(force)
        elif self.typ == 'water':
            water(force)
        elif self.typ == 'guardian':
            guardian(force)
        elif self.typ == 'sage':
            sage(force)
        elif self.typ == 'plant':
            plant(force)
        elif self.typ == 'task':
            task(force)

    def roll_initiative(self):
        initiative = 0
        if self.typ == 'air' or 'man' or 'water' or 'task':
            initiative = ((self.force * 2) + 2) + numpy.random.randint(low=2, high=12)
        elif self.typ == 'earth':
            initiative = ((self.force * 2) - 1) + numpy.random.randint(low=2, high=12)
        elif self.typ == 'beast' or 'sage' or 'plant':
            initiative = (self.force * 2) + numpy.random.randint(low=2, high=12)
        elif self.typ == 'fire':
            initiative = ((self.force * 2) + 3) + numpy.random.randint(low=2, high=12)
        elif self.typ == 'guardian':
            initiative = ((self.force * 2) + 1) + numpy.random.randint(low=2, high=12)
        return initiative

    def roll_astral_initiative(self):
        initiative = (self.force * 2) + numpy.random.randint(low=3, high=18)
        return initiative
