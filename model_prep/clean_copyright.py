def remove_copyright_sections(text):
    start_marker = "PISMOSW"
    end_marker = "(klosowski@ielepolslgliwicepl)"
    
    while start_marker in text and end_marker in text:
        start_index = text.find(start_marker)
        end_index = text.find(end_marker) + len(end_marker)
        text = text[:start_index] + text[end_index:]
    
    return text

with open("bible_pol.txt", "r", encoding="utf-8") as file:
    text = file.read()

cleaned_text = remove_copyright_sections(text)

with open("bible_pol_cleaned.txt", "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("Usunięcie sekcji copyright zakończone!")
