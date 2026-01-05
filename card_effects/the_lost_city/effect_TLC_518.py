"""Effect for Interrogation (TLC_518).

Card Text: Shuffle three 3/3 Ninjas with <b>Stealth</b> into your deck that are <b>Summoned When Drawn</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)