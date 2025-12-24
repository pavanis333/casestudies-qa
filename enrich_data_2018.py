
import json

def enrich_data(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Knowledge Base of Answers for 2018
    updates = {
        # --- 2018 ---
        "2018-CS1": {
            "category": "Administrative Ethics / Rules vs Values",
            "dilemmas": [
                "Rule of Law (Strict Criteria) vs Compassion",
                "Procedural Justice vs Substantive Justice"
            ],
            "questions": [
                {
                    "id": "q",
                    "question": "How should Rakesh respond?",
                    "answer": "**Rakesh's Response**: \n1. **Uphold the Rule**: He *cannot* include ineligible beneficiaries in the specific scheme, as this would be illegal and invite audit objections (Rule of Law). \n2. **Exercise Compassion**: However, he should not abandon them. He can: \n   - Use **discretionary funds** (e.g., District Red Cross Society). \n   - Recommend their case for **Chief Minister's Relief Fund**. \n   - Partner with **NGOs/CSR** initiatives to fund the surgeries. \n**Conclusion**: A civil servant must be a 'change agent', finding solutions *within* or *around* the rules, not breaking them."
                }
            ]
        },
        "2018-CS2": {
            "category": "Conflict of Interest / Political Pressure",
            "dilemmas": [
                "Private Gain (Land value) vs Public Loss (Deforestation/Displacement)",
                "Political Obedience vs Public Accountability"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Critically examine various conflicts of interest and explain what your responsibilities are as a public servant.",
                    "answer": "**Conflicts of Interest**: \n1. **Minister's Interest**: Realignment benefits his farmhouse but costs the public exchequer. \n2. **Personal Interest**: The offer of land for your wife is a bribe (Quid Pro Quo). \n\n**Responsibilities**: \n1. **Fiduciary Duty**: You are a trustee of public resources. Wasting money on a longer route is a breach of trust. \n2. **Environmental Stewardship**: Preventing unnecessary deforestation. \n3. **Fearlessness**: You must refuse the realignment and the land offer. If the Minister persists, record his instructions on file (Rule 3 of All India Services Conduct Rules)."
                }
            ]
        },
        "2018-CS3": {
            "category": "Law & Order / Social Development",
            "dilemmas": [
                "Policing Symptoms (Raids) vs Treating Causes (Development)",
                "Law Enforcement vs Socio-economic Upliftment"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Which new approach will you adopt to bring the problem under control?",
                    "answer": "**Multi-Pronged Strategy (Samdam-Danda-Bhed)**: \n1. **Developmental Intervention**: The root cause is poverty. Liaise with the District Collector to implement MGNREGA and Skill Development schemes in the affected areas. \n2. **Community Policing**: Engage women's Self-Help Groups (SHGs) to act as informers and pressure groups against liquor dens (controlled social pressure). \n3. **Alternative Livelihood**: Promote cottage industries (dairy, poultry) to replace income from distillation. \n4. **Strict Enforcement**: Continue raids but focus on the 'Kingpins' rather than just the poor carriers."
                }
            ]
        },
        "2018-CS4": {
            "category": "Environmental Ethics / Crisis Management",
            "dilemmas": [
                "Right to Livelihood (Workers) vs Right to Health (Villagers)",
                "Economic Growth vs Ecological Sustainability"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "As a senior officer entrusted with the responsibility of handling this issues, how are you going to address it?",
                    "answer": "**Short Term**: \n1. **Immediate Relief**: Ensure unemployment allowance for retrenched workers from the company's assets or state funds. \n2. **Medical Camps**: For the affected villagers. \n\n**Long Term**: \n1. **Polluter Pays**: Seize company assets to fund environmental restoration. \n2. **Re-skilling**: Train the workers for other industries. \n3. **Sustainable Industrialization**: Ensure future units have Zero Liquid Discharge (ZLD) technologies. \n**Conclusion**: You cannot trade health for jobs. The unit must remain closed until it proves 100% compliance, but the state must cushion the blow for the workers."
                }
            ]
        },
        "2018-CS5": {
            "category": "Tax Ethics / Utilitarianism",
            "dilemmas": [
                "Letter of the Law (Technicalities) vs Spirit of the Law (Public Good)",
                "State Revenue vs Public Health Infrastructure"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "As the head of the tax agency, which course of action will you opt and why?",
                    "answer": "**Analysis**: \n- **Option 1 (Ignore Technicalities)**: Pragmatic. Gets the tax, allows the hospital to come up (Public Good). \n- **Option 2 (Strict Enforcement)**: Rigid. Wastes time, potentially kills the hospital project. \n\n**Decision**: **Option 1**. \n**Reason**: Technical defaults (procedural errors) should be distinguished from Tax Evasion (criminal intent). Since the doctor is paying the substantial dues, penalizing him for minor technicalities is 'Tax Terrorism'. Facilitating the hospital serves the larger public interest of the neglected region, which aligns with the state's ultimate goal of welfare."
                }
            ]
        },
        "2018-CS6": {
            "category": "Whistleblowing / International Ethics",
            "dilemmas": [
                "National Security vs Civil Liberties (Privacy)",
                "Legal Duty (Espionage Act) vs Moral Duty (Transparency)"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Do you agree that Snowden’s actions were ethically justified even if legally prohibited? Why or why not?",
                    "answer": "**Yes, Ethically Justified.** \n**Arguments**: \n1. **Social Contract**: Governments exist to serve people. Mass surveillance without consent violates the contract. \n2. **Transparency**: A democracy cannot function if citizens don't know the extent of state power. \n3. **Higher Law**: When positive law (Espionage Act) violates natural justice (Privacy), civil disobedience is a moral duty (Gandhian principle). \n\n**Counter-View**: He compromised security methods. However, the *scale* of the violation (global dragnet) arguably outweighed the security risks."
                }
            ]
        }
    }

    # Apply updates
    count = 0
    for case in data:
        cid = case.get('id')
        if cid in updates:
            print(f"Updating {cid}...")
            up = updates[cid]
            if 'category' in up:
                case['category'] = up['category']
            if 'dilemmas' in up:
                case['dilemmas'] = up['dilemmas']
            
            kb_qs = {q['id']: q for q in up['questions']}
            
            for i, q_obj in enumerate(case['questions']):
                qid = q_obj.get('id')
                if qid in kb_qs:
                    q_obj['answer'] = kb_qs[qid]['answer']
                elif len(case['questions']) == len(up['questions']):
                    key = chr(97 + i)
                    if key in kb_qs:
                        q_obj['answer'] = kb_qs[key]['answer']
            
            count += 1

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully enriched {count} cases.")

if __name__ == "__main__":
    enrich_data('src/data.json')
