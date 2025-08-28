fav_movies = ["Sandlot", "Dune", "Batman", "Spider-Man"]

#print(fav_movies[2])

#Challenge: Make a list of your 3 favorite numbers and print the first number from your list

#fav_numbers = [7, 14, 21]
#print(fav_numbers[0])

print(len(fav_movies)) #Find the length of a list
fav_movies.append("Iron-Man") #Add an object to the end of the list

print(len(fav_movies)) 
print(fav_movies)

fav_movies.insert(1,"Batman") #locate the index, Insert the object
print(fav_movies)

del(fav_movies[1])
print(fav_movies)


#Challenge: Remove enough items from fav_movies until there's only one movie left
fav_movies.remove("Batman")
fav_movies.remove("Dune")
fav_movies.remove("Spider-Man")
print(fav_movies)