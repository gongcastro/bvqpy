import pandas as pd
import 
def participants():
    bvq.connect()
    docid = "164DMKLRO0Xju0gdfkCS3evAq9ihTgEgFiuJopmqt7mo"
    raw = gc.open_by_key(docid)
    participants = pd.DataFrame(raw.get_all_records())