#!/usr/bin/env python

# Cálculo de emisións

# Variables
KMS_DIARIOS = 0
DIAS_LABORAIS_SEMANAIS = 0
SEMANAS = 0

# Cada medio de transporte ten o seu índice de emisións medio (gramos por km)
# https://www.movilidad-idae.es/destacados/emisiones-de-co2-por-modos-de-transporte-motorizado
EMISION_X_KM = 121

cantidade_de_emisions = KMS_DIARIOS * DIAS_LABORAIS_SEMANAIS * SEMANAS * EMISION_X_KM
print('O teu consumo é:', cantidade_de_emisions, 'gC02')


