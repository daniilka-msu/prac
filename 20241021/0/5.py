from collections import Counter

def count_word_occurrences(text):
 words = text.lower().split()
 word_counts = Counter(words)
 return word_counts


if __name__ == "__main__":
 text = "This is a test. This is a test. This is a test!"
 word_counts = count_word_occurrences(text)
 for word, count in word_counts.items():
  print(f"{word}: {count}")

