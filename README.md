# DPSChallenge
This repository contains code for analyzing and visualizing historical data on traffic accidents in Munich, Germany, as well as forecasting future accident trends. The project utilizes data from the "Monatszahlen Verkehrsunfälle" dataset, which provides monthly accident counts across different categories from 2000 to 2020.
**Data Visualisation**
The central component of this project is a line chart that illustrates the yearly trends in traffic accidents by category from 2000 to 2020. The chart, shown below, displays three different accident categories: "Alkoholunfälle" (alcohol-related accidents), "Fluchtunfälle" (hit-and-run accidents), and "Verkehrsunfälle" (overall traffic accidents).
![newplot (9)](https://github.com/preetammnaik/DPSChallenge/assets/102791651/e93a1c84-0009-4089-9720-c7c954050ef0)
![newplot (10)](https://github.com/preetammnaik/DPSChallenge/assets/102791651/386c45c6-8596-471d-bf9f-c569c051cecc)
![newplot (11)](https://github.com/preetammnaik/DPSChallenge/assets/102791651/a2bd61f9-4630-4da3-836b-63e85b040552)
![newplot (12)](https://github.com/preetammnaik/DPSChallenge/assets/102791651/e9e456c5-e886-47bb-9841-52586ea5dd1a)


The chart clearly shows the fluctuations in accident counts over the years, with overall traffic accidents (green line) being the most numerous, followed by hit-and-run incidents (red line), and alcohol-related accidents (blue line) being the least frequent.

**Forecasting Model**
In addition to visualizing historical data, this project also includes a machine learning model capable of forecasting future accident trends. Specifically, the model focuses on predicting the number of "Alkoholunfälle" (alcohol-related accidents) of type "insgesamt" (total) for a given year and month.
The model is deployed as a web service, exposing an endpoint that accepts a POST request with a JSON payload containing the desired year and month. The service then returns a JSON response with the predicted accident count for the specified time period.
Deployment and Usage

The forecasting model has been deployed to a cloud service, and the source code is available on GitHub. To use the model, send a POST request to the deployed endpoint with a JSON payload in the following format:

{
  "year": 2021,
  "month": 1
}

The service will respond with a JSON object containing the predicted accident count:

{
  "prediction": 42
}

Please refer to the repository's documentation for more details on deployment, usage, and implementation specifics.
