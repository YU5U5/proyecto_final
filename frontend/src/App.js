// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Register from './componentes/register';
import Login from './componentes/login';


const App = () => {
  return (
    <Router>
      <div style={{ padding: '20px' }}>
        <nav>
          <ul style={{ listStyle: 'none', display: 'flex', gap: '15px' }}>
            <li>
              <Link to="/">Registro</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<Register />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
