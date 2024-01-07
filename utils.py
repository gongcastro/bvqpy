import pandas as pd
import os


def make_fixture(obj, file: str) -> None:
    path = "/home/gongcastro/Documents/bvqpy/tests/fixtures/" + file + ".pkl"

    if isinstance(obj, pd.DataFrame):
        obj = obj.head()
        obj.to_pickle(path)
    else:
        pickle.dump(object, path)
