 FastAPI Machine Test
 
Technologies Used
- FastAPI
- PostgreSQL
- SQLAlchemy


 Database Design

 categories table

 Column | Type |
|--------|------|
| id | Integer |
| name | String |


 products table

| Column | Type |
|--------|------|
| id | Integer |
| name | String |
| price | Integer |
| category_id | Foreign Key |


    APIs

  Category APIs
- GET /api/categories?page=1
- POST /api/categories
- GET /api/categories/{id}
- PUT /api/categories/{id}
- DELETE /api/categories/{id}


   Product APIs
- GET /api/products?page=1
- POST /api/products
- GET /api/products/{id}
- PUT /api/products/{id}
- DELETE /api/products/{id}


## Run Project

uvicorn app.main:app --reload
