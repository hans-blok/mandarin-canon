import re

file_path = r'c:\git\mandarin-canon\grondslagen\aeo\mandarin-ordeningsconcepten.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix encoding artifacts for Dutch characters
content = content.replace('Ã«', 'ë')
content = content.replace('Ã©', 'é')
content = content.replace('Ã¯', 'ï')
content = content.replace('â†’', '→')
content = content.replace('â€”', '—')
content = content.replace('â€‘', '-')

# Remove weird characters and emojis
weird_chars = [
    ' ’«', ' ·ï¸', ' âŒ', ' â­', ' ’¡', ' “', ' ¤', ' §­', ' ”’', ' “š', ' Œ', ' § ', ' “‹',
    ' 📝', ' ⭐', ' ❌', ' 💫', ' 🔄',
    '’«', '·ï¸', 'âŒ', 'â­', '’¡', '“', '¤', '§­', '”’', '“š', 'Œ', '§ ', '“‹',
    '📝', '⭐', '❌', '💫', '🔄',
    '·ï¸', 'ï¸'
]

for char in weird_chars:
    content = content.replace(char, '')

# Also rename "inhoudelijke as" to "betekenis-as" as requested previously
content = content.replace('Inhoudelijke as', 'Betekenis-as')
content = content.replace('inhoudelijke as', 'betekenis-as')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleanup complete.")
