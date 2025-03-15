// Login.js
import React, { useState } from 'react';
import axios from 'axios';


const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [error, setError] = useState(null);


  const { email, password } = formData;

  const onChange = e =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = async e => {
    e.preventDefault();
    try {
      // Cambia la URL por la de tu endpoint de login
      const response = await fetch('http://localhost:8000/login/', {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
          email,
          password
        })  
      });
      const data = await response.json();
      if (response.ok){
        console.log(data);
      }
      
      document.cookie = "token=" + data.access_token + "; path=/";
      setError(null);
    } catch (err) {
      setError('Error al iniciar sesión');
      console.error(err);
    }
  };

  localStorage.getItem('token');

  return (
    <div>
      <h2>Login</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={onSubmit}>
        <input
          type="email"
          name="email"
          value={email}
          onChange={onChange}
          placeholder="Email"
          required
        />
        <input
          type="password"
          name="password"
          value={password}
          onChange={onChange}
          placeholder="Contraseña"
          required
        />
        <button type="submit">Iniciar Sesión</button>
      </form>
      <br />
    </div>
  );
};

export default Login;
