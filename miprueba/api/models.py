from django.db import models
import random
import time
import random
from datetime import datetime, timedelta


class Token:
    def __init__(self):
        self.tokens = {}  # diccionario para almacenar los tokens y su tiempo de expiración

    def generar_token(self, cliente):
        # Generar token aleatorio de 6 dígitos
        token = str(random.randint(100000, 999999))
        # Calcular tiempo de expiración (60 segundos a partir de ahora)
        expiracion = datetime.now() + timedelta(seconds=60)
        # Agregar token y tiempo de expiración al diccionario de tokens
        self.tokens[cliente] = (token, expiracion)
        # Retornar el token generado
        return token

    def usar_token(self, cliente, token):
        # Verificar si el cliente tiene un token válido
        if cliente in self.tokens:
            token_guardado, expiracion = self.tokens[cliente]
            # Verificar si el token guardado es igual al proporcionado
            if token_guardado == token:
                # Verificar si el token ha expirado
                if datetime.now() < expiracion:
                    # Retornar éxito y tiempo restante del token
                    tiempo_restante = expiracion - datetime.now()
                    return f'Token válido. Tiempo restante: {tiempo_restante.total_seconds()} segundos'
                else:
                    # Retornar error de token expirado
                    return 'Error: token expirado'
            else:
                # Retornar error de token inválido
                return 'Error: token inválido'
        else:
            # Retornar error de cliente desconocido
            return 'Error: cliente desconocido'

    def autogenerar_token(self, cliente):
        # Verificar si el cliente tiene un token válido
        if cliente in self.tokens:
            token_guardado, expiracion = self.tokens[cliente]
            # Verificar si el token ha expirado
            if datetime.now() >= expiracion:
                # Generar un nuevo token y actualizar su tiempo de expiración
                self.generar_token(cliente)
        else:
            # Generar un nuevo token para el cliente
            self.generar_token(cliente)
