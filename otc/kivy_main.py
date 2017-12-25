import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

kivy.resources.resource_add_path('./fonts/')
font1 = kivy.resources.resource_find("SourceHanSansCN-Medium.otf")

class TestApp(App):
	def build(self):
		layout = GridLayout(cols=2)
		for x in range(10):
			layout.add_widget(Label(text='测试',font_name = font1))

		return layout

TestApp().run()