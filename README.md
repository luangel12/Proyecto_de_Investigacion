# Comparación preliminar de OCR en cartas de restaurantes peruanos

Este repositorio corresponde a la primera versión de la prueba de concepto del proyecto de investigación: 
"Recomendación nutricional mediante un sistema de apoyo de elección de platos en cartas de restaurantes peruanos usando visión computacional".

## Objetivo del avance

Implementar una prueba preliminar para comparar el desempeño de dos motores OCR aplicados a imágenes de cartas de restaurantes peruanos:

- Tesseract OCR
- EasyOCR

## Estado actual

En esta primera entrega se presenta la estructura inicial del repositorio, la organización prevista del flujo experimental y los documentos metodológicos asociados al proyecto. La implementación del pipeline OCR será completada en los siguientes avances del curso.

## Estructura propuesta

- `data/`: imágenes de cartas de restaurantes.
- `notebooks/`: pruebas exploratorias con modelos OCR.
- `src/`: scripts principales del pipeline.
- `results/`: resultados de extracción y métricas comparativas.

## Próximos pasos

1. Cargar el dataset inicial de imágenes de menús.
2. Implementar extracción de texto con Tesseract.
3. Implementar extracción de texto con EasyOCR.
4. Comparar resultados mediante métricas como CER, WER y tiempo de procesamiento.
5. Documentar resultados preliminares en tablas y gráficos.