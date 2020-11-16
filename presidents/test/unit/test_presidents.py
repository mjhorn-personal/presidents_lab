import pytest
from presidents_lab.presidents.presidents import search_presidents
import re

def get_president_list():
    president_file = open('unit.presidents.txt', 'r')
    lines = president_file.readlines()
    presidents_list = []
    for line in lines:
        presidents_list.append(line.strip())
    return presidents_list

@pytest.mark.parametrize("president", get_president_list())
def test_search_presidents(president):
    found = False
    test_presidents = search_presidents()

    for test_president in test_presidents:
        match = re.search(president, test_president)
        if match:
            found = True
    assert found is True