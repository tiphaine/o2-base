# -*- coding: utf-8 -*-
import click

from src.data.insee.get_data import get_population_commune
from src.data.insee.make_data import make_population_commune


@click.group()
def cli():
    pass


def insee_population():
    get_population_commune()
    make_population_commune()



@cli.command()
def insee():
    insee_population()


@cli.command()
def caf():
    insee_population()


if __name__ == '__main__':
    cli()
