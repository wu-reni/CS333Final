class Recipe:
    def __init__(self, name, ingredients = {}, instructions = []):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    def addIngredient(self, ingredient, quantity):
        num = int(''.join(filter(str.isdigit, quantity)))
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += num
        else:
            self.ingredients[ingredient] = num
        return True

    def removeIngredient(self, ingredient, quantity):
        if ingredient in self.ingredients:
            num = int(''.join(filter(str.isdigit, quantity)))
            original = int(self.ingredients[ingredient])
            if original <= num:
                del self.ingredients[ingredient]
            else:
                self.ingredients[ingredient] = original - num
            return True
        else:
            return False

    def addInstruction(self, instruction):
        self.instructions.append(instruction)
        return True

    def removeInstruction(self, instruction):
        if instruction in self.instructions:
            self.instructions.remove(instruction)
            return True
        else:
            return False

    def __str__(self):
        ingredients = ", ".join(f"{ingredient}: {quantity}" for ingredient, quantity in self.ingredients.items())
        instructions = "\n".join(self.instructions)
        return f"Recipe Name: {self.name}\nIngredients: {ingredients or 'None'}\nInstructions: {instructions or 'None'}\n"