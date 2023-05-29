from resgatados.models.usuario import Usuario
from resgatados.models.animal import Animal
from dataclasses import is_dataclass
import pytest

def test_if_it_is_a_dataclass():
    assert is_dataclass(Usuario) == True
    assert is_dataclass(Animal) == True

