# 19. Write a program to create the power set of a given set.
def power_set(s):
    """Generate the power set of the given set s."""
    power_set_list = [[]]
    for elem in s:
        power_set_list += [curr + [elem] for curr in power_set_list]
    return [set(subset) for subset in power_set_list]
given_set = {1, 2, 3}
result = power_set(given_set)
print("Power set of", given_set, "is:")
for subset in result:
    print(subset)

    
