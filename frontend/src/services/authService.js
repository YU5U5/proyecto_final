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