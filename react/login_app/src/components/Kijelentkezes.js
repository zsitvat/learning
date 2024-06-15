
import { useNavigate } from "react-router-dom";
import { logout } from "../services/AuthService";

export function Kijelentkezes() {
  const history = useNavigate();

  return (
    <button
      className="btn btn-danger m-3 float-right"
      onClick={() => {
        logout().finally(() => {
          history.push("/");
        });
      }}
    >
      Kijelentkezés
    </button>
  );
}

    