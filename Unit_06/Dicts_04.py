# 04. Forum Topics
line = input()
forum_dict = {}

# def unique(sequence):
#     seen = set()
#     return [x for x in sequence if not(x in seen or seen.add(x))]

while not line == "filter":
    words = line.split(" -> ")
    topic = words[0]
    hashtags = words[1].split(", ")

    if topic not in forum_dict.keys():
        forum_dict[topic] = hashtags
    else:
        forum_dict[topic].extend(hashtags)

    line = input()

sequence = set(input().split(', '))

for topic, hashtags in forum_dict.items():
    ht_set = sorted(set(hashtags), key= hashtags.index)

    if sequence.issubset(ht_set):
        print(f"{topic} | {', '.join(map(lambda x: '#' + x, ht_set))}")

