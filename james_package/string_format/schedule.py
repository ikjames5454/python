exam_st_date = '11, 12, 2014'

day,month,year = exam_st_date.split(',')
formatted = f"{day}/{month}/{year}"
print(formatted)