```
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.String, primary_key=True)
    pw = db.Column(db.String, nullable=False)


class Note(db.Model):
    __tablename__ = "notes"
    user = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    note = db.Column(db.Text, nullable=False)
    note_id = db.Column(db.String, primary_key=True)


class Image(db.Model):
    __tablename__ = "images"
    uid = db.Column(db.String, primary_key=True)
    owner = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
```

This code snippet defines SQLAlchemy models for three database tables: `User`, `Note`, and `Image`. Let's break down each model and its attributes:

1. **User Model (`User`)**:
   - `id`: This column represents the user's ID. It is defined as a primary key and of type `db.String`.
   - `pw`: This column represents the user's password. It is of type `db.String` and is set to `nullable=False`, meaning it cannot be null.

2. **Note Model (`Note`)**:
   - `user`: This column represents the user associated with the note. It is of type `db.String` and is set to `nullable=False`.
   - `timestamp`: This column represents the timestamp when the note was created. It is of type `db.DateTime` and is set to `nullable=False`.
   - `note`: This column represents the content of the note. It is of type `db.Text` and is set to `nullable=False`.
   - `note_id`: This column represents the unique identifier for the note. It is defined as a primary key and of type `db.String`.

3. **Image Model (`Image`)**:
   - `uid`: This column represents the unique identifier for the image. It is defined as a primary key and of type `db.String`.
   - `owner`: This column represents the owner of the image. It is of type `db.String` and is set to `nullable=False`.
   - `name`: This column represents the name of the image file. It is of type `db.String` and is set to `nullable=False`.
   - `timestamp`: This column represents the timestamp when the image was uploaded. It is of type `db.DateTime` and is set to `nullable=False`.

Additionally:
- The `__tablename__` attribute is used to specify the name of the database table associated with each model.
- The `db.Model` class serves as the base class for all models, providing common functionality such as query building and data serialization.
- `db.Column` is used to define columns within a model, specifying the column name, data type, and any additional constraints.

Overall, these models define the structure of the database tables used in your Flask application, including the relationships between different entities (users, notes, and images) and the attributes associated with each entity.