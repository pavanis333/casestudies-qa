
import json

def enrich_data(json_path):
    print(f"Reading {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File not found.")
        return

    # Knowledge Base of Answers for 2013
    updates = {
        # --- 2013 ---
        "2013-CS1": {
            "category": "RTI / Administrative Integrity",
            "dilemmas": [
                "Self-Preservation vs Accountability",
                "Truth vs Disciplinary Action"
            ],
            "questions": [
                {
                    "id": "q",
                    "question": "Evaluate the options and suggest a course of action.",
                    "answer": "**Evaluation**: \n1. **Refer to Superior**: Shifting responsibility. If the superior advises concealment, you become complicit. \n2. **Transfer/Leave**: Escapism. The error remains. \n3. **Camouflage/Compromise**: Fraudulent manipulation of records. Criminal offense. \n\n**Suggestion**: **Full Disclosure with Explanation**. \n- Disclose the information as requested under the RTI Act. \n- Simultaneously, file a 'Suo Moto' note to the Disciplinary Authority admitting the *bona fide* error (mistake without malice). \n- Owning up to a mistake is honorable; hiding it turns a mistake into a crime."
                }
            ]
        },
        "2013-CS2": {
            "category": "Public Safety / Professional Ethics",
            "dilemmas": [
                "Obedience to Hierarchy vs Duty to Public Safety",
                "Project Deadline vs Structural Integrity"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Analyze the ethical issues in this case. ... Suggest what course of action...",
                    "answer": "**Issues**: The Chief Engineer is prioritizing speed over safety (Utilitarian error). Collusion with the contractor is suspected. \n\n**Course of Action**: **Issue Written Stop-Work Order**. \n1. **Document**: I cannot rely on oral verbal orders. I will write a formal inspection note highlighting the defects. \n2. **Issue Notice**: Use my authority as Exec. Engineer to order the contractor to Rectify (re-do) the defective parts. \n3. **Escalate**: If the CE overrules me in writing, I will send a copy of my dissent to the Municipal Commissioner/Vigilance. \n**Reason**: If the flyover collapses later, 'I was just following orders' is no defense. Safety is non-negotiable."
                }
            ]
        },
        "2013-CS3": {
            "category": "Child Labour / Law Enforcement",
            "dilemmas": [
                "Legal Loopholes vs Spirit of Law",
                "Economic Exploitation vs Child Rights"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "bring out and discuss the ethical issues involved...",
                    "answer": "1. **Subversion of Law**: Using the 'Household' exception to run a sweatshop. \n2. **Complicity of Parents**: Poverty forcing parents to lie about the relationship. \n3. **Hazardous Industry**: Firecrackers are dangerous; employing children here is a violation of Article 24 (Fundamental Right)."
                },
                {
                    "id": "b",
                    "question": "What would be your reaction after your above visit?",
                    "answer": "**Reaction**: IMMEDIATE ACTION. \n1. **Separate & Interview**: I will separate the children from the 'owner' and interview them individually. The 'smirk' indicates they are coached. They will break under gentle questioning. \n2. **Medical Test**: Age verification (ossification test) if needed. \n3. **Rescue**: Invoke the Bonded Labour System (Abolition) Act. \n4. **Seal the Unit**: For violating the Child Labour (Prohibition) Act."
                }
            ]
        },
        "2013-CS4": {
            "category": "Nepotism / Institutional Integrity",
            "dilemmas": [
                "Funding (Institutional Interest) vs Merit (Faculty Selection)",
                "Quid Pro Quo vs fairness"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the options available to you?",
                    "answer": "1. **Succumb**: Select the relative, get the funds. \n2. **Refuse & Risk Funds**: Reject the relative, face delays in funding. \n3. **Diplomatic Refusal**: Ensure the selection process is recorded and transparent."
                },
                {
                    "id": "b",
                    "question": "Evaluate each of these options ... giving reasons.",
                    "answer": "**Selected Option**: **Strict Merit-Based Selection (Refusal)**. \n**Reasoning**: \n- The funds are a right of the institute, not a personal favor from the functionary. \n- Selecting an incompetent professor damages the institute for 30 years (generations of students suffer). \n- I will proceed with the interview. If the relative is truly merit-worthy, they get in. If not, they don't. I will record the interview to prove objectivity. If funding is stalled, I will approach the Ministry's Higher Secretary or Media."
                }
            ]
        },
        "2013-CS5": {
            "category": "Insider Trading / Corruption",
            "dilemmas": [
                "Official Secrecy vs Superior's Order",
                "Public Trust vs Personal Networking"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the options available to you?",
                    "answer": "1. **Obey**: Leak the info. \n2. **Refuse**: Cite Official Secrets Act. \n3. **Refuse & Report**: Inform the Vigilance dept."
                },
                {
                    "id": "b",
                    "question": "Evaluate each of these options ... giving reasons.",
                    "answer": "**Selected Option**: **Refuse & maintain Secrecy**. \n**Reason**: Leaking fiscal policy is a crime (Insider Trading). It defrauds the public and creates an uneven playing field. My loyalty is to the Constitution, not the superior. I will politely but firmly tell the superior: 'Sir, sharing this would be a violation of the Official Secrets Act and I cannot do it.'"
                }
            ]
        },
        "2013-CS6": {
            "category": "Sexual Harassment / Corporate Leadership",
            "dilemmas": [
                "Profit (Star Performer) vs Dignity of Women",
                "Short-term Revenue vs Toxic Culture",
                "Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013"
            ],
            "questions": [
                {
                    "id": "a",
                    "question": "Analyze the ethical issues in this case.",
                    "answer": "The core issue is **Workplace Safety vs Profit**. Retaining a predator because he brings revenue is morally bankrupt. \n\n**Action Plan**: \n1. **Reject Resignation**: I will ask Mrs. X to hold her resignation and assure her of safety. \n2. **Zero Tolerance**: Immediate suspension of Mr. A pending enquiry. \n3. **ICC Enquiry**: Refer the case to the Internal Complaints Committee (ICC) as per the POSH Act. \n4. **Dismissal**: If the SMS evidence (indecent messages) proves the guilt, terminate Mr. A immediately regardless of his sales targets. A toxic leader destroys the company culture in the long run."
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
                    elif 'i' in kb_qs and i == 0:
                         q_obj['answer'] = kb_qs['i']['answer']
                         
            count += 1

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully enriched {count} cases.")

if __name__ == "__main__":
    enrich_data('src/data.json')
