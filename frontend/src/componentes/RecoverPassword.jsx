import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { solicitarRecuperacion, confirmarToken, restablecerContraseña } from "../services/authService";
import { Container, Form, Button, Alert } from "react-bootstrap";

const RecoverPassword = () => {
  const [paso, setPaso] = useState(1);  // 1: Ingresar correo, 2: Ingresar código, 3: Nueva contraseña
  const [email, setEmail] = useState("");
  const [codigo, setCodigo] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [mensaje, setMensaje] = useState(null);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  // 🔹 Paso 1: Enviar código de recuperación al correo
  const handleSolicitar = async (e) => {
    e.preventDefault();
    setMensaje(null);
    setError(null);

    try {
      await solicitarRecuperacion(email);
      setMensaje("Código enviado a tu correo.");
      localStorage.setItem("user_email", email);
      setPaso(2); // Ir al siguiente paso
    } catch (err) {
      setError("No se pudo enviar el código. Verifica tu correo.");
    }
  };

  // 🔹 Paso 2: Verificar código ingresado
  const handleVerificarCodigo = async (e) => {
    e.preventDefault();
    setMensaje(null);
    setError(null);

    try {
      await confirmarToken(codigo);
      setMensaje("Código verificado correctamente.");
      localStorage.setItem("reset_token", codigo);
      setPaso(3); // Ir al siguiente paso
    } catch (err) {
      setError("Código incorrecto. Inténtalo de nuevo.");
    }
  };

  // 🔹 Paso 3: Restablecer contraseña
  const handleRestablecer = async (e) => {
    e.preventDefault();
    setMensaje(null);
    setError(null);

    if (password !== confirmPassword) {
      setError("Las contraseñas no coinciden.");
      return;
    }

    try {
      const token = localStorage.getItem("reset_token");
      await restablecerContraseña(token, password, confirmPassword);
      setMensaje("Contraseña cambiada con éxito. Redirigiendo...");

      setTimeout(() => navigate("/login"), 2000);
    } catch (err) {
      setError("Error al cambiar la contraseña. Inténtalo de nuevo.");
    }
  };

  return (
    <Container className="mt-5">
      <h2>Recuperar Contraseña</h2>

      {paso === 1 && (
        <Form onSubmit={handleSolicitar}>
          <Form.Group controlId="formEmail">
            <Form.Label>Correo Electrónico</Form.Label>
            <Form.Control type="email" placeholder="Ingrese su correo" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </Form.Group>
          <Button variant="primary" type="submit" className="mt-3">Enviar Código</Button>
        </Form>
      )}

      {paso === 2 && (
        <Form onSubmit={handleVerificarCodigo}>
          <Form.Group controlId="formCodigo">
            <Form.Label>Ingresa el Código</Form.Label>
            <Form.Control type="text" placeholder="Código recibido" value={codigo} onChange={(e) => setCodigo(e.target.value)} required />
          </Form.Group>
          <Button variant="primary" type="submit" className="mt-3">Verificar Código</Button>
        </Form>
      )}

      {paso === 3 && (
        <Form onSubmit={handleRestablecer}>
          <Form.Group controlId="formPassword">
            <Form.Label>Nueva Contraseña</Form.Label>
            <Form.Control type="password" placeholder="Nueva contraseña" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </Form.Group>
          <Form.Group controlId="formConfirmPassword">
            <Form.Label>Confirmar Contraseña</Form.Label>
            <Form.Control type="password" placeholder="Confirma tu contraseña" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} required />
          </Form.Group>
          <Button variant="success" type="submit" className="mt-3">Cambiar Contraseña</Button>
        </Form>
      )}

      {mensaje && <Alert variant="success" className="mt-3">{mensaje}</Alert>}
      {error && <Alert variant="danger" className="mt-3">{error}</Alert>}
    </Container>
  );
};

export default RecoverPassword;
