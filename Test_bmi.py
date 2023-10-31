import Lab3_submodule.Lab2.bmi as bmi

def test_bmi_normal_weight():
    weight = 57
    height = 1.68
    result = bmi.calculate_bmi(weight, height)
    assert (result == 0)


def test_bmi_overweight():
    weight = 80
    height = 1.68
    result = bmi.calculate_bmi(weight, height)
    assert (result == 1)


def test_bmi_underweight():
    weight = 40
    height = 1.68
    result = bmi.calculate_bmi(weight, height)
    assert (result == -1)