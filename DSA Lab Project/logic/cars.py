class Car_Node:
    def __init__(self, car_id, brand, mileage, price_per_day, available=True):
        self.car_id = car_id
        self.brand = brand
        self.mileage = mileage
        self.price_per_day = price_per_day
        self.available = available
        self.next = None

class Car_Inventory:
    def __init__(self): 
        self.head = None

    def add_car(self, car_id, brand, mileage, price_per_day):
        new_car = Car_Node(car_id, brand, mileage, price_per_day)
        new_car.next = self.head
        self.head = new_car

    def get_car(self, car_id):
        current = self.head
        while current:
            if current.car_id == car_id:
                return current
            current = current.next
        return None

    def display_available_cars(self):
        current = self.head
        cars = []
        while current:
            if current.available:
                cars.append((current.car_id, current.brand, current.mileage, current.price_per_day))
            current = current.next
        return cars

class Rental_Node:
    def __init__(self, customer_id, customer_name, car_id, rent_date, return_date=None):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.car_id = car_id
        self.rent_date = rent_date
        self.return_date = return_date
        self.left = None
        self.right = None

class Rental_Records_BST:
    def __init__(self):
        self.root = None

    def insert(self, root, node):
        if not root:
            return node
        if node.customer_id < root.customer_id:
            root.left = self.insert(root.left, node)
        else:
            root.right = self.insert(root.right, node)
        return root

    def add_rental(self, customer_id, customer_name, car_id, rent_date):
        new_rental = Rental_Node(customer_id, customer_name, car_id, rent_date)
        self.root = self.insert(self.root, new_rental)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(f"Customer ID: {root.customer_id}, Name: {root.customer_name}, Car ID: {root.car_id}, Rented: {root.rent_date}, Returned: {root.return_date}")
            self.inorder(root.right)

    def search(self, root, customer_id):
        if not root or root.customer_id == customer_id:
            return root
        if customer_id < root.customer_id:
            return self.search(root.left, customer_id)
        return self.search(root.right, customer_id)

class Rental_Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, customer_id, customer_name, car_id):
        self.items.append((customer_id, customer_name, car_id))

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

def quick_sort(cars, key_index):
    def partition(arr, low, high):
        pivot = arr[low] 
        left = low + 1
        right = high

        while True:
            while left <= right and arr[left][key_index] <= pivot[key_index]:
                left += 1
            while left <= right and arr[right][key_index] >= pivot[key_index]:
                right -= 1
            if left > right:
                break
            arr[left], arr[right] = arr[right], arr[left]

        arr[low], arr[right] = arr[right], arr[low]  
        return right

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quick_sort_recursive(arr, low, pivot_index - 1)
            quick_sort_recursive(arr, pivot_index + 1, high)

    cars_copy = cars[:]
    quick_sort_recursive(cars_copy, 0, len(cars_copy) - 1)
    return cars_copy
