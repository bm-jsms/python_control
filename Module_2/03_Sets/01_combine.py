my_first_set = {1, 2, 3, 4, 5}
my_second_set = {3, 4, 5, 6, 7}

intersection_set = my_first_set.intersection(my_second_set)
union_set = my_first_set.union(my_second_set)
subset_set = my_first_set.issubset(my_second_set)
diferece_set = my_first_set.difference(my_second_set)


print(intersection_set)  # {3, 4, 5}
print(union_set)  # {1, 2, 3, 4, 5, 6, 7}
print(subset_set)  # False
print(diferece_set)  # {1, 2}
