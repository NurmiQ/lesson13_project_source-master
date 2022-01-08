import json


def read_json():
    with open('posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


# print(read_json())


def get_hash():
    match_hash = []
    g_hash = read_json()
    for tag in g_hash:
        content = tag['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                match_hash.append(word[1:])
    return match_hash


# print(get_hash())
