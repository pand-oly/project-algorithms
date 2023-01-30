def is_palindrome_iterative(word: str) -> bool:
    """Faça o código aqui."""
    if len(word) == 0 or word is None:
        return False

    start = 0
    end = len(word) - 1
    result = True

    while start != end:
        if word[start] == word[end]:
            result = True
        else:
            return False

        start += 1
        end -= 1

        if start >= end:
            break

    return result
