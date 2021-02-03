# -*- coding: utf-8 -*-
from odoo import api, fields, models
from pprint import pprint

    
class FocPrint(models.Model):
    _inherit = 'account.move'
 
    def foc_price(self):
        price_dict = {}
        for line in self.invoice_line_ids:
            if line.price_unit != 0:
                
                product_id = line.product_id.id
                qty = line.quantity
                price_dict[product_id] =   {'code':line.product_id.default_code,'quantity':line.quantity,'unit_price':line.price_unit,'name':line.product_id.name,'foc':0.0,'price_subtotal':line.price_subtotal}
        return price_dict
    
    def foc_dict(self):
        foc_dict = {}
        for line in self.invoice_line_ids:
            if line.price_unit == 0:
                
                product_id = line.product_id.id
                qty = line.quantity
                foc_dict[product_id] =  {'code':line.product_id.default_code,'quantity':0.0,'unit_price':line.price_unit,'name':line.product_id.name,'foc':line.quantity,'price_subtotal':line.price_subtotal}
        return foc_dict

    
    def full_dictionary(self):
        foc_dict = self.foc_dict()
        price_dict = self.foc_price()
        # product_id_list = {}
        product_set = set()
        full_dict = {}
        full_set = []
        for line in self.invoice_line_ids:
            product_set.add(line.product_id.id)
            # product_id_list.append(line.product_id.id)
        
        for product in product_set:
           
            foc_bool = foc_dict.get(product,False)
            price_bool = price_dict.get(product,False)
            
            if foc_bool and price_bool:
                vals ={
                    'product_id':product,
                    'code':price_bool.get('code',''),
                    'name':price_bool.get('name',''),
                    'quantity':price_bool.get('quantity',0.0),
                    'unit_price':price_bool.get('unit_price',0.0),
                    'foc':foc_bool.get('foc',0.0),
                    'price_subtotal':price_bool.get('price_subtotal')
                }     
            if foc_bool and not price_bool: 
                vals ={
                    'product_id':product,
                    'code':foc_bool.get('code',''),
                    'name':foc_bool.get('name',''),
                    'quantity':foc_bool.get('quantity',0.0),
                    'unit_price':foc_bool.get('unit_price',0.0),
                    'foc':foc_bool.get('foc',0.0),
                    'price_subtotal':foc_bool.get('price_subtotal')
                }      
            if price_bool and not foc_bool:
                vals ={
                    'product_id':product,
                    'code':price_bool.get('code',''),
                    'name':price_bool.get('name',''),
                    'quantity':price_bool.get('quantity',0.0),
                    'unit_price':price_bool.get('unit_price',0.0),
                    'foc':price_bool.get('foc',0.0),
                    'price_subtotal':price_bool.get('price_subtotal')
                }
            full_set.append(vals)
        print("Printing full set")
        pprint(full_set)
        return full_set
                    
                        
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # def foc_adding(self):
    #     counter = 0
    #     in_counter = 0
    #     no_counter = 0
        
        
    #     for line in self.invoice_line_ids:
    #         counter += 1 
    #         if line.price_unit == 0:
    #             in_counter += 1
    #         elif line.price_unit != 0:
    #             no_counter +=1
    #     if counter == in_counter or counter == no_counter:
    #         result = []
    #         if counter == in_counter:
    #             print("counter........", counter)
    #             print("in_counter.........", in_counter)    
    #             for line in self.invoice_line_ids:
    #                 product_idno = line.product_id.id
    #                 product_id = line.product_id
    #                 label = line.name
    #                 price = line.price_unit
    #                 subtotal = line.price_subtotal
    #                 qty = line.quantity
    #                 dummy = {}
    #                 dummy["product_id"] = product_id.name
    #                 dummy["product_idno"] = product_idno
    #                 dummy["label"] = label
    #                 dummy["price"] = price
    #                 dummy["subtotal"] = subtotal
    #                 dummy["foc"] = 0
    #                 dummy["qty"] = qty                      
    #                 result.append(dummy)
    #         elif counter == no_counter:
    #             print("counter........", counter)
    #             print("no_counter.........", no_counter)    
    #             for line in self.invoice_line_ids:
    #                 product_idno = line.product_id.id
    #                 product_id = line.product_id
    #                 label = line.name
    #                 price = line.price_unit
    #                 subtotal = line.price_subtotal
    #                 qty = line.quantity
    #                 dummy = {}
    #                 dummy["product_id"] = product_id.name
    #                 dummy["product_idno"] = product_idno
    #                 dummy["label"] = label
    #                 dummy["price"] = price
    #                 dummy["subtotal"] = subtotal
    #                 dummy["foc"] = 0
    #                 dummy["qty"] = qty                      
    #                 result.append(dummy)
                        
            
    #         print("this is cool.")
            
    #         return result
    #     else:
    #         table = self.foc_quantity_result()
    #         foc = self.foc_noprice()
    #         for dict in table:
    #             for key,value in foc.items():
    #                 if dict['product_idno'] == key:
    #                     dict['foc'] = value
    #         return(table)
