class TestClass:
    def test_one(self):
        x = "dave"
        assert 'e' in x

    def test_two(self):
        x='hello'
        assert hasattr(x,"check")