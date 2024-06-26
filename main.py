# Reni Wu
# CS 333 Final Project
# April 27, 2024

from recipe import Recipe
from tests import Tests
from user import User
import unittest

def main():
    user = User()
    choice = 'a'
    print("Welcome to your recipe manager!\n")  
    while choice != '0':
        choice = input("(1) Access your pantry \n(2) Access your recipes \n(0) to quit\n")
        if choice == '1':
            pantryChoice = 'a'
            while pantryChoice != '0':
                pantryChoice = input("(1) View Your Pantry \n(2) Add To Your Pantry \n(3) Remove From Your Pantry \n(0) To Return to Main Menu \n")
                if pantryChoice == '1':
                    viewPantry(user)
                elif pantryChoice == '2':
                    addToPantry(user)
                elif pantryChoice == '3':
                    removeFromPantry(user)
        elif choice == '2': 
            recipeChoice = 'a'
            while recipeChoice != '0':
                print("Your Recipes: \n" + user.viewRecipes() + '\n')
                recipeChoice = input("(1) Add New Recipe \n(2) Edit Existing Recipe \n(3) Remove a Recipe \n(0) To Return to Main Menu \n")
                if recipeChoice == '1':
                    recipeName = input("What would you like to name your recipe? ")
                    user.addRecipe(recipeName)
                    addChoice = 'a'
                    while addChoice != '0':
                        addChoice = editRecipeMenu()
                        editMatch(addChoice, recipeName, user)                           
                elif recipeChoice == '2':
                    toEdit = input("Which recipe would you like to edit? ")
                    if user.hasRecipe(toEdit):
                        editChoice = 'a'
                        while editChoice != '0':
                            editChoice = editRecipeMenu()
                            editMatch(editChoice, toEdit, user)
                    else:
                        print("Recipe could not be found")
                elif recipeChoice == '3':
                    toRemove = input("Which recipe would you like to remove? ")
                    if not user.removeRecipe(toRemove):
                        print("Recipe could not be found")

def viewPantry(user):
    if user.pantryIsEmpty():
        print("You don't have any ingredients yet.\n")
    else:
        for item in user.pantry.items:
            print(str(user.pantry.items[item]) + " " + item + "(s)")

def addToPantry(user):
    toAdd = input("What would you like to add? ")
    quant = input("How many " + toAdd + "(s) would you like to add? ")
    user.addToPantry(toAdd, quant)

def removeFromPantry(user):
    toRemove = input("What would you like to remove? ")
    if user.getItemQuantity(toRemove) == 0:
        print("You don't have any " + toRemove + "(s)\n")
    else: 
        quant = input("How many " + toRemove + "(s) would you like to remove? ")
        user.removeFromPantry(toRemove, quant)

def editRecipeMenu():
    return input("(1) to add ingredients \n(2) to add instructions \n(3) to edit or remove ingredients \n(4) to remove instructions \n(0) to stop\n")

def editMatch(choice, name, user):
    if choice == '1':
        ingredient = input("What ingredient would you like to add? ")
        quantity = input("How many would you like to add? ")
        if not user.addIngredient(name, ingredient, quantity):
            print("Could not add ingredient")
    elif choice == '2':
            instructions = input("What instructions would you like to add? ")
            user.addInstruction(name, instructions)
    elif choice == '3':
            ingredient = input("What ingredient would you like to remove? ")
            quantity = input("How many would you like to remove? ")
            if not user.removeIngredient(name, ingredient, quantity):
                print("Could not remove ingredient")   
    elif choice == '4':
            instructions = input("What instructions would you like to remove? ")
            if not user.removeInstruction(name, instructions):
                print("Could not remove instruction")    

if __name__ == "__main__":
    main() 