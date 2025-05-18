import matplotlib.pyplot as plt


def plot_hourly_prices(df):

    """Get JPG format image of a graph that displays electricity prices by hour."""

    plt.figure(figsize=(18, 6))
    plt.plot(df['Hour'], df['Price'], marker='o', linestyle='-')
    plt.title('Hourly Electricity Prices')
    plt.xlabel('Hour')
    plt.ylabel('Price (€ / MWh)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("hourly_prices.png")


def csv_metrics(df):

    """Get CSV file of variety of different metrics based on prices on that day."""

    df.to_csv("metrics.csv", index=False)


def csv_hourly_prices(df):

    """Get CSV file of prices each hour."""

    df.to_csv("hourly_prices.csv", index=False)

