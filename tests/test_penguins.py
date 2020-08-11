from palmerpenguins.penguins import load_penguins
import pytest


def test_shape_load_penguins():
    assert load_penguins().shape == (344, 8)


def test_shape_load_penguins_X_y():
    assert load_penguins(return_X_y=True)[0].shape == (344, 4)
