import requests

def check_command_is_for_covid_cases(command):
    country = get_country(command).capitalize()
    cases = get_covid_cases(country)
    return (f"The current active cases in {country} are {cases}")


def get_country(command):                   # For getting only the country name for the whole query
    country = command.split()[-1]
    if country == "?":
        country = command.split()[-2]
    return country


def get_covid_cases(country):               # For getting current covid cases
    totalActiveCases = 0
    response = requests.get('https://api.covid19api.com/live/country/' + country + '/status/confirmed').json()
    for data in response:
        totalActiveCases += data.get('Active')
    return totalActiveCases

#print(check_command_is_for_covid_cases('active cases of covid in India ?')) # Example