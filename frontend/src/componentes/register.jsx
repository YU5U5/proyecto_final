// Register.js
import React, { useState } from 'react';
import axios from 'axios';

const Register = () => {
  const [formData, setFormData] = useState({
    nombre: '',
    celular: '',
    email: '',
    password: '',
    confirmPassword: ''
  });
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const { nombre, celular, email, password, confirmPassword } = formData;

  const onChange = e =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = async e => {
    e.preventDefault();
    if (password !== confirmPassword) {
      setError('Las contraseñas no coinciden');
      return;
    }
    try {
      const response = await axios.post('http://localhost:8000/registro/', {
        nombre,
        celular,
        email,
        password,
        confirmPassword
      });
      setSuccess('Usuario registrado exitosamente');
      setError(null);
      // Si el endpoint retorna un token, podrías almacenarlo en cookie aquí
      // Ejemplo:
      // const { token } = response.data;
      // Cookies.set('token', token);
    } catch (err) {
      setError('Error en el registro');
      console.error(err);
    }
  };

  return (
    <div>
      <h2>Registro de Usuario</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green' }}>{success}</p>}
      <form onSubmit={onSubmit}>
        <input
          type="text"
          name="nombre"
          value={nombre}
          onChange={onChange}
          placeholder="Nombre"
          required
        />
        <input
          type="text"
          name="celular"
          value={celular}
          onChange={onChange}
          placeholder="Celular"
          required
        />
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
        <input
          type="password"
          name="confirmPassword"
          value={confirmPassword}
          onChange={onChange}
          placeholder="Confirmar Contraseña"
          required
        />
        <button type="submit">Registrarse</button>
      </form>
    </div>
  );
};

export default Register;
