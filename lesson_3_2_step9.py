#s = 'My Name is Julia'
#if 'Name' in s:
    #print('Substring found')

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    if substring not in full_string:
        print(f"expected '{substring}' to be substring of '{full_string}'")

def test_substring1(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

test_substring1('some_text', 'soe')





