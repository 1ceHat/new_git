def all_variants(text):
    len_slice = 0
    length = len(text)
    while len_slice <= length:
        for i in range(length):
            cur_slice = text[i:i+len_slice]
            for j in range(i+len_slice, length):
                if text[j] not in cur_slice:
                    yield cur_slice + text[j]
            if len_slice == 0:
                break
        len_slice += 1


a = all_variants('abcdefghgklmnopqrstuvwxyz')
for i in a:
    print(i)