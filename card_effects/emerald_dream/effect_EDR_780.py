"""Effect for Bloodthistle Illusionist (EDR_780).

Card Text: [x]<b>Battlecry:</b> Summon a copy
of this. One secretly dies
when it takes damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_780t")