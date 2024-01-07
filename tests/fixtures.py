import pytest
import pandas as pd
import os


@pytest.fixture(scope="package")
def participants():
    return pd.read_pickle("/home/gongcastro/Documents/bvqpy/tests/fixtures/participants.pkl")
