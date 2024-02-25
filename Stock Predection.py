import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from datetime import datetime, timedelta
import requests
import json

# Function to get historical stock data
def get_stock_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

# Function to preprocess data for prediction
def preprocess_data(data):
    data['Date'] = data.index
    data['Date'] = data['Date'].astype(int) / 10**9  # Convert date to Unix timestamp
    return data

# Function to build and train the prediction model
def build_model(X_train, y_train):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

# Function to make predictions
def make_predictions(model, X_test):
    predictions = model.predict(X_test)
    return predictions

# Function to fetch live stock data using an API
def get_live_stock_data(api_url, symbol):
    response = requests.get(api_url.format(symbol))
    data = json.loads(response.text)
    return data['latestPrice']

# Main function
def main():
    # Define the stock symbol and time period for historical data
    stock_symbol = 'AAPL'
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    # Get historical stock data
    historical_data = get_stock_data(stock_symbol, start_date, end_date)
    processed_data = preprocess_data(historical_data)

    # Define features and target variable
    X = processed_data[['Date']]
    y = processed_data['Close']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Build and train the model
    model = build_model(X_train, y_train)

    # Make predictions
    predictions = make_predictions(model, X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

    # Get live stock data for prediction
    api_url = 'https://financialmodelingprep.com/api/v3/quote/{0}'
    live_stock_price = get_live_stock_data(api_url, stock_symbol)

    # Prepare live data for prediction
    live_data = preprocess_data(pd.DataFrame({'Date': [datetime.now()]}))
    live_prediction = make_predictions(model, live_data[['Date']])

    print(f'Predicted Close Price for {stock_symbol}: ${live_prediction[0]:.2f}')
    print(f'Live Stock Price: ${live_stock_price:.2f}')

if __name__ == "__main__":
    main()
