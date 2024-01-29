import click
from cloud.management.commands.setenvcloud import setenv
from cloud.management.commands.setupcloud import setup
from cloud.management.commands.cleancloud import clean


@click.group()
def main():
    pass


commands = [setenv, setup, clean]

for c in commands:
    main.add_command(c)

if __name__ == "__main__":
    main()
