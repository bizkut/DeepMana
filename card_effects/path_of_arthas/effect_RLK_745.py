"""Effect for Malignant Horror (RLK_745).

Card Text: [x]<b>Reborn</b>
At the end of your turn,
spend 4 <b>Corpses</b> to summon
a copy of this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_745t")