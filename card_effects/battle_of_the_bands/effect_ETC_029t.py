"""Effect for Keyboard Amplifier (ETC_029t).

Card Text: <b>Spell Damage +1</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
