import timeit

def count_unique_vowels_consonants(text):
 vowels = set("aeiou")
 consonants = set("bcdfghjklmnpqrstvwxyz")
 unique_vowels = vowels.intersection(set(text.lower()))
 unique_consonants = consonants.intersection(set(text.lower()))
 return len(unique_vowels), len(unique_consonants)


if __name__ == "__main__":
 text = "aabABbcD123" * 1000
 timer = timeit.Timer(lambda: count_unique_vowels_consonants(text))
 time = timer.timeit(number=1000)
 print(f"Среднее время выполнения: {time:.6f} секунд")

