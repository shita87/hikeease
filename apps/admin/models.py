from apps import db

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    mountain_name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    contact = db.Column(db.String(64))
    difficulty = db.Column(db.String(64))
    price = db.Column(db.Integer)
    height = db.Column(db.String(64))
    coordinate = db.Column(db.String(64))
    mountain_pic = db.Column(db.String(64))
    facility = db.Column(db.String(64))
    fullbook = db.Column(db.String(64))
    available = db.Column(db.String(64))
    description = db.Column(db.String(64))

    def __repr__(self):
        return f"<Product {self.name}>"