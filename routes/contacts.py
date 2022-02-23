from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@contacts.route('/new', methods=['POST'])
def add_contact():
    fullname = request.form['fullname']
    print(request.form['fullname'])
    email = request.form['email']
    print(request.form['email'])
    phone = request.form['phone']
    print(request.form['phone'])

    new_contact = Contact(fullname, email, phone)
    print(new_contact)

    db.session.add(new_contact)
    db.session.commit()

    flash('Contact added successfully')

    return redirect(url_for('contacts.index')) # return 'saving a contact'
    

@contacts.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    print(id)
    contact = Contact.query.get(id)
    if request.method == 'POST':
        print('updating a contact')
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        db.session.commit()
        print('contact updated')
        flash('Contact updated successfully')
        return redirect(url_for('contacts.index')) # return 'updating a contact'
    return render_template('update.html', contact=contact) # return 'updating a contact'

@contacts.route('/delete/<id>')
def delete(id):
    print(id)
    contact = Contact.query.get(id)
    print(contact)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact deleted successfully')
    return redirect(url_for('contacts.index')) # return 'delete a contact'

@contacts.route('/about')
def about():
    return render_template('about.html')