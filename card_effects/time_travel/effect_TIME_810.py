"""Effect for Past Silvermoon (TIME_810).

Card Text: [x]Deal 5 damage to a
random enemy minion.
<i>Advance to the present!</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 5, source)