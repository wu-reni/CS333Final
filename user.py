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

    def hasRecipe(self, recipeName):
        for recipe in self.recipes: 
            if recipe.name == recipeName:
                return recipe
        return False

    def removeRecipe(self, recipeName):
        recipe = self.hasRecipe(recipeName)
        if recipe:
            self.recipes.remove(recipe)
            return True
        return False

    def addIngredient(self, recipeName, ingredient, quantity):
        recipe = self.hasRecipe(recipeName)
        if recipe:
            return recipe.addIngredient(ingredient, quantity)
        return False

    def removeIngredient(self, recipeName, ingredient, quantity):
        recipe = self.hasRecipe(recipeName)
        if recipe:
                return recipe.removeIngredient(ingredient, quantity)
        return False

    def addInstruction(self, recipeName, instruction):
        recipe = self.hasRecipe(recipeName)
        if recipe:
            return recipe.addInstruction(instruction)
        return False

    def removeInstruction(self, recipeName, instruction):
        recipe = self.hasRecipe(recipeName)
        if recipe:
            return recipe.removeInstruction(instruction)
        return False