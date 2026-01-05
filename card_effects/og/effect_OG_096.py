"""Effect for Twilight Darkmender (OG_096).

Card Text: <b>Battlecry:</b> If your C'Thun  has at least 10 Attack, restore #10 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 10, source)