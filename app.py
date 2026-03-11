from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
import os
 
app = Flask(__name__)
 
# Change this to your own secret key
app.config["SECRET_KEY"] = "9f4c1c6c8c8c5f5c9d8d0f5f3d3a7e8b2c1d9a0e6f7b8c9d1e2f3a4b5c6d7e8"
 
# IMPORTANT:
# Replace root and YOUR_MYSQL_PASSWORD with your actual MySQL username and password.
# If your Workbench connection uses a different host/port, change them too.
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/restaurant_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
 
db = SQLAlchemy(app)
 
 
class User(db.Model):
    __tablename__ = "users"
 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
 
    reviews = db.relationship("Review", backref="user", lazy=True)
 
 
class Review(db.Model):
    __tablename__ = "reviews"
 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
 
 
class MenuItem(db.Model):
    __tablename__ = "menu_items"
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
 
 
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now())
