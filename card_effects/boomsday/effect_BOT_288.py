"""Effect for Lab Recruiter (BOT_288).

Card Text: <b>Battlecry:</b> Shuffle 3 copies of a friendly minion into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass