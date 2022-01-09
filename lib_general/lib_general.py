"""
Temp Lib for functions that need to be sorted
"""
from datetime import datetime, timedelta


def is_email_blank(email):
    """
    Checks an email address has been entered
    """
    return email == ''


def check_competition_date(competition_date, now=datetime.now()):
    """
    Checks that the competition is in the future
    """
    return competition_date - now > timedelta(0)


def check_competition_places(places_required_as_int, total_places_as_int):
    """
    Compares the requested amount of places for a competition
    with the available amount of places remaining
    """
    return total_places_as_int - places_required_as_int >= 0


def check_club_points(places_required_as_int, total_points_as_int):
    """
    Compares the requested amount of places for a competition
    with the number of points the club has
    """
    return total_points_as_int - places_required_as_int >= 0


def check_required_places_amount(places_required_as_int, limit=12):
    """
    Checks if the amount of places desired is below the max limit allowed
    """
    return places_required_as_int <= limit


def check_booking_possible(has_enough_places, has_enough_points,
                           competition_is_in_the_future, places_required_is_below_limit):
    """
    Checks if the booking of a competition made by a club is possible
    """
    return has_enough_places and has_enough_points and competition_is_in_the_future and places_required_is_below_limit