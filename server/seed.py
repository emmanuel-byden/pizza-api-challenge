from app import app, db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        restaurants = [
            Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5432"),
            Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, 5467"),
            Restaurant(name="Kiki's Pizza", address="Forest Road, Kilimani, 1234")
        ]
        
        pizzas = [
            Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese"),
            Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
            Pizza(name="California", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")
        ]
        
        db.session.add_all(restaurants)
        db.session.add_all(pizzas)
        db.session.commit()
        
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=15, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=12, restaurant_id=2, pizza_id=1),
            RestaurantPizza(price=20, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=8, restaurant_id=3, pizza_id=1),
            RestaurantPizza(price=18, restaurant_id=3, pizza_id=2)
        ]
        
        db.session.add_all(restaurant_pizzas)
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()