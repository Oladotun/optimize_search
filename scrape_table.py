import requests
from bs4 import BeautifulSoup
import csv

def scrape_and_save_to_csv(url, csv_filename):
    # Send an HTTP request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the HTML table in the parsed HTML
        table = soup.find('table')

        # Extract table headers
        headers = [header.text.strip().lower().replace(" ", "_") for header in table.find_all('th', {'scope': 'col'})]
        # Extract table rows
        rows = []
        for row in table.find_all('tr'):
            zip_code = [data.text.strip() for data in row.find_all('th', {'scope': 'row'} )]
            row_data = [data.text.strip() for data in row.find_all('td')]
            if row_data:
                if zip_code:
                    row_data.insert(0,zip_code[0])
                rows.append(row_data)
        # print(rows)
        # # Write data to CSV file
        with open(csv_filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)
            writer.writerows(rows)

        print(f"Data scraped successfully and saved to {csv_filename}")
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Example usage:
url_to_scrape = 'https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2023_code/2023summary.odn?&year=2023&fmrtype=Final&selection_type=county&fips=2403399999'
csv_filename = 'output_data.csv'
scrape_and_save_to_csv(url_to_scrape, csv_filename)
