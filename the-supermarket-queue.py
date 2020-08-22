def queue_time(customers, n):
    count = 0
    while len(customers) >= n:
        for i in range(n):
            if customers[i] > 0: customers[i] -= 1
        customers = list(filter(lambda a: a > 0, customers))
        count += 1

    while len(customers) != 0:
        for i in range(len(customers)):
            if customers[i] > 0: customers[i] -= 1
        customers = list(filter(lambda a: a > 0, customers))
        count += 1

    return count


print(queue_time([1,2,3,4,5], 2))