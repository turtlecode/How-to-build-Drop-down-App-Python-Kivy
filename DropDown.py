import kivy
kivy.require('1.9.0')
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp

dropdown = DropDown()
for index in range(10):

    btn = Button(text='Value % d' % index, size_hint_y=None, height=40)
    btn.bind(on_release=lambda btn: dropdown.select(btn.text))
    dropdown.add_widget(btn)
    mainbutton = Button(text='Hello', size_hint=(None, None), pos=(350, 300))
    mainbutton.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

runTouchApp(mainbutton)



