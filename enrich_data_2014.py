
import json

def enrich_data(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Knowledge Base of Answers for 2014
    updates = {
        # --- 2014 ---
        "2014-CS1": {
            "category": "Environment vs Development",
            "dilemmas": [
                "Economic Growth vs Ecological Sustainability",
                "Short-term Gain vs Long-term Survival"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Analyze the ethical issues in this case. ... strategies ...",
                    "answer": "**Strategies for Sustainable Development**: \n1. **Green GDP**: Incorporate environmental costs into economic accounting. \n2. **EIA (Environmental Impact Assessment)**: Make it independent and binding, not just a formality. \n3. **Polluter Pays Principle**: Strict reinforcement. \n4. **Renewable Shift**: Incentivize transition to solar/wind (National Solar Mission). \n5. **Circular Economy**: Reduce-Reuse-Recycle to minimize waste."
                }
            ]
        },
        "2014-CS2": {
            "category": "Administrative Ethics / Integrity",
            "dilemmas": [
                "Pragmatism (Survival) vs Idealism (Values)",
                "Individual Gain vs Systemic Rot"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Critically analyze the above viewpoints ... what will be your advice...?",
                    "answer": "**Critique**: \n1. **Path of Least Resistance**: Allows evil to flourish. 'The only thing necessary for the triumph of evil is for good men to do nothing.' \n2. **Minority Ineffectiveness**: History proves otherwise. Gandhi, Mandela were minorities. \n3. **Small Bribes**: 'Grease money' destroys the poor. It is not efficiency; it is extortion. \n\n**Advice**: \n\"Friend, true success is not just career growth but inner peace. If you compromise now on small things, you will eventually compromise on national security or public safety. Be the 'change you want to see'. A system of 100 corrupt officers needs 1 honest leader to check them.\""
                }
            ]
        },
        "2014-CS3": {
            "category": "Workplace Ethics / Sexual Harassment (False Complaint)",
            "dilemmas": [
                "Personal Reputation vs Duty to Discipline",
                "Justice for Women vs Misuse of Laws"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Evaluate all of them and suggest the best course of action...",
                    "answer": "**Options Analysis**: \n1. **Go Soft**: Saves reputation but encourages indiscipline. (Cowardly). \n2. **Ignore Commission**: Disrespectful to a statutory body. (Arrogant). \n\n**Best Course**: **Proceed Firmly + Cooperate with Commission**. \n1. **Disciplinary Action**: Continue proceedings against the ringleaders. Do not bargain. \n2. **Commission Reply**: Submit a detailed explanation proving the *timing* of the complaint (it came *after* the show-cause notice). Attach evidence of their indiscipline and the show-cause notices. \n3. **Defamation**: Warn that filing a false complaint is punishable under IPC."
                }
            ]
        },
        "2014-CS4": {
            "category": "Corporate Ethics / Corruption",
            "dilemmas": [
                "Business Survival vs Ethical Integrity",
                "Shareholder Value vs National Value"
            ],
            "questions": [
                {
                    "id": "i",
                    "question": "What those arguments could be? Could there be any better way...?",
                    "answer": "**Arguments for Bribing**: Saves jobs, ensures company survival, 'everyone does it'. \n**Arguments against**: Illegal, feeds the corruption cycle, risk of blacklisting if caught. \n\n**The Third Way (Ethical Action)**: \n1. **Refuse to Bribe**: Stand firm. \n2. **Record the Demand**: Use a spy camera/voice recorder to capture the officer demanding the bribe. \n3. **Whistleblow**: Send the proof to the Vigilance Commission (CVC) and the Minister in charge. \n4. **Publicize**: If the tender is unfairly rejected, approach the courts/media with the evidence. This risky path protects your integrity and might even win you the contract due to public pressure."
                }
            ]
        },
        "2014-CS5": {
            "category": "Whistleblowing / Administrative Corruption",
            "dilemmas": [
                "Conformity vs Conscience",
                "Career Safety vs Public Interest"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Indicate various options ... How would you help him...?",
                    "answer": "**Options**: \n1. **Follow Advice (Ignorance)**: Safe career, spiritual death. \n2. **Resign**: Escapism. \n3. **Fight from Within**: Gather evidence, report to CVC/CBI. \n\n**Advice**: \nChoose **Option 3**. \n- Document everything. \n- Use **Anonymous Whistleblowing** mechanisms (PIDPI Resolution) to protect identity. \n- Do not be disillusioned; the system is testing your mettle. Real service begins when you fight the rot, not just sign files."
                }
            ]
        },
        "2014-CS6": {
            "category": "Urbanization / Migration",
            "dilemmas": [
                "Urban Pull vs Rural Push",
                "Liberty of Movement vs Unmanageable Cities"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Educated rural youth are trying to shift to urban areas;",
                    "answer": "**Reason**: Lack of 'White Collar' jobs in villages. Agriculture is seen as 'low status'. \n**Solution**: **Rurban Mission**. Create urban-like amenities (internet, cafes, service sector jobs) in rural clusters."
                },
                {
                    "id": "b",
                    "question": "Landless poor peiople are migrating to urban slums;",
                    "answer": "**Reason**: Distress migration due to farm mechanization and drought. \n**Solution**: **MGNREGA 2.0**. Link it to agriculture to make farming viable. **MSME Clusters** in villages to absorb surplus labor."
                },
                {
                    "id": "c",
                    "question": "Even some farmers are selling off their land ... What feasible steps...?",
                    "answer": "**Steps**: \n1. **Make Farming PROFITABLE**: MSP reform, better irrigation, Food Processing industries near farms (Amul model). \n2. **Satellite Towns**: Develop Tier-2/3 cities to decongest metros. \n3. **Reverse Migration Incentives**: Tax breaks for industries setting up in rural areas."
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
                    # Handle special case for 2014-CS4 which has "i" instead of "a"
                    elif 'i' in kb_qs and i == 0:
                         q_obj['answer'] = kb_qs['i']['answer']
            
            count += 1

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully enriched {count} cases.")

if __name__ == "__main__":
    enrich_data('src/data.json')
