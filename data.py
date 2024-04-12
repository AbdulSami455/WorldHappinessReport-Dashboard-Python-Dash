import pandas as pd

def load_happiness_data():
    happiness_data = pd.read_csv('world-happiness-report-2021.csv')
    happiness_data.rename(columns={'Country name': 'Country', 'Healthy life expectancy': 'Healthy_life_expectancy'}, inplace=True)
    return happiness_data
