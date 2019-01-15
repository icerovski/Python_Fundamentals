# 08. Append Lists

str_list = list(input().split('|'))

# Empty strings are considered false in a Boolean context
def is_not_blank(my_string):
    if my_string and my_string.strip():
        # my_string is not None AND my_string is not empty or blank
        return True
    # my_string is None OR my_string is empty or blank
    return False


def split_str(a):
    result = " ".join(a.split())
    return result


new_str_list = [split_str(el) for el in reversed(str_list) if is_not_blank(el)]

print(' '.join(new_str_list))