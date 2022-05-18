import os
import unittest

import pytest

import starwars


@pytest.fixture()
def api_fixture():
    with open("some_file.txt", "w") as fout:
        fout.write("hello")
    yield "some_file.txt"
    os.remove("some_file.txt")


class StarWarsTest(unittest.TestCase):
    def setUp(self):
        self.api_key = "..."

    def test_list_people_when_api_is_working_returns_star_wars_characters(self):
        # Arrange

        # Act
        actual = starwars.list_people()

        # Assert
        self.assertTrue(len(actual) > 1000)
        # self.assertGreater(len(actual), 1000)


def test_list_people_when_api_is_working_returns_star_wars_characters(api_fixture):
    api_token = api_fixture

    # Arrange

    # Act
    actual = starwars.list_people()

    # Assert
    assert len(actual) > 0


@pytest.mark.integration
def test_list_people_when_api_is_working_returns_star_wars_characters_has_this_word():
    # Arrange

    # Act
    actual = starwars.list_people()

    # Assert
    for item in actual["results"]:
        print(item['name'])
    assert len(actual) > 1000
