import pandas as pd
import os
from dotenv import dotenv_values


def get_secrets(secret: str) -> str:
    return dotenv_values(".env")[secret]


def make_fixture(obj, file: str) -> None:
    path = "/home/gongcastro/Documents/bvqpy/tests/fixtures/" + file + ".pkl"

    if isinstance(obj, pd.DataFrame):
        obj = obj.head()
        obj.to_pickle(path)
    else:
        pickle.dump(object, path)
