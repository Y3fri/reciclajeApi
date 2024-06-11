import base64
from pathlib import Path
from sqlalchemy import func
from models.producto import Producto  as ProductoModel
from schemas.producto import Producto
from models.cliente_producto import Cliente_producto  as Cliente_productoModule
from schemas.cliente_producto import Cliente_producto

class ProductoService():

    def __init__(self,db) -> None:
        self.db = db

    def save_image(self, base64_image: str, product_name: str) -> str:
        try:
            # Decode the base64 string
            base64_image = base64_image.split(",")[1]  # To handle data URLs
            image_data = base64.b64decode(base64_image)
            # Define paths
            product_folder_path = Path(f"images/{product_name}")
            product_folder_path.mkdir(parents=True, exist_ok=True)
            file_name = f"{product_name}.jpeg"
            file_path = product_folder_path / file_name
            # Save the image to the filesystem
            with open(file_path, "wb") as file:
                file.write(image_data)
            # Return the relative path to be stored in the database
            return str(file_path)
        except Exception as e:
            print(f"Error saving image: {str(e)}")
            raise

    def get_producto(self):      
        result = self.db.query(ProductoModel).filter(ProductoModel.pro_estado== 1,ProductoModel.pro_cantidad >= 1).all()
        producto_list = [
            {
                "pro_empresa": producto.pro_empresa,
                "pro_estado": producto.pro_estado,
                "pro_foto": producto.pro_foto,
                "pro_nombre": producto.pro_nombre,
                "pro_puntos": producto.pro_puntos,
                "pro_cantidad": producto.pro_cantidad,
                "pro_id": producto.pro_id,                
                "nombre_empresa": producto.empresa.inf_razon_social,
                "nombre_estado": producto.estado.est_nombre,                
            }
            for producto in result
        ]
        return producto_list
    
    def get_productoTodo(self):      
        result = self.db.query(ProductoModel).all()
        producto_list = [
            {
                "pro_empresa": producto.pro_empresa,
                "pro_estado": producto.pro_estado,
                "pro_foto": producto.pro_foto,
                "pro_nombre": producto.pro_nombre,
                "pro_puntos": producto.pro_puntos,
                "pro_cantidad": producto.pro_cantidad,
                "pro_id": producto.pro_id,                
                "nombre_empresa": producto.empresa.inf_razon_social,
                "nombre_estado": producto.estado.est_nombre,                
            }
            for producto in result
        ]
        return producto_list



    def create_producto(self, producto: Producto):          
        try:            
            file_path = self.save_image(producto.pro_foto, producto.pro_nombre)
            new_producto = ProductoModel(
                pro_empresa=producto.pro_empresa,
                pro_estado=producto.pro_estado,
                pro_foto=file_path,
                pro_nombre=producto.pro_nombre,
                pro_puntos=producto.pro_puntos,
                pro_cantidad=producto.pro_cantidad,                
            )
            self.db.add(new_producto)
            self.db.commit()

        except Exception as e:         
            print(f"Error en la inserción: {str(e)}")
            self.db.rollback()
            raise
    
    def update_producto(self, id: int, producto: Producto):
        result = self.db.query(ProductoModel).filter(ProductoModel.pro_id == id).first()
        result.pro_empresa = producto.pro_empresa
        result.pro_estado = producto.pro_estado        
        if producto.pro_foto != result.pro_foto:            
            file_path = self.save_image(producto.pro_foto, producto.pro_nombre)
            result.pro_foto = file_path
        result.pro_nombre = producto.pro_nombre
        result.pro_puntos = producto.pro_puntos
        result.pro_cantidad = producto.pro_cantidad                
        self.db.commit()
        return
    