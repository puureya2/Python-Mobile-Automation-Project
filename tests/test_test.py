
def test(letter):
    assert letter == 10
 
def test_dict(dict):
    for letter in dict:
        print(letter[0])


a = 10
test(a)

dict = {"a": 2, "b": 3, "c": 2}
test_dict(dict)