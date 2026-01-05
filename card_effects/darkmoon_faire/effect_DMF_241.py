"""Effect for High Exarch Yrel (DMF_241).

Card Text: [x]<b>Battlecry:</b> If your deck has
no Neutral cards, gain
<b>Rush</b>, <b>Lifesteal</b>, <b>Taunt</b>,
and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass