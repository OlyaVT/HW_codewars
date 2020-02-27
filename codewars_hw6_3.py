#remove time from date
def shorten_to_date(long_date):
    head, sep, tail = long_date.partition(',')
    return head