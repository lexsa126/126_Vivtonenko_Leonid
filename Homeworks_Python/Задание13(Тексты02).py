def words(s):
    s = s.strip()
    s = s[:800]
    words = s.split()
    return len(words)
text = "Глеб    работает   в    офисе    в Архангельске"
word = words(text)
print(word)