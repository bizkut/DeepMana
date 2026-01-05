"""Effect for Twin Emperor Vek'lor (WON_134).

Card Text: [x]<b><b>Taunt</b>
Battlecry:</b> If your C'Thun has
at least 10 Attack, summon
another Emperor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_134t")