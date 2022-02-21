CREATE SCHEMA grad_project AUTHORIZATION fall2021db96;


CREATE TABLE govt_systems
(id int,
type text,
description text,
PRIMARY KEY (id));

\COPY govt_systems FROM govt_systems.csv WITH CSV HEADER


CREATE TABLE vax_manufacturers
(id int,
vax text,
PRIMARY KEY (id));

\COPY vax_manufacturers FROM vax_manufacturers.csv WITH CSV HEADER


CREATE TYPE geo_region AS ENUM ('Europe & Central Asia', 'Middle East & North Africa', 'South Asia', 'Latin America & Caribbean', 'Sub-Saharan Africa', 'East Asia & Pacific', 'North America');
CREATE TYPE income_levels AS ENUM ('high income', 'low income', 'upper middle income', 'lower middle income', 'not classified');

CREATE TABLE countries
(id int,
name text,
region geo_region,
govt_system int,
population int,
birth_rate float,
life_expectancy float,
income_level income_levels,
gdp_per_cap float,
PRIMARY KEY (id),
FOREIGN KEY(govt_system) REFERENCES govt_systems(id),
constraint pop_above_zero check(population >= 0),
constraint birth_above_zero check(birth_rate >= 0.0),
constraint life_above_zero check(life_expectancy >= 0.0),
constraint gdp_above_zero check(gdp_per_cap >= 0.0));

\COPY countries FROM countries.csv WITH CSV HEADER


CREATE TABLE gini
(id int,
country_id int,
year int,
gini_index float,
PRIMARY KEY (id),
FOREIGN KEY(country_id) REFERENCES countries(id),
constraint gini_above_zero check(gini_index >= 0.0),
constraint gini_below_hundred check(gini_index <= 100.0),
constraint year_above_1900 check(year >= 1900));

\COPY gini FROM gini.csv WITH CSV HEADER


CREATE TABLE govt_trust
(id int,
country_id int,
year int,
trust float,
PRIMARY KEY (id),
FOREIGN KEY(country_id) REFERENCES countries(id),
constraint year_above_1900 check(year >= 1900),
constraint trust_above_zero check(trust >= 0.0),
constraint trust_below_hundred check(trust <= 100.0));

\COPY govt_trust FROM govt_trust.csv WITH CSV HEADER


CREATE TABLE med_trust
(id int,
country_id int,
year int,
trust float,
PRIMARY KEY (id),
FOREIGN KEY(country_id) REFERENCES countries(id),
constraint year_above_1900 check(year >= 1900),
constraint trust_above_zero check(trust >= 0.0),
constraint trust_below_hundred check(trust <= 100.0));

\COPY med_trust FROM med_trust.csv WITH CSV HEADER


CREATE TABLE covid
(id int,
country_id int,
confirmed_cases int,
deaths int,
recovered int,
deaths_per_hundred float,
recovered_per_hundred float,
doses_per_hundred float,
total_doses text,
fully_vaxed float,
PRIMARY KEY (id),
FOREIGN KEY(country_id) REFERENCES countries(id),
constraint cases_above_zero check(confirmed_cases >= 0),
constraint deaths_above_zero check(deaths >= 0),
constraint recovered_above_zero check(recovered >= 0),
constraint dph_above_zero check(deaths_per_hundred >= 0.0),
constraint dph_below_hundred check(deaths_per_hundred <= 100.0),
constraint rph_above_zero check(recovered_per_hundred >= 0.0),
constraint rph_below_hundred check(recovered_per_hundred <= 100.0),
constraint doses_above_zero check(doses_per_hundred >= 0.0),
constraint vax_above_zero check(fully_vaxed >= 0.0),
constraint vax_below_hundred check(fully_vaxed <= 100.0));

\COPY covid FROM covid.csv WITH CSV HEADER


CREATE TABLE vax_rel
(country_id int,
vax_id int,
PRIMARY KEY (country_id, vax_id),
FOREIGN KEY(country_id) REFERENCES countries(id),
FOREIGN KEY(vax_id) REFERENCES vax_manufacturers(id));

\COPY vax_rel FROM vax_rel.csv WITH CSV HEADER
