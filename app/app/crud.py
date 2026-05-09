import models

def create_category(db, category):
    db_category = models.Category(name=category.name)

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


def get_categories(db, skip, limit):
    return db.query(models.Category).offset(skip).limit(limit).all()

def get_category(db, id):
    return db.query(models.Category).filter(models.Category.id == id).first()

def update_category(db, id, category):
    db_category = get_category(db, id)

    if db_category:
        db_category.name = category.name
        db.commit()
        db.refresh(db_category)

    return db_category


def delete_category(db, id):
    db_category = get_category(db, id)

    if db_category:
        db.delete(db_category)
        db.commit()

    return db_category

def create_product(db, product):
    db_product = models.Product(
        name=product.name,
        price=product.price,
        category_id=product.category_id
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_products(db, skip, limit):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db, id):
    return db.query(models.Product).filter(models.Product.id == id).first()


def update_product(db, id, product):
    db_product = get_product(db, id)

    if db_product:
        db_product.name = product.name
        db_product.price = product.price
        db_product.category_id = product.category_id

        db.commit()
        db.refresh(db_product)

    return db_product


def delete_product(db, id):
    db_product = get_product(db, id)

    if db_product:
        db.delete(db_product)
        db.commit()

    return db_product
