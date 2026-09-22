from config import app, db
from models import Person

with app.app_context():
    # Crea el archivo people.db y la tabla "person"
    db.create_all()

    # Datos de prueba
    PEOPLE = [
        {"fname": "Tooth", "lname": "Fairy"},
        {"fname": "Knecht", "lname": "Ruprecht"},
        {"fname": "Easter", "lname": "Bunny"},
    ]

    # Inserta cada persona en la BD
    for data in PEOPLE:
        person = Person(lname=data["lname"], fname=data["fname"])
        db.session.add(person)
    
    db.session.commit()
    print("¡Base de datos creada e inicializada con éxito!")