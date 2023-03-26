# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:00:26 2023

@author: TARAJIC - UDACITY Projct #2 (Python)
"""
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago','new york city','washington']
        city= input("\n Would you like to see data for Chicago, New York City, or Washington? \n").lower()
        if city in cities:
            break
        else:
            print('please enter valid city name')
    # get user input for month (all, january, february, ... , june)
    while True:
        months= ['All', 'January','February','March','April','May','June']
        days= ['All', 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        filters = ['all', 'day', 'month']
        filter = input("\n Would you like to filter the data by month, day, or not at all? \n").lower()
        month = None
        day = None
        if filter in filters:
            if filter == 'month':
                while True:
                    month = input("\n Which month - January,February,March,April,May,June or - All - for no filter? \n").lower()
                    if month.title() in months:
                        while True:
                            day = input("\n Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or - All - for no filter? \n").lower()
                            if day.title() in days:
                                break
                        else:
                            print('Please enter a valid day')
                        break
                    else:
                        print('Please enter a valid month')
            elif filter == 'day':
                while True:
                    day = input("\n Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or - All - for no filter? \n").lower()
                    if day.title() in days:
                        month = 'all' if month == None else month
                        break
                    else:
                        print('Please enter valid day')
            elif filter == 'all':
                month = 'all' if month == None else month
                day = 'all' if day == None else day
            break
        else:
            print("\n Please enter a valid value - month, day or all for no filter")    

    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    print(city, month, day)
    print('-'*40)
    return city, month, day

# see Udacity course - Practice Problem Nr 3 -
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
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    #filter by month if applicable
    if month != 'all': 
    # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month.title()) + 1
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

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)

        

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)


    # display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))            
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)


    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)


    # display the most frequent combination of start station and end station trip
    df['station_combination'] = df['Start Station']+' -> '+df['End Station']
    favourite_station_combination = df['station_combination'].mode()[0]
    print('the most commonly used combination of start station and end station trip:', favourite_station_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time :", total_travel)

    
    
    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts= df['User Type'].value_counts()
    print("The user types are:\n",user_counts)


    # Display counts of gender
    if 'Gender' in df.columns:
        user_stats_gender=df['Gender'].value_counts()
        print("\nThe counts of each gender are:\n",user_stats_gender)


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']
        # the most common birth year
        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year)
        # the most recent birth year
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)
        # the most earliest birth year
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(city):
    """Displays statistics on the total and average trip duration."""
    df = pd.read_csv(CITY_DATA[city])
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    Number_of_rows = len(df.index)
    pd.set_option('display.max_columns', None)
    while (start_loc<Number_of_rows):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
        if view_data != 'yes':
            break
            
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(city)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

