from models.cliente_producto import Cliente_producto as Cliente_productoModule
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
    
        
    def update_cliente_producto(self, id: int, cliente_producto: Cliente_producto):
        result = self.db.query(Cliente_productoModule).filter(Cliente_productoModule.clip_id == id).first()
        result.reg_idcomuna = cliente_producto.reg_idcomuna
        result.reg_plastico = cliente_producto.reg_plastico
        result.reg_papel = cliente_producto.reg_papel
        result.reg_carton = cliente_producto.reg_carton
        result.reg_metal = cliente_producto.reg_metal
        result.reg_vidrio = cliente_producto.reg_vidrio
        result.reg_ubicacion_lag = cliente_producto.reg_ubicacion_lag
        result.reg_ubicacion_log = cliente_producto.reg_ubicacion_log
        result.reg_numero = cliente_producto.reg_numero
        self.db.commit()
        return