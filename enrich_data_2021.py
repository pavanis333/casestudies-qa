
import json

def enrich_data(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Knowledge Base of Answers for 2021
    updates = {
        # --- 2021 ---
        "2021-CS1": {
            "category": "Administrative Ethics / Mafia",
            "dilemmas": [
                "Personal Safety (Family) vs Professional Duty",
                "Integrity vs Intimidation",
                "Internal Betrayal vs Leadership"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Identify the different options available to Sunil in attending to this situation.",
                    "answer": "1. **Surrender/Transfer**: Request a transfer citing personal reasons or 'health'. \n2. **Go Soft**: Reduce the intensity of raids to appease the mafia. \n3. **Firm Action with Precautions**: Continue the crackdown while securing his family and purging internal moles."
                },
                {
                    "id": "b",
                    "question": "Critically evaluate each of the options listed by you.",
                    "answer": "1. **Transfer**: Ensures immediate safety but is 'Dereliction of Duty'. It emboldens the mafia and destroys his reputation. \n2. **Go Soft**: Betrayal of the oath of office. It makes him complicit in the corruption. \n3. **Firm Action**: High risk but the only ethical choice. He represents the State's authority; if he buckles, the State fails."
                },
                {
                    "id": "c",
                    "question": "Which of the above, do you think, would be the most appropriate for Sunil to adopt and why?",
                    "answer": "**Option 3 (Firm Action with Precautions)**. \n- **Strategy**: 1. Secure family (Police protection). 2. Internal Cleaning (Suspend/Transfer mole employees). 3. Public Support (Involve media/NGOs to make the mafia's threat public, increasing the cost of retaliation). 4. Seek HQ support (Write to Chief Secretary). \n**Rationale**: Courage is the premier virtue of a civil servant."
                }
            ]
        },
        "2021-CS2": {
            "category": "Educational Administration / Integrity",
            "dilemmas": [
                "Institutional Reputation vs Academic Integrity",
                "Pressure from Elites vs Fairness to Students",
                "Career Ambition (Principalship) vs Conscience"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Discuss the ethical issues involved in the case.",
                    "answer": "**Corruption in Education**: A teacher aiding cheating destroys the sanctity of exams. \n**Conflict of Interest**: Management prioritizing donations/political favor over merit. \n**Quid Pro Quo**: Linking your promotion to covering up a crime."
                },
                {
                    "id": "b",
                    "question": "Critically examine the options available with you as Vice Principal. What option will you adopt and why?",
                    "answer": "**Options**: \n1. **Obey Management**: Save the students, get promoted. (Unethical: Promotes a culture of cheating). \n2. **Strict Action**: Support the Flying Squad. (Ethical: Upholds justice, but risks career). \n\n**Decision**: I will **support the Flying Squad**. \n**Reason**: If a college teaches that money and power can buy grades, it fails its primary purpose. I cannot accept a Principalship built on a foundation of fraud. I will document the management's pressure and, if necessary, expose the nexus to the University."
                }
            ]
        },
        "2021-CS3": {
            "category": "Infrastructure / Corruption",
            "dilemmas": [
                "Political Deadline vs Public Safety",
                "Hierarchical Pressure vs Professional Judgment",
                "Career vs Lives"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Under the given conditions, what are the options available to you as a project manager?",
                    "answer": "1. **Overlook the crack**: Finish on time, get promoted. \n2. **Partial Repair**: Cosmetic fix to hide the crack. \n3. **Stop & Fix**: Insist on reconstruction despite delays."
                },
                {
                    "id": "b",
                    "question": "What are the ethical dilemmas being faced by the project manager?",
                    "answer": "**Public Safety vs Political Expediency**. \n**Professional Integrity (Engineering Ethics) vs Obedience to Authority**. \nA bridge collapse kills real people (morally equivalent to manslaughter if foreseeable)."
                },
                {
                    "id": "c",
                    "question": "What are the professional challenges likely to be faced by the project manager and his response to overcome such challenges?",
                    "answer": "**Challenges**: Threat of transfer, anger of the Minister, isolation by Chief Engineer. \n**Response**: 1. **Written Orders**: Ask the CE to give the 'ignore' order in writing. 2. **Technical Audit**: Request a third-party safety audit (e.g., from IIT) to biologically validate the danger. 3. **Whistleblowing**: If forced, inform the Chief Minister's office directly that an unsafe inauguration will be a political disaster if it collapses later."
                },
                {
                    "id": "d",
                    "question": "What can be the consequences of overlooking the observation raised by the inspecting team?",
                    "answer": "**Catastrophic Structural Failure**: Loss of life, criminal negligence charges, long-term legal battles, and total loss of reputation for the government. 'A stitch in time saves nine'."
                }
            ]
        },
        "2021-CS4": {
            "category": "Medical Ethics / Crisis Management",
            "dilemmas": [
                "Duty to Treat vs Right to Safety (Staff)",
                "Resource Allocation in Pandemics"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What are your criteria and justification for putting your clinical and non-clinical staff to attend to the patients knowing fully well that it is highly infectious disease and resources and infrastructure are limited?",
                    "answer": "**Criteria**: Age/Comorbidities (protect vulnerable staff), Rotation (prevent burnout), and specialization. \n**Justification**: \n1. **Social Contract**: Medical professionals have a duty to serve in crises. \n2. **Utilitarianism**: The hospital exists to save lives; if staff flee, society collapses. \nHowever, as Admin, I have a **reciprocal duty** to provide them best possible PPE, insurance, and quarantine facilities."
                },
                {
                    "id": "b",
                    "question": "If yours is a private hospital, whether your justification and decision would remain same as that of a public hospital?",
                    "answer": "**Yes, absolutely.** \nMedical ethics (Hippocratic Oath) is universal, not dependent on ownership. Private hospitals also operate on public land/license (Land Grant conditions). Turning away patients in a national disaster is both unethical and often illegal (under the Epidemic Diseases Act/Disaster Management Act)."
                }
            ]
        },
        "2021-CS5": {
            "category": "Corporate Ethics / Food Safety",
            "dilemmas": [
                "Profit vs Public Health",
                "Double Standards (Export vs Domestic)",
                "Regulatory Capture"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What action do you visualise should be taken by the competent authority against the food company for violating the laid down domestic food standard and selling rejected export products in domestic market?",
                    "answer": "1. **Immediate Recall**: Seize all existing stock. \n2. **Heavy Penalty**: Fine them significantly under the Food Safety and Standards Act (FSSAI). \n3. **License Suspension**: Temporarily halt production to force compliance. \n4. **Criminal Proceedings**: If hazardous substances were found, file cases for endangering public life."
                },
                {
                    "id": "b",
                    "question": "What course of action is available with the food company to resolve the crisis and bring back its lost reputation?",
                    "answer": "1. **Full Disclosure**: Admit the fault publicly (Crisis Communication). \n2. **Voluntary Recall**: Don't wait for orders. \n3. **Third-Party Audit**: Hire a reputed global firm to certify quality. \n4. **Leadership Change**: Fire the managers responsible for the unethical decision to sell rejected goods."
                },
                {
                    "id": "c",
                    "question": "Examine the ethical dilemma involved in the case.",
                    "answer": "**Corporate Greed vs Consumer Trust**. The company treated domestic citizens as 'second-class' by feeding them rejected food. This violates the Kantian principle of treating humans as ends, not means to profit."
                }
            ]
        },
        "2021-CS6": {
            "category": "Workplace Culture / Emotional Intelligence",
            "dilemmas": [
                "Resilience vs Self-Respect",
                "Hierarchy vs Dignity",
                "Personal Peace vs Professional Struggle"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the options available with Pawan to cope with the situation?",
                    "answer": "1. **Suffer in Silence**: Detrimental to health. \n2. **Retaliate**: unprofessional. \n3. **Constructive Engagement**: Seek a private meeting to discuss specific work issues/boundaries. \n4. **Formal Complaint/Transfer**: If toxicity persists."
                },
                {
                    "id": "b",
                    "question": "What approach Pawan should adopt for bringing peace, tranquility and congenial environment in the office and home?",
                    "answer": "**Compartmentalization**. He must learn to 'leave work at work'. \n**Meditation/Counseling**: To rebuild self-esteem. \n**Communication**: Explicitly tell the boss, 'I value your feedback, but the tone is affecting my morale.' Sometimes bullies back down when confronted professionally."
                },
                {
                    "id": "c",
                    "question": "As an outsider, what are your suggestions for both boss and subordinate...",
                    "answer": "**For Boss**: Leadership is about empathy. A demoralized team is an unproductive team. Seek therapy for personal issues. \n**For Subordinate**: Don't internalize criticism. Document everything. Build a support network."
                },
                {
                    "id": "d",
                    "question": "In the above scenario, what type of training would you suggest for officers at various levels in the government offices?",
                    "answer": "1. **Emotional Intelligence (EQ)**: Managing self and others' emotions. \n2. **Soft Skills/Communication**: How to give feedback constructively. \n3. **Stress Management**: Yoga/Mindfulness as part of the official curriculum (Mission Karmayogi)."
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
