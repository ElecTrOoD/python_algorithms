# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке. Примечание: в сумму не включаем пустую строку и
# строку целиком. Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9

from hashlib import sha256


def find_substring(string):
    hash_list = set()
    for i in range(len(string)):
        for j in range(len(string), i, -1):
            substring = bytes(string[i:j], encoding='utf-8')
            string_hash = sha256(substring).hexdigest()
            hash_list.add(string_hash)
    exceptions = [sha256(bytes(string, encoding='utf-8')).hexdigest(), sha256(b'').hexdigest()]
    list(map(lambda x: hash_list.discard(x), exceptions))
    # Не решил как лучше будет удалять ненужные хеши из множества. Больше нравится список исключений, потому что в
    # любой момент можно добавить новое правило не плодя кучу повторяющегося кода.
    # hash_list.discard(sha1(bytes(string, encoding='utf-8')).hexdigest())
    # hash_list.discard(sha1(b'').hexdigest())
    return len(hash_list)


a = 'Привет world!'
b = 'sova'
c = 'papa'
e = 'a'

print(find_substring(a))
print(find_substring(b))
print(find_substring(c))
print(find_substring(e))
