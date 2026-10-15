from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tienda.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definición del modelo Product
class Product(db.Model):
    __tablename__ = "products"  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0, nullable=False)  # Valor por defecto 0

    # Representación legible del objeto
    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price}, stock={self.stock})>"

# Función para inicializar y crear las tablas en la base de datos
def init_db():
    with app.app_context():
        # Borramos las tablas existentes para reiniciar limpio con los 10 registros
        db.drop_all()
        db.create_all()
        print("Base de datos y tablas creadas exitosamente.")

# 1. CREATE (Crear 10 registros)
def create_products():
    with app.app_context():
        p1 = Product(name="Laptop Gamer", price=1200.50, stock=5)
        p2 = Product(name="Mouse Inalámbrico", price=25.99, stock=50)
        p3 = Product(name="Teclado Mecánico", price=75.00, stock=15)
        p4 = Product(name="Monitor 24 Pulgadas", price=180.00, stock=10)
        p5 = Product(name="Audífonos Bluetooth", price=45.50, stock=30)
        p6 = Product(name="Silla Ergonómica", price=250.00, stock=8)
        p7 = Product(name="Disco SSD 1TB", price=95.00, stock=25)
        p8 = Product(name="Memoria RAM 16GB", price=65.00, stock=20)
        p9 = Product(name="Tarjeta Gráfica", price=450.00, stock=4)
        p10 = Product(name="Webcam HD", price=35.00, stock=12)

    
        db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        db.session.commit()
        print("\n--- 10 PRODUCTOS CREADOS EXITOSAMENTE ---")


def read_products():
    with app.app_context():
        print("\n--- LISTADO DE TODOS LOS PRODUCTOS ---")
        products = Product.query.all()
        for p in products:
            print(p)

        # Consulta con filtro (ejemplo: productos con precio mayor a 100)
        print("\n--- PRODUCTOS CON PRECIO > 100 ---")
        filtrados = Product.query.filter(Product.price > 100.0).all()
        for p in filtrados:
            print(p)

        # Obtener un solo registro por ID
        print("\n--- BUSCAR PRODUCTO POR ID (ID=1) ---")
        product = Product.query.filter_by(id=1).first()
        if product:
            print(product)
        else:
            print("Producto no encontrado.")


def update_product():
    with app.app_context():
        print("\n--- ACTUALIZANDO PRODUCTO ---")
        product = Product.query.filter_by(id=3).first() # Buscamos el producto 3
        if product:
            product.price = 85.00  # Actualizamos el precio
            product.stock = 18     # Actualizamos el stock
            db.session.commit()
            print("Producto actualizado exitosamente:", product)
        else:
            print("Producto no encontrado para actualizar.")

def delete_product():
    with app.app_context():
        print("\n--- ELIMINANDO PRODUCTO ---")
        product = Product.query.filter_by(id=2).first() # Buscamos el producto 2
        if product:
            db.session.delete(product)
            db.session.commit()
            print("Producto eliminado satisfactoriamente.")
        else:
            print("Producto no encontrado para eliminar.")

# Ejecución principal
if __name__ == "__main__":
    init_db()          # Crea la base de datos limpia
    create_products()  # C (Create) - Inserta los 10 registros
    read_products()    # R (Read)
    update_product()   # U (Update)
    delete_product()   # D (Delete)
    read_products()    