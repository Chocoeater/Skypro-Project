import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_ex(state_ex):
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) == state_ex


def test_filter_by_state_other(state_other):
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED',
                             'date': '2018-10-14T08:21:33.419441'}], 'CANCELED') == state_other


@pytest.mark.parametrize('value, expected', [
    (
            [{}], []
    ),
    (
            [{'id': 939719570, 'date': '2018-06-30T02:08:58.425572'}], []
    )
])
def test_filter_by_state(value, expected):
    assert filter_by_state(value) == expected


def test_sort_by_date_decreasing(decreasing):
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) == decreasing


def test_sort_by_date_increasing(increasing):
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                        decreasing=False) == increasing


def test_sort_by_date_same(same):
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 615064591, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}]) == same


def test_sort_by_date_type():
    with pytest.raises(TypeError, match='Дата должна быть строкой'):
        sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': 20190703}])
