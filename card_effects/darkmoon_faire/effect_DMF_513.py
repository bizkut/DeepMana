"""Effect for Shadow Clone (DMF_513).

Card Text: <b>Secret:</b> After a minion attacks your hero, summon a copy of it with <b>Stealth</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_513t")