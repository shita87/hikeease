from apps import db
from apps.home import blueprint
from apps.home.models import Booking
from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound
from datetime import datetime
import base64
from werkzeug.utils import secure_filename


@blueprint.route('/')
def index():
    return render_template('home/index.html', segment='index')

@blueprint.route('/contact_us')
def contact_us():
    return render_template('home/contact_us.html', segment='index')

@blueprint.route('/galery')
def galery():
    return render_template('home/galery.html', segment='index')

@blueprint.route('/<template>')
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'
        segment = get_segment(request)
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500

def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "pdf"}

def allowed_file(filename):
    """Check if file has an allowed extension"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@blueprint.route('/bookings', methods=['POST'])
def create_booking():
    data = request.json
    try:
        # Get the base64 encoded file content
        identity_file = data.get('identity_file')

        if identity_file:
            # Save the Base64 string as-is in the database (already base64 encoded)
            pass  # You don't need to decode the file here since it's already base64 encoded

        # Create booking object
        new_booking = Booking(
            group_name=data.get('group_name'),
            member_name=data.get('member_name'),
            member_email=data.get('member_email'),
            nationality=data.get('nationality', ''),
            age=data.get('age'),
            phone=data.get('phone'),
            emergency_phone=data.get('emergency_phone'),
            identity_type=data.get('identity_type'),
            identity_number=data.get('identity_number'),
            identity_file=identity_file,  # Store the Base64 encoded file content
            mountain_name=data.get('mountain_name'),
            climb_date=datetime.strptime(data['climb_date'], '%Y-%m-%d') if 'climb_date' in data else None,
            province=data.get('province'),
            city=data.get('city'),
            addr=data.get('addr')
        )

        db.session.add(new_booking)
        db.session.commit()

        return jsonify({"message": "Booking created successfully", "id": new_booking.id}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400