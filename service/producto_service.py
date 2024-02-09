from sqlalchemy import func
from models.producto import Producto  as ProductoModel
from schemas.producto import Producto
from models.cliente_producto import Cliente_producto  as Cliente_productoModule
from schemas.cliente_producto import Cliente_producto

class ProductoService():

    def __init__(self,db) -> None:
        self.db = db

    def get_producto(self):      
        result = self.db.query(ProductoModel).filter(ProductoModel.pro_estado== 1).all()
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
            new_producto = ProductoModel(
                pro_empresa=producto.pro_empresa,
                pro_estado=producto.pro_estado,
                pro_foto=producto.pro_foto,
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
        result.pro_foto = producto.pro_foto
        result.pro_nombre = producto.pro_nombre
        result.pro_puntos = producto.pro_puntos
        result.pro_cantidad = producto.pro_cantidad                
        self.db.commit()
        return
    