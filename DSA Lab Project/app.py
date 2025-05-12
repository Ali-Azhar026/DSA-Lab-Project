from flask import Flask, render_template, request, redirect, url_for
from logic.cars import Car_Inventory, Rental_Records_BST, Rental_Queue, quick_sort

app = Flask(__name__)

inventory = Car_Inventory()
records = Rental_Records_BST()
queue = Rental_Queue()

@app.route('/')
def home():
    available_cars = quick_sort(inventory.display_available_cars(), 3)
    return render_template('index.html', cars=available_cars)

@app.route('/add_car', methods=['POST'])
def add_car():
    car_id = int(request.form['car_id'])
    brand = request.form['brand']
    mileage = float(request.form['mileage'])
    price = float(request.form['price'])
    inventory.add_car(car_id, brand, mileage, price)
    return redirect(url_for('home'))

@app.route('/rent_car', methods=['POST'])
def rent_car():
    customer_id = int(request.form['customer_id'])
    name = request.form['name']
    car_id = int(request.form['car_id'])
    queue.enqueue(customer_id, name, car_id)
    return redirect(url_for('process_rental'))

@app.route('/process_rental')
def process_rental():
    if not queue.is_empty():
        customer_id, name, car_id = queue.dequeue()
        car = inventory.get_car(car_id)
        if car and car.available:
            car.available = False
            records.add_rental(customer_id, name, car_id, "2025-04-28")
    return redirect(url_for('home'))

@app.route('/return_car', methods=['POST'])
def return_car():
    car_id = int(request.form['car_id'])
    car = inventory.get_car(car_id)
    if car:
        car.available = True
    return redirect(url_for('home'))

@app.route('/records')
def view_records():
    return render_template('records.html', records=_inorder_list(records.root))

def _inorder_list(node):
    if node is None:
        return []
    return _inorder_list(node.left) + [node] + _inorder_list(node.right)

if __name__ == '__main__':
    app.run(debug=True)
