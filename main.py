#George is concerned with the inconsistent growth of his plant.
# He wants us to write a program to perform some simple analysis with him.

#a week passed and George gathered more data.
# He wants to combine the data from the 2 weeks to perform further analysis.

growth = [3, 1, 2, 4, 2, 3, 2]
growth.sort()

new_growth = [2, 0, 3, 2, 4, 5, 4]
joined_growth = growth + new_growth
joined_smallest_growth = min(joined_growth)
biggest_growth = growth[len(growth) - 1]
smallest_growth = growth[0]
average_growth = sum(growth) / len(growth)
joined_biggest_growth = max(joined_growth)
joined_average_growth = sum(joined_growth) / len(joined_growth)
joined_smallest_growth_count = joined_growth.count(joined_smallest_growth)
joined_biggest_growth_count = joined_growth.count(joined_biggest_growth)

print(f"The smallest growth in the week is: {smallest_growth}cm")
print(f"The biggest growth in the week is: {biggest_growth}cm")
print(f"The average growth in the week is: {average_growth}cm")
print(f'The smallest growth in these 2 weeks is: {joined_smallest_growth}cm')
print(f'The biggest growth in these 2 weeks is: {joined_biggest_growth}cm')
print(f'The average growth in these 2 weeks is: {joined_average_growth}cm')
print(f'The smallest growth happened {joined_smallest_growth_count} times in these 2 weeks')
print(f'The biggest growth happened {joined_biggest_growth_count} times in these 2 weeks')


