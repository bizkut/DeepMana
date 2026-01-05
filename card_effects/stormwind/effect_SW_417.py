"""Effect for SI:7 Assassin (SW_417).

Card Text: [x]Costs (1) less for each SI:7
card you've played this game.
<b>Combo:</b> Destroy an
enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()