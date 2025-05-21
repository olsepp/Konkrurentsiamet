from src import data_processing
from src import visualize

df = data_processing.get_dataframe()
metrics_df = data_processing.get_summary_dataframe()
# Use this to get a graph of hourly prices as jpg image
visualize.plot_hourly_prices(df)

# Use this to get csv file of hourly prices
visualize.csv_hourly_prices(df)

# Use this to get additional metrics CSV file
visualize.csv_metrics(metrics_df)
