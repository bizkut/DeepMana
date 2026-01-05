"""Effect for Jade Chieftain (WON_084).

Card Text: <b>Battlecry:</b> Summon a{1} {0} <b>Jade Golem</b>. Give it <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_084t")