import click
import graphics
import time

click.echo(graphics.APP_NAME)
time.sleep(1)
click.echo('\nWelcome to Foliage Friend!\n')

graphics.type_out('\nThis app is designed to help you choose the best plants based on your specific needs and preferences.\n'
               'Whether you are looking for plants that are easy to care for,\n'
               'delicious to eat, or simply for the ✨ aesthetics ✨, this app has got it covered.\n')

graphics.type_out('Simply answer a few questions about you and our app will recommend the perfect plants for you.\n')
graphics.type_out('We hope you enjoy using our app and discovering new plants to add to your collection!\n')

