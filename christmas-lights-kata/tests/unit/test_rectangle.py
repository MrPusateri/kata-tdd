from christmas_lights_kata.domain.rectangle import Rectangle


def test_corners_can_be_given_in_any_order():
    expected = Rectangle((1, 1), (2, 2))

    assert Rectangle((2, 2), (1, 1)) == expected
    assert Rectangle((1, 2), (2, 1)) == expected
    assert Rectangle((2, 1), (1, 2)) == expected


def test_rectangle_includes_both_corners():
    rectangle = Rectangle((0, 0), (1, 1))

    assert set(rectangle.coordinates()) == {(0, 0), (0, 1), (1, 0), (1, 1)}


def test_rectangle_with_the_same_corner_is_a_single_light():
    rectangle = Rectangle((0, 1), (0, 1))

    assert list(rectangle.coordinates()) == [(0, 1)]
