from db_conn import DB_CONN
from matches import Match

class UserCoupon(object):

	def __init__(self, user_id, coupon_id):
		self.start_date = None
		self.end_date = None
		self.bets = []

	def won(self):
		pass

	def ratio(self):
		pass

	def add_bet(self, match, col_i):
		self.bets.append([match, col_i])
		if self.start_date is None or self.start_date > match.datetime
		pass

	def save(self):
		pass
