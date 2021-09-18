#Very basic OOP quiz:

#1:
#Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object. 
#The values of these attributes can be easily changed at the object level.  The following code illustrates a famous quote by 
#George Bernard Shaw, using objects to represent people. Fill in the blanks to make the code satisfy the behavior described in the 
#quote. 

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1


martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       
#different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
    you.apples, me.apples = me.apples, you.apples
    return you.apples, me.apples

def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    you.ideas += me.ideas
    me.ideas = you.ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


#2:
#The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), 
#and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function to 
#return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified 
#minimal population. For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) 
#should return "Sofia, Bulgaria". 

class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052


city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675


city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
	return_city = City()

	if city1.population >= min_population and city1.elevation > return_city.elevation:
		return_city = city1

	if city2.population >= min_population and city2.elevation > return_city.elevation:
		return_city = city2

	if city3.population >= min_population and city3.elevation > return_city.elevation:
		return_city = city3

	if return_city.name:
		return "{}, {}".format(return_city.name, return_city.country)
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""


#3:
#We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation 
#of each Furniture class instance, so that the describe_furniture function can format a sentence that describes these 
#pieces as follows: "This piece of furniture is made of {color} {material}"
class Furniture:
    color = ""
    material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"