// CRUDPeliculas.js

import React, { useState } from 'react';

const CRUDPeliculas = () => {
  // Estado para almacenar la lista de películas
  const [peliculas, setPeliculas] = useState([]);
  
  // Estado para almacenar los datos de la nueva película a agregar
  const [nuevaPelicula, setNuevaPelicula] = useState({
    nombre: '',
    genero: '',
    duracion: ''
  });

  // Función para manejar cambios en los campos del formulario de nueva película
  const handleChange = (e) => {
    const { name, value } = e.target;
    setNuevaPelicula({ ...nuevaPelicula, [name]: value });
  };

  // Función para agregar una nueva película a la lista
  const agregarPelicula = () => {
    setPeliculas([...peliculas, nuevaPelicula]);
    // Limpiar el formulario después de agregar la película
    setNuevaPelicula({ nombre: '', genero: '', duracion: '' });
  };

  // Función para eliminar una película de la lista
  const eliminarPelicula = (index) => {
    const nuevasPeliculas = peliculas.filter((_, i) => i !== index);
    setPeliculas(nuevasPeliculas);
  };

  return (
    <div>
      <h2>CRUD de Películas</h2>

      {/* Formulario para agregar una nueva película */}
      <form onSubmit={(e) => e.preventDefault()}>
        <input
          type="text"
          name="nombre"
          placeholder="Nombre de la película"
          value={nuevaPelicula.nombre}
          onChange={handleChange}
        />
        <input
          type="text"
          name="genero"
          placeholder="Género"
          value={nuevaPelicula.genero}
          onChange={handleChange}
        />
        <input
          type="number"
          name="duracion"
          placeholder="Duración (minutos)"
          value={nuevaPelicula.duracion}
          onChange={handleChange}
        />
        <button onClick={agregarPelicula}>Agregar Película</button>
      </form>

      {/* Lista de películas */}
      <ul>
        {peliculas.map((pelicula, index) => (
          <li key={index}>
            {pelicula.nombre} - {pelicula.genero} ({pelicula.duracion} minutos)
            <button onClick={() => eliminarPelicula(index)}>Eliminar</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CRUDPeliculas;
