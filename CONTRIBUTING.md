# Cómo contribuir

Gracias por revisar este proyecto. Es una pieza de portafolio con alcance
deliberadamente acotado; las contribuciones más útiles son las que mejoran la
claridad del flujo, la cobertura de pruebas o la accesibilidad de la demo.

## Entorno

- Python 3.11 o superior para el servicio de dominio.
- Cualquier navegador moderno para la demo. No hay compilación ni `node_modules`.

```bash
python -m pip install -r requirements-dev.txt
python -m pytest
```

Para revisar la interfaz:

```bash
python -m http.server 8000 --directory web
```

## Estructura del paquete

`src/app` replica a propósito el espacio de nombres del backend del portafolio.
Así, sincronizar un cambio entre este repositorio y el proyecto original es una
copia directa del archivo, fácil de revisar en un *diff*. No renombres el paquete
sin actualizar ambos lados.

## Convenciones

- **Commits**: [Conventional Commits](https://www.conventionalcommits.org/).
  Prefijos usados: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `perf`,
  `ci`, `style`. Ámbito opcional en minúsculas, por ejemplo
  `fix(service): impide aprobar un plan ya resuelto`.
- **Idioma**: documentación y mensajes de interfaz en español; identificadores,
  mensajes de commit y nombres de archivo técnicos pueden ir en inglés.
- **Estilo**: 4 espacios en Python, 2 en CSS/JS/HTML, línea de 100 columnas.
- **Pruebas**: cualquier cambio de comportamiento necesita una prueba que falle
  antes del cambio y pase después.

## Reglas de alcance

Este repositorio es determinista por diseño. Un cambio que introduzca cualquiera
de las siguientes cosas debe discutirse antes en un *issue*:

- una llamada de red en tiempo de ejecución;
- un proveedor de modelos o cualquier dependencia de IA;
- escrituras en archivos, bases de datos o servicios externos;
- credenciales, cadenas de conexión o datos personales;
- datos con licencia incompatible con la fuente documentada en `docs/DATA.md`.

## Flujo de revisión

1. Abre un *issue* que describa el problema observable.
2. Trabaja en una rama corta: `feat/…`, `fix/…` o `docs/…`.
3. Asegura `python -m pytest` en verde y la interfaz sin errores de consola.
4. Envía el *pull request* con contexto, decisión y evidencia del cambio.
