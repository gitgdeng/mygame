class Settings():
	""" 存储外星人入侵的所有设置的类  """

	def __init__(self):
		""" 初始化游戏的设置 """
		# 屏幕设置
		self.screen_width = 500
		self.screen_height = 400
		self.bg_color = (230, 230, 230)

		# 飞船的设置
		self.ship_speed_factor = 1.5
		self.ship_limit = 1

		# 子弹设置
		self.bullet_speed_factor = 30
		self.bullet_width = 30
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullet_allowed = 300

		# 外星人设置
		self.alien_speed_factor = 10
		self.fleet_drop_speed = 3
		# fleet_direction 为1表示右，-1为左
		self.fleet_direction = 1

		# 以什么样的速度加快游戏节奏
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		""" 初始化随游戏进行而变化的设置 """
		self.ship_speed_factor = 1.8
		self.bullet_speed_factor = 36
		self.alien_speed_factor = 12

		# fleet_direction 为1表示右，-1为左
		self.fleet_direction = 1

	def increase_speed(self):
		""" 提高速度设置 """
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale


