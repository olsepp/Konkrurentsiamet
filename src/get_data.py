from bs4 import BeautifulSoup


def get_raw_data():

    """Get raw electricity price data by hour."""

    # Open locally downloaded html file and read it
    with open("../nordpool_full.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Define results dictionary
    results = {}

    # Find all tables
    table = soup.find_all("table")

    if len(table) < 2:
        raise ValueError("Expected at least 2 tables")

    # Get rows of second table since this is the table that has the needed data
    rows = table[1].find_all("tr")

    # Go through all rows to get data from cells
    for row in rows:
        cells = row.find_all("td")
        if len(cells) >= 2:
            hour = cells[0].get_text(strip=True)
            price = cells[1].get_text(strip=True)

            # Replace all commas with periods to be able to convert prices to float
            if price:
                try:
                    results[hour] = float(price.replace(",", "."))
                except ValueError:
                    print(f"Skipping invalid price: {price} at hour {hour}")

    # Return final dictionary, hours as keys and prices as values
    return results


def get_right_order():

    """Since the first value we need is the last element in raw data dictionary, bring it to the front."""

    raw_data = get_raw_data()

    # Check if getting data was successful
    if not raw_data:
        return {}

    # Define dictionary for final result
    structured_data = {}

    # Move last element from rax data to start
    last_key = list(raw_data.keys())[-1]
    structured_data[last_key] = raw_data[last_key]

    # Add the remaining items
    for hour, price in raw_data.items():
        if hour != last_key:
            structured_data[hour] = price

    return structured_data


print(get_right_order())
