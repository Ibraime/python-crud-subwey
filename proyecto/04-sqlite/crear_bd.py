import sqlite3

# 1. Conectar a la base de datos (se crea el fichero si no existe)
conn = sqlite3.connect("subway.db")
cursor = conn.cursor()

# 2. Activar soporte de claves foráneas (SQLite lo trae desactivado por defecto)
cursor.execute("PRAGMA foreign_keys = ON")

# 3. Crear tabla de ingredientes
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredientes (
        nombre TEXT PRIMARY KEY,
        precio REAL NOT NULL CHECK (precio > 0),
        stock INTEGER NOT NULL CHECK (stock >= 0)
    )
""")

# 4. Crear la tabla de usuarios
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        nombre TEXT PRIMARY KEY
    )
""")

# 5. Crear la tabla de bocadillos
cursor.execute("""
CREATE TABLE IF NOT EXISTS bocadillos (
    nombre TEXT PRIMARY KEY,
    autor_nombre TEXT NOT NULL,
    es_promocion INTEGER DEFAULT 0,
    descuento REAL DEFAULT 0,
    FOREIGN KEY (autor_nombre) REFERENCES usuarios(nombre)
)
""")

# 6. Crear tabla de la relación N:M
cursor.execute("""
CREATE TABLE IF NOT EXISTS bocadillo_ingredientes (
    bocadillo_nombre TEXT,
    ingrediente_nombre TEXT,
    PRIMARY KEY (bocadillo_nombre, ingrediente_nombre),
    FOREIGN KEY (bocadillo_nombre) REFERENCES bocadillos(nombre),
    FOREIGN KEY (ingrediente_nombre) REFERENCES ingredientes(nombre)
)
""")

# 7. Insertar datos iniciales, replace para que no de error y los devuelva a su estado por defecto para hacer pruebas

cursor.execute("INSERT OR REPLACE INTO ingredientes (nombre, precio, stock) VALUES ('tomate', 3, 20)")
cursor.execute("INSERT OR REPLACE INTO ingredientes (nombre, precio, stock) VALUES ('aguacate', 7, 8)")
cursor.execute("INSERT OR REPLACE INTO ingredientes (nombre, precio, stock) VALUES ('queso', 2, 42)")


cursor.execute("INSERT OR REPLACE INTO usuarios (nombre) VALUES ('Anónimo')")
cursor.execute("INSERT OR REPLACE INTO usuarios (nombre) VALUES ('Oficial')")
cursor.execute("INSERT OR REPLACE INTO usuarios (nombre) VALUES ('usuario_test')")


cursor.execute("INSERT OR REPLACE INTO bocadillos (nombre, autor_nombre) VALUES ('vegetal', 'Anónimo')")
cursor.execute("INSERT OR REPLACE INTO bocadillo_ingredientes (bocadillo_nombre, ingrediente_nombre) VALUES ('vegetal', 'tomate')")
cursor.execute("INSERT OR REPLACE INTO bocadillo_ingredientes (bocadillo_nombre, ingrediente_nombre) VALUES ('vegetal', 'aguacate')")

cursor.execute("INSERT OR REPLACE INTO bocadillos (nombre, autor_nombre) VALUES ('caprese', 'Anónimo')")
cursor.execute("INSERT OR REPLACE INTO bocadillo_ingredientes (bocadillo_nombre, ingrediente_nombre) VALUES ('caprese', 'tomate')")
cursor.execute("INSERT OR REPLACE INTO bocadillo_ingredientes (bocadillo_nombre, ingrediente_nombre) VALUES ('caprese', 'queso')")

conn.commit()
print("Base de datos creada con datos iniciales.")

# 8. Consultar los datos iniciales
print("\n--- Ingredientes ---")
cursor.execute("SELECT * FROM ingredientes")
for fila in cursor.fetchall():
    print(fila)

print("\n--- Usuarios ---")
cursor.execute("SELECT * FROM usuarios")
for fila in cursor.fetchall():
    print(fila)

print("\n--- Bocadillos ---")
cursor.execute("SELECT * FROM bocadillos")
for fila in cursor.fetchall():
    print(fila)

print("\n--- Bocadillo_Ingrediente ---")
cursor.execute("SELECT * FROM bocadillo_ingredientes")
for fila in cursor.fetchall():
    print(fila)

conn.close()

