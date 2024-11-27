import pandas as pd

df = pd.DataFrame(
    data={
        "col1":[1, 2, 3],
        "col2":['a', 'b', 'c'],
        "col3":[True, True, False]
    }
)

print(df.head())