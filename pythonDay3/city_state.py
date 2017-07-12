dict={'pune':'maharashtra', 'hyderabad':'telangana', 'chennai':'tamilnadu'}
#print(dict[raw_input("Enter a city to know the state in which city is located: ")])
inv_dict=dict(zip(dict.values(), dict.keys()))
#inv_dict = {v: k for k, v in dict.iteritems()}
print(inv_dict[raw_input("Enter a state to know the city located in it: ")])