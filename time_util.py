"""
Some simple time math stuff
"""

import argparse
import arrow


def main():
    """Main function"""
    args = _get_args()
    args.func(args)
# End def


def _get_args():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('start_date')
    add_parser.add_argument('addend', type=int)
    add_parser.add_argument('unit')
    add_parser.set_defaults(func=_add_date)

    delta_parser = subparsers.add_parser('delta')
    delta_parser.add_argument('start_date')
    delta_parser.add_argument('end_date')
    delta_parser.set_defaults(func=_delta_date)

    epoch_2_human_parser = subparsers.add_parser('epoch2human')
    epoch_2_human_parser.add_argument('timestamp')
    epoch_2_human_parser.add_argument('-t', '--timezone')
    epoch_2_human_parser.set_defaults(func=_epoch_2_human)

    human_2_epoch_parser = subparsers.add_parser('human2epoch')
    human_2_epoch_parser.add_argument('date')
    human_2_epoch_parser.set_defaults(func=_human_2_epoch)

    yesterday_parser = subparsers.add_parser('yesterday')
    yesterday_parser.add_argument('-t', '--timezone')
    yesterday_parser.set_defaults(func=_yesterday)

    return parser.parse_args()
# End def


def _add_date(args):
    add_date(args.start_date, args.unit, args.addend)
# End def


def add_date(start_date, unit, addend):
    """
    Find the date so many days into the future
    """

    if unit == 'days':
        print arrow.get(start_date).replace(days=addend)
    elif unit == 'months':
        print arrow.get(start_date).replace(months=addend)
    elif unit == 'years':
        print arrow.get(start_date).replace(years=addend)
    else:
        print 'ERROR: Do not recognise unit {}'.format(unit)

# End def


def _delta_date(args):
    delta_date(args.start_date, args.end_date)
# End def


def delta_date(start, end):
    """
    Find the number of days between two dates
    """
    print arrow.get(end) - arrow.get(start)
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
        print date.to(timezone)
    else:
        print date
    # End if/else
# End def

def _human_2_epoch(args):
    human_2_epoch(args.date)
# End def

def human_2_epoch(date):
    """
    Convert human readable to epoch
    """
    print arrow.get(date).format('X')
# End def

def _yesterday(args):
    yesterday(args.timezone)
# End def

def yesterday(timezone=None):
    """
    Get the timestamp for the start and end of yesterday
    """
    print arrow.now(timezone).floor('day').replace(days=-1).format('X')
    print arrow.now(timezone).floor('day').format('X')

if __name__ == '__main__':
    main()
# End if
