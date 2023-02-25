CONTENT_STORE_SIZE = 5
PACKET_LIFETIME = 20
MAX_STEPS = 550


# 前缀匹配的长度
# the length of prefix compactible
def count_prefix_length(s1, s2):
    i, len1, len2 = 0, len(s1), len(s2)
    while i < len1 and i < len2 and s1[i] == s2[i]:
        i += 1
    return i
