from models.cliente_producto import Cliente_producto as Cliente_productoModule
from schemas.cliente_producto import Cliente_producto
from models.cliente_producto import Cliente_producto  as Cliente_productoModel
from models.sso_cliente import Sso_cliente as Sso_clienteModel
from models.producto import Producto  as ProductoModel
from schemas.cliente_producto import Cliente_producto

class Cliente_productoService():

    def __init__(self,db) -> None:
        self.db = db

    def get_cliente_producto(self):      
        result = self.db.query(Cliente_productoModule).all()
        cliente_producto_list = [
            {
                "clip_id": cliente_producto.cli_id,
                "clip_idcliente": cliente_producto.clip_idcliente,
                "clip_idproducto": cliente_producto.clip_idproducto,    
                "clip_estado":cliente_producto.clip_estado,            
                "clip_latitud": cliente_producto.clip_latitud,
                "clip_longitud": cliente_producto.clip_longitud,
                "clip_cantidad":cliente_producto.clip_cantidad,
                "nombres": cliente_producto.sso_cliente.cli_nombres,
                "apellidos": cliente_producto.sso_cliente.cli_apellidos,
                "producto": cliente_producto.producto.pro_nombre,                
            }
            for cliente_producto in result
        ]
        return cliente_producto_list
    
    
    def create_cliente_producto(self, cliente_producto: Cliente_producto):
        try:
            
            with self.db.begin() as transaction:                
                producto = self.db.query(ProductoModel).filter_by(pro_id=cliente_producto.clip_idproducto).first()
                if not producto:
                    raise ValueError("Producto no encontrado")
                
                cliente = self.db.query(Sso_clienteModel).filter_by(cli_id=cliente_producto.clip_idcliente).first()
                if not cliente:
                    raise ValueError("Cliente no encontrado")
                
                puntos_necesarios = producto.pro_puntos * cliente_producto.clip_cantidad

                if cliente.cli_totalpuntos < puntos_necesarios:
                    raise ValueError("El cliente no tiene suficientes puntos") 

                if producto.pro_cantidad < cliente_producto.clip_cantidad:
                    raise ValueError("No hay suficiente cantidad del producto")                       
                cliente.cli_totalpuntos -= puntos_necesarios
                
                producto.pro_cantidad -= cliente_producto.clip_cantidad
                
                new_punto = Cliente_productoModel(
                    clip_idcliente=cliente_producto.clip_idcliente,
                    clip_idproducto=cliente_producto.clip_idproducto,
                    clip_estado=cliente_producto.clip_estado,
                    clip_latitud=cliente_producto.clip_latitud,
                    clip_longitud=cliente_producto.clip_longitud,
                    clip_cantidad=cliente_producto.clip_cantidad,
                    clip_direccion_apartamento=cliente_producto.clip_direccion_apartamento,
                    clip_barrio_conjunto=cliente_producto.clip_barrio_conjunto,
                )
                self.db.add(new_punto)
                
                self.db.commit()

        except Exception as e:
            print(f"Error en la inserción: {str(e)}")
            self.db.rollback()
            raise

    def update_cliente_producto(self, id: int, cliente_producto: Cliente_producto):
        result = self.db.query(Cliente_productoModel).filter(Cliente_productoModel.clip_id == id).first()
        result.clip_idcliente=cliente_producto.clip_idcliente
        result.clip_idproducto= cliente_producto.clip_idproducto              
        result.clip_estado=cliente_producto.clip_estado
        result.clip_latitud=cliente_producto.clip_latitud
        result.clip_longitud=cliente_producto.clip_longitud
        result.clip_cantiad= cliente_producto.clip_cantidad
        result.clip_direccion_apartamento=cliente_producto.clip_direccion_apartamento
        result.clip_barrio_conjunto=cliente_producto.clip_barrio_conjunto              
        self.db.commit()
        return