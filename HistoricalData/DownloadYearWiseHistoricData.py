from datetime import date
from jugaad_data.nse import bhavcopy_save


# Making all necessary imports for the code
from datetime import date
from jugaad_data.nse import bhavcopy_save

import pandas as pd
from jugaad_data.holidays import holidays
from random import randint
import time, os

# Change the range of the dates for one year each
# Date should be specified in the format of MM/DD/YYYY
date_range = pd.bdate_range(start='01/01/2019', end='12/31/2019',
                            freq='C', holidays=holidays(2019))

savepath = os.path.join('C:', os.sep, "C:\\Users\\rocks\\Documents\\Stocks\\Archive\\2019\\")

# start and end dates in "MM-DD-YYYY" format
# holidays() function in (year,month) format
# freq = 'C' is for custom

dates_list = [x.date() for x in date_range]
# print(dates_list)

for dates in dates_list:
    try:
        bhavcopy_save(dates, savepath)
        print(dates)
        time.sleep(randint(1, 4))  # adding random delay of 1-4 seconds
    except (ConnectionError, ReadTimeoutError) as e:
        time.sleep(60)  # stop program for 10 seconds and try again.
        try:
            bhavcopy_save(dates, savepath)
            time.sleep(randint(1, 5))
        except (ConnectionError, ReadTimeoutError) as e:
            print(f'{dates}: File not Found')