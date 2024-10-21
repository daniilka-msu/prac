from collections import Counter

def can_make_note(article, note):
 article_words = Counter(article.lower().split())
 note_words = Counter(note.lower().split())
 difference = note_words - article_words
 return difference == Counter()

if __name__ == "__main__":
 article = "держитесь подальше от торфяных болот"
 note = "держитесь подальше"

 if can_make_note(article, note):
  print("Записку можно сделать из статьи.")
 else:
  print("Записку нельзя сделать из статьи.")

