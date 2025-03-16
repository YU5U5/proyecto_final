import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./componentes/Login";
import Register from "./componentes/Register";  // ✅ Verifica que la importación es correcta

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />  // ✅ Página de inicio
        <Route path="/register" element={<Register />} />  // ✅ Ruta corregida (sin "/")
      </Routes>
    </Router>
  );
}

export default App;
