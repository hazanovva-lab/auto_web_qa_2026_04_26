from src.Rectangle import Square
import pytest


def test_rectangle_area_positive(api_server):
    side_a, _, _ = api_server(type_of_number="integer")
    r = Square(side_a)
    assert r.get_area == 9
