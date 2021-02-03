# -*- coding: utf-8 -*-

##############################################################################
#
#    Author: Al Kidhma
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <https://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'NCP invoice Report ',
    'version': '13.1',
    'category': 'Invoice',
    'sequence': 2,
    'summary': 'NCP invoice Report',
    'description': """
Generate NCP invoice Report
    """,
    'author': 'Al Kidhma',
    'depends': ['account'],
    'data': [
        'report/report_invoice.xml',
        'report/account_report.xml',
        'report/quotation_template.xml',
        'report/quotation_report.xml',
        'report/delivery_template.xml',
        'report/delivery_report.xml',

    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
