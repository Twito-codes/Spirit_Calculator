options = ['Air', 'Earth', 'Fire', 'Water', 'Beast', 'Man', 'Guardian', 'Sage', 'Plant', 'Task']


def air(stats, sila):
    special = []
    stats['body'] = sila - 2
    stats['agility'] = sila + 3
    stats['reaction'] = sila + 4
    stats['strength'] = sila - 3
    stats['willpower'] = sila
    stats['intuition'] = sila
    stats['charisma'] = sila
    stats['logic'] = sila
    optional_powers = 'Elemental attack, Energy Aura, Fear, Guard, Noxious breath, Psychokinesis'
    powers = 'Accident, Concealment, Confusion, Engulf, Movement, Search'
    special.append(('Sprint', 'Spirits of air move +10m per hit when sprinting.'))
    return stats, special, optional_powers, powers


def earth(stats, sila):
    special = []
    stats['body'] = sila + 4
    stats['agility'] = sila - 2
    stats['reaction'] = sila - 1
    stats['strength'] = sila + 4
    stats['willpower'] = sila
    stats['logic'] = sila - 1
    stats['intuition'] = sila
    stats['charisma'] = sila
    optional_powers = 'Concealment, Confusion, Engulf, Elemental attack, Fear'
    powers = 'Binding, Guard, Movement, Search'
    return stats, special, optional_powers, powers


def beast(stats, sila):
    special = []
    stats['body'] = sila + 2
    stats['agility'] = sila + 1
    stats['reaction'] = sila
    stats['strength'] = sila + 2
    stats['willpower'] = sila
    stats['logic'] = sila
    stats['intuition'] = sila
    stats['charisma'] = sila
    optional_powers = f'Concealment, Confusion, Guard, Natural weapon ({sila}P),' \
                      f' Noxious Breath, Search, Venom'
    powers = 'Animal control, Enhanced senses (Hearing, Low light vision, Smell), Fear, Movement'
    return stats, special, optional_powers, powers


def fire(stats, sila):
    special = []
    stats['body'] = sila + 1
    stats['agility'] = sila + 2
    stats['reaction'] = sila + 3
    stats['strength'] = sila - 2
    stats['willpower'] = sila
    stats['logic'] = sila
    stats['intuition'] = sila + 1
    stats['charisma'] = sila
    optional_powers = 'Fear, Guard,Noxious breath, Search'
    powers = 'Accident, Confusion, Elemental attack, Energy aura, Engulf'
    special.append(('Allergy', 'Water (Severe)'))
    special.append(('Sprint', 'Spirits of air move + 5m per hit when sprinting'))
    return stats, special, optional_powers, powers


def man(stats, sila):
    special = []
    stats['body'] = sila + 1
    stats['agility'] = sila
    stats['reaction'] = sila + 2
    stats['strength'] = sila - 2
    stats['willpower'] = sila
    stats['logic'] = sila
    stats['intuition'] = sila + 1
    stats['charisma'] = sila
    optional_powers = 'Fear, Innate spell (Known by summoner), Movement, Psychokinesis'
    powers = 'Accident, Concealment, Confusion, Enhanced senses (Low light, Thermographic vision), ' \
             'Guard, Influence, Search'
    return stats, special, optional_powers, powers


def water(stats, sila):
    special = []
    stats['body'] = sila
    stats['agility'] = sila + 1
    stats['reaction'] = sila + 2
    stats['strength'] = sila
    stats['willpower'] = sila
    stats['logic'] = sila
    stats['intuition'] = sila
    stats['charisma'] = sila
    optional_powers = 'Accident, Binding, Elemental attack, Energy aura, Guard, Weather control'
    powers = 'Concealment, Confusion, Engulf, Movement, Search'
    special.append(('Allergy', 'Fire(Severe)'))
    special.append(('Sprint', 'Spirits of water move twice as fast when in water'))
    return stats, special, optional_powers, powers


def guardian(stats, sila):
    special = []
    stats['body'] = sila + 1
    stats['agility'] = sila + 2
    stats['reaction'] = sila + 3
    stats['strength'] = sila + 2
    stats['willpower'] = sila
    stats['logic'] = sila
    stats['intuition'] = sila
    stats['charisma'] = sila
    optional_powers = f'Animal control, Concealment'
    f'Elemental attack (Summoners choice), Natural weapon (DV = {sila + 2})'
    f'Psychokinesis, Skill (Combat skill)'

    powers = 'Fear, Guard, Magical guard, Movement'
    return stats, special, optional_powers, powers


def sage(stats, sila):
    special = []
    stats['body'] = sila + 3
    stats['agility'] = sila - 1
    stats['reaction'] = sila + 2
    stats['strength'] = sila + 1
    stats['willpower'] = sila
    stats['logic'] = sila
    stats['intuition'] = sila
    stats['charisma'] = sila
    optional_powers = 'Engulf, Enhanced Senses (Hearing, Low light, Thermographic, Smell), Fear, Influence'
    powers = 'Confusion, Divining, Guard, Magical Guard, Search, Shadow Cloak'
    return stats, special, optional_powers, powers


def plant(stats, sila):
    special = []
    stats['body'] = sila + 2
    stats['agility'] = sila - 1
    stats['reaction'] = sila
    stats['strength'] = sila + 1
    stats['willpower'] = sila
    stats['logic'] = sila - 1
    stats['intuition'] = sila
    stats['charisma'] = sila
    optional_powers = 'Accident, Confusion, Movement, Noxious Breath, Search'
    powers = 'Concealment, Engulf, Fear, Guard, Magical guard, Silence'
    return stats, special, optional_powers, powers


def task(stats, sila):
    special = []
    stats['body'] = sila
    stats['agility'] = sila
    stats['reaction'] = sila + 2
    stats['strength'] = sila + 2
    stats['willpower'] = sila
    stats['logic'] = sila
    stats['intuition'] = sila
    stats['charisma'] = sila
    optional_powers = 'Concealment, Enhanced Senses (Hearing, Low-Light, Thermographic, Smell), ' \
                      'Influence, Psychokinesis, Skill (Technical or Physical)'
    powers = 'Accident, Binding, Movement, Search'
    return stats, special, optional_powers, powers
