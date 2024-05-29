import pandas as pd


def readFileAndFilter(path):
    df = pd.read_csv(path)

    df = df.rename(columns={'MONATSZAHL': 'Category', 'AUSPRAEGUNG': 'Accident-type',
                            'JAHR': 'Year', 'MONAT': 'Month', 'WERT': 'Value'})

    df['MonthPart'] = df['Month'].apply(lambda x: None if x == 'Summe' else x[-2:])

    df = df[df['Year'] < 2021]

    return df


data = readFileAndFilter('AccidentData.csv')

print(data)
