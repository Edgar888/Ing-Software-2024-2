// App.js

import React from 'react';
import './App.css';
import CRUDClientes from './components/CRUDClientes/CRUDClientes';
import CRUDPeliculas from './components/CRUDPeliculas/CRUDPeliculas';
import CRURentas from './components/CRURentas/CRURentas';

function App() {
  return (
    <div className="app">
      <h1>Sistema de Gestión de Rentas de Películas</h1>
      <CRUDClientes />
      <CRUDPeliculas />
      <CRURentas />
    </div>
  );
}

export default App;
