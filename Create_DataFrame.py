import pandas as pd

studying_and_age = [
    ['engineering', 20],
    ['math', 30],
    ['biology', 23]
]

def create_dataframe(studying_and_age):
    df = pd.DataFrame(studying_and_age, columns=['Studyng', 'Age'])
    print (df.to_string(index=False))
    return df

create_dataframe(studying_and_age)
