(sqlite3 clientes.sqlite < clientes.sql )

# Base de datos en SQLite3

## Crear la base de datos apartir de un script 

```bash
sqlite3 clientes.sqlite < clientes.sql
```

## Consulto las tablas que existen
```bash
.table
```
## Consulto los campos tablas
```bash
.schema
```

## Consulto la descripcion
```bash
.show
```
## Solo cabeceras
```bash
.header ON
```

## Ordeno mis campos por columnas
```bash
.mode colum|list|csv
```
## Salir de sqlite
```bash
.quit
```