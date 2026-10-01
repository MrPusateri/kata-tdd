from typing import Set, List

from configure_wardrobe_kata.domain.wardrobe_element import WardrobeElement


def combine(catalog: Set[WardrobeElement], wall_length: int) -> List | List[List[WardrobeElement]]:
    base_solution = [[]]
    fail_solution = []

    if wall_length==0:
        return base_solution
    if wall_length<0:
        return fail_solution
    
    combinations = list()

    for i, we in enumerate(sorted(list(catalog))):
        for rest in combine(sorted(list(catalog))[i:], wall_length - we.length):
            combinations.append(rest + [we])

    return combinations


def cheap_combinations(catalog: Set[WardrobeElement], wall_length: int) -> List | List[List[WardrobeElement]]:
    combinations = combine(catalog, wall_length)
    return sorted(combinations, key= lambda combination: sum([we.price for we in combination]))