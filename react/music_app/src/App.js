import { BrowserRouter,NavLink, Route, Routes } from 'react-router-dom';
import './App.css';
import InstrumentListPage from './pages/InstrumentListPage';
import React from 'react';

function App() {
  return (
    <Navbar />
  );
}

export default App;


const Navbar = () => {
  return ( 
    <BrowserRouter>
      <nav className="navbar navbar-expand-sm navbar-dark bg-dark">
      <div className="collapse navbar-collapse" id="navbarNav">
        <ul className="navbar-nav">
          <li className="nav-item">
              <NavLink to="/" className={(navData) => (navData.isActive ? "active" : 'none')} exact="true">
                <span className="nav-link">Hangszerek</span>
              </NavLink>
          </li>
          <li className="nav-item">
            <NavLink to="/new" className={(navData) => (navData.isActive ? "active" : 'none')} >
              <span className="nav-link">Új hangszer</span>
            </NavLink>
          </li>
        </ul>
      </div>
    </nav>
    <PageRoutes />
  </BrowserRouter>
)
}


const PageRoutes = () => {
  return(
    <Routes>
    <Route path="/" component={InstrumentListPage} exact="true">
    </Route>
    <Route path="/instrument/:id">
      
    </Route>
    <Route path="/new">

    </Route>
  </Routes>

  )
}