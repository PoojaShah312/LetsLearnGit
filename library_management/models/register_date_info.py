from odoo import models,fields,api
from datetime import date

class RegisterDateInfo(models.Model):
	_name = 'register.date.info'

	entry_id = fields.Integer(string="Entry id")
	customer_name = fields.Char(string="Customer Name")
	book_code = fields.Integer(string="Book Code",readonly=True)
	books_name = fields.Char(string="Book name")
	incoming_date = fields.Date(string="Incoming Date",readonly=True)
	outgoing_date = fields.Date(string="Outgoing Date",readonly=True)

	
	def return_button(self):
		model_rec = self.env['issue.book.info'].search([])
		for rec in self:
			rec.incoming_date = date.today()
		for record in model_rec:
			record.return_date = self.incoming_date

		print("><<><<<<><><>>")