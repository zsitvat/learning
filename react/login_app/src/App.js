
import "./App.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Bejelentkezes } from "./components/Bejelentkezes";
import { SzallasLista } from "./pages/SzallasLista";
import { SzallasSingle } from "./pages/SzallasSingle";
import "bootstrap/dist/css/bootstrap.min.css"

export default function App() {
  return (
    <BrowserRouter>
      <Routes>

      <Route path="/" exact element={<Bejelentkezes/>} />
        <Route path="/bejelentkezes"  element={<Bejelentkezes/>} />

        <Route path="/osszes-szallas" element={<SzallasLista/>} />

        <Route path="/szallas-:szallasId">
          {(props) => <SzallasSingle id={props.match.params.szallasId} />}
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

    