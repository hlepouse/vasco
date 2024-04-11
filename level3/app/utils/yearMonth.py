from dataclasses import dataclass
import os

# This describes a given year and month
@dataclass(eq = True, frozen = True)
class YearMonth:
    year: int
    month: int

    def __post_init__(self):

        if not (1 <= self.month <= 12):
            raise ValueError("Month must be between 1 and 12")
        
        if not (int(os.getenv('YEAR_MIN')) <= self.year <= int(os.getenv('YEAR_MAX'))):
            raise ValueError("Year must be between {} and {}".format(os.getenv('YEAR_MIN'), os.getenv('YEAR_MAX')))
        
    def __eq__(self, other):

        return self.year == other.year and self.month == other.month

    def __lt__(self, other):

        # In python, tuple comparison is by lexical order
        return (self.year, self.month) < (other.year, other.month)

    def __le__(self, other):

        # In python, tuple comparison is by lexical order
        return (self.year, self.month) <= (other.year, other.month)

    def previous(self):

        if self.month > 1:
            return YearMonth(self.year, self.month-1)
        
        return YearMonth(self.year-1, 12)
    
    def next(self):

        if self.month < 12:
            return YearMonth(self.year, self.month+1)
        
        return YearMonth(self.year+1, 1)

