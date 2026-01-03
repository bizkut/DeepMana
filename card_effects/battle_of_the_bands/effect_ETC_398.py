"""Effect for ETC_398 in BATTLE_OF_THE_BANDS"""

def setup(game, source):
    if source.controller and source.controller.hero:
        source.controller.hero.lifesteal = True