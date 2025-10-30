# Task 2

class Mathematician:

    def square_nums(self, nums):
        return [num**2 for num in nums]

    def remove_positives(self, nums):
        negative_numbers = []
        for num in nums:
            if num < 0 :
                negative_numbers.append(num)
        return negative_numbers

    def filter_leaps(self, years):
        leaps_years = []
        for year in years:
        # піддивилася умови як вираховувати математично високосні роки
            if (year % 4 == 0 and year % 100 != 0) or (year %400 == 0) :
                leaps_years.append(year)
        return leaps_years

m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

