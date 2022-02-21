-- 1. What percent of the population is vaccinated for the country(s) that had the lowest trust in government in 2018?

SELECT c.name, v.fully_vaxed
FROM govt_trust g JOIN countries c ON g.country_id = c.id JOIN covid v ON c.id = v.country_id
WHERE g.year = 2018
AND g.trust = (SELECT MIN(trust)
               FROM govt_trust
               WHERE year = 2018);


-- 2. What are the names of the countries and vaccination doses distributed for countries that have access to Sputnik V or CanSino vaccines?

(SELECT c.name, d.total_doses
FROM vax_manufacturers m, vax_rel v, countries c, covid d
WHERE m.id = v.vax_id
AND v.country_id = c.id
AND v.country_id = d.country_id
AND m.vax = 'Sputnik V')
UNION
(SELECT c.name, d.total_doses
FROM vax_manufacturers m, vax_rel v, countries c, covid d
WHERE m.id = v.vax_id
AND v.country_id = c.id
AND v.country_id = d.country_id
AND m.vax = 'CanSino');


-- 3. Which Asian countries don’t offer the Sinovac vaccine?

(SELECT c.name
FROM countries c JOIN vax_rel v ON c.id = v.country_id
WHERE region = 'East Asia & Pacific'
OR region = 'South Asia')
EXCEPT
(SELECT c.name
FROM countries c JOIN vax_rel v ON c.id = v.country_id JOIN vax_manufacturers m ON v.vax_id = m.id
WHERE m.vax = 'Sinovac');


-- 4. Which countries had the greatest inequality in 2014 for each government system?  Not including any countries that didn’t report Gini index data in that year.

SELECT c.name, s.type, g.gini_index
FROM countries c, govt_systems s, gini g, (SELECT s.type, MAX(g.gini_index) AS gini_index
                                           FROM countries c, govt_systems s, gini g
                                           WHERE c.govt_system = s.id
                                           AND c.id = g.country_id
                                           AND g.year = 2014
                                           GROUP BY s.type) AS max_inequality
WHERE c.govt_system = s.id
AND c.id = g.country_id
AND g.year = 2014
AND s.type = max_inequality.type
AND g.gini_index = max_inequality.gini_index;


-- 5. How many countries in the low income level category have access to the Johnson & Johnson vaccine?

SELECT DISTINCT COUNT(*)
FROM countries c JOIN vax_rel r ON c.id = r.country_id JOIN vax_manufacturers v ON r.vax_id = v.id
WHERE c.income_level = 'low income'
AND v.vax = 'Johnson&Johnson';


-- 6. Out of the countries with presidential systems, how many COVID-related deaths have there been in each country where more than 50% of the population trusts doctors and nurses in 2018?

SELECT c.name, v.deaths
FROM countries c JOIN govt_systems g ON c.govt_system = g.id JOIN med_trust m ON c.id = m.country_id JOIN covid v ON c.id = v.country_id
WHERE g.type = 'Presidential System'
AND m.year = 2018
AND m.trust > 50;


-- 7. Which geographic region(s) have at least one country that has received doses of the Pfizer/BioNTech vaccine brand?

SELECT c.region
FROM countries c, vax_rel r, vax_manufacturers v
WHERE c.id = r.country_id
AND r.vax_id = v.id
AND v.vax = 'Pfizer/BioNTech'
GROUP BY c.region;


-- 8. What are the names, government systems, and GDP per capita of countries where over 50% of the population trusts the government and over 50% of the population has been vaccinated?

SELECT country.name, g.type, country.gdp_per_cap
FROM govt_systems g JOIN (SELECT c.name, c.govt_system, c.gdp_per_cap
                          FROM countries c JOIN govt_trust g ON c.id = g.country_id JOIN med_trust m ON c.id = m.country_id
                          WHERE g.trust > 50
                          AND m.trust > 50) AS country
ON g.id = country.govt_system;


-- 9. How many of the countries that have not received any doses of the Moderna vaccine are high income or upper middle income?

SELECT COUNT(*)
FROM ((SELECT DISTINCT c.name
       FROM vax_manufacturers v, vax_rel r, (SELECT *
                                             FROM countries
                                             WHERE income_level = 'high income'
                                             OR income_level = 'upper middle income') AS c
       WHERE v.id = r.vax_id
       AND r.country_id = c.id
       AND v.vax != 'Moderna')
       EXCEPT
       (SELECT DISTINCT c.name
        FROM vax_manufacturers v, vax_rel r, (SELECT *
                                              FROM countries
                                              WHERE income_level = 'high income'
                                              OR income_level = 'upper middle income') AS c
        WHERE v.id = r.vax_id
        AND r.country_id = c.id
        AND v.vax = 'Moderna')) AS not_moderna_countries;


-- 10. What are the names, government systems, populations, and income levels of countries that have experienced more than 5 COVID deaths per 100 cases and had less than 50 doses per 100 people?

