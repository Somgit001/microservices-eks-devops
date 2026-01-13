from flask import Flask, jsonify, request
from datetime import datetime
import os
import random
import string

app = Flask(__name__)
PORT = int(os.getenv('PORT', 3004))

payments = []

def generate_transaction_id():
    return 'TXN' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'payment-service',
        'version': '1.0.0',
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/payments')
def get_payments():
    user_id = request.args.get('user_id')
    filtered = payments
    if user_id:
        filtered = [p for p in filtered if p['user_id'] == int(user_id)]
    return jsonify({'success': True, 'data': filtered, 'count': len(filtered)})

@app.route('/api/payments/process', methods=['POST'])
def process_payment():
    data = request.get_json()
    success = random.random() > 0.1
    
    new_payment = {
        'id': generate_transaction_id(),
        'order_id': data.get('order_id'),
        'user_id': data.get('user_id'),
        'amount': data.get('amount'),
        'method': data.get('method', 'card'),
        'status': 'completed' if success else 'failed',
        'created_at': datetime.utcnow().isoformat() + 'Z'
    }
    
    payments.append(new_payment)
    
    if success:
        return jsonify({'success': True, 'data': new_payment}), 201
    else:
        return jsonify({'success': False, 'message': 'Payment failed', 'data': new_payment}), 402

if __name__ == '__main__':
    print(f'🚀 Payment Service running on port {PORT}')
    app.run(host='0.0.0.0', port=PORT)
