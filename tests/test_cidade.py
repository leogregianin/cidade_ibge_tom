import pytest

from cidade_ibge_tom.cidade import info_cidade


def test_info_cidade_ibge_5222302():
    cidade = info_cidade(codigo='5222302')
    esperado = {'ibge': '5222302', 'tom': '1068', 'nome': 'Vila Propício-GO'}
    assert cidade == esperado

def test_info_cidade_tom_1068():
    cidade = info_cidade(codigo='1068')
    esperado = {'ibge': '5222302', 'tom': '1068', 'nome': 'Vila Propício-GO'}
    assert cidade == esperado

def test_info_cidade_ibge_5222302_erro():
    cidade = info_cidade(codigo='5222300')
    esperado = {}
    assert cidade == esperado

def test_info_cidade_tom_erro():
    cidade = info_cidade(codigo='9999')
    esperado = {}
    assert cidade == esperado
