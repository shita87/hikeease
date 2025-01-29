from apps.admin import blueprint
from apps import db
from apps.home.models import Booking
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound


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