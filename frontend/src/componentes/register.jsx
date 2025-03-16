import React, { useState } from "react";
import { Form, Button, Container, Alert } from "react-bootstrap";
import { registerUser } from "../services/authService";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [formData, setFormData] = useState({
    nombre: "",       // 🔹 Cambiar "username" a "nombre"
    email: "",
    celular: "",      // 🔹 Agregar campo celular
    password: "",
    confirmPassword: "",
  });

  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      setError("Las contraseñas no coinciden");
      return;
    }

    try {
      await registerUser(formData);
      setSuccess("Registro exitoso 🎉");
      setError(null);
      setTimeout(() => navigate("/login"), 2000);
    } catch (error) {
      setError("Error en el registro");
    }
  };

  return (
    <Container className="mt-5">
      <h2>Registro</h2>
      {error && <Alert variant="danger">{error}</Alert>}
      {success && <Alert variant="success">{success}</Alert>}
      <Form onSubmit={handleSubmit}>
        <Form.Group>
          <Form.Label>Nombre</Form.Label>
          <Form.Control type="text" name="nombre" onChange={handleChange} required />
        </Form.Group>
        <Form.Group>
          <Form.Label>Correo</Form.Label>
          <Form.Control type="email" name="email" onChange={handleChange} required />
        </Form.Group>
        <Form.Group>
          <Form.Label>Celular</Form.Label>
          <Form.Control type="text" name="celular" onChange={handleChange} required />
        </Form.Group>
        <Form.Group>
          <Form.Label>Contraseña</Form.Label>
          <Form.Control type="password" name="password" onChange={handleChange} required />
        </Form.Group>
        <Form.Group>
          <Form.Label>Confirmar Contraseña</Form.Label>
          <Form.Control type="password" name="confirmPassword" onChange={handleChange} required />
        </Form.Group>
        <Button variant="primary" type="submit" className="mt-3">
          Registrarse
        </Button>
      </Form>
    </Container>
  );
};

export default Register;
