import API_URL from "../config";

export const loginUser = async (credentials) => {
  try {
    const response = await fetch(`${API_URL}/api/login/`, { 
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "ngrok-skip-browser-warning": "true",
      },
      body: JSON.stringify(credentials),
      credentials: "include",
    });

    if (!response.ok) {
      throw new Error("Error en el login");
    }

    return await response.json();
  } catch (error) {
    console.error("❌ Error en el login:", error);
    throw error;
  }
};


//............registro...............................................................................


export const registerUser = async (userData) => {
  try {
    console.log("🔍 Enviando datos al backend:", userData);

    const response = await fetch(`${API_URL}/registro/register/`, { // ✅ URL corregida
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "ngrok-skip-browser-warning": "true",
      },
      body: JSON.stringify(userData),
      credentials: "include",
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error("❌ Error en el registro:", errorData);
      throw new Error(errorData.mensaje || "Error en el registro");
    }

    return await response.json();
  } catch (error) {
    console.error("❌ Error en el registro:", error);
    throw error;
  }
};

//................. recoverpassword...................................................................


// 🔹 Solicitar código de recuperación
export const solicitarRecuperacion = async (email) => {
  const response = await fetch(`${API_URL}/recover_password/solicitar/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ correo_electronico: email }),
  });

  if (!response.ok) throw new Error("Error en la solicitud de recuperación.");
  return await response.json();
};

export const confirmarToken = async (token) => {
  const response = await fetch(`${API_URL}/recover_password/confirmar/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ token }),
  });

  if (!response.ok) throw new Error("Código inválido.");
  return await response.json();
};

export const restablecerContraseña = async (token, password, confirmPassword) => {
  const response = await fetch(`${API_URL}/recover_password/restablecer/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ token, nueva_contraseña: password, confirmar_contraseña: confirmPassword }),
  });

  if (!response.ok) throw new Error("Error al restablecer la contraseña.");
  return await response.json();
};
