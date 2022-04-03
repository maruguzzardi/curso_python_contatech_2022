def count_words(string: str) -> dict:
    string = string.split()
    words = {}
    for index in string:
        if index in words:
            words[index] += 1
        else:
            words[index] = 1
    return words


def most_repeated(words: dict) -> tuple:
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq


text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))
