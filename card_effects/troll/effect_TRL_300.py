"""Effect for Shirvallah, the Tiger (TRL_300).

Card Text: [x]<b>Divine Shield</b>, <b>Rush</b>, <b>Lifesteal</b>
 Costs (1) less for each Mana
you've spent on spells.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass