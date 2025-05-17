from src import data_processing
from src import visualize

df = data_processing.get_dataframe()
metrics_df = data_processing.get_summary_dataframe()
# Use this to get a graph as jpg image
img_result = visualize.plot_hourly_prices(df)

# Use this to get csv file of hourly prices
csv_result = visualize.csv_hourly_prices(df)

# Use this to get additional metrics CSV file
csv_metrics = visualize.csv_metrics(metrics_df)
