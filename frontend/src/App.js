import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./componentes/Login";
import Register from "./componentes/Register";
import RecoverPassword from "./componentes/RecoverPassword";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />  // ✅ Página de inicio
        <Route path="/login" element={<Login />} />  // 🔥 Se agrega la ruta correcta para login
        <Route path="/register" element={<Register />} />
        <Route path="/recover-password" element={<RecoverPassword />} />
      </Routes>
    </Router>
  );
}

export default App;
