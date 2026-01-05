"""Effect for Amateur Puppeteer (TOY_828t).

Card Text: [x]<b>Mini</b>, <b>Taunt</b> <b>Deathrattle:</b> Give Undead in your hand +2/+2.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent
    pass
