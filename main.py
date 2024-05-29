import pandas as pd
import plotly.express as px
from fbprophet import Prophet


def readFileAndFilter(path):
    df = pd.read_csv(path)

    df = df.rename(columns={'MONATSZAHL': 'Category', 'AUSPRAEGUNG': 'Accident-type',
                            'JAHR': 'Year', 'MONAT': 'Month', 'WERT': 'Value'})

    df['MonthPart'] = df['Month'].apply(lambda x: None if x == 'Summe' else x[-2:])

    df = df[df['MonthPart'].notna()]

    df = df[df['Year'] < 2021]

    return df


def plotHistoricalGraph(df):
    grouped_data = df.groupby(['Category', 'Year']).sum()['Value'].unstack().reset_index()
    print(grouped_data)

    melted_data = pd.melt(grouped_data, id_vars=['Category'], var_name='Year', value_name='Value')

    print(melted_data)

    # Plotting
    fig = px.line(melted_data, x='Year', y='Value', color='Category',
                  title='Yearly Trends in Munich Traffic Accidents by Category (2000-2020)',
                  labels={'Value': 'Number of Accidents', 'Year': 'Year'},
                  markers=True,  # Adding markers to each data point for better visibility
                  hover_data={'Value': ':,.0f'})

    fig.update_layout(
        barmode='group',
        xaxis_title='Year',
        yaxis_title='Number of Accidents',
        legend_title='Category',
        hovermode='x unified',
        template='plotly_white'
    )

    fig.show()

