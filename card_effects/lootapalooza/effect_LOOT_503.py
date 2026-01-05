"""Effect for Lesser Onyx Spellstone (LOOT_503).

Card Text: Destroy 1 random enemy minion.
<i>(Play 3 <b>Deathrattle</b> cards to upgrade.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()