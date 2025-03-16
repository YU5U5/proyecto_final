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
