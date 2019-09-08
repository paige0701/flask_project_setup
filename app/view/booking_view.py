from flask import Blueprint

booking_view = Blueprint('booking_view', __name__)

@booking_view.route('/')
def display_home():
    return 'This is home'
