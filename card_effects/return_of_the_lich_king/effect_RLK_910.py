"""Effect for Shadow Suffusion (RLK_910).

Card Text: [x]Give your minions
"<b>Deathrattle:</b> Deal 3
damage to a random
enemy."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)