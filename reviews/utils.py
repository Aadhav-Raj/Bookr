def average_rating(rating_list):
    if not rating_list:
        return 0

    return round(sum(rating_list) / len(rating_list))

import time
class  timezone:
    def now(self):
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        return curr_time



