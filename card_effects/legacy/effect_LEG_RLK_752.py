"""Effect for Rime Sculptor (LEG_RLK_752).

Card Text: [x]<b>Battlecry:</b> Summon two
2/1 Rime Elementals with
"<b>Deathrattle:</b> Deal 2 damage
to a random enemy."
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 2, source)


def deathrattle(game, source):
    pass