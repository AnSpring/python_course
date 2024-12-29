# importing random and string to create random keys and values
import random
import string

# set the random generated values not changeable
random.seed(42)

#create an empty list where we will add random keys and values
list_of_dicts = []
# create a loop to run 3 times and create 3 different dicts
for i in range(3):
    # create an empty dict
    new_dict = {}
    # create a loop to run 5 times and add 5 keys and values in each dict
    for i in range(5):
        key = random.choice(string.ascii_lowercase) # adding random characters as a key
        value = random.randint(0, 100) # adding random numbers as a value
        new_dict[key] = value
    list_of_dicts.append(new_dict) # adding these values in list_of_dicts
print(list_of_dicts) # print in the console

# combining dictionaries
combined_dict = {} # empty dict is created where each letter will create a list with number of dict and value
# i - the amount of iterations through which the loop will run
for i in range(len(list_of_dicts)):
    current_dict = list_of_dicts[i]
    for k, v in current_dict.items(): # returning key and value for each dict
        # if there's no key we create a record
        if k not in combined_dict:
                combined_dict[k] = [[i + 1, v]] # add the list with number of dict and value
        else:
                combined_dict[k].append([i + 1, v]) # if the key exists - adding a new record
print(combined_dict) #print whole combined dict in the console

# create empty dict
final_dict = {}
# run the loop through key-value from the combined_dict
for k, v in combined_dict.items():
    # if the key has only one value
    if len(v) == 1:
        final_dict[k] = v[0][1] # add this value to the final_dict
    else:
        # and finding the max value
        max_value = v[0] # from the beginning our first value is a max
        for i in v: # run the loop through the values
            if i[1] > max_value[1]: # compare the current values
                max_value = i # and if we have another one bigger value - update it
        final_dict[k + '_' + str(max_value[0])] = max_value[1] # form a new key with position and record a max value
print(final_dict) #print our dict in the console

