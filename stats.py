def count_words(text):
    count = len(text.split())
    return count


def character_times(text):
    text = text.lower()
    characters_count = {}
    for c in text:
        if c in characters_count:
            characters_count[c] += 1
        else:
            characters_count[c] = 1
        
    return characters_count

def sort_on(items):
    return items["num"]

def sorted_dictionary(dic):
    sorted_dics = []
    for key in dic:
        if key.isalpha():
            sorted_dics.append({'name': key, "num": dic[key]})
    sorted_dics.sort(reverse=True, key=sort_on)
    return sorted_dics

