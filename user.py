from pantry import Pantry
from recipe import Recipe

class User: 
    def __init__(self, name =""):
        self.name = name; 
        self.pantry = Pantry()
        self.recipes = []

    def addToPantry(self, item, quantity):
        self.pantry.addItem(item, quantity)

    def removeFromPantry(self, item, quantity):
        self.pantry.removeItem(item, quantity)

    def getItemQuantity(self, item):
        return self.pantry.getQuantity(item)
    
    def pantryIsEmpty(self):
        return not bool(self.pantry.items)

    def viewRecipes(self):
        if not self.recipes:
            return "You don't have any recipes yet."
        else:
            recipe_list = "\n\n".join(str(recipe) for recipe in self.recipes)
            return recipe_list

    def addRecipe(self, recipeName, ingredients = {}, instructions = []):
        newRecipe = Recipe(recipeName, ingredients, instructions)
        self.recipes.append(newRecipe) 

    def removeRecipe(self, recipeName):
        for recipe in self.recipes:
            if recipe.name == recipeName:
                self.recipes.remove(recipe)
                return True
        return False

    def addIngredient(self, recipeName, ingredient, quantity):
        for recipe in self.recipes:
            if recipe.name == recipeName:
                recipe.addIngredient(ingredient, quantity)
                return True
        return False

    def removeIngredient(self, recipeName, ingredient, quantity):
        for recipe in self.recipes: 
            if recipe.name == recipeName:
                return recipe.removeIngredient(ingredient, quantity)
        return False

    def addInstruction(self, recipeName, instruction):
        for recipe in self.recipes: 
            if recipe.name == recipeName:
                return recipe.addInstruction(instruction)
        return False

    def removeInstruction(self, recipeName, instruction):
        for recipe in self.recipes: 
            if recipe.name == recipeName:
                return recipe.removeInstruction(instruction)
        return False

        


            
    