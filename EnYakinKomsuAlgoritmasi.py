def open_file(file_name):
    with open(file_name, "r") as f:
        text = f.read()
        f.close()
        return text

def parse_words(text):
    #her kelimeyi tek tek ayirma islemi
    words = text.split(' ')
    words = [s.strip() for s in words if s.strip() != '']
    return words

def count_word_in_words(word, sentence):
    #kelime sayisini bulma islemi
    count = 0
    words = sentence.split()
    for w in words:
        if word.lower() in w.lower():
            count += 1
    return count

def count_word_in_text(word, text):
    #aranan kelimeyi text'te bulma islemi
    words = parse_words(text)
    counts = []
    for s in words:
        count = count_word_in_words(word, s)
        counts.append(count)
    return sum(counts)


def main(text, word_list):
    for word in word_list:
        count = count_word_in_text(word=word, text=text)
        print(f'{word} kelimesi text icinde {count} kez gecmektedir.')
        
if __name__ == '__main__':
    text = open_file("alice_in_wonderland.txt")
    word_list = ["upon", "sigh","Dormouse", "jury-box", "swim"]
    main(text=text, word_list=word_list)
