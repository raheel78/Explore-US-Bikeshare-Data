## TODO: import all necessary packages and functions
import sys
import csv
import time
from datetime import datetime
from collections import Counter
import matplotlib.pyplot as plt
import statistics as stat

## to indicate that a user did not select a variable (used in functions)
not_defined = -1


## Filenames
data_files = {'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}

## allowed selections for time_period
periods = ['month', 'day', 'none']

## allowed selection for month names / mapping
month_names = {'January':1,
               'February':2,
               'March':3,
               'April':4,
               'May':5,
               'June':6}
#               'July':7,
#               'August':8,
#               'Sepember':9,
#               'October':10,
#               'November':11,
#               'December':12}

## allowed selections for weekday names / mapping
week_day_names = {'Monday':0,
                  'Tuesday':1,
                  'Wednesday':2,
                  'Thursday':3,
                  'Friday':4,
                  'Saturday':5,
                  'Sunday':6}

#helper utility function for printing
def p(str):
	print(str)
	
	
# helper functions to map month/weekday-ints to month/weekday-names and vice versa
def month_to_name(month):
    ''' converts a month number to a month name; uses dict(month_names) 
        Args: (int) month: 1 to 12, 1 represents January
        Returns: (str) month_name: January, February, ..., December
    '''
    for k,v in month_names.items():
        if v == month:
            return k

def week_day_to_name(week_day):
    ''' converts a weekday number to a weekday name; uses dict(week_day_names) 
        Args: (int) month: 0 to 6, 0 represents Monday
        Returns: (str) month_name: Monday, Tuesday, ..., Sunday
    '''
    for k,v in week_day_names.items():
        if v == week_day:
            return k

# helper functions basic statistic
def get_mean(value_list):
    ''' calculates the arithmetic average of a given list of numbers 
        Args: (list) value_list
        Returns: (float) avg
    '''
    avg = float(sum(value_list)) / len(value_list)
    return avg

def get_median(value_list):
    ''' calculates the median of a given list of numbers 
        Args: (list) value_list
        Modules: statistics
        Returns: (float) median
    '''
    return stat.median(value_list)

def get_stdv(value_list):
    ''' calculates the standard deviation of a given list of numbers 
        Args: (list) value_list
        Modules: statistics
        Returns: (float) stdev
    '''
    return stat.stdev(value_list)

# helper function to sort, select and print dictionaries (frequencies)
def first_n(freq_dict, n=5, sort_by_key = True, as_reversed=True, as_text=True):
    ''' returns the first n values of a key-value-pair (dictionary) 
        
        Args: (dict) freq_dict
        Optional Args: 
            (int)  n: number of items to be returned
            (bool) sort_by_key: sort order either by keys or values of freq_dict
            (bool) as_reversed: True -> highest items, False -> smallest items
            (bool) as_text: True -> str(list of n keys:values), False: list(n keys:values) 
        Returns: 
            (str) or (list) depending on optional arg 'as_text'
    '''
    if sort_by_key:
        k,v = list(zip(*sorted(freq_dict.items(), key=lambda t: t[0], reverse=as_reversed)))
    else:
        k,v = list(zip(*sorted(freq_dict.items(), key=lambda t: t[1], reverse=as_reversed)))

    if as_text:
        text = ''
        for i in range(0,n,1):
            text = text + str(i +1)+ ', ' + str(k[i]) + ': ' +str(v[i]) + '\n'
        return text
    else:
        return list(zip(k[0:n],v[0:n]))


def get_data(filename):
    ''' reads lines of a csv-file as a list of ordered dictionaries
        Args: (str) filename, e.g. Washington.csv
        Modules: csv, datetime, sys
        Returns: list of ordered dictionaries
    '''
    limit_rows = False
    counter = 0
    max_rows = 30000

    data = []

    try:
        f_in = open(filename,'r')

    except Exception as e:
       p("Exception occurred: {}".format(e))
       sys.exit(1)

    else:
        csv_reader = csv.DictReader(f_in)

        for row in csv_reader:
            
            if limit_rows:
                if counter < max_rows:
                    
                    # additional column for easier / more readable filtering of month, weekday
                    row['start'] = datetime.strptime(row['Start Time'],'%Y-%m-%d %H:%M:%S')
                    data.append(row)
    
                    counter +=1
            else:
                    row['start'] = datetime.strptime(row['Start Time'],'%Y-%m-%d %H:%M:%S')
                    data.append(row)

        f_in.close()
        return data


def get_city():
    ''' Asks the user to choose a city and returns the filename of that city
        Args: none.
        Returns: (str) filename, e.g. Washington.csv
    '''
    while True:
        try:
            city = str(input('\nHello! Let\'s explore some US bikeshare data!\n'
                             'Would you like to see data for Chicago, New York, or Washington?\n'))
            #city = 'chicago'
            city = city.strip().lower()
        except:
            p('Something went wrong!')
            continue

        if  city not in data_files.keys():
            p('Not an appropriate choice!')
            continue

        else:
            #valid input break while loop
            break

    #p(city)
    return city


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.
    Args:
        none.
    Returns:
        (str) time period: month, day, none
    '''

    # TODO: handle raw input and complete function
    while True:
        try:
            time_period = str(input('\nWould you like to filter the data by month, day, or not at'
                                    ' all? Type "none" for no time filter.\n'))
            #time_period = 'none'
            time_period = time_period.strip().lower()
        except:
            p('Something went wrong!')
            continue

        if  time_period not in periods:
            p('Not an appropriate choice!')
            continue

        else:
            #valid input break while loop
            break

    #p(time_period)
    return time_period


def get_month():
    '''Asks the user for a month and returns the specified month.
    Args:
        none.
    Returns:
        (str) monthnames: January, February, March, April, May, June, July,
                          August, Sepember, October, November, December
    '''
    # TODO: handle raw input and complete function
    while True:
        try:
            month_name = str(input('\nWhich month? January, February, March, April, May, or June?\n'))
            #month_name = 'January'
            month_name = month_name.strip().capitalize()
        except:
            p('Something went wrong!')
            continue

        if  month_name not in month_names.keys():
            p('Not an appropriate choice!')
            continue

        else:
            #valid input break while loop
            break

    #p(month_name)
    return month_name


def get_week_day():
    '''Asks the user for a weekday and returns the specified day.
    Args:
        none.
    Returns:
        (str) returns names of weekdays: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    '''

    # TODO: handle raw input and complete function

    while True:
        try:
            week_day_name = str(input('\nWhich Weekday? Monday, Tuesday, '
                            'Wednesday, Thursday, Friday, Saturday, Sunday? .\n'))
            #week_day_name = 'Monday'
            week_day_name = week_day_name.strip().capitalize()
        except:
            p('Something went wrong!')
            continue

        if  week_day_name not in week_day_names.keys():
            p('Not an appropriate choice!')
            continue

        else:
            #valid input break while loop
            break

    #p(week_day_name)
    return week_day_name

def popular_month(data):
    '''Counts starttimes per month and returns month with the maximum count
       Args: (list(ordered dict)) data: list of orered dicts
       Modules: datetime
       Functions: get_mean()
       Returns: 
           (str) Name of Month: January, February, ...
           (int) Maximum Count of trips in Month
           (float) Average Count of trips in Month
    '''
    # frequency of startdate per month
    # please note this function uses column 'Start time'
    # following functions use column 'start' and Counter from collections

    d = {}
    for row in data:
        start_date = datetime.strptime(row['Start Time'],'%Y-%m-%d %H:%M:%S')
        if start_date.month in d:
            d[start_date.month] +=1
        else:
            d[start_date.month] = 1

    # find highest value, month in d
    max_value = 0
    max_month = ''
    for el in d:
        if d[el] > max_value:
            max_value = d[el]
            max_month = el

    avg_value = get_mean(list(d.values()))

    return max_month, max_value, avg_value
    #return datetime.strftime(datetime.strptime(str(max_month),'%m'),'%B')


def avg_trips_per_day(data, month, week_day):
    '''Calculates average number of trips based on the 'start'-column of the dataset
    Args:
        (list(ordered dict)) data: list of ordered dicts, (int) month , (int) week_day
    Modules: collections
    Functions: get_mean()
    Gobal Variable : not_defined, if -1 no user selection
    Returns:
        (float) average
    '''

    if (month == not_defined and week_day == not_defined): #no filter
        days_list = [row['start'].date() for row in data ]
        c = Counter(days_list)
        k,v = zip(*sorted(c.items(), key=lambda t: t[1], reverse=True)) # not necessary only for plotting tbd
        return get_mean(v)

    elif month != -1: # month only is defined
        days_list = [row['start'].date() for row in data if row['start'].month == month]
        c = Counter(days_list)
        k,v = zip(*sorted(c.items(), key=lambda t: t[1], reverse=True)) # not necessary only for plotting tbd
        return get_mean(v)

    else:  #week_day != -1 , week_day only is define
        days_list = [row['start'].date() for row in data if row['start'].weekday() == week_day]
        c = Counter(days_list)
        k,v = zip(*sorted(c.items(), key=lambda t: t[1], reverse=True)) # not necessary only for plotting tbd
        return get_mean(v)


def popular_week_day(data, month):
    '''Calculates average number of trips based on the 'start'-column of the dataset
    Args:
        (list(ordered dict)) data: list of ordered dicts, (int) month , (int) week_day
    Modules: collections
    Functions: get_mean()
    Gobal Variable : not_defined, if -1 no user selection
    Returns:
        (float) average
    '''
    if month != not_defined: # month is defined
        
        # count trips as weekdays - nominator
        trips = Counter([row['start'].weekday() for row in data if row['start'].month == month] )

        # count weekdays - denominator
        days = list(set([ (row['start'].date() , row['start'].weekday() ) 
                                                 for row in data if row['start'].month == month] ))
        k,v = zip(*days)
        wdays = Counter(v)

    else: # month is not defined
        
        # count trips as weekdays - nominator
        trips = Counter([row['start'].weekday() for row in data ] )

        # count weekdays - denominator
        days = list(set([ (row['start'].date() ,row['start'].weekday() ) for row in data ] ))
        k,v = zip(*days)
        wdays = Counter(v)

    avg_trips = dict((k,trips[k]/wdays[k]) for k in trips.keys())
    
    return avg_trips

def popular_hour(data, month, week_day):
    '''Calculates number of trips based on the 'start'-column of the dataset
    Args:
        (list(ordered dict)) data: list of ordered dicts, (int) month , (int) week_day
    Modules: collections
    Functions: get_mean()
    Gobal Variable : not_defined, if -1 no user selection
    Returns:
        (float) number of trips
    '''
    #p('Month: ', month)
    #p('Weekday: ', week_day)

    if (month == not_defined and week_day == not_defined):
        l = [row['start'].hour for row in data  ]
        c = Counter(l)
        #p('1: ',c)
        return c

    elif month != not_defined:
        l = [row['start'].hour for row in data if row['start'].weekday() == month ]
        c = Counter(l)
        #p('2: ',c)
        return c

    else: # week_day != not_defined:
        l = [row['start'].hour for row in data if row['start'].weekday() == week_day ]
        c = Counter(l)
        #p('3: ',c)
        return c


def trip_duration(data, month, week_day):
    '''selects duration of trips in minutes based on the 'start'-column of the dataset
    Args:
        (list(ordered dict)) data: list of ordered dicts, (int) month , (int) week_day
    Modules: collections
    Gobal Variable : not_defined, if -1 no user selection
    Returns:
        (list) duration of trips in minutes
    '''
    #p('Month: ', month)
    #p('Weekday: ', week_day)

    if (month == not_defined and week_day == not_defined):
        l = [float(row['Trip Duration'])/60.0 for row in data  ]
        #p('1: ',l)
        return l

    elif month != not_defined:
        l = [float(row['Trip Duration'])/60.0 for row in data if row['start'].weekday() == month ]
        #p('2: ',l)
        return l

    else: # week_day != not_defined:
        l = [float(row['Trip Duration'])/60.0 for row in data if row['start'].weekday() == week_day ]
        #p('3: ',l)
        return l


def popular_stations(data, kind):
    '''selects start- or end-stations from data
    Args:
        (list(ordered dict)) data: list of ordered dicts
        (str) kind: 'start' or 'end --> start station column or end station column
    Modules: collections
    Returns:
        (list) list with start or end stations
    '''
    # TODO: complete function
    if kind == 'start':
        stations = Counter([row['Start Station'] for row in data])
        return stations
    elif kind == 'end':
        stations = Counter([row['End Station'] for row in data])
        #k,v = zip(*sorted(stations.items(), key=lambda t: t[1], reverse=True))
        return stations  
    

def popular_trip(data):
    '''selects trip connections from data based on the columns 'start' and 'end'-station
       counts unique connections independent of the direction of the trip
       e. g. 'Street 1' to 'Street 2' means the same as 'Street 2' to 'Street1'
    Args:
        (list(ordered dict)) data: list of ordered dicts
    Modules: collections
    Returns:
        (dict) connections: counts
    '''
    # TODO: complete function
    fs_trips =  Counter([frozenset((row['Start Station'] , row['End Station'] )) for row in data ])
    
    # convert to dictionary
    d = {}
    for k,v in fs_trips.items():
        d[' - '.join(k)] = v
        
    return d



## counter by fieldname method, in the methods above used Counter from collections
## next, a dictionary is used to test different programming approaches!  
def get_count_by_field(data, month, week_day, field_name):
    '''counts the number of items in a specified field_name (column)
    Args:
        (list(ordered dict)) data: list of ordered dicts, (int) month, (int) week_day, (str) field_name
    Returns:
        (dict) key: counts
    '''
    # TODO: complete function
    d = {}
    if (month == not_defined and  week_day == not_defined):
        for row in data:
            if row[field_name] in d:
                #p(row[field_name])
                d[row[field_name]] += 1
            else:
                d[row[field_name]] = 1
    elif month != not_defined:
        for row in data:
            if row['start'].month == month:
                if row[field_name] in d:
                    d[row[field_name]] += 1
                else:
                    d[row[field_name]] = 1
    else: # week_day != not_defined:
        for row in data:
            if row['start'].weekday() == week_day:
                if row[field_name] in d:
                    d[row[field_name]] += 1
                else:
                    d[row[field_name]] = 1
    
    # replace empty cells with 'Unknown'               
    if '' in d.keys():
        d['Unknown'] = d.pop('')
                    
    return d

def get_users(data, month, week_day):
    '''counts the number of different 'user types' in the data
    Args:
        (list(ordered dict)) data: list of ordered dicts, (int) month, (int) week_day
    Functions: get_count_by_field()
    Returns:
        (dict) key: counts
    '''
    # TODO: complete function
    return get_count_by_field(data, month, week_day,'User Type')    

def get_gender(data, month, week_day):
    '''counts the number of different 'gender' in the data
    Args:
        (list(ordered dict)) data: list of ordered dicts, (int) month, (int) week_day
    Functions: get_count_by_field()
    Returns:
        (dict) key: counts
    '''
    # TODO: complete function
    
    return get_count_by_field(data, month, week_day,'Gender')   

def get_age(data, month, week_day):
    '''calculates the age of the user
    Args:
        (list(ordered dict)) data: list of ordered dicts, (int) month, (int) week_day
    Returns:
        (dict) age: counts
    '''
    # TODO: complete function
    byears = get_count_by_field(data, month, week_day,'Birth Year')  
    age ={}
    current_year = datetime.now().year
    for k in byears:
        if k != 'Unknown':
            age[current_year- int(float(k))] = byears[k]
    return age

def display_data(data):
    '''prints 5 rows of the data, user can continue to print 5 rows until end of data is reached
    Args:
        (list(ordered dict)) data: list of ordered dicts
    Returns:
        None
    '''
   
    records = str(input('\nWould you like to see the individual records? Type \'yes\' or \'no\'.\n'))
    if records == 'yes':
        cont = True
        n_records = 5
        current_pos = 0
        # initial column length based on header
        max_col_len = {}
        for row in data[0:1]:
            for k,v in row.items():
                max_col_len[k] = len(str(k))
                
        while cont:
            
            if current_pos + n_records > len(data):
                n_records = len(data) - current_pos
                p("You reached the end of the list, remaining records {}\n".format(n_records))
                cont = False
            else:
                p("Current position in list {} to {}:\n".format(current_pos, current_pos + n_records))
            
            # determine column-width for the next n rows
            for row in data[current_pos: current_pos + n_records]:
                for k,v in row.items():
                    #p(k)
                    if max_col_len[k] < len(str(v)):
                        max_col_len[k] = len(str(v))
            
            # print header
            text = ""
            for k in max_col_len.keys():
                if k != 'start':    # skip added date field
                    text = text + '|{0: <{width}}'.format(str(k),width=max_col_len[k])
            p(text)
            
            # print data
            for row in data[current_pos:current_pos + n_records]:
                text = ""
                for k,v in row.items():
                    if k != 'start':
                        text = text + '|{0: <{width}}'.format(str(v),width=max_col_len[k])
                p(text)
            
            current_pos += n_records
            
            if cont:
                next_records = str(input('\nWould you like to continue? Type \'yes\' or \'no\'.\n'))
                if next_records =='yes':
                    cont = True
                else:
                    cont = False
                    
def calculate_statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.
    Args:
        none.
    Returns:
        none.
    '''

    # Filter by city (Chicago, New York, Washington)
    city_name = get_city()

    # default values for filter settings (function parameters to indicate as not defined)
    month = not_defined          #-1 means not defined: possible range: 1 to 12 , dictionary: month_names
    week_day = not_defined       #-1 means not defined: possible range: 0 to 6 , dictionary: week_day_names

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'month':
        month_name = get_month()
        month = month_names[month_name]
    elif time_period == 'day':
        week_day_name = get_week_day()
        week_day = week_day_names[week_day_name]

    # Print user selections:
    p('\nYour Selections:')
    p('City: {}'.format(city_name.capitalize()))
    p('Time Period: {}'.format(time_period))
    if time_period == 'month':
        p('Month: {}'.format(month_name))
    if time_period == 'day':
        p('Weekday: {}'.format(week_day_name))


    # Read data from file and store in list of ordered dicts
    p('\nRetrieving data ... \nBe patient and sit tide, we are crunching numbers  ... (almost there!)')
    start_time = time.time()
    data = get_data(data_files[city_name])
    p("That took %s seconds." % (time.time() - start_time))
    p('\nCalculating the first statistic...\n')


    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()

        #TODO: call popular_month function and print the results
        month_int, max_value, avg_value = popular_month(data)
        p('What is the most popular month?\n')
        p('... and the winner is {} with {:,.0f} trips'.format(month_to_name(month_int), max_value))
        p('to give you an idea, the average number per month equals to {:,.0f} trips\n'.format(avg_value))

        p("That took %s seconds." % (time.time() - start_time))
        wait_dummy = input('Press key to continue ...')
        p("Calculating the next statistic...\n")


    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results
        week_day_int = popular_week_day(data, month)

        # get counts for plot in sorted order
        k,v = zip(*sorted(week_day_int.items(), key=lambda t: t[1], reverse=True))

        p("That took %s seconds." % (time.time() - start_time))

        # plot data
        fig = plt.figure(figsize=(8,5))
        ax1 = fig.add_subplot(111)
        barlist = ax1.bar(k,v)
        barlist[0].set_color('red')
        ax1.set_xticks(range(len(k)))
        ax1.set_xticklabels([x[0] for x in sorted(week_day_names.items(),key=lambda x: x[1])])
        ax1.set_xlabel('Weekday')
        ax1.set_ylabel('Average number of trips')
        ax1.set_title('Popular Weekdays - Average number of trips')
        plt.show()

        wait_dummy = input('Press key to continue ...')
        p("Calculating the next statistic...\n")
        
    # Extra
    # What is the average number of trips per day
    if time_period == 'none' or time_period == 'month' or time_period == 'day':
        start_time = time.time()

        avg_trips = avg_trips_per_day(data,month,week_day)

        p('{:,.1f} trips per day on average!\n'.format(avg_trips))
        
        p("That took %s seconds." % (time.time() - start_time))
        wait_dummy = input('\nPress key to continue ...')
        p("Calculating the next statistic...\n")


    # What is the most popular hour of day for start time?
    if time_period == 'none' or time_period == 'month' or time_period == 'day':
        start_time = time.time()

        # TODO: call popular_hour function and print the results
        hours_int = popular_hour(data, month, week_day)

        # get counts for plot in sorted order
        k,v = zip(*sorted(hours_int.items(), key=lambda t: t[1], reverse=True))

        p("That took %s seconds." % (time.time() - start_time))

        # plot data
        fig = plt.figure(figsize=(8,5))
        ax1 = fig.add_subplot(111)
        barlist = ax1.bar(k,v)
        barlist[0].set_color('red')
        #barlist[1].set_color('red')
        ax1.set_xticks(range(len(k)))
        ax1.set_xlabel('Hour')
        ax1.set_ylabel('Number of trips')
        ax1.set_title('Popular Hours - Number of trips per hour')
        plt.show()


        wait_dummy = input('Press key to continue ...')
        p("Calculating the next statistic...\n")


    # What is the total trip duration and average trip duration?
    if time_period == 'none' or time_period == 'month' or time_period == 'day':
        start_time = time.time()


        # TODO: call trip_duration function and print the results
        tripd_mins = trip_duration(data, month, week_day)
        total_v = sum(tripd_mins)
        mean_v = get_mean(tripd_mins)
        median_v = get_median(tripd_mins)
        stdv_v = get_stdv(tripd_mins)

        p('What about trip duration?')
        p('sum of all minutes: {:,.0f} !!!???'.format(total_v))
        p('to make it clear, the average user spent {:,.0f} minutes on a bike\n'.format(mean_v))

        p("That took %s seconds." % (time.time() - start_time))
        p('\n... not everybody is the same, here is the distribution:\n')

        wait_dummy = input('Press key to continue ...')

        fig = plt.figure(figsize=(8,5))
        ax1 = fig.add_subplot(111)
        ax1.hist(tripd_mins, bins=range(0,95,5), rwidth=0.9)#, range=o)

        ax1.set_xticks(range(0,95,5))
        ax1.set_ylabel('Number of trips')
        ax1.set_xlabel('Minutes')
        ax1.set_title('Distribution of trip duration [Minutes]')

        ax1.axvline(mean_v, color='red', linestyle='dashed', linewidth=2)
        ax1.axvline(median_v, color='black', linestyle='dashed', linewidth=2)

        textstr = 'Mean: {:.0f}\nMedian: {:.0f}\nStdv: {:.1f}'.format(mean_v,median_v,stdv_v)
        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
        # place a text box in upper left in axes coords
        ax1.text(0.65, 0.95, textstr, transform=ax1.transAxes, fontsize=14,
                verticalalignment='top', bbox=props)

        plt.show()

        wait_dummy = input('\nPress key to continue ...')
        p("Calculating the next statistic...\n")


    # What is the most popular start station and most popular end station?
    if time_period == 'none' :
        start_time = time.time()
   
        # TODO: call popular_stations function and print the results
        start_st = popular_stations(data,'start')
        start_st_top = first_n(start_st,5,False,True,True)
        start_st_bot = first_n(start_st,5,False, False,True)
        
        p("Let\'s take a closer look at stations ...")
        p("Popular Starts:")
        p(start_st_top)
        p("Least popular:")
        p(start_st_bot)
        
        end_st = popular_stations(data,'end')
        end_st_top = first_n(end_st,5,False,True,True)
        end_st_bot = first_n(end_st,5,False,False,True)
        
        p("\nPopular Ends:" )
        p(end_st_top)
        p("Least popular:")
        p(end_st_bot)
    
    
        p("\nThat took %s seconds." % (time.time() - start_time))
        wait_dummy = input('\nPress key to continue ...')
        p("Calculating the next statistic...")
        
    # What is the most popular trip?  
    if time_period == 'none':       
        start_time = time.time()

        # TODO: call popular_trip function and print the results
        connections = popular_trip(data)
        top_connections = first_n(connections,5,False,True,True)

        p('\nWhat are the most popular trips?')
        p(top_connections)
        p('Please note that count is independent of the directions.\n')
    
        p("That took %s seconds." % (time.time() - start_time))
        wait_dummy = input('\nPress key to continue ...')
        p("Calculating the next statistic...")


    # What are the counts of each user type?   
    if time_period == 'none' or time_period == 'month' or time_period == 'day':     
        start_time = time.time()
 
        # TODO: call users function and print the results
        users_count = get_users(data,month,week_day)
        users_count_sort = first_n(users_count,len(users_count),False,True,True)
    
        p('\nWhat are the counts of each user type?')
        p(users_count_sort)
    
        p("That took %s seconds." % (time.time() - start_time))
        wait_dummy = input('\nPress key to continue ...')
        p("Calculating the next statistic...")
        
    # What are the counts of gender?
    if (time_period == 'none' and not city_name =='washington'):     
        start_time = time.time()
        
        # TODO: call gender function and print the results
        gender_count = get_gender(data,month,week_day)
        gender_count_sort = first_n(gender_count,len(gender_count),False,True,True)
    
        p('\nWhat are the counts of gender?')
        p(gender_count_sort)
    
        p("That took %s seconds." % (time.time() - start_time))
        wait_dummy = input('\nPress key to continue ...')
        p("Calculating the next statistic...")
    
    
    if time_period == 'none' and city_name !='washington':     
        start_time = time.time()
        
        # TODO: call birth_years function and print the results
        age_count = get_age(data,month,week_day)
        oldest = first_n(age_count,5,True,True,True)
        youngest = first_n(age_count,5,True,False,True)
        current_year = datetime.now().year
        avg_age = get_mean([ (current_year - int(float(row['Birth Year']))) for row in data if row['Birth Year'] != "" ])

        p('\n\nmaybe some data quality issues ...')  
        p('\nLooking at age of users (age / count): ')
        p('\nOldest:')
        p(oldest)
        p('\nYoungest:')
        p(youngest)
        p('\nAverage Age {:.0f}:'.format(avg_age))
            
        p("That took %s seconds." % (time.time() - start_time))
        p("See the age distribution by gender:" )
        wait_dummy = input('\nPress key to continue ...')
        
        #ignores non-numbers: lstrip('-').replace('.','',1).isdigit()
        birth_year_list_men = [ (current_year - int(float(row['Birth Year']))) 
                                   for row in data if row['Gender'] == "Male" 
                                   and row['Birth Year'].lstrip('-').replace('.','',1).isdigit() ]
        
        birty_year_list_women = [ (current_year - int(float(row['Birth Year']))) 
                                       for row in data if row['Gender'] == "Female" 
                                       and row['Birth Year'].lstrip('-').replace('.','',1).isdigit() ]

        fig = plt.figure(figsize=(8,4))
        plt.hist(x=birth_year_list_men, normed=True,bins=range(0,100,5), alpha=0.5, label='Male')
        plt.hist(x=birty_year_list_women, normed=True, bins= range(0,100,5), alpha=0.5, label='Female')
        plt.xticks(range(0,100,5))
        plt.legend(loc='upper right')
        plt.show()
        
        wait_dummy = input('\nPress key to continue ...')
        #p("Calculating the next statistic...")
 

    # Display five lines of data at a time if user specifies that they would like to
    display_data(data)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        calculate_statistics()



if __name__ == "__main__":
	calculate_statistics()
	
	