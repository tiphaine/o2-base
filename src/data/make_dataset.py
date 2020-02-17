# -*- coding: utf-8 -*-
import click

from src.data.insee.get_data import get_population_commune, get_confiance_menages
from src.data.insee.make_data import make_population_commune, make_confiance_menages
from src.data.world_bank.get_data import get_inflation_country
from src.data.world_bank.make_data import make_inflation_country


@click.group()
def cli():
    pass


def insee_population():
    get_population_commune()
    make_population_commune()


def insee_confiance_menage():
    get_confiance_menages()
    make_confiance_menages()


def world_bank_inflation():
    get_inflation_country()


@cli.command()
def insee():
    insee_population()
    insee_confiance_menage()


@cli.command()
def world_bank():
    world_bank_inflation()
    make_inflation_country()


@cli.command()
def caf():
    insee_population()


if __name__ == '__main__':
    cli()
