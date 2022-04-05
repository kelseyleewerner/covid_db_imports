import csv

ginis = []
id_counter = 1
skip_keys = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code']
countries = ['Chile', 'Iceland', 'Nigeria', 'China', 'United States', 'Australia', 'Botswana', 'Korea, Rep.', 'Uruguay', 'Russian Federation', 'Yemen, Rep.', 'Rwanda', 'Brazil', 'India', 'Croatia', 'Italy', 'Ecuador', 'Saudi Arabia', 'Germany', 'Egypt, Arab Rep.', 'Iraq', 'Hungary', 'France', 'Kenya', 'Austria']

with open('../raw_data_sets/gini-index-by-country.csv', 'r') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        raw_item = dict(row)

        if raw_item['Country Name'] in countries:
            for key in raw_item:
                if key in skip_keys:
                    continue
                if raw_item[key] == '':
                    continue
                formatted_item = {
                    'id': id_counter,
                    'country_id': raw_item['Country Name'],
                    'year': key,
                    'gini_index': raw_item[key]
                }
                ginis.append(formatted_item)
                id_counter += 1


with open('../finalized_data/gini.csv', 'w', newline='') as file:
    fieldnames = ['id', 'country_id', 'year', 'gini_index']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for gini in ginis:
        writer.writerow(gini)

print('FINISHED')

