El módulo contiene el desarrollo para añadir un nuevo modelo purchase_order_invoice_mail_followers_extra que está disponible en Odoo desde el apartado Compras > Compras > Seguidores extra compras

El objetivo de este módulo es que para un contacto (contacto A) podamos añadir seguidores adicionales (contacto B, contacto D y contacto E).

Cada vez que se valida una compra se revisa si ese partner_id tiene "Seguidores extra" y en ese caso, los añade como seguidores de la compra. 

Este desarrollo se ha realizado con el objetivo de que al enviar por email una compra (por defecto cualquier email se envía a todos los seguidores de la compra -salvo al remitente) llegue a diferentes personas de Contabilidad, etc sin necesidad de añadir a los seguidores manualmente.
