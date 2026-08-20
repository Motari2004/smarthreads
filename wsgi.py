# wsgi.py
from app import app as application

# Vercel looks for 'app' or 'application'
app = application