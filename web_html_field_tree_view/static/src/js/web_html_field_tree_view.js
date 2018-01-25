// © 2018 Robert J Sullivan
// License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

odoo.define('web_html_field_tree_view.ColumnHtml', function (require) {
    "use strict";

    var core = require('web.core');
    var listview = require('web.ListView');
    var formats = require('web.formats');
    var registry = core.list_widget_registry;

    var ColumnHtml = listview.Column.extend({
        _format: function (row_data, options) {
        // Removed _.escape() function to display html content.
        // Before : return _.escape(formats.format_value(row_data[this.id].value, this, options.value_if_empty));
        return formats.format_value(row_data[this.id].value, this, options.value_if_empty);
        }
    });

    registry.add('field.formattedhtml', ColumnHtml);
});