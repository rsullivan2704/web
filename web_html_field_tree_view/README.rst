.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=======================
HTML Field in Tree View
=======================

Column extension to properly display html data in a tree view.

This module was adapted from the code found `here
<https://stackoverflow.com/questions/45102334/display-html-in-tree-view-odoo>`_.


Installation
============

To install this module, you need to:

* Go to Apps
* Search by the module name "HTML Field in Tree View" or by the module technical name "*web_html_field_tree_view*"
* Click install button

Usage
=====

This module adds a new field type (formattedhtml) to Odoo. Any field defined using this type will render its html value as formatted html in a list/tree view. 

When using *formattedhtml* in a field definition (within another module) the model should include the following import statement:

* **from odoo.addons import web_html_field_tree_view**

Known issues
============

* Fields defined as *formattedhtml* will throw an error when viewing them in a form view. The workaround is to add **widget="html"** to the field definition in the form view.


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/rsullivan2704/web/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.


Credits
=======

Contributors
------------

* Robert J Sullivan

Maintainer
----------

This module is maintained by Robert J Sullivan
