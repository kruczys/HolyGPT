import re

def clean_text(text):
    text = re.sub(r'[,.!?;:"\'”\-]', '', text)
    
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        if not re.search(r'\d+$', line):
            cleaned_lines.append(line)
    
    cleaned_text = '\n'.join(cleaned_lines)
    cleaned_text = re.sub(r'PISMOSW\s*\d+\s*BETA.*?\(\w+@\w+\.\w+\)', '', cleaned_text, flags=re.DOTALL)
    
    return cleaned_text

with open("bible_pol_unclean.txt", "r", encoding="utf-8") as file:
    raw_text = file.read()

cleaned_text = clean_text(raw_text)

with open("bible_pol.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("Czyszczenie zakończone!")
