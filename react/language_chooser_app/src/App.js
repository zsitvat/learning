import './App.css';
import React from 'react';
import dict from './dict';
import 'bootstrap/dist/css/bootstrap.css';


const Context = React.createContext();

function App() {
  const [language, setLanguage] = React.useState("hun");

  return (
    <Context.Provider value={{language, setLanguage}}>
      <div className="container">
        <LanguageChooser/>
        <Container/>
      </div>
    </Context.Provider>
  )

}

const Container = () => {
  return (
    <div className="container-fluid">
      <Frame />
    </div>
  );
};

const LanguageChooser = () => {
  const { language, setLanguage } = React.useContext(Context);

  return (
    <nav className="navbar navbar-light bg-light p-0">
      <label className="w-100 p-3">
        <h3>{dict[language].changeLanguage}:</h3>
        <select
          className="form-control"
          defaultValue={language}
          onChange={(e) => {
            setLanguage(e.target.value);
          }}
        >
          <option value="hun">{dict[language].hungarian}</option>
          <option value="en">{dict[language].english}</option>
          <option value="spa">{dict[language].spanish}</option>
        </select>
      </label>
    </nav>
  );
};

const Frame = () => {
  return (
    <div className="border p-5 bg-secondary">
      <div className="row">
        <Greetings />
        <Content />
      </div>
      <div className="row">
        <Footer />
      </div>
    </div>
  );
};

const Greetings = () => {
  const { language } = React.useContext(Context);

  return (
    <div className="col-6 bg-warning jumbotron m-0 rounded-0">
      <h1>{dict[language].greetings}!</h1>
    </div>
  );
};

const Content = () => {
  const { language } = React.useContext(Context);

  return (
    <div className="col-6 bg-light text-dark jumbotron m-0 rounded-0">
      <p>{dict[language].content}</p>
    </div>
  );
};

const Footer = () => {
  const { language } = React.useContext(Context);

  return (
    <div className="col-12 bg-dark text-light jumbotron m-0 rounded-0">
      <p>{dict[language].goodLuck}</p>
    </div>
  );
};


export default App;
