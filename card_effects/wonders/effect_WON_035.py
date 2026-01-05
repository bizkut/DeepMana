"""Effect for Goblin Blastmage (WON_035).

Card Text: [x]<b>Battlecry:</b> If you control
a Mech, deal 6 damage
randomly split among
all enemies.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 6, source)