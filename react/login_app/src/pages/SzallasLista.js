
import { useEffect, useState } from "react";
import { useNavigate, NavLink } from "react-router-dom";
import { fetchHitelesitessel } from "../services/AuthService";

export function SzallasLista() {
  const [szallasok, setSzallasok] = useState([]);
  const [isPending, setPending] = useState(false);
  const history = useNavigate();

  useEffect(() => {
    setPending(true);
    fetchHitelesitessel
      .get("https://kodbazis.hu/api/szallasok")
      .then((res) => res.data)
      .then((tartalom) => {
        setPending(false);
        setSzallasok(tartalom);
      })
      .catch(() => {
        setPending(false);
        history.push("/");
      });
  }, [history]);

  return "szállás lista";
}

    