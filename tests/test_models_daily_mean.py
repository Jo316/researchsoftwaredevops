import pytest 
import datetime
import pandas as pd 
import pandas.testing as pdt 


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (
            pd.DataFrame(
                data=[ [0.0, 0.0], [0.0, 0.0], [0.0, 0.0] ],
                index=[ pd.to_datetime('2000-01-01 01:00'),
                        pd.to_datetime('2000-01-01 02:00'),
                        pd.to_datetime('2000-01-01 03:00') ],
                columns=[ 'A', 'B' ]
            ),
            pd.DataFrame(
               data=[ [0.0, 0.0] ],
               index=[ datetime.date(2000, 1, 1) ],
               columns=[ 'A', 'B' ]
            )
        ),
        (
            pd.DataFrame(
                data=[ [1, 2], [3, 4], [5, 6] ],
                index=[ pd.to_datetime('2000-01-01 01:00'),
                        pd.to_datetime('2000-01-01 02:00'),
                        pd.to_datetime('2000-01-01 03:00') ],
                columns=[ 'A', 'B' ],
            ),
            pd.DataFrame(
                data=[ [3.0, 4.0] ],
                index=[ datetime.date(2000, 1, 1) ],
                columns=[ 'A', 'B' ]
            )
        ),
    ])
def test_daily_mean(test_input, expected_output):
    """Test mean function works for array of zeroes and positive integers."""
    from catchment.models import daily_mean
    pdt.assert_frame_equal(daily_mean(test_input), expected_output)