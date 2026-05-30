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

    total_characters = 0

    for word in words:
        total_characters += len(word)

    if len(words) > 0:
        return total_characters / len(words)
    else:
        return 0


def count_paragraphs(text):

    if not text.strip():
        return 1

    paragraphs = re.split(r'\n\s*\n', text.strip())

    return len(paragraphs)


def count_sentences(text):

    if not text.strip():
        return 1

    sentence_count = 0


    for character in text:

        # CONDITIONAL
        if character == "." or character == "!" or character == "?":
            sentence_count += 1

    return sentence_count


news_article = """
The latest science fiction movie has been receiving massive attention from movie fans around the world.
Many viewers praised the visual effects, action scenes, and emotional storytelling throughout the film.

Critics have also shared positive reviews about the performances of the lead actors.
Some fans believe the movie could become one of the biggest blockbuster releases of the year!

The director explained that the movie was inspired by classic action and adventure films from the early 2000s.
Movie discussions on social media continue to grow every day.
"""


search_word = "movie"

print("Specific word count:", count_specific_word(news_article, search_word))

print("Most common word:", identify_most_common_word(news_article))

print("Average word length:", calculate_average_word_length(news_article))

print("Paragraph count:", count_paragraphs(news_article))

print("Sentence count:", count_sentences(news_article))