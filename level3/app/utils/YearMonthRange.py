from dataclasses import dataclass
from app.utils.YearMonth import YearMonth

# This describes a range between two YearMonth
# start and end are included in the range
# eq and frozen are required for the class to be hashable
@dataclass(eq = True, frozen = True)
class YearMonthRange:
    start: YearMonth
    end: YearMonth

    def __post_init__(self):

        if not (self.start <= self.end):
            raise ValueError("Range is empty")
        
    def size(self):

        # A bit of arithmetic here, but better than iterating through the range
        # Don't forget that start and end are included in the range
        return (self.end.year - self.start.year) * 12 + self.end.month - self.start.month + 1
    
    # This is a generator that iterates through all YearMonth between start and end, in chronological order
    def iterate(self):

        currentYearMonth = self.start

        while currentYearMonth <= self.end:

            yield currentYearMonth
            currentYearMonth = currentYearMonth.next()

    # Quarters are between 1 and 4
    def fromQuarter(year, quarter):

        startMonth = (quarter - 1) * 3 + 1
        endMonth = startMonth + 2

        return YearMonthRange(YearMonth(year, startMonth), YearMonth(year, endMonth))