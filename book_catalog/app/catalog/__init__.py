from flask import Blueprint

catalog = Blueprint('catalog', __name__, template_folder='templates')
from app.catalog import routes,models  # to avoid circular imports
