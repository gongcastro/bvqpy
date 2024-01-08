import pandas as pd
import numpy as np
from bvqpy import connect
from gspread.client import Client


def participants() -> pd.core.frame.DataFrame:
    """
    Retrieve and update local and/or remote data from formr

    This function generates a data frame with the information of all participants
    that have participated or are candidates to participate in any of the
    versions of BVQ.

    Parameters
    ----------
    con: Connection to formr and Google Spreadsheets, as returned by `bvqpy.connect`

    Returns
    -------
    DataFrame: A data frame with all participants that have participated or are candidates to participate in any of the versions of BVQ Each row corresponds to a questionnaire response and each column represents a variable.

    See also
    --------
    connect: Connect to formr and Google Spreadsheets
    """

    ss = "164DMKLRO0Xju0gdfkCS3evAq9ihTgEgFiuJopmqt7mo"

    con = connect()
    df = con.open_by_key(ss).sheet1.get_all_records()
    df = pd.DataFrame(df)
    df = df.replace(r"^\s*$", np.nan, regex=True)

    # transform types
    df.astype({"include": bool,
               "time": int})
    df.include = df.include == "TRUE"
    date_cols = ["date_birth", "date_sent"]
    df[date_cols] = df[date_cols].apply(
        lambda x: pd.to_datetime(x, dayfirst=True))

    # filter rows
    df = df.dropna(subset=["code"])
    df = df[df["include"]]

    # select and rename columns
    df = df[["id", "code", "time", "date_birth", "date_sent",
             "version", "randomisation", "call"]]
    df = df.rename(columns={"id": "child_id",
                            "code": "response_id",
                            "randomisation": "version_list"})

    # fix values
    df = df.replace("bl-|BL-|bl|BL", "", regex=True)
    df.response_id = df.response_id.astype("O")
    df.response_id = df.child_id.astype("O")

    # reorder table
    df.sort_values(["response_id"],
                   key=lambda col: pd.to_numeric(col), ascending=False)

    return df
