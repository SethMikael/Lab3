import price_info


def test_cost_of_fruit():
    cost = price_info.cost_of_fruits('apple', 5)
    cost_apple = 5 * 1.20
    assert (cost == cost_apple)


def test_total_cost_shopping():
    total_cost = price_info.total_cost_shopping()
    assert (total_cost == 46.75)