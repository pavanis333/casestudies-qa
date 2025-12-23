import json
import re

def update_scenarios(json_path, text_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    with open(text_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Dictionary to map year -> map of case_number -> scenario text
    scenarios_db = {}
    
    # Split by years. We know years are 4 digits on a line.
    # But checking the text file, years are printed as "2025\n" etc.
    # We can split by year headers.
    
    years = [2025, 2024, 2023, 2022, 2021, 2020, 2018, 2013] # Added known years from json
    
    # We need to process the text to associate blocks with years.
    # A simple way involves finding the indices of the year headers.
    
    year_indices = []
    for year in years:
        # Regex for year on a standalone line, possibly with whitespace
        matches = list(re.finditer(rf'^\s*{year}\s*$', text, re.MULTILINE))
        for m in matches:
            year_indices.append((year, m.start()))
            
    year_indices.sort(key=lambda x: x[1])
    
    for i in range(len(year_indices)):
        year, start_idx = year_indices[i]
        end_idx = year_indices[i+1][1] if i + 1 < len(year_indices) else len(text)
        
        year_block = text[start_idx:end_idx]
        scenarios_db[year] = {}
        
        # Regex to find case studies within the year block
        # Patterns: 
        # 1. Standard: "1. Text..."
        # 2. Q-Format: "Q.1 Text..." (seen in 2024)
        
        # We use an alternation group.
        # Group 1 will be the number if it matches "1."
        # Group 2 will be the number if it matches "Q.1"
        
        case_splits = list(re.finditer(r'^\s*(?:(\d+)\.|Q\.(\d+))\s+', year_block, re.MULTILINE))
        
        for j in range(len(case_splits)):
            # Determine which group matched
            if case_splits[j].group(1):
                case_num = int(case_splits[j].group(1))
            else:
                case_num = int(case_splits[j].group(2))
            
            c_start = case_splits[j].end()
            
            # End is either the next case start or the next year (which corresponds to end of string here)
            # BUT, we only want the scenario part, not the questions.
            # So we look for the first occurrence of "(a)" or "a)" after c_start
            
            c_end_limit = case_splits[j+1].start() if j + 1 < len(case_splits) else len(year_block)
            case_full_text = year_block[c_start:c_end_limit]
            
            # Find the start of questions
            # Common patterns: "(a)", "a)", "Q.1 (a)"?, "1.", etc. 
            # From the text, it seems mostly "(a)" or "a)"
            
            q_start_match = re.search(r'^\s*\(?a\)', case_full_text, re.MULTILINE)
            if q_start_match:
                scenario_text = case_full_text[:q_start_match.start()]
            else:
                # Fallback: maybe it didn't match (a), try just taking the whole block if it looks like there are no questions?
                # Or look for "Question" word?
                # Let's just strip and assume it's the scenario if no (a) found, though likely there is one.
                scenario_text = case_full_text
            
            # Clean up text
            scenario_text = scenario_text.strip()
            # Remove multiple newlines
            scenario_text = re.sub(r'\n+', ' ', scenario_text)
            
            scenarios_db[year][case_num] = scenario_text

    # Now update the json data
    updated_count = 0
    for item in data:
        y = item.get('year')
        cn = item.get('case_number')
        
        if y in scenarios_db and cn in scenarios_db[y]:
            new_text = scenarios_db[y][cn]
            if len(new_text) > 20: # Sanity check, ensure it's not empty or just a few chars
                item['scenario'] = new_text
                updated_count += 1
            else:
                print(f"Warning: Extracted text for {y} Case {cn} seems too short: {new_text[:50]}...")
        else:
            print(f"Warning: Could not find scenario for {y} Case {cn}")

    print(f"Updated {updated_count} scenarios.")

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    update_scenarios('src/data.json', 'extracted_text.txt')
