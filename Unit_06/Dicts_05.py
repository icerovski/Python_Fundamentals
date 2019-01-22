# 05. Social Media Posts

line = input()
words = line.split()
social_media_dict = {}


while not line == "drop the media":
    command = words[0]
    post_name = words[1]

    if command == "post":
        social_media_dict[post_name] = {'Likes': 0,
                                        'Dislikes': 0,
                                        'Comments': []}
    elif command == "like":
        if post_name in social_media_dict.keys():
            social_media_dict[post_name]['Likes'] += 1

    elif command == "dislike":
        if post_name in social_media_dict.keys():
            social_media_dict[post_name]['Dislikes'] += 1

    elif command == "comment":
        author = words[2]
        content = words[3:]
        if post_name in social_media_dict.keys():
            comment = {author: content}
            social_media_dict[post_name]['Comments'].append(comment)

    line = input()
    words = line.split()

for post, post_data in social_media_dict.items():
    print(f"Post: {post} | Likes: {post_data['Likes']} | Dislikes: {post_data['Dislikes']}")
    print("Comments:")
    if not post_data["Comments"]:
        print('None')
        continue

    for i in post_data['Comments']:
        for author, comment in i.items():
            print(f"*  {author}: {' '.join(comment)}")
