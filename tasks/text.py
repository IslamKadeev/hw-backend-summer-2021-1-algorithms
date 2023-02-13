from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """

    if " ".join(text.split()) == " ":
        return None, None

    text = text.split()
    sortedtext = sorted(text)

    if len(sortedtext) <= 1:
        return None, None
    else:
        shortest_word = sortedtext[0]
        longest_word = sortedtext[-1]
        for element in sortedtext:

            if element.split().count(','):
                element = "".join(element[:-1])

            if len(element) > len(longest_word):
                longest_word = element
            if len(element) < len(shortest_word):
                shortest_word = element

    return shortest_word, longest_word
