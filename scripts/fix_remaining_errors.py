import os
import sys
sys.path.insert(0, os.getcwd())
from simulator import CardDatabase

db = CardDatabase.get_instance()
db.load()

error_ids = ['CORE_CS2_074', 'CORE_EX1_162', 'CORE_EX1_507', 'CORE_EX1_509', 'CORE_EX1_565', 'CORE_EX1_604', 'CS3_017', 'GDB_110', 'GDB_231', 'GDB_843', 'RLK_958', 'SC_002', 'SC_412']

def regenerate_safe(card_id):
    card = db._cards.get(card_id)
    if not card: return
    
    text = card.text.lower() if card.text else ''
    card_type_str = str(card.card_type)
    is_spell = 'SPELL' in card_type_str or '5' in card_type_str
    
    if is_spell:
        func = 'def on_play(game, source, target):'
    else:
        func = 'def battlecry(game, source, target):'
    
    safe_text = card.text.replace('"', "'").replace('\n', ' ') if card.text else ""
    
    content = f'"""Effect for {card.name} ({card.card_id}).\n\nCard Text: {safe_text}\n"""\n\n{func}\n    player = source.controller\n    pass\n'
    
    # Find folder
    for folder in os.listdir('card_effects'):
        if folder.startswith('_') or folder == '__pycache__':
            continue
        path = f'card_effects/{folder}/effect_{card_id}.py'
        if os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Regenerated safe: {path}')
            return

for cid in error_ids:
    regenerate_safe(cid)
