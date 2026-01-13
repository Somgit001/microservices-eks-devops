const express = require('express');
const app = express();
const PORT = process.env.PORT || 3002;

app.use(express.json());

let products = [
  { id: 1, name: 'Laptop Pro', price: 1299.99, stock: 50, category: 'Electronics' },
  { id: 2, name: 'Wireless Mouse', price: 29.99, stock: 200, category: 'Accessories' },
  { id: 3, name: 'USB-C Cable', price: 19.99, stock: 150, category: 'Accessories' },
  { id: 4, name: 'Monitor 4K', price: 499.99, stock: 30, category: 'Electronics' }
];

app.get('/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    service: 'product-service', 
    version: '1.0.0',
    timestamp: new Date().toISOString()
  });
});

app.get('/api/products', (req, res) => {
  const { category, minPrice, maxPrice } = req.query;
  let filtered = products;
  
  if (category) filtered = filtered.filter(p => p.category.toLowerCase() === category.toLowerCase());
  if (minPrice) filtered = filtered.filter(p => p.price >= parseFloat(minPrice));
  if (maxPrice) filtered = filtered.filter(p => p.price <= parseFloat(maxPrice));
  
  res.json({ success: true, data: filtered, count: filtered.length });
});

app.get('/api/products/:id', (req, res) => {
  const product = products.find(p => p.id === parseInt(req.params.id));
  if (!product) return res.status(404).json({ success: false, message: 'Product not found' });
  res.json({ success: true, data: product });
});

app.post('/api/products', (req, res) => {
  const newProduct = {
    id: products.length + 1,
    name: req.body.name,
    price: parseFloat(req.body.price),
    stock: parseInt(req.body.stock),
    category: req.body.category
  };
  products.push(newProduct);
  res.status(201).json({ success: true, data: newProduct });
});

app.listen(PORT, () => {
  console.log(`🚀 Product Service running on port ${PORT}`);
});
