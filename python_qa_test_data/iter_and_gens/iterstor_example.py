from datetime import datetime, timedelta

from itertools_and_functools import start


class DateRangeIterator:
     def __init__(self, start_date, end_date, step_days=1):

         self.current_date = datetime.strptime(start_date, "%Y-%m-%d")
         self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
         self.step = timedelta(days=step_days)




     def __iter__(self):
         return self



     def __next__(self):
        if self.current_date > self.end_date:
            raise StopIteration
        result = self.current_date
        self.current_date += self.step
        return result.strftime("%Y-%m-%d")


start_date = '2023-01-01'
end_date = '2023-01-10'
step_days = 2


date_range_iterator = DateRangeIterator (start_date, end_date, step_days)
for date in date_range_iterator:
    print(date)