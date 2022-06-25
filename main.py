# from kivymd.app import MDApp
# from kivymd.uix.screen import MDScreen
# from kivymd.uix.button import MDRectangleFlatButton


# class MainApp(MDApp):
#     def build(self):
#         self.theme_cls.theme_style = "Dark"  # "Light"
#         screen = MDScreen()
#         screen.add_widget(
#             MDRectangleFlatButton(
#                 text="Hello, World",
#                 pos_hint={"center_x": 0.5, "center_y": 0.5},
#             )
#         )
#         return screen


# MainApp().run()

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
msg = "Playing the song Faded"
class Demo(MDApp):


	def build(self):

		# defining screen
		screen = MDScreen()
		self.theme_cls.theme_style = "Dark"

		# defining 1st label
		l = MDLabel(text="Welcome!", pos_hint={'center_x': 0.8,
											'center_y': 0.8},
					theme_text_color="Custom",
					text_color=(0.5, 0, 0.5, 1),
					font_style='Caption')

		# defining 2nd label
		# l1 = MDLabel(text=msg, pos_hint={'center_x': 0.5,
		# 								'center_y': 0.5},
		# 			theme_text_color="Custom",
		# 			text_color=(0.7, 0, 0.4, 1),
		# 			font_style='H2')

		# defining 3rd label
		# l2 = MDLabel(text="Welcome!", pos_hint={'center_x': 0.8,
		#                                         'center_y': 0.2},
		#              theme_text_color="Custom",
		#              text_color=(0.5, 0, 0.5, 1),
		#              font_style='H1')
		display_label = MDLabel(text=msg.title(),
					halign="center",
					theme_text_color="Custom",
					text_color=(0.5, 0, 0.5, 1),
					font_style='H2')

		screen.add_widget(display_label)

		# screen.add_widget(l1)
		# screen.add_widget(l2)
		return screen


if __name__ == "__main__":
	Demo().run()