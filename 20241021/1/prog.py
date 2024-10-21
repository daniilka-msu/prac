def letters(text):
 pairs = set()
 for i in range(len(text) - 1):
  if text[i].isalpha() and text[i + 1].isalpha():
   pairs.add((text[i].lower(), text[i + 1].lower()))
 return len(pairs)

if __name__ == "__main__":
 text = input("")
 result = letters(text)
 print(result)

