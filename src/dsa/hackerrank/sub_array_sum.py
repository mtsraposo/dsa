def gen_cumulative_numbers(numbers):
    cumulative_numbers = []
    cum_sum = 0
    zeros_count = 0
    for number in numbers:
        cum_sum += number
        zeros_count += 1 if number == 0 else 0
        cumulative_numbers += [[cum_sum, zeros_count]]
    return cumulative_numbers


def findSum(numbers, queries):
    cum_numbers = gen_cumulative_numbers(numbers)
    sum_list = []
    for query in queries:
        index_start = query[0]-2
        index_end = query[1]-1

        sum_start = 0 if index_start < 0 else cum_numbers[index_start][0]
        subarray_sum = cum_numbers[index_end][0] - sum_start

        count_start = 0 if index_start < 0 else cum_numbers[index_start][1]
        zero_count = cum_numbers[index_end][1] - count_start
        zero_sum = query[2] * zero_count
        sum_list += [subarray_sum + zero_sum]
    return sum_list


numbers = [5, 10, 10, 0, 0]
queries = [[1, 2, 5]]

findSum(numbers, queries)
