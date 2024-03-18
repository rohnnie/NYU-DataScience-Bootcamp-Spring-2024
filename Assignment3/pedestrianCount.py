import pandas as pd
import ssl
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pd.read_csv('https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD',storage_options={'verify': False})
    
    print(df)
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
    weekdays_df = df[df['hour_beginning'].dt.dayofweek < 5]
    pedestrian_counts_by_day = weekdays_df.groupby(weekdays_df['hour_beginning'].dt.dayofweek)['Pedestrians'].sum()

    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    plt.plot(days_of_week, pedestrian_counts_by_day)
    plt.title('Pedestrian Counts for Each Day of the Week')
    plt.xlabel('Day of the Week')
    plt.ylabel('Pedestrian Counts')
    plt.show()