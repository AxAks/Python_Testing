"""
File for Unit Tests in route purchase_places
"""
import pytest

from libs.lib_purchase_places import extract_club_name, extract_competition_name, extract_required_places, \
    check_competition_places, check_club_points, check_required_places_amount, check_booking_possible, book_places, \
    convert_competition_places_to_int, convert_club_points_to_int


def test_an_entered_competition_name_should_return_a_string(test_future_competition):
    """
    Checks that the input is a valid string
    """
    form = {'competition_name': test_future_competition['name']}
    assert 'competition_name' in form.keys()
    assert isinstance(extract_competition_name(form), str)


def test_an_empty_competition_name_should_return_an_empty_string():
    """
    Checks that the input is a valid string
    """
    form = {'competition_name': ''}
    assert 'competition_name' in form.keys()
    assert extract_competition_name(form) == ''


def test_a_converted_competition_places_should_return_a_int(test_future_competition):
    """
    Checks that the input can be converted into an integer
    """
    competition_places = test_future_competition['number_of_places']
    assert isinstance(convert_competition_places_to_int(competition_places), int)


def test_a_converted_competition_places_should_raise_value_error_if_empty():
    """
    Checks that the input can be converted into an integer
    """
    competition_places = ''
    with pytest.raises(ValueError):
        assert convert_competition_places_to_int(competition_places)


def test_a_converted_competition_places_should_raise_value_error_if_negative():
    """
    Checks that the input can be converted into an integer
    """
    competition_places = '0'
    with pytest.raises(ValueError):
        assert convert_competition_places_to_int(competition_places)


def test_a_converted_club_points_should_return_a_int(test_club):
    """
    Checks that the input can be converted into an integer
    """
    club_points = test_club['points']
    assert isinstance(convert_club_points_to_int(club_points), int)


def test_a_converted_club_points_should_raise_value_error_if_empty():
    """
    Checks that the input can be converted into an integer
    """
    club_points = ''
    with pytest.raises(ValueError):
        assert convert_club_points_to_int(club_points)


def test_a_converted_club_points_should_raise_value_error_if_negative():
    """
    Checks that the input can be converted into an integer
    """
    club_points = '0'
    with pytest.raises(ValueError):
        assert convert_club_points_to_int(club_points)


def test_enough_places_in_competition_should_return_true():
    places_required_as_int = 6
    total_places_in_competition_as_int = 25
    assert check_competition_places(places_required_as_int, total_places_in_competition_as_int) is True


def test_not_enough_places_in_competition_should_return_false():
    places_required_as_int = 26
    total_places_in_competition_as_int = 25
    assert check_competition_places(places_required_as_int, total_places_in_competition_as_int) is False


def test_enough_points_for_club_should_return_true():
    places_required_as_int = 13
    total_club_points_as_int = 13
    assert check_club_points(places_required_as_int, total_club_points_as_int) is True


def test_not_enough_points_for_club_should_return_false():
    places_required_as_int = 14
    total_club_points_as_int = 13
    assert check_club_points(places_required_as_int, total_club_points_as_int) is False


def test_an_entered_club_name_should_return_a_string(test_club):
    """
    Checks that the input is a valid string
    """
    form = {'club_name': test_club['name']}
    assert 'club_name' in form.keys()
    assert isinstance(extract_club_name(form), str)


def test_an_empty_club_name_should_return_an_empty_string():
    """
    Checks that the input is a valid string
    """
    form = {'club_name': ''}
    assert 'club_name' in form.keys()
    assert extract_club_name(form) == ''




def test_an_entered_amount_of_places_should_return_a_int():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': '2'}
    assert 'places' in form.keys()
    assert isinstance(extract_required_places(form), int)


def test_an_empty_amount_of_places_should_raise_a_value_error():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': ''}
    assert 'places' in form.keys()
    with pytest.raises(ValueError):
        extract_required_places(form)


