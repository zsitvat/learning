import "./App.css";
import React from "react";
import UseEffect from "./useeffect";

function App() {
  return React.createElement(
    "div",
    {
      className: "ms-5 border border-primary p-2 m-2",
    },
    "App",
    React.createElement(BoxComponent3, {
      hatterSzin: "red",
      felirat: "BOX1",
      szam: 0,
    }),
    React.createElement(BoxComponent3, {
      hatterSzin: "blue",
      felirat: "BOX2",
      szam: 10,
    }),
    React.createElement(BoxComponent3, {
      hatterSzin: "green",
      felirat: "BOX3",
      szam: 20,
    }),
    <Aktivalas />,
    <UseEffect />
  );
}

/*
function BoxComponent(props) {
  const [szamlaloAllapota, ujSzamlaloAllapotBeallitasa] = React.useState();
  return React.createElement(
    "div",
    {
      style: {
        width: "200px",
        height: "200px",
        backgroundColor: props.hatterSzin,
      },
      className: "p-2 m-5 rounded",
      onClick: () => {
        ujSzamlaloAllapotBeallitasa("teszt")
      }
    },
    React.createElement("h1", {}, szamlaloAllapota)
  );
}



function BoxComponent2(){
  return <div 
     style={{backgroundColor: "green",width: "100px",height: "100px"}}
      className="box p-2 m-5 rounded">
          Box
          </div>
}
*/

function BoxComponent3(props) {
  const [szam, szamBeallitasa] = React.useState(props.szam);

  return (
    <div
      style={{
        backgroundColor: props.hatterSzin,
        width: "100px",
        height: "100px",
      }}
      className="box p-2 m-5 rounded"
      onClick={() => szamBeallitasa((elozoAllapot) => elozoAllapot + 1)}
    >
      {props.felirat}_{szam}
    </div>
  );
}

/*****************************************/

function Aktivalas(props) {
  const [isActive, setActive] = React.useState(false);
  return (
    <div className="border">
      <Box isActive={isActive} />
      <ButtonComponent isActive={isActive} setActive={setActive} />
      App szintű state:
      {isActive ? " Aktív" : " Inaktív"}
    </div>
  );
}

function Box(props) {
  return (
    <div
      style={{
        width: "200px",
        height: "200px",
        backgroundColor: props.isActive ? "green" : "firebrick",
      }}
    >
      {" "}
      {props.isActive ? "Aktív" : "Inaktív"}
    </div>
  );
}

function ButtonComponent({ isActive, setActive }) {
  return (
    <div
      style={{ width: "200px", height: "200px" }}
      className="p-2 m-5 border rounded"
    >
      <button
        className="btn btn-success m-2"
        disabled={isActive}
        onClick={() => {
          setActive(true);
        }}
      >
        Aktiválás
      </button>
      <button
        className="btn btn-danger m-2"
        disabled={!isActive}
        onClick={() => {
          setActive(false);
        }}
      >
        Deaktiválás
      </button>
    </div>
  );

  /*return React.createElement(
    "div",
    {
      style: {
        width: "200px",
        height: "200px",
      },
      className: "p-2 m-5 border rounded",
    },
    React.createElement(
      "button",
      {
        className: "btn btn-success m-2",
        disabled: isActive,
        onClick: () => {
            setActive(true);
        }
      },
      "Aktiválás"
    ),
    React.createElement(
      "button",
      {
        className: "btn btn-danger m-2",
        disabled: !isActive,
        onClick: () => {
            setActive(false);
        }
      },
      "Deaktiválás"
    )
  );*/
}

export default App;
