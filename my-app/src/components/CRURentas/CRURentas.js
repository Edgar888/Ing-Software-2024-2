// CRURentas.js

import React, { useState } from 'react';

const CRURentas = () => {
  // Estado para almacenar los datos de la renta
  const [rentaData, setRentaData] = useState({
    idUsuario: '',
    idPelicula: '',
    fechaRenta: '',
    diasRenta: '',
    entregada: false
  });

  // Función para manejar cambios en los campos del formulario
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setRentaData({
      ...rentaData,
      [name]: value
    });
  };

  // Función para manejar el envío del formulario
  const handleSubmit = (event) => {
    event.preventDefault();
    // Aquí puedes manejar la lógica para enviar los datos al servidor
    console.log('Datos de renta enviados:', rentaData);
    // Puedes resetear los campos del formulario si es necesario
    setRentaData({
      idUsuario: '',
      idPelicula: '',
      fechaRenta: '',
      diasRenta: '',
      entregada: false
    });
  };

  return (
    <div className="crud-rentas">
      <h2>CRU Rentas</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="idUsuario"
          value={rentaData.idUsuario}
          onChange={handleInputChange}
          placeholder="ID Usuario"
          required
        />
        <input
          type="text"
          name="idPelicula"
          value={rentaData.idPelicula}
          onChange={handleInputChange}
          placeholder="ID Película"
          required
        />
        <input
          type="date"
          name="fechaRenta"
          value={rentaData.fechaRenta}
          onChange={handleInputChange}
          placeholder="Fecha de Renta"
          required
        />
        <input
          type="number"
          name="diasRenta"
          value={rentaData.diasRenta}
          onChange={handleInputChange}
          placeholder="Días de Renta"
          required
        />
        <button type="submit">Agregar Renta</button>
      </form>
    </div>
  );
};

export default CRURentas;
