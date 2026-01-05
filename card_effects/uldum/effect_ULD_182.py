"""Effect for Spitting Camel (ULD_182).

Card Text: [x]At the end of your turn,
  deal 1 damage to another  
random friendly minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 1, source)