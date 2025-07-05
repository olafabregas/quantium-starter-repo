import csv
import glob

# Path to your data folder
data_files = glob.glob('data/*.csv')

output_rows = []
for file in data_files:
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['product'] == 'Pink Morsel':
                sales = float(row['quantity']) * float(row['price'])
                output_rows.append({
                    'sales': sales,
                    'date': row['date'],
                    'region': row['region']
                })

# Write to formatted_sales_data.csv
with open('formatted_sales_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['sales', 'date', 'region']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in output_rows:
        writer.writerow(row)
