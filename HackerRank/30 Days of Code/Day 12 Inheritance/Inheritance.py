# Project name : HackerRank: Day 12: Inheritance
# Link         : https://www.hackerrank.com/challenges/30-inheritance/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-30
# Description  :
# Status       : Accepted (166469429)
# Tags         : python
# Comment      : 

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, first_name, last_name, id_num, scores):
        super().__init__(first_name, last_name, id_num)
        self.scores = scores
    
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg_score = sum(self.scores)/len(self.scores)
        if avg_score >= 90:
            return 'O'
            
        if avg_score >= 80:
            return 'E'

        if avg_score >= 70:
            return 'A'

        if avg_score >= 55:
            return 'P'

        if avg_score >= 40:
            return 'D'

        return 'T'

line = input().split()