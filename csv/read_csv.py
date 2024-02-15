import csv
import functools
import matplotlib.pyplot as plt


def get_population(country_dict):
  population_dict = {
      '2022': int(country_dict['2022 Population']),
      '2020': int(country_dict['2020 Population']),
      '2015': int(country_dict['2015 Population']),
      '2010': int(country_dict['2010 Population']),
      '2000': int(country_dict['2000 Population']),
      '1990': int(country_dict['1990 Population']),
      '1980': int(country_dict['1980 Population']),
      '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'imgs/{name}.png')
  plt.close()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      country_dic = {key: value for key, value in iterable}
      data.append(country_dic)
    return data


def read_csvDos(path):
  total = 0
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    total = functools.reduce(lambda ac, row: ac + int(row[1]), reader, 0)
    print(total)
    return total


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,
                       data))
  return result


def challenge():
  data = read_csv('./world_population.csv')
  country = input('Type country => ')
  name = country
  result = population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = get_population(country)
    generate_bar_chart(name, labels, values)


def challengeTwo():
  data = read_csv('world_population.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  generate_pie_chart(countries ,percentages)
