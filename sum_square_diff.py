sum_of_squares = 0

for i in range(1,101):
    sum_of_squares = sum_of_squares + i*i

summ = sum(range(1,101))
square_of_sum = summ * summ

print(square_of_sum - sum_of_squares)
