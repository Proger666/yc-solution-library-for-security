import base64
import json
import os
import requests


# Проверить какие .state индексы существуют
# На основе этого парсить нужные папки в include
# в каждом файле взять строку и найти по id объект и сравнить
# Если отличается - удалить и импортировать
# Если не отличается - continue