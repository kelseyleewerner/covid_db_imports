import csv

measurements = []
id_counter = 1
countries1 = ['Chile', 'Iceland', 'Nigeria', 'China', 'US', 'Australia', 'Botswana', 'South Korea', 'Uruguay', 'Russia', 'Yemen', 'Rwanda', 'Brazil', 'India', 'Croatia', 'Italy', 'Ecuador', 'Saudi Arabia', 'Germany', 'Egypt', 'Iraq', 'Hungary', 'France', 'Kenya', 'Austria']
# NOTE: US IS WEIRD IN THIS SET

with open('../raw_data_sets/country-wise-covid-latest.csv', 'r') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        raw_item = dict(row)

        if raw_item['Country/Region'] in countries1:
            if raw_item['Country/Region'] == 'US':
                raw_item['Country/Region'] = 'United States'
            elif raw_item['Country/Region'] == 'China':
                raw_item['Country/Region'] = 'Mainland China'

            formatted_item = {
                'id': id_counter,
                'country_id': raw_item['Country/Region'],
                'confirmed_cases': raw_item['Confirmed'],
                'deaths': raw_item['Deaths'],
                'recovered': raw_item['Recovered'],
                'deaths_per_hundred': raw_item['Deaths / 100 Cases'],
                'recovered_per_hundred': raw_item['Recovered / 100 Cases']
            }
            measurements.append(formatted_item)
            id_counter += 1


final_list = []
countries2 = ['Chile', 'Iceland', 'Nigeria', 'Mainland China', 'United States', 'Australia', 'Botswana', 'South Korea', 'Uruguay', 'Russia', 'Yemen', 'Rwanda', 'Brazil', 'India', 'Croatia', 'Italy', 'Ecuador', 'Saudi Arabia', 'Germany', 'Egypt', 'Iraq', 'Hungary', 'France', 'Kenya', 'Austria']
# NOTE: CHINA IS WEIRD IN THIS SET

with open('../raw_data_sets/worldwide-vaccine-data.csv', 'r') as file:
    csv_file = csv.DictReader(file)

    for row in csv_file:
        raw_item = dict(row)

        if raw_item['Country'] in countries2:
            found_item = list(filter(lambda measurement: measurement['country_id'] == raw_item['Country'], measurements))[0]

            found_item['doses_per_hundred'] = raw_item['Doses administered per 100 people']
            found_item['total_doses'] = raw_item['Total doses administered']
            found_item['fully_vaxed'] = raw_item["% of population fully vaccinated"]

            final_list.append(found_item)


with open('../finalized_data/covid.csv', 'w', newline='') as file:
    fieldnames = ['id', 'country_id', 'confirmed_cases', 'deaths', 'recovered', 'deaths_per_hundred', 'recovered_per_hundred', 'doses_per_hundred', 'total_doses', 'fully_vaxed']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for item in final_list:
        writer.writerow(item)

print('FINISHED')