
import json

def enrich_data(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Knowledge Base of Answers for 2015
    updates = {
        # --- 2015 ---
        "2015-CS1": {
            "category": "Corporate Governance / Crisis Management",
            "dilemmas": [
                "Safety of Employees vs Political Pressure",
                "Integrity vs Appeasement"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Assume you are the CEO of the company. What would you do to diffuse the volatile situation on the date of gate-crashing?",
                    "answer": "**Immediate Action**: \n1. **Dialogue**: I will walk out to meet the leaders (showing courage) but keep a physical barrier (gate) for safety. \n2. **De-escalation**: Politely but firmly state that we are a professional organization and recruitment follows a process. \n3. **Buy Time**: Ask them to submit a list of candidates and promise to review it as per norms. \n4. **Backup**: Simultaneously, signal my security head to alert the police nearby."
                },
                {
                    "id": "b",
                    "question": "What could be the long-term solution to the issue discussed in the case?",
                    "answer": "**Long-term Solution**: \n1. **Transparent Recruitment**: Publish all vacancies online with clear criteria (merit-based). \n2. **Political Neutrality Policy**: A written policy that the company does not entertain political recommendations. \n3. **Community Engagement**: Run local skill development programs (CSR) so the youth feel the company adds value to them, reducing hostility."
                },
                {
                    "id": "c",
                    "question": "Analyze the consequences of each of your suggested actions.",
                    "answer": "- **Refusing Mob**: (Positive) Maintains integrity/morale. (Negative) Risk of temporary violence/vandalism. \n- **Accepting lists**: (Positive) Temporary peace. (Negative) Sets a precedent for blackmail; employees will lose respect for management."
                }
            ]
        },
        "2015-CS2": {
            "category": "Social Justice / Caste Discrimination",
            "dilemmas": [
                "Right to Equality (Dalit Cook) vs Cultural Prejudices",
                "Education (School Attendance) vs Social beliefs"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Discuss some feasible strategies to overcome the conflict and to create right ambience.",
                    "answer": "**Strategies**: \n1. **Lead by Example**: I (Sarpanch) will publicly eat the meal prepared by the cook along with my family. \n2. **Community Lunch (Sahabhoj)**: Organize a village festival where everyone eats together. \n3. **Legal Awareness**: Educate parents that untouchability is a crime (PCR Act). \n4. **Involve Mothers**: Form a 'Mothers' Committee' to supervise food quality, shifting focus from 'caste' to 'nutrition'."
                },
                {
                    "id": "b",
                    "question": "What should be the responsibilities of different social segments...?",
                    "answer": "- **Administration**: Enforce the law, do not transfer the cook (appeasement). \n- **Elders**: Must adapt to modern constitutional values. \n- **Teachers**: Validated the scientific temper in students."
                }
            ]
        },
        "2015-CS3": {
            "category": "Business Ethics / Public Health",
            "dilemmas": [
                "Profitability vs Social Welfare",
                "Accountability to Shareholders vs Duty to Humanity"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Identify the various actions that you could take;",
                    "answer": "1. **Ignore the discovery** (Focus on profit). \n2. **Full Commercial Launch** (High price to recover 50cr). \n3. **CSR/Partnership Model** (Develop it at cost/subsidy)."
                },
                {
                    "id": "b",
                    "question": "Evaluate the pros and cons of each of your actions.",
                    "answer": "- **Ignore**: High profit, but unethical. Loss of potential cure. \n- **Commercial**: Recovers cost, but the poor tribals (target group) can't afford it. Dead product. \n- **Partnership (Recommended)**: Partner with Govt (DBT/Ayushman Bharat) or WHO. They fund the R&D, company manufactures it. \n  *Pros*: Covers cost, saves lives, huge brand goodwill. \n  *Cons*: Lower profit margins."
                }
            ]
        },
        "2015-CS4": {
            "category": "Disaster Management / Triage",
            "dilemmas": [
                "Equality of Life vs VIP Culture",
                "Vulnerable Sections vs Powerful People"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "As a civil services officer ... what would be the order in which you would rescue these people and why?",
                    "answer": "**Order of Rescue**: \n1. **Medical Emergencies (Patients)**: Threat to life is immediate. \n2. **Minors (Children)**: Most vulnerable, future of the nation. \n3. **Women & Senior Citizens**: Physically less capable of surviving harsh conditions. \n4. **Tourists/Hikers**: Generally fit, can wait slightly longer. \n5. **VIPs (Politicians/Officers)**: As public servants, they should be the *last* to leave (Captain of the ship). \n6. **Prisoners**: State's responsibility, but lower priority than free citizens in medical triage. \n\n**Justification**: Protocol of 'Antyodaya' and Medical Triage (Save the most critical first). VIP status is irrelevant in a disaster."
                }
            ]
        },
        "2015-CS5": {
            "category": "Corruption / Heritage Conservation",
            "dilemmas": [
                "Obedience to Senior vs Investigating Fraud",
                "Development (School) vs Heritage (Fort)"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "List the likely vested interests of the concerned parties.",
                    "answer": "1. **Senior Officer**: Wants a smooth visit, possibly complicit or just wants 'work done'. \n2. **Predecessor**: Likely took a bribe/favour from the Sarpanch (relative) to acquire useless land. \n3. **Sarpanch**: Sold his own/relative's land at high 'development' rates."
                },
                {
                    "id": "b",
                    "question": "Discuss the options... Can you suggest any other option?",
                    "answer": "**My Option**: **Written Report with Alternatives**. \n I will prepare a report stating: \n1. The land is a **Heritage Site** (ASI rules prohibit construction). \n2. Technical non-feasibility (walls running across). \n3. **Conflict of Interest** (Predecessor-Sarpanch link). \n4. **Propose an Alternative Plot**: Identify a better site closer to the village and suggest a 'Land Swap' to save government money. This protects me, saves the heritage, and ensures the school is actually useful."
                }
            ]
        },
        "2015-CS6": {
            "category": "Gender Issues / Social Reform",
            "dilemmas": [
                "Tradition vs Modernity",
                "Safety vs Freedom",
                "Patriarchy vs Constitutional Rights"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What steps would you take to ensure girls’ safety without disrupting their education?",
                    "answer": "1. **Safe Transport**: Arrange dedicated school buses or escort groups ('Police Didi' patrols). \n2. **Zero Tolerance**: Arrest the molesters immediately to restore confidence. \n3. **Self-Defense**: Judo/Karate training in schools."
                },
                {
                    "id": "b",
                    "question": "How would you manage and mould patriarchic attitude of the village elders...?",
                    "answer": "1. **Persuasion (Soft Power)**: Show them achievers (ISRO women scientists, etc.). \n2. **Highlight Economics**: Educated girls earn more -> Family prospers. \n3. **Engage 'Positive Deviants'**: Fathers who support their daughters should be made 'Ambassadors' to convince other elders."
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
