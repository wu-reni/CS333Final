from pantry import Pantry
from recipe import Recipe
from user import User
import unittest

class Tests(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.pantry = Pantry()
        self.pantry.addItem("apple", '3 slices')
        self.recipe = Recipe("Apple Pie")
        self.recipeName = "Spaghetti and Meatballs"
        self.ingredients = {'Spaghetti': '8', 'Meatballs': '8', 'Tomato Sauce':'1'}
        self.instructions = ["Cook spaghetti", "Heat tomato sauce and meatballs", "Serve spaghetti with sauce and meatballs"]
        self.user.addRecipe(self.recipeName, self.ingredients, self.instructions)  

    def testPantryAddNewItem(self):
        self.pantry.addItem("cheese", "3 slices")
        self.assertEqual(self.pantry.items["cheese"], 3)

    def testPantryAddExistingItem(self):
        self.pantry.addItem("apple", '3 slices')
        self.assertEqual(self.pantry.items["apple"], 6)

    def testPantryRemoveMissingItem(self):
        self.assertFalse(self.pantry.removeItem("cheese", '3'))
            
    def testPantryRemovePartialItem(self):
        self.pantry.removeItem("apple", '2 slices')
        self.assertEqual(self.pantry.items["apple"], 1)
    
    def testGetQuantity(self):
        self.assertEqual(self.pantry.getQuantity("apple"), 3)

    def testPantryRemoveEntireItem(self):
        self.pantry.removeItem("apple", '3 slices')
        self.assertEqual(self.pantry.getQuantity("apple"), 0)

    def testUserAddPantry(self):
        self.assertTrue(self.user.addToPantry("banana", '3'))
        self.assertEqual(self.user.pantry.items["banana"], 3)

    def testUserRemovePantry(self):
        self.user.addToPantry("banana", '3')
        self.assertTrue(self.user.removeFromPantry("banana", '3'))
        self.assertEqual(self.user.getItemQuantity("banana"), 0)
        
    def testUserPantryIsEmpty(self):
        self.assertFalse(self.user.pantryIsEmpty())

    def testRecipeAddIngredient(self):
        self.recipe.addIngredient("apple", '1 slices')
        self.assertEqual(self.recipe.ingredients["apple"], 1)
        self.recipe.addIngredient("apple", '4 slices')
        self.assertEqual(self.recipe.ingredients["apple"], 5)

    def testRecipeRemoveNonExistingIngredient(self):
        self.assertFalse(self.recipe.removeIngredient("lemon", '1'))
    
    def testRecipeRemoveIngredient(self):
        self.recipe.addIngredient("bread", '4 slices')
        self.recipe.removeIngredient("bread", '3 slices')
        self.assertEqual(self.recipe.ingredients["bread"], 1)
    
    def testRecipeRemoveEntireIngredient(self):
        self.recipe.addIngredient("bread", '4 slices')
        self.assertTrue(self.recipe.removeIngredient("bread", '5 slices'))

    def testRecipeAddInstruction(self):
        self.recipe.addInstruction("Preheat oven to 350")
        self.assertEqual(self.recipe.instructions, ["Preheat oven to 350"])
    
    def testRemoveNonexistingInstruction(self):
        self.assertFalse(self.recipe.removeInstruction("Whisk eggs"))

    def testRemoveExistingInstruction(self):
        self.assertTrue(self.recipe.removeInstruction("Preheat oven to 350"))

    def testViewRecipesNoRecipes(self):
        self.user2 = User()
        self.assertEqual(self.user2.viewRecipes(), "You don't have any recipes yet.")

    def testViewRecipes(self):
        self.user = User()
        self.recipeOne = Recipe("Recipe 1")
        self.recipeOne.ingredients = {}
        self.user.recipes = [self.recipeOne]
        self.assertEqual(self.user.viewRecipes(), "Recipe Name: Recipe 1\nIngredients: None\nInstructions: None\n")

    def testUserAddRecipe(self):
        recipe = self.user.recipes[0]
        self.assertEqual(recipe.name, self.recipeName)
        self.assertEqual(recipe.ingredients, self.ingredients)
        self.assertEqual(recipe.instructions, self.instructions)

    def testUserRemoveRecipe(self):
        self.assertTrue(self.user.removeRecipe("Spaghetti and Meatballs"))

    def testUserRemoveNonexistingRecipe(self):
        self.assertFalse(self.user.removeRecipe("Sandwich"))

    def testUserAddIngredient(self):
        self.assertTrue(self.user.addIngredient(self.recipeName, "Salt", "1 TSP"))
        self.assertFalse(self.user.addIngredient("Something that doesn't exist", "Something", 1))

    def testUserRemoveIngredient(self):
        self.assertTrue(self.user.removeIngredient(self.recipeName, "Spaghetti", "4"))
        self.assertFalse(self.user.removeIngredient(self.recipeName, "Cheese", "1 slice"))
        self.assertFalse(self.user.removeIngredient("Something random", "Cheese", "1 slice"))

    def testUserAddInstruction(self):
        self.assertTrue(self.user.addInstruction(self.recipeName, "Boil something"))
        self.assertFalse(self.user.addInstruction("Something random", "Cheese"))

    def testUserRemoveInstruction(self):
        self.assertTrue(self.user.removeInstruction(self.recipeName, "Cook spaghetti"))
        self.assertFalse(self.user.removeInstruction("Something random", "Cheese"))
    
    def testUserHasRecipe(self):
        self.assertTrue(self.user.hasRecipe(self.recipeName))
        self.assertFalse(self.user.hasRecipe("Something Random"))