import spacy
from spacy.lang.en.stop_words import STOP_WORDS
nlp = spacy.load('en_core_web_md')
domain_stop_words = ['chapter', '<', '>', ';', 'vinegar', 'of', '%']
for word in domain_stop_words:
    STOP_WORDS.add(word)
STOP_WORDS1 = STOP_WORDS.copy()
STOP_WORDS1.discard('other')


def nlp0(sentence):
    sentence = sentence.lower()

    word_list = [token.lemma_ for token in nlp(sentence)
                 if not token.is_stop and not token.is_punct]

    return word_list


def nlp1(sentence):
    sentence = sentence.lower()
    word_list = [str(token.lemma_) for token in nlp(sentence)
                 if str(token) not in STOP_WORDS1 and not token.is_punct]
    word_list1 = []
    flag = 0
    for i in word_list:
        if i == 'other':
            if flag == 0:
                word_list1.append(i)
            flag = 1
        else:
            word_list1.append(i)

    return word_list1


