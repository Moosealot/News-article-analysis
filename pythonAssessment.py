import re
from collections import Counter


def count_specific_word(text, search_word):
    if not text:
        return 0

    text = text.lower()
    search_word = search_word.lower()

    words = re.findall(r'\b\w+\b', text)

    count = 0
    index = 0

    while index < len(words):
        if words[index] == search_word:
            count += 1

        index += 1

    return count


def identify_most_common_word(text):
    if not text.strip():
        return None

    text = text.lower()

    words = re.findall(r'\b\w+\b', text)

    word_counts = Counter(words)

    return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    if not text.strip():
        return 0

    words = re.findall(r'\b\w+\b', text)

    if len(words) == 0:
        return 0

    total_characters = 0

    for word in words:
        total_characters += len(word)

    return total_characters / len(words)


def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = re.split(r'\n\s*\n', text.strip())

    return len(paragraphs)


def count_sentences(text):
    if not text.strip():
        return 1

    sentences = re.findall(r'[.!?]', text)

    return len(sentences)


news_article = """
Technology companies are rapidly advancing artificial intelligence solutions.
Many startups are investing heavily in NLP technologies.

These innovations are transforming industries worldwide.
Will AI replace traditional jobs? Experts continue to debate this issue!

Artificial intelligence is becoming more common every day.
"""


search_word = "artificial"

print("Specific word count:", count_specific_word(news_article, search_word))

print("Most common word:", identify_most_common_word(news_article))

print("Average word length:", calculate_average_word_length(news_article))

print("Paragraph count:", count_paragraphs(news_article))

print("Sentence count:", count_sentences(news_article))