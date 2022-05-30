def clear_string(text):
    return_word = text
    for char in text:
        if str(char) in "!@#$%^&*()_+=?/-<>,.';:][{} ":
            return_word = return_word.replace(char, "")

    return str(return_word).lower()
