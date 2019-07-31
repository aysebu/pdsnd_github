import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    months=['january', 'february', 'march', 'april', 'may', 'june','all']
    days=["monday","tuesday","wednesday","thursday","friday", \
          "saturday","sunday","all"]
    cities=["chicago", "new york city", "washington"]
    
  #Asks user to specify a city, month, and day to analyze.
    # TO DO: get user input for city (chicago, new york city, washington).HINT: Use a while loop to handle invalid inputs
    city = input('Please enter the name of the city to analyze: Chicago, New York City or Washington ? ').lower()
    while True:
        if city in cities:
            break
        else:
            city=input("Your city input is not valid.Pleace choose one of the three options: Chicago, New York City, Washington: ").lower()
   
    month=input("Pleace choose  a month to filter or \"all\" option: ").lower()
    while True:
        if month in months:
            break
        else:
            month=input("Your month input is not valid.Pleace choose  a month or all option: ").lower()
   
    day=input("Pleace choose  a day to filter or \"all\" option: ").lower()
    while True:
        if day in days:
            break
        else:
            day=input("Your day input is not valid. Pleace choose a day or all option: ").lower()

    print('-'*40)
    
    return city,month,day
    
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df["Start Time"] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] =  df["Start Time"].dt.month
    popular_month = df['month'].mode()[0]
    print("The most popular start hour: ", popular_month)
    
    # TO DO: display the most common day of week
    df['week'] =  df["Start Time"].dt.week
    popular_week = df['week'].mode()[0]
    print("The most popular start week: ", popular_week)
     
    # TO DO: display the most common start hour
    df['hour'] =  df["Start Time"].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular start hour: ", popular_hour)
     

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\n The most popular start stations is :', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\n The most popular end stations is :', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    station_combination = df[['Start Station', 'End Station']].mode().loc[0]
    print('\n The most frequent combination of start station and end station is:\n',station_combination)
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time : ",total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time :",mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df,c):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("\nCount of each user type:\n",user_types)
    
    if c != 'washington':
        gender_stats = df['Gender'].value_counts()
        print("\nCount of each gender:\n",gender_stats)


    # TO DO: Display earliest, most recent, and most common year of birth
    if c != 'washington':
        earliest_birth = int(df['Birth Year'].min())
        most_recent_birth = int(df['Birth Year'].max())
        most_common_birth_date = int(df['Birth Year'].mode())
        print("\nThe earliest birth date among customers: ", earliest_birth)
        print("\nThe most recent birth date among customers: ", most_recent_birth)
        print("\nThe most recent birth date among customers: ", most_common_birth_date)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    x=0
    while True: 
        display = input("\nWould you like to see raw data?Please type yes or no.")
        if display.lower() == "no":
            break
        else:
            print(df.iloc[x:x+5])
            x+=5

    
     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)
    

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            break


if __name__ == "__main__":
    main()


    
