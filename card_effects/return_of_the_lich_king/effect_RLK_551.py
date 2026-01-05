"""Effect for Blightblood Berserker (RLK_551).

Card Text: <b>Taunt</b>, <b>Lifesteal</b>, <b>Reborn</b>
<b>Deathrattle:</b> Deal 3 damage to a random enemy.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    import random
    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])
    if targets: game.deal_damage(random.choice(targets), 3, source)