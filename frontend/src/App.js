import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./componentes/Login";
import Register from "./componentes/Register";
import RecoverPassword from "./componentes/RecoverPassword";
//import Procedures from "./componentes/Procedures.jsx";


function App() {
  return (
    <Router>
      <Routes>
        
        <Route path="/login" element={<Login />} />  // 🔥 Se agrega la ruta correcta para login
        <Route path="/register" element={<Register />} />
        <Route path="/recover-password" element={<RecoverPassword />} />
        {/* <Route path="/Procedures" element={<Procedures />} /> */}
      </Routes>
    </Router>
  );
}

export default App;
