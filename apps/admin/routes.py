from apps.admin import blueprint
from apps import db
from apps.home.models import Booking
from apps.admin.models import Product
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound


# Mange Booking

@blueprint.route('/admin')
@login_required
def index():
    bookings = Booking.query.all()
    if request.args.get('format') == 'json':
        return jsonify([{
            "id": b.id,
            "group_name": b.group_name,
            "member_name": b.member_name,
            "member_email": b.member_email,
            "nationality": b.nationality,
            "age": b.age,
            "phone": b.phone,
            "emergency_phone": b.emergency_phone,
            "identity_type": b.identity_type,
            "identity_number": b.identity_number,
            "identity_file": b.identity_file,
            "mountain_name": b.mountain_name,
            "climb_date": b.climb_date.strftime('%Y-%m-%d') if b.climb_date else None,
            "province": b.province,
            "city": b.city,
            "addr": b.addr
        } for b in bookings])

    return render_template('admin/admin.html', bookings=bookings)

@blueprint.route('/admin/booking/<int:booking_id>', methods=['GET'])
@login_required
def get_booking(booking_id):
    booking = Booking.query.get(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    
    return jsonify({
        "id": booking.id,
        "group_name": booking.group_name,
        "member_name": booking.member_name,
        "member_email": booking.member_email,
        "nationality": booking.nationality,
        "age": booking.age,
        "phone": booking.phone,
        "emergency_phone": booking.emergency_phone,
        "identity_type": booking.identity_type,
        "identity_number": booking.identity_number,
        "identity_file": booking.identity_file,
        "mountain_name": booking.mountain_name,
        "climb_date": booking.climb_date.strftime('%Y-%m-%d'),
        "province": booking.province,
        "city": booking.city,
        "addr": booking.addr
        })

@blueprint.route('/admin/bookings/<int:id>', methods=['DELETE'])
@login_required
def delete_booking(id):
    try:
        booking = Booking.query.get(id)

        if not booking:
            return jsonify({"error": "Booking not found"}), 404

        # Delete the booking
        db.session.delete(booking)
        db.session.commit()
        return jsonify({"message": "Booking deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Manage Product
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "pdf"}

def allowed_file(filename):
    """Check if file has an allowed extension"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@blueprint.route('/manage_product', methods=['POST'])
@login_required
def add_product():
    data = request.json
    try:
        mountain_pic = data.get('mountain_pic')
        if mountain_pic:
            pass

        new_product = Product (
            mountain_name = data.get('mountain_name'),
            location = data.get('location'),
            contact = data.get('contact'),
            difficulty = data.get('difficulty'),
            price = data.get('price'),
            height = data.get('height'),
            coordinate = data.get('coordinate'),
            mountain_pic = data.get('mountain_pic'),
            facility = data.get('facility'),
            description = data.get('description'),
            fullbook = data.get('fullbook'),
            available = data.get('available')
        )

        db.session.add(new_product)
        db.session.commit()

        return jsonify({"message": f"New Product Created Successully"}), 201
    except Exception as e:
        return jsonify({"error:": str(e)}), 400

@blueprint.route('/manage_product', methods=['GET'])
@login_required
def get_product():
    products = Product.query.all()
    if request.args.get('format') == 'json':
        return jsonify([{
            "id": b.id,
            "mountain_name": b.mountain_name,
            "location": b.location,
            "contact": b.contact,
            "difficulty": b.difficulty,
            "price": b.price,
            "height": b.height,
            "coordinate": b.coordinate,
            "mountain_pic": b.mountain_pic,
            "facility": b.facility,
            "fullbook": b.fullbook,
            "description": b.description,
            "available": b.available,
        }for b in products])
    return render_template('admin/manage_product.html', products=products)
    
@blueprint.route('/manage_product/<int:id>')
@login_required
def view_product(id):
    try:
        product = Product.query.get(id)
        if not product:
            return jsonify({"error": "Product not found"}), 404
        return jsonify({
            "id": product.id,
            "mountain_name": product.mountain_name,
            "location": product.location,
            "contact": product.contact,
            "difficulty": product.difficulty,
            "price": product.price,
            "height": product.height,
            "coordinate": product.coordinate,
            "mountain_pic": product.mountain_pic,
            "facility": product.facility,
            "fullbook": product.fullbook,
            "description": product.description,
            "available": product.available,
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
@blueprint.route('/manage_product/<int:id>', methods=['DELETE'])
@login_required
def delete_product(id):
    try:
        product = Product.query.get(id)

        if not product:
            return jsonify({"error": "Product not found"}), 404

        # Delete the booking
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}),201

    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
