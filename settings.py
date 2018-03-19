class Settings():
	""" 存储外星人入侵的所有设置的类  """

	def __init__(self):
		""" 初始化游戏的设置 """
		# 屏幕设置
		self.screen_width = 400
		self.screen_height = 300
		self.bg_color = (120, 120, 230)

		# 飞船的设置
		self.ship_speed_factor = 3.0

		# 子弹设置
		self.bullet_speed_factor = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_allowed = 3

