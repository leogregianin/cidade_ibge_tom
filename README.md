# cidade_ibge_tom
[![PyPI](https://img.shields.io/pypi/v/cidade_ibge_tom)](https://pypi.org/project/cidade_ibge_tom/) ![pyversions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue) ![https://github.com/leogregianin/cidade_ibge_tom/actions](https://github.com/leogregianin/cidade_ibge_tom/workflows/CI/badge.svg?branch=main)


## Cidade IBGE TOM

Demonstra informações da Cidade pelo código IBGE ou pelo código TOM.

`Código IBGE` é um padrão de código das Cidades brasileiras, que é composto por 7 dígitos, sendo os 2 primeiros o código do Estado.

`Código TOM` é um padrão de código das Cidades brasileiras utilizado por sistemas, por exemplo, [SIAFI](https://siafi.tesouro.gov.br/) - Sistema Integrado de Administração Financeira do Governo Federal, que é composto por 4 dígitos. A tabela completa dos códigos pode ser obtida [aqui](https://www.tesourotransparente.gov.br/ckan/dataset/lista-de-municipios-do-siafi/resource/eebb3bc6-9eea-4496-8bcf-304f33155282).

Neste pacote python temos o código IBGE, código TOM e o nome da Cidade relacionado.

## Instalação

```bash
pip install cidade_ibge_tom
```

## Utilização

* Informando o código IBGE 5300108:
```python
from cidade_ibge_tom import info_cidade

print(info_cidade(codigo='5300108'))
{'ibge': '5300108', 'tom': '9701', 'nome': 'Brasília-DF'}
```

* Informando o código TOM 7107:
```python
from cidade_ibge_tom import info_cidade

print(info_cidade(codigo='7107'))
{'ibge': '3550308', 'tom': '7107', 'nome': 'São Paulo-SP'}
```

## Licença

  MIT License