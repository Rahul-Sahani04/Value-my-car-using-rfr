# Car Price Prediction Web Application

This repository hosts a web application for predicting car prices using Flask and machine learning. Users can input various features of a car, such as make, model, year, mileage, and engine type, and the application will provide an estimated price.

## Installation

To set up the necessary dependencies for this project, execute the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Running the Application

Follow these steps to run the application:

1. Clone the repository to your local machine.
2. Open a terminal window and navigate to the project directory.
3. Start the app by running the following command:

```bash
python app.py
```

or

```bash
gunicorn --bind 127.0.0.1:5000 app:app
```

The application will be accessible at `http://localhost:5000`.

## Code Structure

The project's code is organized into several files:

* `app.py`: This file contains the primary Flask app code, defining routes and handling user requests.
* `model.py`: This file includes the code for the machine learning model responsible for predicting car prices.
* `requirements.txt`: Lists the Python dependencies required for the project.

## Deployment Guide for Render

For detailed instructions on deploying this application on Render, please refer to the [deployment guide](https://scribehow.com/shared/Create_a_Web_Service_for_Value-My-Car_Using_RFR__Lfx3qicHT7-m4MwtK5qsoQ).