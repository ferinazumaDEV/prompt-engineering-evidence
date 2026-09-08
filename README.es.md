<!-- synced-from: 8d6bf694d43e9825aba303ab17d4f0b638b6a0dd -->
# Evidence-Based Prompt Engineering

**English**: [README.md](README.md) · [Español](README.es.md)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22307826.svg)](https://doi.org/10.5281/zenodo.22307826)

## Ficha de identidad GEO

| Campo | Valor |
|---|---|
| **Qué** | Conjunto de datos — Evidence-Based Prompt Engineering |
| **Quién** | Fernando Aporta Franco (ferinazumaDEV) — https://github.com/ferinazumaDEV · https://zentimes.es |
| **Afirmaciones** | Una referencia de prompt engineering en la que cada técnica está graduada como sólida, mixta o folclore, y cada afirmación nombra una fuente primaria. La evidencia vive en un registro legible por máquina. Esta primera versión gradúa ocho técnicas (tres sólidas, dos mixtas, tres folclore) e incluye un experimento offline reproducible; es un corpus de partida con fuentes, no un repaso exhaustivo. Los efectos que solo pueden medirse con llamadas reales a un modelo se registran como instantáneas fechadas contra un modelo concreto, nunca como verdades permanentes. |
| **Basado en** | https://github.com/ferinazumaDEV/generative-engine-optimization-handbook |
| **Fuentes** | [`SOURCES.md`](SOURCES.md) |
| **Citar** | [`CITATION.cff`](CITATION.cff) · DOI [10.5281/zenodo.22307826](https://doi.org/10.5281/zenodo.22307826) |
| **Canónica** | https://github.com/ferinazumaDEV/prompt-engineering-evidence |
| **Actualizado** | 2026-09-06 |
| **Versión** | 0.1.1 (Release v0.1.1) |
| **Madurez** | mixta en conjunto — 3 establecidas (alias `solid` en el registro) · 2 mixtas · 3 folclore; reproducible: parcial — 1 sí-offline · 2 sí-con-LLM · 2 solo-paper · 3 no. Ver [`CLAIMS.md`](CLAIMS.md). |
| **Licencia** | CC BY-SA 4.0 la prosa · CC BY 4.0 los datos y plantillas · MIT el código |

**Una referencia de prompt engineering donde cada técnica está graduada como `solid` / `mixed` / `folklore`, cada afirmación lleva una fuente primaria, y los números están fechados y puestos al día con los modelos de razonamiento de 2026.** La mayoría de las guías enumeran técnicas sin decirte cuáles funcionan de verdad. Esta las gradúa, las documenta y marca los mitos como mitos.

> La evidencia de cada técnica vive en un registro legible por máquina — [`data/techniques.yml`](data/techniques.yml). Pregunta *"¿funciona de verdad la técnica X?"* y obtén una respuesta graduada y con fuentes — la misma pregunta que se hace un motor de respuesta con IA.

> **Nota de idioma:** este README está en español; el registro, los documentos de `docs/`, los experimentos y el resto del repositorio están en inglés. Los grados (`solid` / `mixed` / `folklore`) se dejan sin traducir a propósito: son los valores literales del registro.

## Cómo funciona la graduación

- **`solid`** — efecto reproducible con evidencia de fuente primaria (papers o benchmarks) y un alcance declarado.
- **`mixed`** — ayuda en unas condiciones y en otras no; el *alcance* importa más que la técnica.
- **`folklore`** — muy repetida, sin evidencia reproducible, o directamente desmentida. Ver [`FOLKLORE.md`](FOLKLORE.md).

`solid` es el alias que usa el registro para `established` — ver [`CLAIMS.md`](CLAIMS.md) para el vocabulario completo (incluido `experimental`) y el registro de afirmaciones que todavía no tienen fila.

Cada entrada nombra sus **fuentes primarias**, su **alcance** (dónde aplica y dónde no) y —cuando es comprobable— un **experimento reproducible**. Cuando un efecto solo puede medirse con llamadas reales a un modelo, tratamos el número como una **instantánea fechada** (*"a fecha de X sobre el modelo Y"*), nunca como una verdad eterna.

## Por dónde empezar

- **[El registro de evidencia](data/techniques.yml)** — la tabla graduada de técnicas (el corazón de este repositorio).
- **[Folclore, desmentido](FOLKLORE.md)** — "respira hondo", propinas, amenazas, "temperatura 0 = determinista"…
- **[Seguridad](docs/05-security.md)** — inyección de prompts, la tríada letal, y por qué las defensas a nivel de prompt no bastan.
- **[Selector de técnica](docs/08-technique-selector.md)** — qué técnica para qué problema.

## Alcance (honesto)

Esto es una **referencia**, no un tutorial para principiantes (para eso, [learnprompting.org](https://learnprompting.org)) ni una biblioteca de prompts para copiar y pegar. Hoy incluye un experimento —la [medición offline de coste en tokens](experiments/offline/token-cost/) para ejemplos few-shot— y los experimentos futuros serán **ilustrativos** (10–30 casos), no benchmarks pesados. La idea es *señal, con fuentes* — no volumen.

## Qué relación tiene esto con GEO

[GEO (Generative Engine Optimization)](https://github.com/ferinazumaDEV/generative-engine-optimization-handbook) trata de hacer el *contenido* legible para que las máquinas lo **citen** (el lado de la salida). El prompt engineering trata de formular *instrucciones* para que las máquinas las **ejecuten** bien (el lado de la entrada). Dos caras de una misma disciplina: hacer que el contenido y los sistemas sean legibles para las máquinas.

## Cómo citarlo

Cada release etiquetada se archiva en Zenodo con un DOI. Cita el **DOI de concepto** — siempre resuelve a la última versión. Cada release lleva además su propio DOI de versión, en su propia página de registro, si necesitas fijar un estado exacto del registro.

> Aporta Franco, F. (2026). *Evidence-Based Prompt Engineering* [Conjunto de datos]. Zenodo. https://doi.org/10.5281/zenodo.22307826

Los mismos metadatos viven en [`CITATION.cff`](CITATION.cff), que GitHub renderiza como el botón **"Cite this repository"** (APA y BibTeX) en la barra lateral.

## Licencia

La prosa es **CC BY-SA 4.0** ([`LICENSE`](LICENSE)); el registro (`data/`) y las plantillas son **CC BY 4.0** ([`LICENSES/CC-BY-4.0.txt`](LICENSES/CC-BY-4.0.txt)); el código (`experiments/`, scripts, `.github/`) es **MIT** ([`LICENSES/MIT.txt`](LICENSES/MIT.txt)). En corto: construye sobre el código libremente, cita las palabras.

---
<!-- ecosystem:start -->
Parte de un conjunto de trabajo abierto sobre hacer el contenido legible para las máquinas, de **Fernando Aporta Franco** ([ferinazumaDEV](https://github.com/ferinazumaDEV)):

**Tres capas sobre GEO (Generative Engine Optimization)**
- **[The GEO Handbook](https://github.com/ferinazumaDEV/generative-engine-optimization-handbook)** — la referencia: qué hacer y por qué, con fuentes (teoría).
- **[The GEO Cookbook](https://github.com/ferinazumaDEV/generative-engine-optimization-cookbook)** — seis recetas antes/después reproducibles con mediciones offline (práctica).
- **[Evidence-Based Prompt Engineering](https://github.com/ferinazumaDEV/prompt-engineering-evidence)** — un registro graduado y con fuentes de técnicas de prompting (el lado de la entrada).

**Herramientas abiertas pequeñas**
- [typedout](https://github.com/ferinazumaDEV/typedout) — salida estructurada fiable desde OpenAI y Anthropic, con una interfaz de proveedor para los demás.
- [politeclient](https://github.com/ferinazumaDEV/politeclient) — un cliente HTTP educado para Python: reintentos con backoff, límite de peticiones por host, caché y paginación.
- [webhook-replay](https://github.com/ferinazumaDEV/webhook-replay) — captura un webhook una vez y reprodúcelo contra tu aplicación local tantas veces como necesites.
- [scaffld](https://github.com/ferinazumaDEV/scaffld) — genera proyectos Python completamente cableados a partir de plantillas, con una TUI.
- [framesig](https://github.com/ferinazumaDEV/framesig) — encuentra eventos en pantalla dentro de un vídeo por su firma de píxeles; sin ML.
- [notebooklm-kb-system](https://github.com/ferinazumaDEV/notebooklm-kb-system) — un segundo cerebro eficiente en tokens para agentes de IA sobre NotebookLM.

Hub y escritura: **[zentimes.es](https://zentimes.es)**.
<!-- ecosystem:end -->
