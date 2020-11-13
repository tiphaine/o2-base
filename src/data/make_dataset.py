# -*- coding: utf-8 -*-
import click

from caf.get_data import get_caf_alloc_foyers_bas_revenus
from caf.make_data import make_caf_foyers_bas_revenus
from divers.get_data import get_divers_idh2_ile_de_france
from divers.make_data import make_divers_idh2_ile_de_france
from insee.get_data import get_population_commune, \
    get_confiance_menages, get_affaires_batiment, \
    get_insee_couple_famille_menages, \
    get_insee_diplome_formation
from insee.make_data import make_population_commune, \
    make_confiance_menages, make_climat_affaires_batiment, \
    make_insee_couple_famille_menages, make_insee_diplome_formation
from laposte.get_data import get_laposte_base_code_postaux
from laposte.make_data import make_laposte_base_code_postaux
from world_bank.get_data import get_inflation_country
from world_bank.make_data import make_inflation_country
from ecb.get_data import get_forex
from ecb.make_data import make_forex_euros


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


def insee_diplome_formation():
    get_insee_diplome_formation(verbose=True)
    make_insee_diplome_formation()


def laposte_base_code_postaux():
    get_laposte_base_code_postaux(verbose=True)
    make_laposte_base_code_postaux()


def divers_idh2_idf():
    get_divers_idh2_ile_de_france(verbose=True)
    make_divers_idh2_ile_de_france()


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
    insee_diplome_formation()


@cli.command()
def world_bank():
    world_bank_inflation()


@cli.command()
def ecb():
    ecb_forex()


@cli.command()
def caf():
    caf_alloc_foyers_bas_revenus()


@cli.command()
def laposte():
    laposte_base_code_postaux()


@cli.command()
def idh2():
    divers_idh2_idf()


if __name__ == '__main__':
    cli()
