def anangram(a,b):
    a = a.replace(' ','').lower()
    b = b.replace(' ','').lower()

    if(len(a)!=len(b)):
        return False
    counter = {}

    for letter in a:
        if letter in counter:
            counter[letter] +=1 #hello , ol hell
            print(counter)
        else:
            counter[letter] = 1
            print(counter)


    for letter in b:
        if letter in counter:
            counter[letter] -= 1
            print(counter)
        else:
            return False


    for k in counter:
        if counter[k] != 0:
            return False
    print(counter)

    return True
    pass


from nose.tools import assert_equal


class AnagramTest(object):
    def test(self, sol):
        assert_equal(sol('go go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print('ALL TEST CASES PASSED')


# Run Tests
t = AnagramTest()
t.test(anangram)