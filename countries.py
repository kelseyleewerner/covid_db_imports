import csv

raw_countries = []
id_counter = 1

with open('../raw_data_sets/country-data.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        raw_item = dict(row)

        if raw_item['income'] == 'High income: OECD':
            raw_item['income'] = 'high income'
        else:
            raw_item['income'] = raw_item['income'].lower()

        if raw_item['country'] == 'Chile' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 1, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Iceland' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 3, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Nigeria' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 1, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'China' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 6, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'United States' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 1, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Australia' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 4, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Korea, Rep.' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': 'South Korea', 'region': raw_item['region'], 'govt_system': 1, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Uruguay' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 1, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Russian Federation' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': 'Russia', 'region': raw_item['region'], 'govt_system': 2, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Yemen, Rep.' and raw_item['year'] == '2013':
            raw_countries.append({'id': id_counter, 'name': 'Yemen', 'region': raw_item['region'], 'govt_system': 8, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Rwanda' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 1, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Brazil' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 1, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'India' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 3, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Croatia' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 3, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Italy' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 3, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Ecuador' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 1, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Saudi Arabia' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 5, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Germany' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 3, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Egypt, Arab Rep.' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': 'Egypt', 'region': raw_item['region'], 'govt_system': 2, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Iraq' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 3, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Hungary' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 3, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'France' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 2, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Kenya' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 1, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Austria' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 3, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1
        elif raw_item['country'] == 'Botswana' and raw_item['year'] == '2014':
            raw_countries.append({'id': id_counter, 'name': raw_item['country'], 'region': raw_item['region'], 'govt_system': 3, 'population': raw_item['population'], 'birth_rate': raw_item['birth_rate'], 'life_expectancy': raw_item['life_expect'], 'income_level': raw_item['income'], 'gdp_per_cap': raw_item['gdp_percap']})
            id_counter += 1

with open('../finalized_data/countries.csv', 'w', newline='') as file:
    # fieldnames = ['iso2c','iso3c','country','year','gdp_percap','life_expect','population','birth_rate','neonat_mortal_rate','region','income']
    fieldnames = ['id', 'name', 'region', 'govt_system', 'population', 'birth_rate', 'life_expectancy', 'income_level', 'gdp_per_cap']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for country in raw_countries:
        writer.writerow(country)

print('FINISHED')