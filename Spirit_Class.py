import numpy
import Spirit_types


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
        match self.typ:
            case 'air':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.air(self.stats, force)
            case 'earth':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.earth(self.stats, force)
            case 'beast':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.beast(self.stats, force)
            case 'fire':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.fire(self.stats, force)
            case 'man':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.man(self.stats, force)
            case 'water':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.water(self.stats, force)
            case 'guardian':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.guardian(self.stats, force)
            case 'sage':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.sage(self.stats, force)
            case 'plant':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.plant(self.stats, force)
            case 'task':
                self.stats, self.special, self.optional_powers, self.powers = Spirit_types.task(self.stats, force)

    def roll_initiative(self):
        initiative = 0
        match self.typ:
            case 'air' | 'man' | 'water' | 'task':
                initiative = ((self.force * 2) + 2) + numpy.random.randint(low=2, high=12)
            case 'earth':
                initiative = ((self.force * 2) - 1) + numpy.random.randint(low=2, high=12)
            case 'beast' | 'sage' | 'plant':
                initiative = (self.force * 2) + numpy.random.randint(low=2, high=12)
            case 'fire':
                initiative = ((self.force * 2) + 3) + numpy.random.randint(low=2, high=12)
            case 'guardian':
                initiative = ((self.force * 2) + 1) + numpy.random.randint(low=2, high=12)
        return initiative

    def roll_astral_initiative(self):
        initiative = (self.force * 2) + numpy.random.randint(low=3, high=18)
        return initiative
