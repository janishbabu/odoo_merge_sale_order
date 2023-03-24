from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        product_dict = {}
        for record in self.order_line:
            print(record, 'orderline')
            price_template = str(record.price_unit) + str('_') + str(
                record.product_template_id.id)
            print(price_template, 'aaaaaaaaaa')
            if price_template in product_dict:
                product_dict[price_template].append(record.id)
                print(product_dict[price_template], 'aabbbbb')
            else:
                product_dict[price_template] = []
                product_dict[price_template].append(record.id)
                print(product_dict[price_template], 'ccccccc')
        print(product_dict, 'final stage')
        for record1 in product_dict:
            print(record1, 'iiiiiiiiii')
            qty = 0
            for record2 in product_dict[record1]:
                print(record2, 'jjjjjjjjjjj')
                if product_dict[record1].index(record2) != 0:
                    qty += self.env['sale.order.line'].browse(
                        record2).product_uom_qty
                    price = self.env['sale.order.line'].browse(record2).price_unit
                    self.env['sale.order.line'].browse(record2).unlink()
                else:
                    qty += self.env['sale.order.line'].browse(
                        record2).product_uom_qty
                    price = self.env['sale.order.line'].browse(record2).price_unit

            self.env['sale.order.line'].browse(
                product_dict[record1][0]).product_uom_qty = qty
            self.env['sale.order.line'].browse(
                product_dict[record1][0]).price_unit = price
        res = super(SaleOrderLine, self).action_confirm()
        # res = super(SaleOrderLine, self).action_open_label_layout()
        return res
