import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n-----------------------------------------------')
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Please enter one of the following cities: Chicago, New York City, or Washington...  ").title()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred.\n")
            continue
        if city not in ('Chicago', 'New York City', 'Washington'):
            print("Sorry, that's not an appropriate choice.\n")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("\nOk!  Now enter one of the first six months of the year: Jan, Feb, Mar, Apr, May, Jun.  Otherwise, enter 'all' to access data from all six months...  ").title()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred.\n")
            continue
        if month not in ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'All'):
            print("Oops.  Would you please re-enter?  Remember to use this format: Jan, Feb, Mar, Apr, May, Jun.  Or 'all' for data from all months.\n")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("\nGreat.  Now enter a day of the week: Monday, Tuesday, etc.  Otherwise, enter 'all' to access data from the entire week...  ").title()
        except KeyboardInterrupt:
            print("\nSorry, an error occurred.\n")
            continue
        if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'):
            print("Sorry, could you try that again?  Remember to use the full day name.  Or use 'all' for the entire week.\n")
        else:
            break

    print('-'*40)
    return city, month, day



#-------------------------------------------------------------------------------
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
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df



#-------------------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most common month of travel was " + str(popular_month) + ".\n")

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of travel was " + popular_day + ".\n")

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]
    print("The most common hour of travel was " + str(popular_hour) + ".\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



#-------------------------------------------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used starting station for bikeshares was " + popular_start_station + ".\n")

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used ending station for bikeshares was " + popular_end_station + ".\n")

    # TO DO: display most frequent combination of start station and end station trip
    # ***used info from StackOverflow: https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-dataframe-in-pandas-python
    df['Station Combo'] = df['Start Station'] + " | " + df['End Station']
    popular_station_combo = df['Station Combo'].mode()[0]
    print("The most commonly used combination of starting and ending stations was " + popular_station_combo + ".\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#-------------------------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # ***used info received from StackOverflow: https://stackoverflow.com/questions/775049/how-to-convert-seconds-to-hours-minutes-and-seconds
    m, s = divmod(int(df['Trip Duration'].sum()), 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    print("Total bikeshare travel time: " + str(d) + " days, " + str(h) + " hours, " + str(m) + " minutes, " + str(s) + " seconds.")

    # TO DO: display mean travel time
    # used info received from StackOverflow: https://stackoverflow.com/questions/775049/how-to-convert-seconds-to-hours-minutes-and-seconds
    m, s = divmod(int(df['Trip Duration'].mean()), 60)
    h, m = divmod(m, 60)
    print("Average bikeshare travel time: " + str(h) + " hours, " + str(m) + " minutes, " + str(s) + " seconds.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#-------------------------------------------------------------------------------
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Here's a breakdown of bikeshare user types...")
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city not in('Chicago', 'New York City'):
        print("\nSorry, gender statistics for Washington are not available.")
    else:
        print("\nHere's a breakdown of gender among bikeshare users...")
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if city not in('Chicago', 'New York City'):
        print("\nSorry, birth year statistics for Washington are not available.")
    else:
        print("\nAnd lastly, some information on bikeshare users' birth years...")
        print("Earliest birth year among bikeshare users: " + str(int(df['Birth Year'].min())))
        print("Most recent birth year among bikeshare users: " + str(int(df['Birth Year'].max())))
        print("Most common birth year among bikeshare users: " + str(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#-------------------------------------------------------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
