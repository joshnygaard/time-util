"""
Some simple time operations that I frequently use
"""

import argparse

import arrow

def main():
    """Main function"""
    args = _get_args()
    args.func(args)
# End def

def _get_args():
    parser = argparse.ArgumentParser(description='Some simple time operations')

    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser('add', help='Find the date a given number of days/months/years from a given date')
    add_parser.add_argument('start_date', help='Date to start counting. Date must be in ISO 8601 format, or "today" for the current, local date.')
    add_parser.add_argument('addend', type=int, help='Number of days/months/years')
    add_parser.add_argument('unit', choices=['days', 'months', 'years'], help='Unit')
    add_parser.set_defaults(func=_add_date)

    delta_parser = subparsers.add_parser('delta', help='Find the number of days between two dates')
    delta_parser.add_argument('date_1', help='First date. Date must be in ISO 8601 format, or "today" for the current, local date')
    delta_parser.add_argument('date_2', help='Second date. Date must be in ISO 8601 format, or "today" for the current, local date')
    delta_parser.set_defaults(func=_delta_date)

    epoch_2_human_parser = subparsers.add_parser('epoch2human', help='Convert epoch timestamp to human readable format')
    epoch_2_human_parser.add_argument('timestamp', help='Unix epoch timestamp in either milliseconds or seconds')
    epoch_2_human_parser.add_argument('-t', '--timezone', help='Timezone by name or tzinfo. The local timezone is the default')
    epoch_2_human_parser.set_defaults(func=_epoch_2_human)

    human_2_epoch_parser = subparsers.add_parser('human2epoch', help='Convert a human readable time to a Unix timestamp (in seconds)')
    human_2_epoch_parser.add_argument('date', help='Date to convert. Date must be in ISO 8601 format, or "today" for the current, local date.')
    human_2_epoch_parser.set_defaults(func=_human_2_epoch)

    yesterday_parser = subparsers.add_parser('yesterday', help='Return Unix timestamp of the beginning and end of yesterday')
    yesterday_parser.add_argument('-t', '--timezone', help='Timezone by name or tzinfo. The local timezone is the default')
    yesterday_parser.set_defaults(func=_yesterday)

    return parser.parse_args()
# End def

def _parse_date(date):
    if date == 'today':
       date = arrow.now().floor('day')
    # End if
    else:
        date = arrow.get(date)
    # end if/else

    return date
# End def

def _add_date(args):
    add_date(args.start_date, args.unit, args.addend)
# End def

def add_date(start, unit, addend):
    """
    Find the date so many days/months/years into the future from the given date
    """

    start = _parse_date(start)

    if unit == 'days':
        print(start.replace(days=addend))
    elif unit == 'months':
        print(start.replace(months=addend))
    elif unit == 'years':
        print(start.replace(years=addend))
    else:
        print('ERROR: Do not recognise unit {}'.format(unit))
    # End if/else

# End def


def _delta_date(args):
    delta_date(args.date_1, args.date_2)
# End def


def delta_date(start, end):
    """
    Find the number of days between two dates
    """
    start = _parse_date(start)
    end = _parse_date(end)

    print(abs(end - start))
# End def

def _epoch_2_human(args):
    epoch_2_human(args.timestamp, args.timezone)
# End def

def epoch_2_human(timestamp, timezone=None):
    """
    Convert epoch to human readable
    """
    date = arrow.get(timestamp)

    if timezone:
        print(date.to(timezone))
    else:
        print(date)
    # End if/else
# End def

def _human_2_epoch(args):
    human_2_epoch(args.date)
# End def

def human_2_epoch(date):
    """
    Convert human readable to epoch
    """
    print(arrow.get(_parse_date(date)).format('X'))
# End def

def _yesterday(args):
    yesterday(args.timezone)
# End def

def yesterday(timezone=None):
    """
    Get the timestamp for the start and end of yesterday
    """
    print(arrow.now(timezone).floor('day').replace(days=-1).format('X'))
    print(arrow.now(timezone).floor('day').format('X'))
# End def

if __name__ == '__main__':
    main()
# End if
