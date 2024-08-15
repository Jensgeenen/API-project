from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.Date, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=True)  # Nieuw veld toegevoegd

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'due_date': self.due_date.isoformat() if self.due_date else None,
            'user_id': self.user_id,
            'project_id': self.project_id  # Dit is toegevoegd aan de dictionary
        }

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='project', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id
        }

# Een nieuwe gebruiker aanmaken
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        username=data['username'],
        password_hash=data['password_hash'],
        email=data['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# Alle taken ophalen
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks])

# Een specifieke taak ophalen op basis van ID
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify(task.to_dict())

# Taken ophalen voor een specifiek project
@app.route('/projects/<int:id>/tasks', methods=['GET'])
def get_tasks_by_project(id):
    project = Project.query.get_or_404(id)
    tasks = Task.query.filter_by(project_id=project.id).all()
    return jsonify([task.to_dict() for task in tasks])

# Een nieuwe taak aanmaken
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()  # Converteer string naar date object
    new_task = Task(
        title=data['title'],
        description=data.get('description'),
        due_date=due_date,
        user_id=data['user_id'],
        project_id=data.get('project_id')  # Nieuw veld toegevoegd om taak aan project te koppelen
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(new_task.to_dict()), 201

# Een bestaande taak bijwerken
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)
    task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date() if 'due_date' in data else task.due_date
    task.project_id = data.get('project_id', task.project_id)  # Bijwerken van project_id indien gegeven
    db.session.commit()
    return jsonify(task.to_dict())

# Een taak verwijderen
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

# Een nieuw project aanmaken
@app.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    new_project = Project(
        name=data['name'],
        description=data.get('description'),
        user_id=data['user_id']
    )
    db.session.add(new_project)
    db.session.commit()
    return jsonify(new_project.to_dict()), 201

# Alle projecten ophalen
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Project.query.all()
    return jsonify([project.to_dict() for project in projects])

# Een specifiek project ophalen op basis van ID
@app.route('/projects/<int:id>', methods=['GET'])
def get_project(id):
    project = Project.query.get_or_404(id)
    return jsonify(project.to_dict())



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
