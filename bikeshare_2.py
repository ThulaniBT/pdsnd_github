import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#defining month valid input
month_data={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6}
#defining days valid input
day_data={'Sun':0,'Mon':1,'Tues':2,'Wed':3,'Thurs':4,'Fri':5,'Sat':6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #Get user to select a valid city to view desciptive statistics for.


    while True:
        print('\nWhich city would you be interested in?')
        city=input('\nChicago, New York City or Washington? Please enter the city name.\n').lower()
        if city=="chicago":
                print('\nYou have selected Chicago to explore!\n')
                pic=open('Chicago.txt','r')
                print(pic.read())
                pic.close()
        if city=="new york city":
                print('\nYou have selected New York City to explore!\n')
                print('\nHome to the Statue of Liberty!\n')
                f=open('Loveny.txt','r')
                print(f.read())
                f.close()
        if city=="washington":
                print('\nYou have selected Washington to explore!\n')
                print('\nHome to the pentagon!\n')
                pic=open('Pentagon.txt','r')
                print(pic.read())
                pic.close()
        if city not in CITY_DATA:
            print('Please enter a valid city,pay careful attention to spelling!!!')
            continue
        city=CITY_DATA[city]
        break


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month_filter_choice=input('\nDo you want to filter by month?,Please select Y/N\n').title()
        if month_filter_choice=="Y":
            month_filter_choice=True
            month=input('\nPlease select a month from January-June or Jan,Feb,Mar,Apr,May,Jun\n').title()
            if month not in month_data:
                    print('\nInput not recognised,Please enter valid month!!!\n')
                    continue
        elif month_filter_choice=="N":
            month_filter_choice=False
            month='all'
            break
        else:
            print('\nInput not recognised,Please enter a valid selection Y for Yes & N for No!!!\n')
            continue
        month=month_data[month]
        break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day_filter_choice=input('\nDo you want to filter by day? Y/N\n').title()
        if day_filter_choice=="Y":
             day_filter_choice=True
             day=input('\nPlease enter a day to filter by Sun,Mon,Tues,Wed,Thurs,Fri,Sat\n').title()
             if day not in day_data:
                    print('\nInput not recognised,Please enter a valid day!!!\n')
                    continue
        elif day_filter_choice=="N":
             day_filter_choice=False
             day='all'
             break
        else:
            print('\nInput not recognised,Please enter a valid selection Y for Yes & N for No!!!\n')
            continue
        day=day_data[day]
        break


    print('-'*40)
    return city, month, day


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
    #Load relevant datafile
    df=pd.read_csv(city)
    #Retrieve month, day and hour from Starttime column
    df['month']=pd.to_datetime(df['Start Time']).dt.month
    df['day']=pd.to_datetime(df['Start Time']).dt.dayofweek
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour

    #filter by month selected
    if month!='all':
        df=df[df['month']==month]
    if day!='all':
        df=df[df['day']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mc_month=df['month'].value_counts().idxmax()
    #Loop to ensure that the month name is returned instead of the value from month_data
    for key,value in month_data.items():
        if mc_month==value:
            x=key
    print('The most common month is: {}'.format(x))

    # TO DO: display the most common day of week
    mc_day=df['day'].value_counts().idxmax()
    #Loop to ensure that the day name is returned instead of the value from dayyes_data
    for key,value in day_data.items():
        if mc_day==value:
            x=key
    print('The most common day of the week is: {}'.format(x))

    # TO DO: display the most common start hour
    mcs_hour=df['hour'].value_counts().idxmax()
    print('The most common start hour is: {}'.format(mcs_hour))

    #Count for hour
    hour_count=df['hour'].value_counts().max()
    print('Hour count: {}'.format(hour_count))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_start_station=df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is: {}'.format(mc_start_station))

    #Count for start station
    start_count=df['Start Station'].value_counts().max()
    print('Start station Count:{}'.format(start_count))

    # TO DO: display most commonly used end station
    mc_end_station=df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is :{}'.format(mc_end_station))

    #Count for end station
    end_count=df['End Station'].value_counts().max()
    print('End station Count:{}'.format(end_count))


    # TO DO: display most frequent combination of start station and end station trip
    comb_of_start_and_end=df[['Start Station','End Station']].mode().loc[0]
    print('The most frequent combination of start station and end station trip are : {} and {}'.format(comb_of_start_and_end[0],comb_of_start_and_end[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,city):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    if city=="chicago.csv" or city=="new_york_city.csv":
    # TO DO: display total travel time
        #Sum In seconds
        sum_stravel_time=df['Trip Duration'].sum()
        print('The total time is : {} seconds'.format(sum_stravel_time))
        #Converting sum to hours
        sum_travel_time=(df['Trip Duration'].sum())//3600
        print('The total time is : {} hour(s)'.format(sum_travel_time))
        #converting sum to minutes
        min_travel_time=(df['Trip Duration'].sum())/60
        print('The total time is: {} minutes'.format(min_travel_time))

        # TO DO: display mean travel time
        #Average In seconds
        avg_travel_time=df['Trip Duration'].mean()
        print('The mean travel time in seconds is: {}'.format(avg_travel_time))

        #converting average to minutes and seconds
        min_avgtravel_time=(df['Trip Duration'].mean())/60
        x=min_avgtravel_time-(int(min_avgtravel_time))
        print('Basically the mean time is: {} minutes and {} seconds'.format(int(min_avgtravel_time),x*60))

    #for Washington
    else:
        sum_stravel_time=df['Trip Duration'].sum()
        print('The total time is : {} miliseconds'.format(sum_stravel_time))
        #sum In hours
        sum_travel_time=(df['Trip Duration'].sum())/(3.6*(10**6))
        print('The total time is : {} hour(s)'.format(sum_travel_time))
        #Sum In minutes
        min_travel_time=(df['Trip Duration'].sum())/60000
        print('The total time is: {} minutes'.format(min_travel_time))

        # TO DO: display mean travel time
        avg_travel_time=df['Trip Duration'].mean()
        print('The mean travel time is: {}'.format(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    u_types=df['User Type'].value_counts()
    print('The count of user types is: {}'.format(u_types))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def gender_stats(df,city):
    """Displays statistics on the gender of the users."""

    print('\nCalculating Gender Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of gender
    #For chicago and new york city
    if city=="chicago.csv" or city=="new_york_city.csv":
        gender=df['Gender'].value_counts()
        print('There are: {}'.format(gender))
    #For washington
    else:
        print('Sorry,No gender statistics available for Washington. -_-')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def birth_stats(df,city):
    """Displays statistics on the birth years of users."""

    print('\nCalculating Birth year Stats...\n')
    start_time = time.time()
    # TO DO: Display earliest, most recent, and most common year of birth
    #Only for chicago and new york city
    if city=="chicago.csv" or city=="new_york_city.csv":
        birth_year=df['Birth Year']

        #Most common birth year of the city
        mc_by=birth_year.value_counts().idxmax()
        print('The most common birth year is: {}'.format(mc_by))

        #Most recent birth year of the city
        mc_rby=birth_year.max()
        print('The most recent birth year is: {}'.format(mc_rby))

        #The earliest birth year
        early_by=birth_year.min()
        print('The earliest birth year is: {}'.format(early_by))

    #For washington
    else:
        print('Sorry, No birth year statistics available for Washington.-_-')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df,city):
    """Displays raw data to user if user agrees."""
    rawinput_choice=input('\nWould you like to see some of the raw data of {}, Please enter Y/N\n'.format(city)).title()

    if rawinput_choice=="Y":
        rawinput_choice=True
        print('\nRetrieving data....\n')
        x=0
        y=5
        print(df.iloc[x:y])

        #Loop for displaying the raw data 5 records at a time
        while True:
            rawinput_choice=input('\nDo you want to see 5 more?, Y/N\n').title()
            if rawinput_choice=="Y":
                x+=5
                y+=5
                print(df.iloc[x:y])
            elif rawinput_choice=="N":
                break
            else:
                print('\nInput not recognised,Please enter a valid selection Y/N\n')
    elif rawinput_choice=="N":
        rawinput_choice=False
    else:
        print('\nInput not recognised,Please enter a valid selection Y/N\n')
        raw_data(df,city)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df,city)
        user_stats(df)
        gender_stats(df,city)
        birth_stats(df,city)
        raw_data(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
