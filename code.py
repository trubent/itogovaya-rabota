initial_array = ["Hello", "Hi", "a", "Sun", "world", "on", "off", "dog"]

new_array = [""] * len(initial_array)

count = 0

for string in initial_array:
    if len(string) <= 3:
        new_array[count] = string
        count += 1

new_array = new_array[:count]

print(new_array)