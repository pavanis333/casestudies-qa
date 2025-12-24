
import json

def enrich_data(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Knowledge Base of Answers for 2020
    updates = {
        # --- 2020 ---
        "2020-CS1": {
            "category": "Public Finance / Social Justice",
            "dilemmas": [
                "Fiscal Prudence vs Social Welfare",
                "Political Expediency (Polls) vs Long-term Commitment (Housing)",
                "International Reputation vs Domestic Obligation"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Ethical issues involved in re-appropriation of funds from a welfare project to the developmental projects.",
                    "answer": "1. **Distributive Justice**: Diversion of funds from 'weaker sections' (Housing) to corporate/industrial projects violates the principle of prioritizing the most vulnerable (Antyodaya). \n2. **Trust**: The government made a promise (Budgetary Allocation). Breaking it for unrelated projects erodes public trust. \n3. **Accountability**: Funds voted by Parliament for a specific head should not be arbitrarily moved by the Executive."
                },
                {
                    "id": "b",
                    "question": "Given the need for proper utilization of public funds, discuss the options available to Rajesh Kumar. Is resigning a worthy option?",
                    "answer": "**Options**: \n1. **Approve Re-appropriation**: Easy path, pleases seniors, but unethical. \n2. **Resign**: Escapism. Does not solve the problem. \n3. **Innovative Financing**: Suggest alternative routes. \n\n**Is Resigning worthy?**: No. Resignation is a last resort for illegal commands. Here, it is a policy prioritization conflict. A civil servant must stay and advise. \n\n**Recommended Action**: Rajesh should propose a **Supplementary Grant** in the upcoming Winter Session of Parliament or seek a short-term loan/bond issuance for the PSUs, rather than cannibalizing the poor's housing fund."
                }
            ]
        },
        "2020-CS2": {
            "category": "International Relations / Arms Trade",
            "dilemmas": [
                "Self-Reliance (Atmanirbhar) vs Pacifism",
                "Economic Profit vs Moral Responsibility of Arms",
                "Exporting Violence vs Strategic Influence"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "As Chairman of BML, what are your views on the following points?",
                    "answer": "**Views**: The shift from import-dependence to being a 'Net Security Provider' is strategically sound. Exporting arms finances indigenous R&D (Economy of Scale). However, it brings a heavy moral burden to ensure our weapons are not used for human rights violations."
                },
                {
                    "id": "b",
                    "question": "As an arms exporter of a responsible nation like India, what are the ethical issues involved in arms trade? List five ethical factors...",
                    "answer": "**Ethical Issues**: Promoting war for profit; Fueling regional instability; Diverting resources from development to defense. \n\n**5 Ethical Factors for Sale**: \n1. **Human Rights Record** of the buyer nation. \n2. **End-User Agreement**: Guarantee that they won't re-sell to terrorists. \n3. **Regional Stability**: Will this sale trigger an arms race? \n4. **Regime Type**: Is it a democracy or a dictatorship? \n5. **UN Sanctions**: Strict adherence to international bans."
                }
            ]
        },
        "2020-CS3": {
            "category": "Child Labour / Tribal Welfare",
            "dilemmas": [
                "Economic Survival vs Child Rights",
                "Administrative Apathy vs Activism",
                "Enforcement vs Rehabilitation"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Analyze the ethical issues in this case.",
                    "answer": "1. **Child Labour**: Violation of Article 24 and dignity of childhood. \n2. **Systemic Failure**: Compromised NGOs and indifferent administration. \n3. **Poverty Trap**: Parents forced to sell their children's labor for survival. \n\n**Steps to Ameliorate**: \n1. **Rescue & Rehab**: Immediate raids on cotton farms (inter-state coordination). \n2. **MGNREGA Focus**: Create local employment so parents don't migrate. \n3. **Special Schools**: Residential schools (Ashram Shalas) for tribal girls to keep them safe and educated. \n4. **Action against NGOs**: Blacklist the compromised NGOs."
                }
            ]
        },
        "2020-CS4": {
            "category": "Urban Governance / Corruption",
            "dilemmas": [
                "Friendship/Seniority vs Duty",
                "Personal Threat (POSH case) vs Justice for Victims",
                "Corruption vs Safety"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Analyze the ethical issues in this case. What are the options available to you in this situation? Explain your selected course of action.",
                    "answer": "**Issues**: Collusive corruption costing lives; Weaponization of laws (POSH) for blackmail. \n\n**Options**: \n1. **Hush up**: Saves self from false cases, helps friend. (Cowardly & Criminal). \n2. **Strict Report**: Exposes the nexus. Risks retaliation. \n\n**Selected Course**: **Option 2**. I will submit a factual report exposing the illegal basement and poor quality. \n**Handling Threats**: \n- **POSH**: I will request an impartial Internal Complaints Committee (ICC) and document the timing of the threat (it came *after* the enquiry started) to prove mala fide intent. \n- **Friend/Senior**: Professional duty supersedes personal relations. \n- **Builder**: File an FIR for attempted bribery and intimidation."
                }
            ]
        },
        "2020-CS5": {
            "category": "Corporate Social Responsibility (CSR) / Development",
            "dilemmas": [
                "Profit vs Social Development (Harmonized here)",
                "Corporate Paternalism vs State Abdication"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Critically analyse the story of APW and state the ethical issues involved. Do you consider APW as a role model for development of backward areas? Give reasons.",
                    "answer": "**Analysis**: APW represents 'Compassionate Capitalism'. However, the minor fire (excess electricity) shows that even good companies can cut corners. \n**Role Model?**: **Yes**. \n**Reasons**: \n1. **Inclusive Growth**: Local employment and skill development. \n2. **Crisis Management**: Paying wages during lockdown. \n3. **Social Infrastructure**: Building schools/hospitals where the state failed. \n**Caveat**: The State cannot abdicate its duties just because a private player is benevolent. Reliance on one company creates a 'Company Town' vulnerability."
                }
            ]
        },
        "2020-CS6": {
            "category": "Disaster Management / Migrant Crisis",
            "dilemmas": [
                "Right to Movement vs Public Health (Lockdown)",
                "State Paternalism vs Dignity of Labor",
                "Bureaucracy vs Empathy"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "In your opinion what ethical issues arose in the current migrant crisis? What do you understand by an ethical care giving state? What assistance can the civil society render...?",
                    "answer": "**Ethical Issues**: \n1. **Invisibility**: Migrants build the city but were abandoned by it. \n2. **Dignity**: Walking thousands of miles hungry violated their basic human dignity. \n\n**Ethical Care Giving State**: A state that goes beyond 'Law and Order' to ensure 'Welfare'. It anticipates vulnerability and treats the poorest with the same urgency as the rich. \n\n**Civil Society Role**: \n1. **Community Kitchens**: Immediate hunger relief. \n2. **Information Bridge**: Connecting migrants to government schemes/trains. \n3. **Counselling**: Reducing panic and mental agony."
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
