
import json

def diagnose_missing_dilemmas(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    missing = []
    for case in data:
        if "Ethical Dilemma 1" in case.get('dilemmas', []):
            missing.append(case['id'])
    
    print(f"Total cases with placeholder dilemmas: {len(missing)}")
    print("IDs:", missing)

diagnose_missing_dilemmas('src/data.json')
