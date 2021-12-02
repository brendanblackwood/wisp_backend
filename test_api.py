import hug
import api

from inspect import getmembers, isfunction


class Test:
    def test_main__negative_number__invalid():
        """Test that only positive numbers are accepted."""
        response = hug.test.get(api, '/specialmath/-1')
        assert response.status == hug.HTTP_400, 'wrong response code'
        assert response.data == {'errors': {'num': "'-1' must be greater than -1"}}, 'response should contain an error'

    def test_main__float__invalid():
        """Test that only integers are accepted."""
        response = hug.test.get(api, '/specialmath/3.14')
        assert response.status == hug.HTTP_400, 'wrong response code'
        assert response.data == {'errors': {'num': "Invalid whole number provided"}}, 'response should contain an error'

    def test_main__letter__invalid():
        """Test that only integers are accepted."""
        response = hug.test.get(api, '/specialmath/g')
        assert response.status == hug.HTTP_400, 'wrong response code'
        assert response.data == {'errors': {'num': "Invalid whole number provided"}}, 'response should contain an error'

    def test_main__missing_n__not_found():
        """Test that an incomplete route returns a 404 Not Found."""
        response = hug.test.get(api, '/specialmath')
        assert response.status == hug.HTTP_404, 'wrong response code'

    def test_main__small_n__success():
        """Test a simple success case."""
        response = hug.test.get(api, '/specialmath/7')
        assert response.status == hug.HTTP_200, 'wrong response code'
        assert response.data == 79, 'incorrect result'

    def test_main__large_n__success():
        """Test that a sufficiently large number doesn't hang."""
        response = hug.test.get(api, '/specialmath/90')
        assert response.status == hug.HTTP_200, 'wrong response code'
        assert response.data == 19740274219868223074, 'incorrect result'


def main():
    for func in getmembers(Test, isfunction):
        try:
            func[1]()
            print(f'{func[0]} passed')
        except Exception as e:
            print(f'{func[0]} failed: {e}')


if __name__ == '__main__':
    main()