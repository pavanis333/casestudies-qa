
import json

def fix_dilemmas(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Fixes for the mislabeled 2025 (actually 2023) cases
    updates = {
        "2025-CS1": {
            "category": "Crisis Management / Personal vs Professional Duty",
            "dilemmas": [
                "Personal Duty (Son's Rites) vs Professional Duty (DC's Responsibility)",
                "Private Grief vs Public Welfare"
            ]
        },
        "2025-CS2": {
            "category": "Environmental Ethics / Social Justice",
            "dilemmas": [
                "Rights of Homeless (Housing) vs Rights of Nature (Forest)",
                "Immediate Human Needs vs Long-term Ecological Survival"
            ]
        },
        "2025-CS3": {
            "category": "Conflict of Interest / Integrity",
            "dilemmas": [
                "Familial Love (Son) vs Official Secrecy",
                "Political Pressure vs Administrative Neutrality"
            ]
        },
        "2025-CS4": {
            "category": "Corporate Governance / Procedural Integrity",
            "dilemmas": [
                "Career Growth (ACR) vs Financial Rules (GFR)",
                "Obedience to Authority vs Adherence to Law"
            ]
        },
        "2025-CS5": {
            "category": "Public Administration / Welfare Ethics",
            "dilemmas": [
                "Accountability (Punishing past wrongs) vs Efficiency (Moving forward)",
                "Administrative Clean-up vs Political backlash"
            ]
        },
        "2025-CS6": {
            "category": "International Ethics / Humanitarianism",
            "dilemmas": [
                "National Security (Border Control) vs Humanitarian Duty (Refugees)",
                "Rule of Law (No Entry) vs Compassion (Saving wounded)"
            ]
        }
    }

    count = 0
    for case in data:
        cid = case.get('id')
        if cid in updates:
            print(f"Updating dilemmas for {cid}...")
            up = updates[cid]
            case['category'] = up['category']
            case['dilemmas'] = up['dilemmas']
            count += 1

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully fixed dilemmas for {count} cases.")

if __name__ == "__main__":
    fix_dilemmas('src/data.json')
