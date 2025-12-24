
import json

def enrich_data(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Knowledge Base of Answers
    updates = {
        # --- 2022 ---
        "2022-CS1": {
            "category": "Corporate Ethics / Corruption in Defence",
            "dilemmas": [
                "Personal Crisis vs Professional Integrity",
                "Corporate Survival vs National Security",
                "Means vs Ends (Saving job via theft)"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Discuss the ethical issues involved in the case.",
                    "answer": "**Integrity**: Accepting stolen documents is corporate espionage and a criminal offence.\n**Conflict of Interest**: Hiring a rival's employee specifically for confidential data.\n**National Security**: Defence tenders involve sensitive data; compromising the bidding process undermines national safety."
                },
                {
                    "id": "b",
                    "question": "Critically examine the options available to Prabhat in the above situation.",
                    "answer": "1. **Accept the Deal**: Saves job and family finances immediately. *Cons*: Illegal, risk of blackmail later, moral bankruptcy. \n2. **Reject & Report**: Refuse the offer and report Subhash to authorities. *Pros*: Upholds law. *Cons*: Risk of losing job if tender fails. \n3. **Reject but Silence**: Turn down the offer but don't report. *Pros*: Avoids legal complicity. *Cons*: Subhash might sell data elsewhere, still harming the ecosystem."
                },
                {
                    "id": "c",
                    "question": "Which of the above would be the most appropriate for Prabhat and why?",
                    "answer": "**Option 2 (Reject & Report)**. Prabhat must prioritize ethical fortitude over short-term relief. Accepting stolen defence documents is not just 'business'—it's treason adjacent. He should report Subhash to the Ministry, which might even earn his company credibility points. For his personal finances, he should seek legitimate debt restructuring or a different job, rather than financing his life through crime."
                }
            ]
        },
        "2022-CS2": {
            "category": "National Security / Political Pressure",
            "dilemmas": [
                "National Security vs Career Progression",
                "Duty to Constitution vs Duty to Superiors",
                "Honesty vs Obedience"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the Department options available to Ramesh as the Director of the Home Department of the bordering State?",
                    "answer": "He can: \n1. **Withdraw the report** as ordered (Complicity). \n2. **Persist with the report** officially (Defiance). \n3. **Escalate** the matter to Central Agencies (MHA/IB) given the cross-border security implications."
                },
                {
                    "id": "b",
                    "question": "What option should Ramesh adopt and why?",
                    "answer": "He should **adopt Option 3 (Escalate with persistence)**. Illegal migration with forged documents is a threat to national sovereignty. A state officer cannot bury such intelligence. He should send a copy to the Central Ministry of Home Affairs (MHA) under the 'whistleblower' protection logic if state authorities suppress it."
                },
                {
                    "id": "c",
                    "question": "Critically evaluate each of the options.",
                    "answer": "1. **Withdraw**: Ensures promotion/mother's treatment but betrays the nation. \n2. **Persist (State level)**: Likely leads to transfer and harassment without solving the problem. \n3. **Escalate (Central)**: Risky but aligns with the All India Service conduct rules and protects national interest."
                },
                {
                    "id": "d",
                    "question": "What are the ethical dilemmas being faced by Ramesh?",
                    "answer": "**Personal Interest (Mother's cancer care) vs Public Interest (National Security)**. This is a classic 'Crisis of Conscience'."
                },
                {
                    "id": "e",
                    "question": "What policy measures would you suggest to combat the menace of infiltration of illegal migrants from the neighbouring country?",
                    "answer": "1. **Smart Fencing**: Use tech (LIDAR/Cameras) where physical fencing is hard. \n2. **biometric Database**: National Register of Citizens (NRC). \n3. **Border Community Volunteers**: Incentivize locals to report strangers."
                }
            ]
        },
        "2022-CS3": {
            "category": "Media Ethics / Corruption",
            "dilemmas": [
                "Journalistic Integrity vs Personal Gain",
                "Truth vs Loyalty to Employer",
                "Justice for the murdered officer vs Family Health"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the options available with Ashok to cope up with the situation?",
                    "answer": "1. **Accept the bribe/loan** and kill the story. \n2. **Publish elsewhere** (social media/other channel) anonymously. \n3. **Confront CMD** and resign, then go public."
                },
                {
                    "id": "b",
                    "question": "Critically evaluate/examine each of the options identified by Ashok.",
                    "answer": "1. **Accept**: Solves his son's medical crisis but kills his conscience and denies justice to the murdered SP. \n2. **Publish Elsewhere**: High risk of retaliation but gets the truth out. \n3. **Resign & Publish**: Most honorable but financially precarious."
                },
                {
                    "id": "c",
                    "question": "What are the ethical dilemmas being faced by Ashok?",
                    "answer": "**Fiduciary Duty (as father) vs Civic Duty (as journalist)**.\n**Loyalty to Organization vs Commitment to Truth**."
                },
                {
                    "id": "d",
                    "question": "Which of the options, do you think, would be the most appropriate for Ashok to adopt and why?",
                    "answer": "**Resign and Publish**. He cannot work for a channel owned by the mafia he investigates. He should crowd-source or seek help from journalist associations for his son's treatment, but selling the truth of a murder is ethically non-negotiable."
                },
                {
                    "id": "e",
                    "question": "In the above scenario, what type of training would you suggest for police officers posted to such districts where stone mining illegal activities are rampant?",
                    "answer": "1. **Tactical Driving**: To avoid being overrun. \n2. **Drone Surveillance**: To monitor from a safe distance. \n3. **Coordinated Operations**: Never go in small teams; always have backup."
                }
            ]
        },
        "2022-CS4": {
            "category": "Corporate Governance / Whistleblowing",
            "dilemmas": [
                "Honesty vs Job Security",
                "Consumer Safety vs Corporate Profit",
                "Compliance vs Coercion"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Under the given conditions, what are the options available to you as a member of the Inspecting Team?",
                    "answer": "1. **Sign the clearance**: Keep the job, feed the family. \n2. **Refuse to sign**: Risk termination. \n3. **Refuse and Whistleblow**: Inform the board/regulators."
                },
                {
                    "id": "b",
                    "question": "Critically evaluate each of the options listed by you.",
                    "answer": "1. **Sign**: Complicit in fraud. Short-term safety, long-term guilt and legal risk if product fails. \n2. **Refuse**: Personal hardship but professional integrity remains intact. \n3. **Whistleblow**: Protection under law (in theory), but practical blacklisting risks."
                },
                {
                    "id": "c",
                    "question": "What option would you adopt and why?",
                    "answer": "**Refuse to Sign**. Clearing defective goods for domestic markets just because Europe rejected them is unethical double standards (treating domestic citizens as second-class). I would document my dissent. If fired, I can approach labour courts, but I cannot sign off on fraud."
                },
                {
                    "id": "d",
                    "question": "What are the ethical dilemmas being faced by you?",
                    "answer": "**Livelihood (Dependent parents & wife) vs Professional Conscience**. \n**Loyalty to Company vs Loyalty to Consumer**."
                },
                {
                    "id": "e",
                    "question": "What can be the consequences of overlooking the observations raised by the inspecting Team?",
                    "answer": "1. **Brand Erosion**: 'Quality' is trust. Once lost, it's hard to regain. \n2. **Legal Liability**: If the defect causes injury, criminal negligence charges will follow. \n3. **Internal Rot**: It signals to all employees that 'standards don't matter', leading to further decline."
                }
            ]
        },
        "2022-CS5": {
            "category": "Human Resource Management / Crisis Resolution",
            "dilemmas": [
                "Rule of Law (Driver was at fault) vs Compassion (Sole earner died)",
                "Organizational Discipline vs Employee Welfare"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Analyze the ethical issues in this case.",
                    "answer": "The core issue is **Responsibility vs Empathy**. \nTechnically, the driver instigated the fight (Road Rage), so 'Compensation on Duty' rules might not apply strictly. \nHowever, the family is innocent and destitute. \n**Dilemma**: If you compensate a 'guilty' driver, you set a bad precedent (rewarding indiscipline). If you don't, the family starves and the strike paralyzes the city."
                }
                # Note: The original JSON only had one question for this case study. 
                # We can add more context if needed, but sticking to existing structure.
            ]
        },
        "2022-CS6": {
            "category": "Environmental Ethics / Administration",
            "dilemmas": [
                "Environment vs Economy (Jobs)",
                "Public Health vs Livelihood",
                "Duty vs Threat"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the options available to you under the given situation?",
                    "answer": "1. **Close all units immediately**: Legal, but causes massive unemployment. \n2. **Allow them to run**: Saves jobs, but kills people via pollution. \n3. **Phased Compliance**: Give a strict timeline (e.g., 3 months) to install filters/STPs or face closure."
                },
                {
                    "id": "b",
                    "question": "Critically examine the options listed by you.",
                    "answer": "1. **Closure**: Drastic. Punishes workers for owners' faults. \n2. **Status Quo**: Dereliction of duty. Violates Right to Life (Clean Environment). \n3. **Phased**: Balanced. Allows time for transition but keeps the threat of closure real."
                },
                {
                    "id": "c",
                    "question": "What type of mechanism would you suggest to ensure environmental compliance?",
                    "answer": "1. **24x7 Online Monitoring**: Sensors connected to a central server (no manual fudge). \n2. **Polluter Pays Principle**: Heavy fines for violations used to treat affected locals. \n3. **Public Audit**: empower local NGOs to conduct surprise checks."
                },
                {
                    "id": "d",
                    "question": "What are the ethical dilemmas you faced in exercising your option?",
                    "answer": "**Right to Livelihood (Article 21) vs Right to Clean Environment (Article 21)**. Both are fundamental rights. The administrator must harmonize them (Sustainable Development)."
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
                # If existing ID is just an index letter like 'a', match it.
                if qid in kb_qs:
                    q_obj['answer'] = kb_qs[qid]['answer']
                # Fallback: if IDs don't match (e.g. data has '0' or something), use index if length matches
                elif len(case['questions']) == len(up['questions']):
                    # map index 0 to 'a', 1 to 'b'
                    key = chr(97 + i) # a, b, c
                    if key in kb_qs:
                        q_obj['answer'] = kb_qs[key]['answer']
            
            count += 1

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully enriched {count} cases.")

if __name__ == "__main__":
    enrich_data('src/data.json')
