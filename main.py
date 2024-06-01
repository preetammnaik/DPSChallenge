import pandas as pd
import plotly.express as px
from prophet import Prophet
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)


def readFileAndFilter(path):
    df = pd.read_csv(path)
    df = df.rename(columns={'MONATSZAHL': 'Category', 'AUSPRAEGUNG': 'Accident-type',
                            'JAHR': 'Year', 'MONAT': 'Month', 'WERT': 'Value'})
    df = df[df["Month"] != "Summe"]
    df = df[df['Year'] < 2021]
    df = df[(df['Category'] == 'Alkoholunfälle') & (df['Accident-type'] == 'insgesamt')]

    df['Month'] = df['Month'].astype(int) % 100
    df['Date'] = pd.to_datetime(df['Year'].astype(str) + '-' + df['Month'].astype(str) + '-01')
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


def prepare_data_for_prophet(df):
    df_prophet = df.groupby('Date').sum()['Value'].reset_index()
    print(df_prophet['Date'])
    df_prophet.columns = ['ds', 'y']
    return df_prophet


def trainProphetModel(data):
    df_prophet = prepare_data_for_prophet(data)
    model = Prophet()
    model.fit(df_prophet)
    # Print statement for debugging
    print("Saving model to prophet_model.pkl")
    joblib.dump(model, 'prophet_model.pkl')
    return model


def predict_accidents_prophet(year, month):
    # Load the model
    print("Loading model from prophet_model.pkl")
    model = joblib.load('prophet_model.pkl')
    date = pd.to_datetime(f'{year}-{month:02d}-01')
    future = pd.DataFrame({'ds': [date]})
    forecast = model.predict(future)
    return int(forecast['yhat'].iloc[0])





@app.route('/predict', methods=['GET'])
def predict():
    year_param = request.args.get('year')
    month_param = request.args.get('month')
    print("Year parameter:", year_param)
    print("Month parameter:", month_param)

    year = int(year_param)
    month = int(month_param)
    print("Year:", year)
    print("Month:", month)

    model = joblib.load('prophet_model.pkl')

    predicted_value = predict_accidents_prophet(year, month)

    response = {
        'prediction': predicted_value
    }

    return jsonify(response), 200, {'Content-Type': 'application/json'}


if __name__ == "__main__":
    app.run(port=8080)
