from apps import db


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(64), unique=True, nullable=False)
    member_name = db.Column(db.String(64), unique=True, nullable=False)
    member_email = db.Column(db.String(64), unique=True, nullable=False)
    nationality = db.Column(db.String(64))
    age = db.Column(db.Integer)
    phone = db.Column(db.String(64))
    emergency_phone = db.Column(db.String(64))
    identity_type = db.Column(db.String(64))
    identity_number = db.Column(db.String(64))
    identity_file = db.Column(db.String(64))
    mountain_name = db.Column(db.String(64))
    climb_date = db.Column(db.DateTime)
    province = db.Column(db.String(64))
    city = db.Column(db.String(64))
    addr = db.Column(db.String(64))

    def __repr__(self):
        return f"<Booking {self.name}>"
