"""Effect for Rustsworn Initiate (BT_008).

Card Text: <b>Deathrattle:</b> Summon a 1/1 Impcaster with
<b>Spell Damage +1</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_008t")