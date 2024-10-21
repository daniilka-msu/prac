import timeit
from collections import Counter

def count_word_occurrences_dict(text):
 words = text.lower().split()
 word_counts = {}
 for word in words:
  if word in word_counts:
   word_counts[word] += 1
  else:
   word_counts[word] = 1
 return word_counts

def count_word_occurrences_counter(text):
 words = text.lower().split()
 word_counts = Counter(words)
 return word_counts

if __name__ == "__main__":
 text = "This is a test. This is a test. This is a test!" * 1000
 timer_dict = timeit.Timer(lambda: count_word_occurrences_dict(text))
 time_dict = timer_dict.timeit(number=1000)
 timer_counter = timeit.Timer(lambda: count_word_occurrences_counter(text))
 time_counter = timer_counter.timeit(number=1000)
 print(f"Среднее время выполнения dict: {time_dict:.6f} секунд")
 print(f"Среднее время выполнения Counter: {time_counter:.6f} секунд")

