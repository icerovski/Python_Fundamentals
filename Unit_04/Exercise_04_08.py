# 08. Append Lists

str_list = list(input().split('|'))


def split_str(a):
    result = " ".join(a.split())
    return result


new_str_list = [split_str(el) for el in reversed(str_list)]


print(' '.join(new_str_list))