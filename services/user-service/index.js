const express = require('express');
const app = express();
const PORT = process.env.PORT || 3001;

app.use(express.json());

let users = [
  { id: 1, name: 'John Doe', email: 'john@example.com', role: 'customer' },
  { id: 2, name: 'Jane Smith', email: 'jane@example.com', role: 'admin' }
];

app.get('/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    service: 'user-service', 
    version: '1.0.0',
    timestamp: new Date().toISOString()
  });
});

app.get('/api/users', (req, res) => {
  res.json({ success: true, data: users, count: users.length });
});

app.get('/api/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ success: false, message: 'User not found' });
  res.json({ success: true, data: user });
});

app.post('/api/users', (req, res) => {
  const newUser = {
    id: users.length + 1,
    name: req.body.name,
    email: req.body.email,
    role: req.body.role || 'customer'
  };
  users.push(newUser);
  res.status(201).json({ success: true, data: newUser });
});

app.listen(PORT, () => {
  console.log(`🚀 User Service running on port ${PORT}`);
});
