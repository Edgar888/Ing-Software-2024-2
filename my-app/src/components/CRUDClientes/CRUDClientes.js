import React, { useState } from 'react';

const CRUDClientes = () => {
    // Estado para almacenar la lista de clientes
    const [clientes, setClientes] = useState([]);

    // Estado para almacenar los datos de un cliente nuevo o para editar
    const [clienteData, setClienteData] = useState({
        id: null,
        nombre: '',
        apellido: '',
        email: ''
    });

    // Función para manejar cambios en los campos del formulario
    const handleChange = (e) => {
        const { name, value } = e.target;
        setClienteData({ ...clienteData, [name]: value });
    };

    // Función para agregar un nuevo cliente
    const agregarCliente = () => {
        // Aquí puedes agregar la lógica para enviar los datos del cliente al backend
        // y actualizar la lista de clientes
        // Ejemplo de cómo podrías hacerlo:
        // fetch('/api/clientes', {
        //     method: 'POST',
        //     body: JSON.stringify(clienteData),
        //     headers: {
        //         'Content-Type': 'application/json'
        //     }
        // })
        // .then(response => response.json())
        // .then(data => {
        //     setClientes([...clientes, data]);
        //     setClienteData({ id: null, nombre: '', apellido: '', email: '' });
        // })
        // .catch(error => console.error('Error al agregar cliente:', error));
    };

    // Aquí podrías implementar funciones similares para editar, eliminar y listar clientes

    return (
        <div>
            <h2>CRUD de Clientes</h2>
            <form>
                <input type="text" name="nombre" value={clienteData.nombre} onChange={handleChange} placeholder="Nombre" />
                <input type="text" name="apellido" value={clienteData.apellido} onChange={handleChange} placeholder="Apellido" />
                <input type="email" name="email" value={clienteData.email} onChange={handleChange} placeholder="Correo electrónico" />
                <button type="button" onClick={agregarCliente}>Agregar Cliente</button>
            </form>
            {/* Aquí podrías mostrar la lista de clientes y agregar funcionalidades para editar y eliminar */}
        </div>
    );
};

export default CRUDClientes;
