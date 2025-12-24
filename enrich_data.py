
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
    # We map "Year-CaseNum" (e.g., 2024-1) to specific content updates
    
    updates = {
        # --- 2024 ---
        "2024-CS1": {
            "category": "Corporate Ethics / Environment",
            "dilemmas": ["Profitability vs Sustainability", "Short-term gains vs Long-term survival", "Shareholder value vs Stakeholder (Planet) welfare"],
            "questions": [
                {
                    "id": "a",
                    "question": "What is your immediate response to the challenges posed in the above case?",
                    "answer": "1. **Acknowledge & Validate**: Publicly accept the environmental data. Denial will worsen reputation.\n2. **Immediate Audit**: Commission an independent energy audit to identify 'low-hanging fruit' for efficiency.\n3. **Moratorium**: Temporarily pause the expansion of new, non-critical data centers until a renewable energy transition plan is locked in.\n4. **Stakeholder Engagement**: Initiate dialogue with activists and regulators to show proactive intent."
                },
                {
                    "id": "b",
                    "question": "Discuss the ethical issues involved in the above case.",
                    "answer": "**Intergenerational Equity**: destroying the planet for current AI conveniences steals from future generations.\n**Corporate Responsibility**: A company of this size has a moral obligation beyond legal compliance.\n**The 'Greenwashing' Trap**: Balancing honest reporting with public relations.\n**Technological Determinism**: The belief that 'innovation' justifies any cost, which ethically flaws."
                },
                {
                    "id": "c",
                    "question": "Your company has been identified to be penalized by technological giants. What logical and ethical arguments will you put forth to convince about its necessity?",
                    "answer": "**Logical**: 'Green AI' is efficient AI. Reducing energy often correlates with better code optimization. Long-term, renewable energy offers stable pricing compared to volatile fossil fuels.\n**Ethical**: We must operate under the 'Categorical Imperative'—if every company ignored emissions, the planet would collapse. We must lead by example to maintain our 'Social License to Operate'."
                },
                {
                    "id": "d",
                    "question": "Being a conscience being, what measures would you adopt to maintain balance between AI innovation and environmental footprint?",
                    "answer": "1. **Green Algorithms**: Mandate efficiency metrics in code reviews.\n2. **Carbon Pricing**: Implement an internal carbon tax on departments to disincentivize waste.\n3. **Location Strategy**: Move data centers to colder climates (natural cooling) or regions with 100% renewable grids.\n4. **Lifecycle Ethics**: Consider the e-waste of hardware, not just electricity."
                }
            ]
        },
        "2024-CS2": {
            "category": "Internal Security / Radicalization",
            "dilemmas": ["National Security vs Civil Liberties", "Hard Policing vs Soft Power", "Surveillance vs Privacy"],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the options available to Raman to tackle the above situation?",
                    "answer": "1. **Hard Crackdown**: Mass arrests based on social media activity. (Pros: Immediate disruption. Cons: Alienates community, risks creating martyrs).\n2. **Ignore/Observation**: Gather intel without acting. (Pros: Map the network. Cons: High risk of an attack occurring meanwhile).\n3. **Hybrid approach (Deradicalization)**: Targeted surveillance + Community Engagement + Economic opportunities. (Most Balanced)."
                },
                {
                    "id": "b",
                    "question": "What measures would you suggest for strengthening the existing set-up to ensure that such groups do not succeed in penetrating and vitiating the atmosphere in the state?",
                    "answer": "1. **Community Policing**: Revive 'Mohalla Committees' to detect early signs of radicalization.\n2. **Digital Literacy**: Educate youth on recognizing propaganda and 'Check-Verify-Post' protocols.\n3. **Counter-Narrative Cell**: A dedicated team to push positive, nationalistic, and inclusive content to counter extremist narratives online.\n4. **Economic Integration**: Skill development camps specifically in vulnerable areas."
                },
                {
                    "id": "c",
                    "question": "In the above scenario, what action plan would you advise for enhancing the intelligence gathering mechanism of the police force?",
                    "answer": "1. **Social Media Analytics**: Deploy AI tools for sentiment analysis and pattern recognition on open-source data (OSINT).\n2. **HUMINT Reinforcement**: Recruit 'Cyber Volunteers' from colleges to report suspicious activity anonymously.\n3. **Inter-Agency Coordination**: Real-time data sharing between State CID, Central IB, and Cyber Cells to avoid silos."
                }
            ]
        },
        "2024-CS3": {
            "category": "Conflict Resolution / Naxalism",
            "dilemmas": ["Mission Success vs Civilian Safety", "Rule of Law vs Mob Justice", "Duty to Capture vs Duty to Protect Life"],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the options available with Rohit to cope with the situation?",
                    "answer": "1. **Release the Naxalites**: Avoids violence but huge blow to morale and rule of law.\n2. **Use Lethal Force**: Breaks the mob but causes civilian massacres, validating Naxal propaganda.\n3. **Tactical Withdrawal/Negotiation**: Use non-lethal crowd control (tear gas, warning shots), secure the prisoners in a defensive perimeter, and wait for reinforcements/negotiate passage."
                },
                {
                    "id": "b",
                    "question": "What are the ethical dilemmas being faced by Rohit?",
                    "answer": "**Professional Competence vs Humanitarian Concern**: He captured high-value targets (success) but now faces innocent women (humanitarian crisis).\n**Means vs Ends**: Is firing on civilians justified to secure terrorists? (Deontologically: No)."
                },
                {
                    "id": "c",
                    "question": "Which of the options, do you think, would be more appropriate for Rohit to adopt and why?",
                    "answer": "**Option 3 (Tactical Defence & Non-Lethal Force)**. Releasing terrorists is non-negotiable as they are a threat to the state. Firing on tribal women is morally and strategically disastrous. He must hold ground, use riot-control measures, video-graph the aggression for evidence, and sustain until reinforcement arrives or the mob disperses."
                },
                {
                    "id": "d",
                    "question": "In the present situation, what are the extra precautionary measures to be taken by the police in dealing with women protesters?",
                    "answer": "1. **Women Police Personnel**: Mandatory presence to handle female agitators.\n2. **Minimum Force**: Strict adherence to SOPs—water cannons/tear gas before any physical contact.\n3. **Video Documentation**: To counter false allegations of molestation or brutality later.\n4. **Dialogue**: Use megaphones to warn and persuade, appealing to their safety."
                }
            ]
        },
        "2024-CS4": {
            "category": "Conflict of Interest",
            "dilemmas": ["Personal Loyalty vs Professional Integrity", "Profit vs Propriety", "Appearance of Bias vs Merit"],
            "questions": [
                {
                    "id": "a",
                    "question": "What should be Sneha's course of action?",
                    "answer": "She must **recuse herself** immediately from the specific committee or decision-making process involving her brother's bid. She should inform the management of the conflict of interest in writing."
                },
                {
                    "id": "b",
                    "question": "How would she justify what she chooses to do?",
                    "answer": "By citing the principle of **'Nemo judex in causa sua'** (No one should be a judge in their own cause). Even if she is unbiased, the *perception* of bias will damage the hospital's reputation. Recusal protects both her integrity and her brother's bid from future legal challenges."
                },
                {
                    "id": "c",
                    "question": "In this case, how is medical ethics compromised with vested personal interest?",
                    "answer": "Medical ethics prioritizes patient welfare (Beneficence). Procurement based on family ties rather than merit (quality/cost) risks acquiring sub-par equipment, directly endangering patient lives. It turns healthcare into a nepotistic business rather than a service."
                }
            ]
        },
        "2024-CS5": {
            "category": "Resource Administration",
            "dilemmas": ["Livelihood (Farmers) vs Livelihood (Industrial Workers)", "Human Right to Water vs Economic Right to Business"],
            "questions": [
                {
                    "id": "a",
                    "question": "Discuss all options available to the District Collector as a District Magistrate.",
                    "answer": "1. **Ban Industry Water Usage**: Saves water for humans/farms but causes industrial unemployment and economic loss.\n2. **Ignore Farmers**: Leads to law and order breakdown and potential starvation/crop failure.\n3. **Regulated Rationing**: Implement a strict quota for industry, mandate water recycling (Zero Liquid Discharge), and prioritize drinking water > agriculture > industry."
                },
                {
                    "id": "b",
                    "question": "What suitable actions can be taken in view of mutually compatible interests of the stakeholders?",
                    "answer": "1. **Immediate Audit**: Verify industrial consumption. Stop illegal deep borewells.\n2. **Alternative Sources**: Supply treated sewage water (STP) to industries instead of fresh water.\n3. **Crop Compensation**: If crops fail due to necessary rationing, state must compensate.\n4. **Dialogue**: Tripartite meeting (Admin, Farmers, Industry) to agree on a crisis-management formula."
                },
                {
                    "id": "c",
                    "question": "What are the potential administrative and ethical dilemmas for the District Collector?",
                    "answer": "**Administrative**: Managing law & order (protests) vs maintaining economic activity.\n**Ethical**: The hierarchy of needs—Drinking water is a fundamental right (Article 21), industrial profit is secondary. Yet, causing unemployment is also an ethical harm."
                }
            ]
        },
        "2024-CS6": {
            "category": "Bioethics / Corporate Ethics",
            "dilemmas": ["Public Safety vs Corporate Profit", "Scientific Integrity vs Career Progression", "Speed vs Safety"],
            "questions": [
                {
                    "id": "a",
                    "question": "What would you do in such a situation?",
                    "answer": "I would **refuse to manipulate data**. I would document the pressure in writing and explain to management that a flawed drug will eventually destroy the company's reputation and lead to massive lawsuits (e.g., Thalidomide tragedy). If forced, I would consider whistleblowing."
                },
                {
                    "id": "b",
                    "question": "Examine your options and consequences in the light of the ethical questions involved.",
                    "answer": "1. **Comply**: Short-term approval, promotion. Long-term: Deaths, guilt, jail.\n2. **Refuse**: Possible firing. But upholds 'Non-maleficence' (Do no harm).\n3. **Compromise (Partial data)**: Still unethical. Promoting a half-truth is a full lie in science."
                },
                {
                    "id": "c",
                    "question": "How can data ethics and drug ethics save humanity at large in such a scenario?",
                    "answer": "Rigorous data ethics ensures that drugs *actually work*. It prevents the 'illusion of safety'. In a pandemic, a fake cure is worse than no cure because it creates false confidence and stops the search for real solutions. Integrity is the immune system of science."
                }
            ]
        },
        # --- 2023 ---
        "2023-CS1": {
            "category": "Professional Ethics / Banking",
            "dilemmas": ["Compassion vs Integrity", "Means vs Ends", "Fiduciary Duty vs Friendship"],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the ethical issues involved?",
                    "answer": "1. **Misappropriation**: Using dormant funds is theft, regardless of intent.\n2. **Breach of Trust**: Bankers are custodians of public money.\n3. **Moral Hazard**: Setting a precedent that stealing is okay if the cause is 'good'."
                },
                {
                    "id": "c",
                    "question": "How would you react to the situation?",
                    "answer": "I would be compelled to **report this**. While I sympathize with the colleague, the Manager's action is illegal/criminal. I would advise the colleague to self-report to mitigate consequences, but I cannot be complicit by staying silent. The integrity of the banking system is non-negotiable."
                }
            ]
        },
        "2023-CS2": {
            "category": "Medical Ethics / Crisis Management",
            "dilemmas": ["Rule of Law vs Right to Life", "Procedure vs Conscience"],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the ethical issues involved?",
                    "answer": "**Bureaucracy vs Humanity**: Rules say 'only blood banks', but reality demands immediate action.\n**Medical Oath**: The Hippocratic Oath ('First do no harm') implies saving life is the highest duty, yet transfusing unverified blood carries medical risks."
                },
                {
                    "id": "b",
                    "question": "Evaluate the options.",
                    "answer": "**Refuse Transfusion**: The woman likely dies. You are legally safe but morally guilty of inaction.\n**Transfuse**: Risk of infection/reaction and legal penalty. But high chance of saving two lives (mother + child). \n**Decision**: Transfuse. Use the 'Good Samaritan' principles and 'Doctrine of Necessity'. Document the blood group compatibility testing done on the spot (if kits available) to minimize medical risk."
                }
            ]
        },
        "2023-CS3": {
            "category": "Work Culture / Gender Rights",
            "dilemmas": ["Professional Ambition vs Family Responsibility", "Exploitation vs Dedication"],
            "questions": [
                {
                    "id": "a",
                    "question": "Discuss the ethical issues involved in this case.",
                    "answer": "**Toxic Work Culture**: Expecting 24/7 availability erodes human dignity.\n**Work-Life Balance**: The failure of the organization to respect personal boundaries.\n**Gender Roles**: The disproportionate burden on women to balance 'super-mom' and 'super-employee' roles."
                },
                {
                    "id": "b",
                    "question": "Briefly describe at least four laws...",
                    "answer": "1. **Maternity Benefit Act 2017**: 26 weeks leave, mandatory creche for 50+ employees.\n2. **POSH Act 2013**: Prevention of Sexual Harassment.\n3. **Equal Remuneration Act**: No gender pay gap.\n4. **Factories Act 1948**: Limits workings hours and night shifts for women (with exceptions)."
                },
                {
                    "id": "c",
                    "question": "Imagine you are in a similar situation. What suggestions would you make to mitigate such working conditions?",
                    "answer": "1. **Right to Disconnect**: Policy to avoid after-hours calls.\n2. **Outcome over Hours**: Judge performance by results, not face time.\n3. **Support Systems**: Office creches and flexible working hours (flexi-time)."
                }
            ]
        },
        "2023-CS4": {
            "category": "Political Neutrality / Corruption",
            "dilemmas": ["Integrity vs Self-Preservation", "Political Neutrality vs Opportunism"],
            "questions": [
                {
                    "id": "a",
                    "question": "As a conscientious civil servant, evaluate the options available to Vinod.",
                    "answer": "1. **Join the Opposition Member**: Unethical. Violates political neutrality (Conduct Rules).\n2. **Ignore**: Cowardly. Condones corruption.\n3. **Official Action**: Initiate an internal enquiry or send a report to the Lokayukta/CVC based on valid evidence, without involving the opposition party. This upholds the law without playing politics."
                },
                {
                    "id": "b",
                    "question": "In the light of the above case, comment upon the ethical issues that may arise due to the politicization of bureaucracy.",
                    "answer": "1. **Loss of Objectivity**: Civil servants serve parties, not the constitution.\n2. **Cronysim**: Transfers and postings based on loyalty vs merit.\n3. **Policy Paralysis**: Officers fear taking decisions that might upset political masters."
                }
            ]
        },
        "2023-CS5": {
            "category": "Workplace Harassment / Emotional Intelligence",
            "dilemmas": ["Respect for Seniority vs Protection of Junior", "Project Success vs Employee Well-being"],
            "questions": [
                {
                    "id": "a",
                    "question": "What are the ethical issues involved in the above case?",
                    "answer": "**Professional Jealousy**: The Chief Architect prioritizing ego over project success.\n**Workplace Bullying**: Creating a hostile environment.\n**Mental Health**: Assessing the psychological cost of the project on Seema."
                },
                {
                    "id": "b",
                    "question": "What are the options available to you in order to complete the project as well as to retain Seema in the organization?",
                    "answer": "1. **Facilitated Dialogue**: Hold a meeting to define roles clearly, giving the Chief 'Mentorship' status and Seema 'Design Lead'.\n2. **Zero Tolerance**: Warn the Chief Architect that harassment is unacceptable.\n3. **Separation**: If toxicity persists, change Seema's reporting line directly to you."
                },
                {
                    "id": "c",
                    "question": "What would be your response to Seema's predicament?...",
                    "answer": "I would assure her of safety and value. I would institute an **Anonymous Grievance Cell**, regular sensitization workshops on toxic behavior, and a 'Mentorship Program' to bridge generational gaps."
                }
            ]
        },
        "2023-CS6": {
            "category": "Social Media Ethics / Parenting",
            "dilemmas": ["Privacy vs Public Image", "Retaliation vs Restraint", "Parental Protection vs Teaching Resilience"],
            "questions": [
                {
                    "id": "a",
                    "question": "Based on the above case study, discuss the ethical issues involved in the use of social media.",
                    "answer": "**Cyberbullying**: The anonymity of the internet empowering cruelty.\n**Privacy Violation**: Filming minors without consent.\n**Mob Mentality**: Trial by social media without facts."
                },
                {
                    "id": "b",
                    "question": "Discuss the pros and cons of using social media by you to put across the facts...",
                    "answer": "**Pros**: clears the air, controls the narrative, rallies support. \n**Cons**: Validates the trolls, violates the privacy of the *other* children (the bullies are also minors), creates a 'mud-slinging' contest unbecoming of a senior official. \n**Better Path**: Legal route (Cyber Cell) + School Administration action."
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
            
            # Map answers to question IDs
            # We assume order matches or ID matches. The knowledge base uses 'a', 'b', etc.
            # The data might use auto-generated IDs or 'a'.'b'.
            # Let's try to match by ID first, then index.
            
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
