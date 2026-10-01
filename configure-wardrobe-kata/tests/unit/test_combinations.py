from configure_wardrobe_kata.domain.combinations import combine

def test_single_combination_fills_a_50cm_wall_exactly(swedish_furniture_catalog):
    combinations = combine(catalog=swedish_furniture_catalog, wall_length=50)

    assert len(combinations) == 1

def test_returns_empty_list_when_no_combination_fills_the_wall_exactly(swedish_furniture_catalog):
    combinations = combine(catalog=swedish_furniture_catalog, wall_length=25)

    assert combinations == []

def test_returns_multiple_combinations_for_a_250cm_wall(swedish_furniture_catalog):
    combinations = combine(catalog=swedish_furniture_catalog, wall_length=250)

    # uv run pytest -s tests/unit/test_combinations.py
    print(combinations)

    assert len(combinations) > 1

def test_cheapest_combination_has_the_lowest_total_price():
    pass    

def test_cheapest_combination_among_ties_returns_one_valid_option():
    pass
