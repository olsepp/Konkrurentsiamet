from get_data import get_right_order as data
import pandas as pd


def get_dataframe():

    """Return dataframe with hours, prices and other metrics made by using pandas library."""

    # Make dataframe from data dictionary
    df = pd.DataFrame(list(data().items()), columns=["Hour", "Price"])

    return df


def get_summary_dataframe():

    """Return a separate dataframe with additional metrics only."""

    # Get dataframe with only hours and prices to calculate additional metrics
    df = get_dataframe()

    # Calculate additional metrics
    average = round(df["Price"].mean(), 2)

    minimum = df["Price"].min()

    maximum = df["Price"].max()

    price_range = round(maximum - minimum, 2)

    cheapest_hour = df[df["Price"] == minimum]["Hour"].values[0]

    expensive_hour = df[df["Price"] == maximum]["Hour"].values[0]

    # Make a new DataFrame only for metrics
    summary_df = pd.DataFrame([
        {"Metric": "Average", "Value": average},
        {"Metric": "Minimum Price", "Value": minimum},
        {"Metric": "Maximum Price", "Value": maximum},
        {"Metric": "Price Range", "Value": price_range},
        {"Metric": "Cheapest Hour", "Value": cheapest_hour},
        {"Metric": "Most Expensive Hour", "Value": expensive_hour}
    ])

    return summary_df
