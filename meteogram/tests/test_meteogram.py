"""Test use of the meteogram module."""
import datetime

from meteogram import meteogram
from numpy.testing import assert_almost_equal

#
# Example starter test
#
def test_degF_to_degC_at_freezing():
    """
    Test if celsius conversion is correct at freezing.
    """
    # Setup
    freezing_degF = 32.0
    freezing_degC = 0.0

    # Exercise
    result = meteogram.degF_to_degC(freezing_degF)

    # Verify
    assert result == freezing_degC

    # Cleanup - none necessary

#
# Instructor led introductory examples
#

def test_title_case():
    # Setup
    in_string = 'this is a test string'
    desired = 'This Is A Test String'

    # Exercise
    actual = in_string.title()

    # Verify
    assert actual == desired

    # Cleanup - none necessary


#
# Instructor led examples of numerical comparison
#

#
# Exercise 1
#
def test_build_asos_request_url_single_digit_datetimes():
    # Setup
    start = datetime.datetime(2021, 1, 1, 1)
    end = datetime.datetime(2021, 1, 5, 1)
    station = 'FSD'

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    truth_url = 'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2021&month1=01&day1=01&hour1=01&minute1=00&year2=2021&month2=01&day2=05&hour2=01&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes'
    assert result_url == truth_url

    # Cleanup - none

    pass


def test_build_asos_request_url_double_digit_datetimes():
    # Setup
    start = datetime.datetime(2021, 11, 11, 11)
    end = datetime.datetime(2021, 11, 15, 11)
    station = 'FSD'

    # Exercise
    result_url = meteogram.build_asos_request_url(station, start, end)

    # Verify
    truth_url = 'https://mesonet.agron.iastate.edu/request/asos/1min_dl.php?station%5B%5D=FSD&tz=UTC&year1=2021&month1=11&day1=11&hour1=11&minute1=00&year2=2021&month2=11&day2=15&hour2=11&minute2=00&vars%5B%5D=tmpf&vars%5B%5D=dwpf&vars%5B%5D=sknt&vars%5B%5D=drct&sample=1min&what=view&delim=comma&gis=yes'
    assert result_url == truth_url

    # Cleanup - none

    pass

#
# Exercise 1 - Stop Here
#

def test_does_three_equal_three():
    assert 3 == 3

def test_floating_substraction():
    # Setup
    desired = 0.294

    # Exercise
    actual = 1 - 0.706

    # Verify
    # assert abs(actual-desired) < 0.00001
    assert_almost_equal(actual, desired, 6)

    # Cleanup - none

#
def test_vector_components_of_wind_direction_0_degree():
    # Setup
    desired = 0, -100
    # Exercise
    actual = meteogram.wind_components(100, 0)

    # Verify
    assert_almost_equal(actual, desired, 6)
    # Cleanup

def test_vector_components_of_wind_direction_45_degree():
    # Setup
    desired = -85.090352, -52.532198

    # Exercise
    actual = meteogram.wind_components(100, 45)

    # Verify
    assert_almost_equal(actual, desired, 6)

    # Cleanup

def test_vector_components_of_wind_direction_360_degree():
    # Setup
    desired = -95.891572, 28.369109

    # Exercise
    actual = meteogram.wind_components(100, 360)

    # Verify
    assert_almost_equal(actual, desired, 6)

    # Cleanup

def test_vector_components_of_wind_direction_0_speed():
    # Setup
    desired = 0, 0

    # Exercise
    actual = meteogram.wind_components(0, 45)

    # Verify
    assert_almost_equal(actual, desired)

    # Cleanup

#
# Exercise 2 - Stop Here
#

#
# Instructor led mock example
#

#
# Exercise 3
#

#
# Exercise 3 - Stop Here
#

#
# Exercise 4 - Add any tests that you can to increase the library coverage.
# think of cases that may not change coverage, but should be tested
# for as well.
#

#
# Exercise 4 - Stop Here
#

#
# Instructor led example of image testing
#

#
# Exercise 5
#

#
# Exercise 5 - Stop Here
#

#
# Exercise 6
#

#
# Exercise 6 - Stop Here
#

#
# Exercise 7
#

#
# Exercise 7 - Stop Here
#

# Demonstration of TDD here (time permitting)
