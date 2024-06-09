import datetime

def now() :
    return datetime.datetime.now()

now()
print( now() )

date_without_time = datetime.datetime( 2020, 11, 23 )
date_without_time
print( date_without_time )

sunday_afternoon = datetime.datetime( 2021, 6, 13, 16, 52, 59 )
print( 'Year:', sunday_afternoon.year )
print( 'Month:', sunday_afternoon.month )
print( 'Day:', sunday_afternoon.day )
# and on, hour, minute, second, timestamp

print( 'Hour:', sunday_afternoon.hour )
print( 'Minute:', sunday_afternoon.minute )
print( 'Second:', sunday_afternoon.second )
print( 'Timestamp:', sunday_afternoon.timestamp() )

datetime_from_timestamp = datetime.datetime.fromtimestamp( 43211234 )
print( 'Datetime:', datetime_from_timestamp )

def today() :
    return datetime.date.today()

today()
print( today() )
# use print to display the datetime object in ISO standard

birthday_Sophie = datetime.date( 2020, 11, 23 )
print( birthday_Sophie )
birthday_Evelyn = datetime.date.fromisoformat( '1984-02-10' )

today_ = today()
print( 'Current year {}, month {}, day {}.'.format( today_.year, today_.month, today_.day ) )

def get_weekday( date ) :
    return date.strftime( '%A' )

get_weekday( datetime.date( 1971, 2, 7 ) )
get_weekday( datetime.date( 1979, 7, 14 ) )

# date.weekday() returns 0 to 6 for Monday to Sunday
# date.isoweekday() returns 1 to 7 for Monday to Sunday

birthday_Evelyn.weekday()
birthday_Evelyn.isoweekday()

def day_of_month( date ) :
    return date.day

day_of_month( datetime.date( 1971, 2, 7 ) )

def day_of_year( date ) :
    return date.timetuple().tm_yday

day_of_year( datetime.date( 1996, 10, 8 ) )
test = int( day_of_year( datetime.date( 1996, 10, 8 ) ) )

date_from_timestamp = datetime.date.fromtimestamp( 43211234 )
print( 'Date from timestamp:', date_from_timestamp )

today_ = datetime.date.fromisoformat( '2022-07-14' )
today_.toordinal()

year_10 = datetime.date.fromisoformat( '0010-07-14' )
# is that sensible, there was another calendar back then?
year_10.toordinal()

datetime.date.fromordinal( 750_000 ) # year 2054

now_time = datetime.datetime.now().time()
print( now_time )
print( type( now_time ) )

datetime.time()

datetime.time( 11, 28, 45 )
datetime.time( 11, 28, 45, 6789 )

print( datetime.time( 11, 28, 33 ) )

time_lunch = datetime.time( 12, 35, 00 )
print( 'Lunch is at {} hours and {} minutes.'.format( time_lunch.hour, time_lunch.minute ) )

start = datetime.datetime( 2021, 2, 7, 10, 10, 10 )
end = datetime.datetime( 2021, 2, 8, 11, 12, 13 )
end - start

timedelta1  = datetime.timedelta( weeks = 2, days = 3, hours = 5, seconds = 6 )
timedelta2 = datetime.timedelta( days = 7, hours = 8, minutes = 9, seconds = 10 )
timedelta3 = timedelta1 - timedelta2
timedelta3

t1 = datetime.timedelta( seconds = 33 )
t2 = datetime.timedelta( seconds = 54 )
diff1 = t1 - t2 # returns -1 day etc
diff2 = t2 - t1 # returns 21 seconds, how is this defined?
sum = t1 + t2 

diff1 
diff2
sum 
diff2 * 5
diff2 / 2 

today = today()
print( today + datetime.timedelta( weeks = 8, days = 2 ) )

print( datetime.date.fromisoformat( '2013-03-01' ) - datetime.date.fromisoformat( '2013-02-01' ) ) # normal year
print( datetime.date.fromisoformat( '2012-03-01' ) - datetime.date.fromisoformat( '2012-02-01' ) ) # leap year

def days_in_a_month( month, year ) :
    start = datetime.date( year, month, 1 )
    month += 1
    if month > 12 :
        month = 1
        year += 1
    
    end = datetime.date( year, month, 1 )
    return (end - start).days

days_in_a_month( 2, 2013 )
days_in_a_month( 2, 2020 )

def days_in_a_year( year ) :
    start = datetime.date( year, 1, 1 )
    end = datetime.date( year + 1, 1, 1 )
    return (end-start).days

print( days_in_a_year( 2013 ) )
print( days_in_a_year( 2020 ) ) 

import calendar

calendar.isleap( 2020 )
calendar.isleap( 2013 )

now_ = now()
print( now_.strftime( '%H:%M:%S' ) )
print( now_.strftime( '%d.%m.%Y, %H:%M:%S') )

print( 'US:', now_.strftime( '%m/%d/%Y, %H:%M:%S') )
print( 'GB:', now_.strftime( '%d/%m/%Y, %H:%M:%S') )
print( 'GB:', now_.strftime( '%d/%B/%Y, %H:%M:%S') )

date_string = '14 July, 1979'
date_object = datetime.datetime.strptime( date_string, '%d %B, %Y' ) # strptime only for datetime, not date
print( date_object )

## FINISHED :-D