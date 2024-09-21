from MargheritaKitchen import MargheritaKitchen

margherita_kitchen = MargheritaKitchen()
margherita_pizza = margherita_kitchen.create_pizza(type="Margherita", size="small", price=99.99)
margherita_pizza.bake();margherita_pizza.cut();margherita_pizza.pack()