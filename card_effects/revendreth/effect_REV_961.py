"""Effect for Elitist Snob (REV_961).

Card Text: [x]<b>Battlecry:</b> For each Paladin
card in your hand, randomly 
gain <b>Divine Shield</b>, <b>Lifesteal</b>, 
<b>Rush</b>, or <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass