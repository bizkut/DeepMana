"""Effect for Prince Valanar (CORE_ICC_853).

Card Text: <b>Battlecry:</b> If your deck has no 4-Cost cards, gain <b>Lifesteal</b> and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass