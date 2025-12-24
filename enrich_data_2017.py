
import json

def enrich_data(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Knowledge Base of Answers for 2017
    updates = {
        # --- 2017 ---
        "2017-CS1": {
            "category": "Administrative Ethics / Morality",
            "dilemmas": [
                "Ethical Conduct vs Personal Difficulty",
                "Integrity vs Efficiency (Bribery myth)"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "There is a general perception that adhering to ethical conduct one may face difficulties...",
                    "answer": "**Analysis**: It is true that honesty often brings short-term pain (transfers, isolation). However, unfair practices (corruption) create a 'Debt of Guilt' and legal risk. An honest officer sleeps better and earns social capital/respect, which is a higher form of success than ill-gotten wealth."
                },
                {
                    "id": "b",
                    "question": "When the number of people adopting unfair means is large, a small minority...",
                    "answer": "**Disagree**. History is shaped by the determined minority. One honest officer acts as a 'Moral Anchor', preventing the complete collapse of the system. Even one candle conquers darkness."
                },
                {
                    "id": "c",
                    "question": "Sticking to ethical means is detrimental to the larger developmental goals",
                    "answer": "**False dichotomy**. Ethical means *ensure* sustainable development. Corruption leads to poor quality infrastructure (bridge collapses) which retards development. Ethics and Efficiency are complementary, not contradictory."
                },
                {
                    "id": "d",
                    "question": "While one may not involve oneself in large unethical practices, but giving and accepting small gifts...",
                    "answer": "**Demerits**: 'Small gifts' are the gateway drug to grand corruption. They normalize a culture of 'Quid Pro Quo'. It erodes the neutrality of the service. \n**Merits (Perceived)**: Grease the wheels. But this 'efficiency' is discriminatory against the poor who cannot afford even small gifts."
                }
            ]
        },
        "2017-CS2": {
            "category": "Crisis Management / Conflict of Duty",
            "dilemmas": [
                "Personal Duty (Family) vs Professional Ambition (Interview)",
                "Golden Hour (Saving Life) vs Career Milestone"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Analyze the ethical issues in this case. What would you have done...?",
                    "answer": "**Decision**: I would **stop and help**. \n**Justification**: \n1. **Sanctity of Life**: Saving a life (especially relatives in critical condition) outweighs any career opportunity. \n2. **True Test of Character**: The interview tests my *aptitude* for service; the accident tests my *attitude* for service. Leaving bleeding relatives to die to attend an interview on 'public service' is hypocritical. \n**Action Plan**: \n1. Call ambulance/police. \n2. Admit them to the nearest hospital. \n3. Inform family members to come. \n4. Call the UPSC helpline/Chairperson's office to explain the emergency. Even if they don't reschedule, I have passed the test of humanity."
                }
            ]
        },
        "2017-CS3": {
            "category": "Industrial Relations / Empathy",
            "dilemmas": [
                "Technical Rules (Drunk on duty) vs Humanitarian Aid",
                "Profit vs Social Security"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What recommendation would you provide to the management?",
                    "answer": "**Recommendation**: **Deny legal compensation but provide an Ex-Gratia humanitarian grant.** \n**Merits**: \n1. **Legal Safety**: Denying 'Compensation' upholds the rule that being drunk on duty is a violation of safety norms. Rewarding it sets a bad precedent. \n2. **Humanitarianism**: Giving an 'Ex-Gratia' (Goodwill) amount helps the destitute family who are not at fault for the breadwinner's mistake. \n3. **Resolves Strike**: It shows the management is firm on rules but soft on people, pacifying the union."
                }
            ]
        },
        "2017-CS4": {
            "category": "Corporate Ethics / Law",
            "dilemmas": [
                "Truth vs Corporate Interest",
                "Justice for Victim vs Deal for Company"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What will be your response to the situation?",
                    "answer": "**Response**: I will **tell the truth** to the police. \n**Reasoning**: \n1. **Criminal Justice**: A hit-and-run/accident causing injury demands justice. Lying makes me an accomplice to the crime. \n2. **Corporate Reputation**: If I lie and it is revealed later, my company's reputation will be destroyed for covering up a crime. \n3. **Integrity**: No deal is worth the price of a human being's justice. I would try to explain to Company B that honesty is a core value of our partnership, but I cannot perjure myself."
                }
            ]
        },
        "2017-CS5": {
            "category": "Urban Planning / Corruption",
            "dilemmas": [
                "Greed (Builder) vs Safety",
                "Administrative Negligence vs Public Lives"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Give reasons for such incidents taking place across the country. Suggest measures to prevent their occurrence.",
                    "answer": "**Reasons**: 1. **Nexus**: Builder-Politician-Bureaucrat nexus ignoring zoning laws. 2. **Lack of Inspection**: Post-permit surveillance is zero. 3. **Demand-Supply Gap**: High housing demand forces poor into unsafe illegal structures. \n\n**Measures**: \n1. **Geo-tagging**: Satellite monitoring of construction height. \n2. **Structural Safety Audit**: Mandatory before Occupancy Certificate. \n3. **Blacklisting**: Builders causing death should face life bans. \n4. **Town Planning Officers (TPO) Accountability**: The officer in charge of the zone must be held criminally liable for illegal floors added during their tenure."
                }
            ]
        },
        "2017-CS6": {
            "category": "RTI / Governance",
            "dilemmas": [
                "Transparency vs Harassment (RTI Blackmail)",
                "Right to Know vs Right to Function"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What measures would you suggest to separate genuine and non-genuine applications?",
                    "answer": "1. **Proactive Disclosure (Sec 4)**: If the department puts *everything* on the website involves tenders/commissions, the scope for blackmail vanishes. \n2. **Identity Verification**: Verify the citizenship of the applicant (as per Act) to weed out proxies. \n3. **Reasonable Fee**: Increase fees slightly for 'Bulk' applications (without hurting the poor) to deter frivolous mass-filing. \n4. **Ignore Motive**: Legally, you cannot ask *why* they want info. The focus should be on reducing the *secrecy* that makes info valuable for blackmail."
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
