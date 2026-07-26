import pytest
from src.RectangleOOP import Rectangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
        (3, 5, 15),
        (3.5, 5.5, 19.25)
    ],
    ids=["integer", "float"]
)

def test_rectangle_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area ==area

@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        (0, 5),
        (-1, 5.5)
    ],
    ids=["zero value", "negative value"]
)

def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


# @pytest.mark.skip(condition=)
# def test_rectangle_float():
#     r = Rectangle(3.5, 5.5)
#     assert r.get_area == 19.25
#
