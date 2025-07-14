{
    'name': 'SCSS para list_renderer de modulo facturacion', # Nombre que verás en la lista de Apps de Odoo
    'summary': 'Módulo para aplicar estilos SCSS personalizados en la interfaz de Odoo.',
    'description': """
            Este módulo contiene estilos SCSS para el modulo de facturacion y los estilos de la tabla.
        """,
        'author': 'Duvan',
        'website': 'hhttp://localhost:8069/', # Opcional: puedes poner tu URL o dejarlo
        'category': 'Front', # Categoría donde aparecerá en la lista de Apps
        'version': '1.0',
        'depends': ['web', 'base'], # ¡MUY IMPORTANTE! Tu módulo *debe* depender de 'web'
                            # Esto asegura que tus estilos se carguen *después* de los de Odoo,
                            # permitiendo que tus reglas sobrescriban las predeterminadas.
        'data': [
            # Aquí irían archivos XML de vistas, reglas de seguridad, etc., si tuvieras.
            'static/views/actionList.xml',
            # Para este módulo de CSS simple, no necesitas nada aquí por ahora.
        ],
        'assets': {
            # Este es el bundle de assets para el front.
            'web.assets_backend': [
                # Aquí especificas la ruta a tu archivo SCSS.
                # La ruta es relativa a la *raíz de tu módulo* (webNew/).
                'webNew/static/src/src/scss/list_renderer1.scss',
                'webNew/static/views/viewList.xml',
            ],
            # Si en algún momento necesitas que tus estilos también afecten la parte pública
            # de Odoo (ej. sitio web, portal), los agregarías aquí:
            # 'web.assets_frontend': [
            #     'mi_personalizacion_odoo_css/static/src/scss/list_renderer1.scss',
            # ],
        },
        'installable': True, # Indica que el módulo puede ser instalado en Odoo.
        'application': False, # Usualmente 'False' para módulos de personalización de UI.
        'auto_install': False, # Si es 'True', se instalará automáticamente si sus dependencias se instalan.
        'license': 'LGPL-3', # La licencia de tu módulo (puedes elegir otra si lo deseas).
    }