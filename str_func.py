def capitalize_string(input_str):
    """Принимает на вход строку и возвращает ее со всеми заглавными буквами!"""
    return input_str.upper()

def capitalize_first_letters(input_str):
    """Делает заглавными первые буквы каждого слова в строке, поступившей на вход функции."""
    words = input_str.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
