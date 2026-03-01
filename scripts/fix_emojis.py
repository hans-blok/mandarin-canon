import codecs

# Read the file
with codecs.open(r'c:\git\mandarin-canon\grondslagen\aeo\mandarin-ordeningsconcepten.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix encoding issues
replacements = {
    ' ðŸ"': '',
    ' â­': '',
    ' âŒ': '',
    ' ðŸ'«': '',
    ' ðŸ'¡': '',
    ' ðŸ·ï¸': '',
    ' ðŸ"„': '',
    ' ðŸ'¬': '',
    ' ðŸ"š': '',
    ' ðŸ¤': '',
    ' ðŸ§': '',
    ' ðŸ"‹': '',
    ' ðŸ"'': '',
    ' ðŸŒ': '',
    ' ðŸ§ ': '',
    'hiÃ«rarchie': 'hiërarchie',
    'AnalogieÃ«n': 'Analogieën',
    'categorieÃ«n': 'categorieën',
    'Ã©Ã©n': 'één',
    'geÃ¯dentificeerde': 'geïdentificeerde'
}

for old, new in replacements.items():
    content = content.replace(old, new)

# Write back
with codecs.open(r'c:\git\mandarin-canon\grondslagen\aeo\mandarin-ordeningsconcepten.md', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done - emojis removed and encoding fixed')
