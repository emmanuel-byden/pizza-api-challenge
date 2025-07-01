# 🍕 Pizza Restaurant API

A RESTful API for managing pizza restaurants, built with Flask and SQLAlchemy following the MVC (Model-View-Controller) pattern.

## Project Structure

```
.
├── server/
│   ├── __init__.py
│   ├── app.py                # App setup and configuration
│   ├── config.py             # Database configuration
│   ├── models/               # Data models (SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── restaurant.py     # Restaurant model
│   │   ├── pizza.py          # Pizza model
│   │   └── restaurant_pizza.py # Join table model
│   ├── controllers/          # Route handlers (Controllers)
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   └── seed.py               # Database seeding script
├── migrations/               # Database migration files
├── challenge-1-pizzas.postman_collection.json
└── README.md
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd pizza-api-challenge
```

### 2. Create Virtual Environment and Install Dependencies
```bash
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell
```

### 3. Set Flask Application Environment Variable
```bash
export FLASK_APP=server/app.py
```

### 4. Initialize Database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 5. Seed the Database
```bash
python server/seed.py
```

### 6. Run the Application
```bash
flask run
```

The API will be available at `http://127.0.0.1:5000`

## Models

### Restaurant
- **id**: Primary key (integer)
- **name**: Restaurant name (string)
- **address**: Restaurant address (string)
- **Relationships**: Has many RestaurantPizzas (with cascade delete)

### Pizza
- **id**: Primary key (integer)
- **name**: Pizza name (string)
- **ingredients**: Pizza ingredients (string)
- **Relationships**: Has many RestaurantPizzas

### RestaurantPizza (Join Table)
- **id**: Primary key (integer)
- **price**: Price of pizza at restaurant (integer, must be between 1-30)
- **restaurant_id**: Foreign key to Restaurant
- **pizza_id**: Foreign key to Pizza
- **Relationships**: Belongs to Restaurant and Pizza

## API Endpoints

### GET /restaurants
Returns a list of all restaurants.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5432"
  }
]
```

### GET /restaurants/<int:id>
Returns details of a single restaurant with its pizzas.

**Success Response:**
```json
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5432",
  "restaurant_pizzas": [
    {
      "id": 1,
      "price": 10,
      "pizza_id": 1,
      "restaurant_id": 1,
      "pizza": {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      "restaurant": {
        "id": 1,
        "name": "Dominion Pizza",
        "address": "Good Italian, Ngong Road, 5432"
      }
    }
  ]
}
```

**Error Response (404):**
```json
{
  "error": "Restaurant not found"
}
```

### DELETE /restaurants/<int:id>
Deletes a restaurant and all related RestaurantPizzas.

**Success Response:** 204 No Content

**Error Response (404):**
```json
{
  "error": "Restaurant not found"
}
```

### GET /pizzas
Returns a list of all pizzas.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  }
]
```

### POST /restaurant_pizzas
Creates a new RestaurantPizza association.

**Request Body:**
```json
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

**Success Response (201):**
```json
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 3,
    "name": "Kiki's Pizza",
    "address": "Forest Road, Kilimani, 1234"
  }
}
```

**Error Response (400):**
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

## Validation Rules

- **RestaurantPizza.price**: Must be between 1 and 30 (inclusive)
- **Required fields**: All model fields are required except auto-generated IDs
- **Foreign Key Constraints**: restaurant_id and pizza_id must reference existing records

## Testing with Postman

1. **Import Collection:**
   - Open Postman
   - Click "Import"
   - Select `challenge-1-pizzas.postman_collection.json`

2. **Set Base URL:**
   - The collection uses a variable `{{base_url}}`
   - Default value: `http://127.0.0.1:5000`

3. **Test Endpoints:**
   - Run each request in the collection
   - Verify responses match expected formats
   - Test both success and error scenarios

## Sample Data

The seed script creates:

**Restaurants:**
- Dominion Pizza (Ngong Road)
- Pizza Hut (Westgate Mall)
- Kiki's Pizza (Forest Road)

**Pizzas:**
- Cheese Pizza
- Pepperoni Pizza
- California Pizza

**Restaurant-Pizza Associations:**
- Various price points for different restaurant-pizza combinations

## Development Notes

- The application follows MVC architecture for better code organization
- Models include proper relationships and validations
- Controllers handle route logic and error responses
- Cascade delete ensures data integrity when restaurants are removed
- SQLAlchemy migrations manage database schema changes