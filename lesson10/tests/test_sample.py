from pytest import mark


def func(x):
    return x + 1

@mark.smoke
def test_sample():
    assert func(3) == 3

# def sample_test():
#     assert True