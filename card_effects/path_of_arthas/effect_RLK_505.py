"""Effect for Marrow Manipulator (RLK_505).

Card Text: [x]<b>Battlecry:</b> Spend up to 5
<b>Corpses</b>. Deal 2 damage to
a random enemy for each.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 5, source)