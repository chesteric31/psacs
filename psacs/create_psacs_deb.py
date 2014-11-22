from py2deb import Py2deb

p=Py2deb("psacs")
p["/usr/bin"] = ["core/psacs.py|psacs",]
p.author="chesteric31"
p.mail="chesteric31@gmail.com"
p.description="""PSACS for Python Simplified Auto Click System is a system that clicks the mouse for you.
This is very helpful to people with RSI (Repetitive Strain Injury) or similar problems."""
p.generate("1.0.0")

