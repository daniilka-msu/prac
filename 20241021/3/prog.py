import re
from collections import Counter

W = int(input())
text_lines = []

try:
   while True:
      line = input()
      if line == '':
          break
      text_lines.append(line)
except EOFError:
    pass

text = '\n'.join(text_lines)
cleaned_text = re.sub(r'[^a-zA-Z\s]', ' ', text).lower()
words = cleaned_text.split()
words_of_length_W = [word for word in words if len(word) == W]
word_counts = Counter(words_of_length_W)

if word_counts:
    max_count = max(word_counts.values())
    most_popular_words = sorted([word for word, count in word_counts.items() if count == max_count])
    result = ' '.join(most_popular_words)
else:
    result = ""

print(result)

