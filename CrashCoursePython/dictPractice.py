#1:
#The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. Fill in the 
#blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
    emails = []
    for email, users in domains.items():
        for user in users:
            emails.append(user + "@" + email)
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

#2:
#The groups_per_user function receives a dictionary, which contains group names with the list of users. Users can belong to multiple 
#groups. Write a function to return a dictionary with the users as keys and a list of their groups as values. 

def groups_per_user(group_dictionary):
    user_groups = {}
    
    for group, users in group_dictionary.items():
        for user in users:
            if user not in user_groups:
                user_groups[user] = [group]
            else:
                user_groups[user] += [group]

    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))


#3:
#The add_prices function returns the total price of all of the groceries in the  dictionary. 
#Create this function.

def add_prices(basket):
    total = 0

    for item in basket:
        total += basket[item]
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44