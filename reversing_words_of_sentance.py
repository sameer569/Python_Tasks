sentence="i am a python testing engineer"


def reverse_sentence_word(sentence):
    words=sentence.split(" ")

    new_words=[word[::-1] for word in words]

    new_sentence=" ".join(new_words)

    return new_sentence

print(reverse_sentence_word(sentence))
