/** @odoo-module **/

import { KanbanRenderer } from "@web/views/kanban/kanban_renderer";
import { patch } from "@web/core/utils/patch";
import { onWillStart } from "@odoo/owl";

// Parcheamos el KanbanRenderer para agregar lógica condicional al renderizar las tarjetas.
patch(KanbanRenderer.prototype, {
    setup() {
        super.setup();
        // Puedes usar un hook para ejecutar código antes de que el componente se renderice.
        onWillStart(async () => {
            // No necesitamos hacer mucho aquí si solo vamos a añadir un botón específico.
            // La lógica para el botón se añade en el XML de plantilla qweb del Kanban.
        });
    },
    // Sobreescribimos el método para obtener las props de cada card si es necesario
    // o simplemente añadimos la lógica al template.
    // getRecordProps(record) {
    //     const props = super.getRecordProps(record);
    //     // Aquí puedes añadir props personalizadas si las necesitas en tu plantilla
    //     // Por ejemplo, props.isAccountingModule = record.data.name === 'account';
    //     return props;
    // }
});