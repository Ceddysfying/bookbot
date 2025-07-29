def number_of_words(text):
    return len(text.split())

def number_of_chars(text):
    lower_chars = text.lower()
    chars = {}
    
    for char in lower_chars:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars 
    
def sort_on(items):
    return items["num"]

def sort_chars(chars):
    sorted_chars = []

    for key in chars:
        sorted = {}
        sorted["char"] = key
        sorted["num"] = chars[key]
        sorted_chars.append(sorted)
    
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
