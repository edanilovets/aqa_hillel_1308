import pytest

class TestUserData:

    user_id = 10        # default
    related_users = []  # list of ids

    @pytest.fixture(autouse=True)
    def prepare_data(self):
        # get related users from API
        # heavy method: DB, API, etc
        TestUserData.related_users.append(22)
        TestUserData.user_id = 11

    def test_base_user(self):
        assert TestUserData.user_id == 12

    def test_related_user(self):
        assert len(TestUserData.related_users) > 0