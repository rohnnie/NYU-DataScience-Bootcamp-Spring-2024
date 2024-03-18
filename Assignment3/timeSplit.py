import pandas as pd
import ssl
import seaborn as sns 
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pd.read_csv('https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD',storage_options={'verify': False})
    
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

    # Define a function to categorize time of day
    def categorize_time_of_day(hour):
        if 6 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 18:
            return 'Afternoon'
        elif 18 <= hour < 24:
            return 'Evening'
        else:
            return 'Night'

    # Apply the function to create a new column 'time_of_day'
    df['time_of_day'] = df['hour_beginning'].dt.hour.apply(categorize_time_of_day)

    # Group by 'time_of_day' and calculate the total pedestrian count
    pedestrian_activity = df.groupby('time_of_day')['Pedestrians'].sum()

    print(pedestrian_activity)