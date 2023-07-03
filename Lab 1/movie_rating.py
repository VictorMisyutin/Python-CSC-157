#**************************************************************************
# * Name: Victor Misyutin                                           CSC 157
# * Date: 3-6-2023                                                  LAB 1   
# *************************************************************************
# * Problem Statement and Specifications: 
# *     Given the title of a movie, its runtime, the ratings of the 
# *     movie in a focus group, ratings from a review website, and the 
# *     average rating from movie critics. Calculate the average
# *     rating on the website, in your focus group, and in total.
# *
# * Input: 
# *     Movie title,   
# *     run time,
# *     website ratings,
# *     focus group ratings,
# *     average movie critic rating
# * Output: 
# *     Movie title,   
# *     run time,
# *     average website rating,
# *     average focus group rating,
# *     average movie critic rating,
# *     overall movie rating
# *************************************************************************

# GET USER INPUT 
movieTitle = input("Please enter the movie name. \n")
runtime = int(input("Please enter the running time in minutes. \n"))
siteRating1 = int(input("Please enter ratings from the movie review website. \nFirst: "))
siteRating2 = int(input("Second: "))
siteRating3 = int(input("Third: "))
groupRating1 = float(input("Please enter ratings from the focus group.\nFirst: "))
groupRating2 = float(input("Second: "))
criticRating = float(input("Please enter the average movie critic rating. \n"))
# DO CALCULATIONS
runtimeMinutes = int(runtime%60)
runtimeHours =  int((runtime-runtimeMinutes)/60)
averageSiteRating = (siteRating1 + siteRating2 + siteRating3)/3
averageGroupRating = (groupRating1 +groupRating2)/2
overallAverage = round(averageSiteRating*0.2 + averageGroupRating*0.3 + criticRating*0.5)
# FORMAT RATINGS
averageSiteRatingFormatted = "{:.2f}".format(averageSiteRating)
averageGroupRatingFormatted = "{:.2f}".format(averageGroupRating)
# OUTPUT RESULUT
print(f"Title: {movieTitle}")
print(f"Running time: {runtimeHours}h{runtimeMinutes}")
print(f"Average website rating: {averageSiteRatingFormatted}")
print(f"Average focus group rating: {averageGroupRatingFormatted}")
print(f"Average movie critic rating: {criticRating}")
print(f"Overall movie rating: {overallAverage}")

