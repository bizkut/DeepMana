"""Effect for Timeway Warden (TIME_442).

Card Text: [x]<b>Battlecry:</b> Imprison an
enemy minion. It goes
<b>Dormant</b> for 10,000 turns.
   <b>Deathrattle:</b> Awaken it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass


def deathrattle(game, source):
    pass