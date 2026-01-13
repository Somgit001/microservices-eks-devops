from flask import Flask, jsonify, request
from datetime import datetime
import os

app = Flask(__name__)
PORT = int(os.getenv('PORT', 3003))

orders = [
    {
        'id': 1,
        'user_id': 1,
        'products': [{'product_id': 1, 'quantity': 1}],
        'total': 1299.99,
        'status': 'delivered',
        'created_at': '2025-01-01T10:00:00Z'
    },
    {
        'id': 2,
        'user_id': 2,
        'products': [{'product_id': 2, 'quantity': 2}],
        'total': 59.98,
        'status': 'processing',
        'created_at': '2025-01-10T15:30:00Z'
    }
]

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'order-service',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/orders')
def get_orders():
    user_id = request.args.get('user_id')
    status = request.args.get('status')
    filtered = orders
    if user_id:
        filtered = [o for o in filtered if o['user_id'] == int(user_id)]
    if status:
        filtered = [o for o in filtered if o['status'] == status]
    return jsonify({'success': True, 'data': filtered, 'count': len(filtered)})

@app.route('/api/orders/<int:order_id>')
def get_order(order_id):
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return jsonify({'success': False, 'message': 'Order not found'}), 404
    return jsonify({'success': True, 'data': order})

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = {
        'id': len(orders) + 1,
        'user_id': data.get('user_id'),
        'products': data.get('products', []),
        'total': data.get('total', 0),
        'status': 'pending',
        'created_at': datetime.utcnow().isoformat() + 'Z'
    }
    orders.append(new_order)
    return jsonify({'success': True, 'data': new_order}), 201

if __name__ == '__main__':
    print(f'🚀 Order Service running on port {PORT}')
    app.run(host='0.0.0.0', port=PORT)
