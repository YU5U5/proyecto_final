import React, { useState } from "react";
import { Form, Button, Container, Alert } from "react-bootstrap";
import { loginUser } from "../services/authService";
import { useNavigate } from "react-router-dom";
import { Link } from "react-router-dom";

const Login = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const data = await loginUser(formData);
      localStorage.setItem("token", data.access); // ✅ Guarda el token
      setSuccess("Inicio de sesión exitoso 🎉");
      setError(null);
      setTimeout(() => navigate("/"), 2000); // ✅ Redirige después de 2s
    } catch (error) {
      setError("Correo o contraseña incorrectos");
    }
  };

  return (
    <Container className="mt-5">
      <h2>Login</h2>
      {error && <Alert variant="danger">{error}</Alert>}
      {success && <Alert variant="success">{success}</Alert>}
      <Form onSubmit={handleSubmit}>
        <Form.Group>
          <Form.Label>Correo</Form.Label>
          <Form.Control type="email" name="email" onChange={handleChange} required />
        </Form.Group>
        <Form.Group>
          <Form.Label>Contraseña</Form.Label>
          <Form.Control type="password" name="password" onChange={handleChange} required />
        </Form.Group>
        <Button variant="success" type="submit" className="mt-3">
          Iniciar sesión
        </Button> 
      </Form><Link to="/recover-password">¿Olvidaste tu contraseña?</Link>

    </Container>
  );
};

export default Login;
