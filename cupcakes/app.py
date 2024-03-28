from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

app.app_context().push()
connect_db(app)


@app.route('/api/cupcakes')
def list_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes = all_cupcakes)

@app.route('/api/cupcakes/<int:id>')
def show_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def new_cupcake():
    data = request.json
    new_cupcake = Cupcake(flavor=data['flavor'],
                          size=data['size'],
                          rating=data['rating'],
                          image=data['image'])
    db.session.add(new_cupcake)
    db.session.commit()
    response = jsonify(cupcake = new_cupcake.serialize())
    return (response, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def edit_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('flavor', cupcake.image)

    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(message="deleted")
