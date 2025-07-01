from flask import Blueprint, request, jsonify
from app import db
from models.restaurant_pizza import RestaurantPizza
from models.restaurant import Restaurant
from models.pizza import Pizza
from sqlalchemy.exc import IntegrityError

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()
        
        if not data or 'price' not in data or 'pizza_id' not in data or 'restaurant_id' not in data:
            return jsonify({"errors": ["Missing required fields: price, pizza_id, restaurant_id"]}), 400
        
        restaurant = Restaurant.query.get(data['restaurant_id'])
        pizza = Pizza.query.get(data['pizza_id'])
        
        if not restaurant:
            return jsonify({"errors": ["Restaurant not found"]}), 400
        
        if not pizza:
            return jsonify({"errors": ["Pizza not found"]}), 400
        
        restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        return jsonify(restaurant_pizza.to_dict()), 201
        
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Database integrity error"]}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": ["An error occurred while creating restaurant pizza"]}), 500