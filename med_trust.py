import csv

measurements = []
id_counter = 1
countries = ['Chile', 'Iceland', 'Nigeria', 'China', 'United States', 'Australia', 'Botswana', 'South Korea', 'Uruguay', 'Russia', 'Yemen', 'Rwanda', 'Brazil', 'India', 'Croatia', 'Italy', 'Ecuador', 'Saudi Arabia', 'Germany', 'Egypt', 'Iraq', 'Hungary', 'France', 'Kenya', 'Austria']

with open('../raw_data_sets/share-who-trust-doctors-and-nurses.csv', 'r') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        raw_item = dict(row)

        if raw_item['Entity'] in countries:
            formatted_item = {
                'id': id_counter,
                'country_id': raw_item['Entity'],
                'year': raw_item['Year'],
                'trust': raw_item['Share of people who trust doctors and nurses in their country']
            }
            measurements.append(formatted_item)
            id_counter += 1


with open('../finalized_data/med_trust.csv', 'w', newline='') as file:
    fieldnames = ['id', 'country_id', 'year', 'trust']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for measurement in measurements:
        writer.writerow(measurement)

print('FINISHED')