def test_a_negative_amount_of_places_should_raise_a_value_error():
    """
    Checks that the input can be converted into an integer
    """
    form = {'places': '0'}
    assert 'places' in form.keys()
    with pytest.raises(ValueError):
        extract_required_places(form)


def test_places_required_below_limit_should_return_true():
    """

    """
    places_required_as_int = 12
    limit = 12
    assert check_required_places_amount(places_required_as_int, limit) is True


def test_places_required_above_limit_should_return_false():
    """

    """
    places_required_as_int = 13
    limit = 12
    assert check_required_places_amount(places_required_as_int, limit) is False


def test_places_ok_points_ok_competition_date_ok_places_below_limit_ok_should_return_true():
    """
    Must return True when every argument is true
    """
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = True
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is True


def test_places_ok_points_ok_competition_date_nok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true but competition date
    """
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = False
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_nok_competition_date_ok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true but amount of club points
    """
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = True
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_ok_competition_date_ok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true but amount of available places in competition
    """
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = True
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_nok_competition_date_ok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true except:
     - amount of club points
     - amount of available places in competition
    """
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = True
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_ok_competition_date_nok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true except:
     - amount of available places in competition
     - valid competition date
    """
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = False
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_nok_competition_date_nok_places_below_limit_ok_should_return_false():
    """
    Must return false when every argument is true except:
     - amount of club points
     - valid competition date
    """
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = False
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_nok_competition_date_nok_places_below_limit_ok_should_return_false():
    """
    Must return false when only the argument in limitation in places requested is true
    """
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = False
    places_required_is_below_limit = True
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_ok_competition_date_ok_places_below_limit_nok_should_return_false():
    """
    Must return false when every argument is true except:
     - the limitation in places requested
    """
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = True
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_ok_competition_date_nok_places_below_limit_nok_should_return_false():
    """
    Must return false when every argument is true except:
    - valid competition date
    - the limitation in places requested
    """
    has_enough_places = True
    has_enough_points = True
    competition_is_in_the_future = False
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_nok_competition_date_ok_places_below_limit_nok_should_return_false():
    """
    Must return false when every argument is true except:
    - clubs points
    - the limitation in places requested
    """
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = True
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_ok_competition_date_ok_places_below_limit_nok_should_return_false():
    """
    Must return false when every argument is true except:
    - available places in competition
    - the limitation in places requested
    """
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = True
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_nok_competition_date_ok_places_below_limit_nok_should_return_false():
    """
    Must return false when only the argument of competition date is true
    """
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = True
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_ok_competition_date_nok_places_below_limit_nok_should_return_false():
    """
    Must return false when only the argument in clubs points is true
    """
    has_enough_places = False
    has_enough_points = True
    competition_is_in_the_future = False
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_ok_points_nok_competition_date_nok_places_below_limit_nok_should_return_false():
    """
    Must return false when only the argument in available places in competition is true
    """
    has_enough_places = True
    has_enough_points = False
    competition_is_in_the_future = False
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_places_nok_points_nok_competition_date_nok_places_below_limit_nok_should_return_false():
    """
    Must return false when all arguments are false
    """
    has_enough_places = False
    has_enough_points = False
    competition_is_in_the_future = False
    places_required_is_below_limit = False
    assert check_booking_possible(has_enough_places, has_enough_points,
                                  competition_is_in_the_future, places_required_is_below_limit) is False


def test_book_places(test_club, test_future_competition, test_required_places_6):
    """
    cas nominal
    """
    total_places_as_int = 18
    needed_amount_of_points = 18
    total_points_as_int = 20
    updated_club, updated_competition = book_places(test_club, test_future_competition,
                                                    test_required_places_6, total_places_as_int,
                                                    needed_amount_of_points, total_points_as_int)
    assert updated_club['points'] == 0
    assert updated_competition['places'] == 14


def test_book_places_error(test_club, test_future_competition, test_required_places_6):
    """
    cas d'erreur 1 a faire
    """
    return True is False