SELECT c.name, g.type, c.population, c.income_level
FROM countries c JOIN covid v ON c.id = v.country_id JOIN govt_systems g ON c.govt_system = g.id
WHERE v.deaths_per_hundred > 5
AND v.doses_per_hundred < 50;


-- 11. What is the Gini index for each recorded year for all high income countries, put in order from earliest record year to most recent recorded year?

SELECT c.name, g.year, g.gini_index
FROM countries c JOIN gini g ON c.id = g.country_id
WHERE c.income_level = 'high income'
ORDER BY c.name, g.year;


-- 12. What is the country name, birth rate, life expectancy, total number of recovered COVID cases, number of recovered COVID cases per 100 cases, total doses administered, and total doses administered per 100 people for all countries that have distributed doses of Sputnik V, Sinovac, Sinopharm/Beijing, or CanSino vaccines?

SELECT DISTINCT c.name, c.birth_rate, c.life_expectancy, d.recovered, d.recovered_per_hundred, d.total_doses, d.doses_per_hundred
FROM countries c JOIN vax_rel r ON c.id = r.country_id JOIN vax_manufacturers v ON r.vax_id = v.id JOIN covid d ON c.id = d.country_id
WHERE v.vax = 'Sputnik V'
OR v.vax = 'Sinovac'
OR v.vax = 'Sinopharm/Beijing'
OR v.vax = 'CanSino';


-- 13. What is the average number of confirmed COVID cases for each region?

SELECT c.region, AVG(v.confirmed_cases)
FROM countries c JOIN covid v ON c.id = v.country_id
GROUP BY c.region;


-- 14. What is the most common system of government for countries who have vaccinated more than 50% of their population?

SELECT g.type, COUNT(*)
FROM countries c, covid v, govt_systems g
WHERE c.id = v.country_id
AND c.govt_system = g.id
AND v.fully_vaxed > 50
GROUP BY g.type
ORDER BY COUNT(*) DESC;


-- 15. Which vaccine brand is available in the most countries in the sample?

SELECT m.vax
FROM vax_manufacturers m JOIN vax_rel r ON m.id = r.vax_id
GROUP BY m.vax
HAVING COUNT(*) = (SELECT MAX(count)
                   FROM (SELECT vax_id, COUNT(*)
                         FROM vax_rel
                         GROUP BY vax_id) AS vax_count);


-- 16. Which countries have a population greater than 1 million people and have more than 100,000 COVID-related deaths? What percentage of the population of these countries trusted doctors, nurses, and the government in 2018?

SELECT sub_countries.name, m.trust AS medical_trust, g.trust AS government_trust
FROM med_trust m, govt_trust g, ((SELECT DISTINCT id, name
                                  FROM countries
                                  WHERE population > 1000000)
                                 INTERSECT
                                 (SELECT DISTINCT c.id, c.name
                                  FROM countries c JOIN covid v ON c.id = v.country_id
                                  WHERE v.deaths > 100000)) AS sub_countries
WHERE sub_countries.id = m.country_id
AND sub_countries.id = g.country_id;


-- 17. Which countries outside of North America have greater than 100,000 confirmed COVID cases?  And what are the populations, GDP per capita, and government systems of these countries?

SELECT c.name, c.population, c.gdp_per_cap, g.type AS gov_system
FROM countries c JOIN covid v ON c.id = v.country_id JOIN govt_systems g ON c.govt_system = g.id
WHERE c.name NOT IN (SELECT name
                     FROM countries
                     WHERE region = 'North America')
AND v.confirmed_cases > 100000;


-- 18. How many vaccination doses per person have been given in each high income country?

SELECT c.name, (CAST(v.total_doses AS float) / CAST(c.population AS float)) AS doses_per_person
FROM countries c JOIN covid v ON c.id = v.country_id
WHERE c.income_level = 'high income';


-- 19. Have any countries in the sample had access to more than 3 vaccine brands? If yes, then list the names of the countries and the vaccine brands received, and if not, then show the empty table with the same headers.

SELECT c.name, m.vax
FROM countries c, vax_rel r, vax_manufacturers m
WHERE c.id = r.country_id
AND r.vax_id = m.id
AND c.id IN (SELECT c.id
             FROM countries c JOIN vax_rel r ON c.id = r.country_id
             GROUP BY c.id
             HAVING COUNT(*) > 3);


-- 20. Which country(s) have had the greatest number of COVID-related deaths for each income level? Include the country name, income level, government system, as well as level of trust in the government and medical professionals (in 2018) for each country in the list.

SELECT c.name, c.income_level, g.type AS gov_system, m.trust AS medical_trust, t.trust AS gov_trust
FROM countries c, covid d, govt_systems g, med_trust m, govt_trust t,
  (SELECT c.income_level, MAX(v.deaths)
   FROM countries c JOIN covid v ON c.id = v.country_id
   GROUP BY c.income_level) AS i
WHERE c.id = d.country_id
AND c.govt_system = g.id
AND c.id = m.country_id
AND m.year = 2018
AND c.id = t.country_id
AND t.year = 2018
AND c.income_level = i.income_level
AND d.deaths = i.max;
