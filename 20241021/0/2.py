def count_unique_vowels_consonants(text):
 vowels = set("aeiou")
 consonants = set("bcdfghjklmnpqrstvwxyz")
 unique_vowels = vowels.intersection(set(text.lower()))
 unique_consonants = consonants.intersection(set(text.lower()))
 return len(unique_vowels), len(unique_consonants)


if __name__ == "__main__":
 text = "aabABbcD123"
 unique_vowels, unique_consonants = count_unique_vowels_consonants(text)
 print(f"Гласных: {unique_vowels}")
 print(f"Согласных: {unique_consonants}")

