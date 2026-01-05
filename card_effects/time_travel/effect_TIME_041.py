"""Effect for Futuristic Forefather (TIME_041).

Card Text: [x]<b>Taunt</b>. <b>Battlecry:</b> Look at 3
cards. Guess which one is
in your opponent's hand
to gain +4 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)