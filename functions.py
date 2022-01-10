import json


def read_json(filename):
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# print(read_json())


def get_hash(data):
    match_hash = []
    for tag in data:
        content = tag['content']
        words = content.split()
        for word in words:
            if word.startswith('#'):
                match_hash.append(word[1:])
    return match_hash


# print(get_hash())


def get_posts_by_tag(data, tag):
    results = []
    for post in data:
        if f'#{tag}' in post['content']:
            results.append(post)
    return results


# print(get_posts_by_tag('пирог'))


def add_post(filename, post):
    posts = read_json()
    posts.append(post)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False, indent=4, sort_keys=True)
