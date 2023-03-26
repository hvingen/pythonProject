"""Een lijst woorden uit een URL ophalen en printen.

Gebruik:
    python3 words.py
"""


import sys
from urllib.request import urlopen


def fetch_words(url):
    """Een lijst woorden uit een URL ophalen.

    Args:
        url: De URL van een UTF-8-tekstdocument

    Retourneert:
        Een lijst strings met de woorden
        uit het document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """Druk één item per regel af.

    Args:
        items: Een iterabele reeks afdrukbare items.
    """
    for item in items:
        print(item)


def main(url):
    """Drukt elk woord uit een document af dat van een URL komt.

    Args:
        url: De URL van een UTF-8-tekstdocument.
    """
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1]) # Het 0-de argument is de modulebestandsnaam.

