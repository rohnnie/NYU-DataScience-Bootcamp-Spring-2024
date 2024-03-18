import pandas as pd
import ssl
import seaborn as sns 
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    df = pd.read_csv('https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD',storage_options={'verify': False})
    
    df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

    # Filter data for the year 2019 and Brooklyn Bridge location
    brooklyn_bridge_2019 = df[(df['hour_beginning'].dt.year == 2019) & (df['location'] == 'Brooklyn Bridge')]

    # Group by weather summary and calculate total pedestrian counts
    pedestrian_counts_by_weather = brooklyn_bridge_2019.groupby('weather_summary')['Pedestrians'].sum().reset_index()

    # Create a pivot table to have weather summaries as columns
    pivot_table = brooklyn_bridge_2019.pivot_table(index='hour_beginning', columns='weather_summary', values='Pedestrians', aggfunc='sum')

    # Calculate the correlation matrix
    correlation_matrix = pivot_table.corr()

    # Plotting
    plt.figure(figsize=(10, 8))
    sns.barplot(data=pedestrian_counts_by_weather, x='weather_summary', y='Pedestrians')
    plt.title('Total Pedestrian Counts by Weather Summary in 2019')
    plt.xlabel('Weather Summary')
    plt.ylabel('Total Pedestrian Counts')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Display correlation matrix
    print("Correlation Matrix between Weather Patterns and Pedestrian Counts:")
    print(correlation_matrix)