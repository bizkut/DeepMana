"""Generate effects for ALL collectible cards (Arena support)."""

import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from simulator import CardDatabase


def get_primary_number(text, default=1):
    nums = [int(n) for n in re.findall(r'\b(\d+)\b', text)]
    return nums[0] if nums else default


def generate_effect_code(card):
    text = card.text.lower() if card.text else ''
    card_type_str = card.card_type.name if hasattr(card.card_type, 'name') else str(card.card_type)
    
    is_spell = 'SPELL' in str(card_type_str) or card_type_str == '5'
    has_battlecry = 'battlecry' in text
    has_deathrattle = 'deathrattle' in text
    
    if is_spell:
        func_sig = 'def on_play(game, source, target):'
    elif has_deathrattle and not has_battlecry:
        func_sig = 'def deathrattle(game, source):'
    else:
        func_sig = 'def battlecry(game, source, target):'
    
    lines = [
        f'"""Effect for {card.name} ({card.card_id}).',
        f'',
        f'Card Text: {card.text}',
        f'"""',
        '',
        'from simulator.enums import CardType',
        '',
        func_sig,
        '    player = source.controller',
        '    opponent = player.opponent',
        ''
    ]
    
    amount = get_primary_number(card.text, 1) if card.text else 1
    
    if 'deal' in text and 'damage' in text:
        if 'all' in text and 'enemy' in text:
            lines.append(f'    for m in list(opponent.board): game.deal_damage(m, {amount}, source)')
        elif 'random' in text:
            lines.append('    import random')
            lines.append(f'    targets = list(opponent.board) + ([opponent.hero] if opponent.hero else [])')
            lines.append(f'    if targets: game.deal_damage(random.choice(targets), {amount}, source)')
        else:
            lines.append(f'    if target: game.deal_damage(target, {amount}, source)')
    elif 'draw' in text:
        lines.append(f'    player.draw({amount})')
    elif 'summon' in text:
        lines.append(f'    game.summon_token(player, "{card.card_id}t")')  
    elif 'discover' in text:
        lines.append('    import random')
        lines.append('    from simulator import CardDatabase')
        lines.append('    db = CardDatabase.get_instance()')
        lines.append('    cards = [c.card_id for c in db._cards.values() if c.collectible][:100]')
        lines.append('    def on_discover(game, chosen_id):')
        lines.append('        from simulator.factory import create_card')
        lines.append('        c = create_card(chosen_id, game)')
        lines.append('        if c: player.add_to_hand(c)')
        lines.append('    game.initiate_discover(player, random.sample(cards, 3), on_discover)')
    elif 'destroy' in text:
        if 'random' in text:
            lines.append('    import random')
            lines.append('    if opponent.board: random.choice(list(opponent.board)).destroy()')
        else:
            lines.append('    if target: target.destroy()')
    elif 'restore' in text or 'heal' in text:
        lines.append(f'    if target: game.heal(target, {amount}, source)')
    elif 'give' in text or '+' in (card.text or ''):
        lines.append('    if target:')
        lines.append(f'        target._attack += {amount}')
        lines.append(f'        target._max_health += {amount}')
    elif 'gain' in text and 'armor' in text:
        lines.append(f'    if player.hero: player.hero.gain_armor({amount})')
    elif 'silence' in text:
        lines.append('    if target: game.silence(target)')
    elif 'freeze' in text:
        lines.append('    if target: target.frozen = True')
    else:
        lines.append('    pass')
    
    if has_deathrattle and has_battlecry:
        lines.extend(['', '', 'def deathrattle(game, source):', '    pass'])
    
    return '\n'.join(lines)


def main():
    print("=== Arena Card Effect Generator ===\n")
    
    db = CardDatabase.get_instance()
    db.load()
    
    existing_folders = set(os.listdir('card_effects'))
    generated = 0
    skipped = 0
    
    for card in db._cards.values():
        if not (card.collectible and card.text and len(card.text.strip()) > 5):
            continue
        
        # Check if exists in any folder
        found = False
        for folder in existing_folders:
            if folder.startswith('_') or folder == '__pycache__':
                continue
            path = f'card_effects/{folder}/effect_{card.card_id}.py'
            if os.path.exists(path):
                found = True
                break
        
        if found:
            skipped += 1
            continue
        
        # Create in appropriate folder
        folder = card.card_set.lower().replace(' ', '_')
        dir_path = f'card_effects/{folder}'
        os.makedirs(dir_path, exist_ok=True)
        
        code = generate_effect_code(card)
        with open(f'{dir_path}/effect_{card.card_id}.py', 'w', encoding='utf-8') as f:
            f.write(code)
        generated += 1
        
        if generated % 500 == 0:
            print(f'  Progress: {generated}')
    
    print(f"\n=== Complete ===")
    print(f"Generated: {generated}")
    print(f"Already existed: {skipped}")


if __name__ == "__main__":
    main()
