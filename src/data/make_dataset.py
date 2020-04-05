# -*- coding: utf-8 -*-
import click

from src.data.caf.get_data import get_caf_alloc_foyers_bas_revenus
from src.data.caf.make_data import make_caf_foyers_bas_revenus
from src.data.insee.get_data import get_population_commune, get_confiance_menages, get_affaires_batiment, get_insee_couple_famille_menages
from src.data.insee.make_data import make_population_commune, make_confiance_menages, make_climat_affaires_batiment, make_insee_couple_famille_menages
from src.data.world_bank.get_data import get_inflation_country
from src.data.world_bank.make_data import make_inflation_country
from src.data.ecb.get_data import get_forex
from src.data.ecb.make_data import make_forex_euros


@click.group()
def cli():
    pass


def caf_alloc_foyers_bas_revenus():
    get_caf_alloc_foyers_bas_revenus(verbose=True)
    make_caf_foyers_bas_revenus()


def insee_population():
    get_population_commune()
    make_population_commune()


def insee_confiance_menage():
    get_confiance_menages()
    make_confiance_menages()


def insee_affaires_batiment():
    get_affaires_batiment()
    make_climat_affaires_batiment()


def insee_couple_famille_menages():
    get_insee_couple_famille_menages(verbose=True)
    make_insee_couple_famille_menages()


def world_bank_inflation():
    get_inflation_country()
    make_inflation_country()


def ecb_forex():
    get_forex()
    make_forex_euros()


@cli.command()
def insee():
    insee_population()
    insee_confiance_menage()
    insee_affaires_batiment()
    insee_couple_famille_menages()


@cli.command()
def world_bank():
    world_bank_inflation()


@cli.command()
def ecb():
    ecb_forex()


@cli.command()
def caf():
    caf_alloc_foyers_bas_revenus()


if __name__ == '__main__':
    cli()
