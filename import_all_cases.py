import json
import re
import os

def parse_text_to_cases(text_path):
    if not os.path.exists(text_path):
        print(f"Error: {text_path} not found.")
        return {}

    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find all year headers
    # Years seem to be on their own lines: ^20\d\d$
    year_pattern = re.compile(r'^\s*(20\d{2})\s*$', re.MULTILINE)
    matches = list(year_pattern.finditer(text))
    
    parsed_data = {}

    for i in range(len(matches)):
        year = int(matches[i].group(1))
        start_idx = matches[i].end()
        end_idx = matches[i+1].start() if i + 1 < len(matches) else len(text)
        
        year_block = text[start_idx:end_idx]
        parsed_data[year] = parse_year_block(year_block, year)

    return parsed_data

def parse_year_block(block, year):
    # Split by case number.
    # We'll use a regex that looks for start of line + number + DOT.
    # Strict regex to avoid matching ages, amounts, etc.
    
    # Regex: ^\s*(?:Q\.\s*(\d{1,2})\.?|(\d{1,2})\.)\s+
    # Matches "1. ", "Q.1 ", "Q.1. "
    # Ensures that if there is no "Q.", there MUST be a dot after the number.
    
    case_pattern = re.compile(r'^\s*(?:Q\.\s*(\d{1,2})\.?|(\d{1,2})\.)\s+', re.MULTILINE)
    case_matches = list(case_pattern.finditer(block))
    
    cases = []
    
    for i in range(len(case_matches)):
        # Group 1 is for Q.N format, Group 2 is for N. format
        case_num = int(case_matches[i].group(1) or case_matches[i].group(2))
        start_idx = case_matches[i].end()
        
        # End is start of next case
        end_idx = case_matches[i+1].start() if i + 1 < len(case_matches) else len(block)
        
        full_case_text = block[start_idx:end_idx].strip()
        
        # Attempt to split scenario and questions
        # Look for the first (a) or a)
        q_start = re.search(r'^\s*\(?[a-z]\)', full_case_text, re.MULTILINE)
        
        if q_start:
            scenario = full_case_text[:q_start.start()].strip()
            raw_questions = full_case_text[q_start.start():].strip()
        else:
            scenario = full_case_text
            raw_questions = ""
            
        # Clean scenario text (remove excessive newlines)
        scenario = re.sub(r'\n+', ' ', scenario)
        
        # Parse questions from raw text
        questions_list = []
        if raw_questions:
            # Split by (a), (b), etc.
            q_splits = list(re.finditer(r'^\s*\(?([a-z])\)', raw_questions, re.MULTILINE))
            for k in range(len(q_splits)):
                q_id = q_splits[k].group(1)
                q_s = q_splits[k].end()
                q_e = q_splits[k+1].start() if k + 1 < len(q_splits) else len(raw_questions)
                q_text = raw_questions[q_s:q_e].strip().replace('\n', ' ')
                questions_list.append({
                    "id": q_id,
                    "question": q_text,
                    "answer": "Answer to be developed..." # Placeholder
                })
        
        cases.append({
            "case_number": case_num,
            "scenario": scenario,
            "questions": questions_list
        })
        
    return cases

def generate_fresh_data(json_path, parsed_cases):
    """
    Generates a fresh data.json from parsed_cases.
    It attempts to PRESERVE existing answers from the old json_path if they exist.
    """
    existing_answers_map = {}
    
    # Try to read existing answers to preserve them
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
            for item in old_data:
                # Store questions for (Year, CaseNum)
                key = (item['year'], item['case_number'])
                existing_answers_map[key] = item.get('questions', [])
    except (FileNotFoundError, json.JSONDecodeError):
        print("No valid existing data found. Starting completely fresh.")

    new_data_list = []
    
    # Flatten parsed_cases into a list
    all_years = sorted(parsed_cases.keys(), reverse=True)
    
    for year in all_years:
        # Sort cases by number
        cases = sorted(parsed_cases[year], key=lambda x: x['case_number'])
        
        for p_case in cases:
            key = (year, p_case['case_number'])
            
            # Check if we have existing answers to preserve
            preserved_questions = None
            if key in existing_answers_map:
                old_qs = existing_answers_map[key]
                # Simple check: if old questions look populated (have substantial answers), use them
                # Check if at least one answer is not the placeholder
                has_real_answer = any(q.get('answer') and "Answer to be developed" not in q.get('answer') for q in old_qs)
                if has_real_answer:
                    preserved_questions = old_qs
            
            final_questions = preserved_questions if preserved_questions else p_case['questions']
            
            # fallbacks for empty questions if PDF didn't split well
            if not final_questions:
                 final_questions = [{"id": "a", "question": "Analyze the issues.", "answer": "Answer to be developed..."}]

            new_item = {
                "id": f"{year}-CS{p_case['case_number']}",
                "year": year,
                "case_number": p_case['case_number'],
                "title": f"UPSC {year} Case Study {p_case['case_number']}",
                "category": "General Ethics", # Placeholder, ideally we'd have a classifier
                "scenario": p_case['scenario'],
                "dilemmas": ["Ethical Dilemma 1", "Ethical Dilemma 2"], # Placeholder
                "questions": final_questions
            }
            new_data_list.append(new_item)

    # Write fresh data
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(new_data_list, f, indent=2, ensure_ascii=False)
    
    print(f"Generated fresh data.json with {len(new_data_list)} cases.")
    print("Orphaned cases (not in PDF) have been removed.")

if __name__ == "__main__":
    parsed = parse_text_to_cases('extracted_text.txt')
    generate_fresh_data('src/data.json', parsed)
