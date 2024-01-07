import pandas as pd
import pytest
import numpy as np


@pytest.fixture(scope="package")
def participants() -> pd.DataFrame:
    """Retrieve participants object as fixture"""
    return pd.read_pickle("tests/fixtures/participants.pkl")


def test_class(participants: pd.DataFrame) -> NoReturn:
    """Check that participants is a Pandas DataFrame"""
    assert isinstance(participants, pd.DataFrame)


def test_colnames(participants: pd.DataFrame) -> NoReturn:
    """Check column names"""
    req = ["child_id", "response_id", "time", "date_birth",
           "date_sent", "version", "version_list", "call"]
    cols = participants.columns
    for col in req:
        assert col in req


def test_classes(participants: pd.DataFrame) -> NoReturn:
    """Check column classes"""
    schema = {"child_id": np.dtype("O"),
              "response_id": np.dtype("O"),
              "date_birth": np.dtype("<M8[ns]"),
              "date_sent": np.dtype("<M8[ns]"),
              "time": np.dtype("int64"),
              "version": np.dtype("O"),
              "version_list": np.dtype("O"),
              "call": np.dtype("O")}
    assert participants.dtypes.to_dict() == schema
