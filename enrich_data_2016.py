
import json

def enrich_data(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Knowledge Base of Answers for 2016
    updates = {
        # --- 2016 ---
        "2016-CS1": {
            "category": "Corporate Ethics / Whistleblowing",
            "dilemmas": [
                "Livelihood (Family) vs Public Health (River)",
                "Loyalty to Company vs Loyalty to Society"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What arguments can you advance to show her that keeping quiet is not morally right?",
                    "answer": "1. **Complicity**: Silence is consent. If she knows about the poison and does nothing, she is morally (and legally) complicit in the harm caused to the villagers. \n2. **Utilitarianism**: The health of thousands of villagers > the salary of one person. \n3. **Long-term Risk**: If the company is caught later, she might face criminal negligence charges for being the compliance engineer who ignored it."
                },
                {
                    "id": "b",
                    "question": "What course of action would you advice her to adopt and why?",
                    "answer": "**Advice**: **Whistleblow anonymously**. \n**Action Plan**: \n1. **Gather Evidence**: Collect samples/documents proving the discharge. \n2. **Anonymous Reporting**: Send the evidence to the State Pollution Control Board and Media. \n3. **Search for new job**: This company is unethical and unsustainable; she should leave asap anyway. \n**Why**: This protects her identity (and family income) while ensuring the pollution stops."
                }
            ]
        },
        "2016-CS2": {
            "category": "Development vs Displacement",
            "dilemmas": [
                "National Development vs Tribal Rights",
                "Monetary Compensation vs Loss of Culture/Livelihood"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Analyze the ethical issues in this case. ... what would be the main elements of your suggested policy?",
                    "answer": "**Issues**: Injustice of 'Privatizing Profits, Socializing Costs'. Tribals lose their land (mother) for cash which they cannot manage. \n\n**Policy Elements**: \n1. **Land for Land**: Compensation should be land-based, not just cash. \n2. **Skill Development**: Mandatory training for youth before displacement. \n3. **Stakeholder Share**: Displaced families should get percentage shares/stock in the new project (be owners, not victims). \n4. **Social Impact Assessment (SIA)**: Must be binding."
                }
            ]
        },
        "2016-CS3": {
            "category": "Administrative Discretion / Compassion",
            "dilemmas": [
                "Rule of Law (Documents) vs Social Justice (Destitution)",
                "Bureaucratic Rigidness vs Human Rights"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Can you think of a rational way to resolve this dilemma?",
                    "answer": "**Yes**. The 'Rational Way' is to help her **get** the documents, not just reject her. \n**Action**: \n1. As an officer, I can order a field enquiry (Panchnama) to verify her status. \n2. Use this official verification to issue her a temporary ID/certificate. \n3. Enroll her provisionally while her permanent papers are processed."
                },
                {
                    "id": "b",
                    "question": "Give your reasons for it.",
                    "answer": "**Reason**: Rules exist to prevent fraud, not to exclude the genuine poor. If I am convinced of her destitution, my duty is to bridge the gap between her and the state, not build a wall of paperwork. This is the spirit of 'Antyodaya'."
                }
            ]
        },
        "2016-CS4": {
            "category": "Domestic Violence / Intervention",
            "dilemmas": [
                "Privacy vs Human Rights",
                "Professional Relationship (Boss) vs Moral Duty"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Just ignore thinking about it because it is their personal matter.",
                    "answer": "**Consequence**: You become a bistander to a crime. The violence will escalate, potentially leading to severe injury or death. Morally indefensible."
                },
                {
                    "id": "b",
                    "question": "Repost the case to the appropriate authority.",
                    "answer": "**Consequence**: Police/Women's Commission might intervene. However, without evidence, it might be 'he said, she said'. It will destroy your relationship with the boss and might affect your career."
                },
                {
                    "id": "c",
                    "question": "Your own innovative approach towards situation.",
                    "answer": "**Approach**: **Constructive Intervention**. \n1. **Talk to the Wife**: Wait for a moment when the boss is away, offer her help/helplines. Empower her to file the complaint herself. \n2. **Subtle Signal**: Mention generally in office discussions about strict laws against domestic violence to let the boss know society watches. \n3. **Anonymous Tip**: If violence continues, call the police anonymously/Neighbours when the shouting starts."
                }
            ]
        },
        "2016-CS5": {
            "category": "Development / Socio-economic Impact",
            "dilemmas": [
                "Economic Growth vs Social Order",
                "Outsiders vs Locals"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Identify the issues involved in the case.",
                    "answer": "1. **Cultural Shock**: Influx of 'aliens' (migrants) disturbing the tranquil rural life. \n2. **Inflation**: High salaries of company empoyees driving up local prices. \n3. **Gentrification**: Locals feeling marginalized in their own land."
                },
                {
                    "id": "b",
                    "question": "What can be suggested to satisfy the company’s goal and to address the residents’ concern?",
                    "answer": "**Suggestions**: \n1. **Local Hiring Quota**: Ensure 50%+ jobs go to locals to give them a stake. \n2. **CSR for Community**: Invest in local schools/hospitals open to all, not just employees. \n3. **Township Integration**: Design company housing to be inclusive, not a gated fortress. \n4. **Dialogue**: Regular town-halls to address grievances."
                }
            ]
        },
        "2016-CS6": {
            "category": "NGOs / Governance",
            "dilemmas": [
                "Voluntarism vs Red Tape",
                "Corruption vs Public Service"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Analyze the ethical issues in this case. ... What measures can you suggest...?",
                    "answer": "**Issues**: \n1. **Harassment of the Good**: Honest NGOs faced with bribe demands quit, leaving only the corrupt ones. \n2. **Bureaucratic Apathy**: Viewing all NGOs with suspicion. \n\n**Measures**: \n1. **Single Window Clearance**: For school permits. \n2. **Deemed Approval**: If no objection is raised in 30 days, permission is automatic. \n3. **Online Tracking**: No physical interface with officials (reduces bribery). \n4. **Accreditation**: Rating NGOs based on transparency; 'Green Channel' for top-rated NGOs like Saraswati's."
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
