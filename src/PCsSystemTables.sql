create table Producto(
	fabricante varchar(30),
	modelo varchar(20) primary key,
	tipo varchar(9) check (upper(tipo) = 'PC' or upper(tipo) = 'LAPTOP' or upper(tipo) = 'IMPRESORA')
);

create table PC(
	modelo varchar(20) primary key references Producto(modelo),
	velocidad float,
	ram int,
	disco int,
	precio float
);