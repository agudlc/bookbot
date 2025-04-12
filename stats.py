def count_words(text):
    return len(text.split())

def characters_count(text):
    count = {}
    for character in text:
        ch_lower = character.lower()
        if (ch_lower in count):
            count[ch_lower] += 1
        else:
            count[ch_lower] = 1
    return count

def sort_on(dict):
    return dict["count"]

def sort_ch(ch_dic):
    sorted_list = []
    for k in ch_dic:
        sorted_list.append(
            {
                "character": k,
                "count": ch_dic[k]
            }
        )
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list