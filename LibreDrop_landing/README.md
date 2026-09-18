# LibreLabs Landings

Landing oficial de **LibreDrop**: una sola página que presenta la familia **LibreDrop** y
vende **LibreDrop Cloud** (servicio administrado de LibreLabs, **Q100/mes**).

Construida con **HTML, CSS y JS vanilla** (sin frameworks), lista para deploy estático en
[Vercel](https://vercel.com) o cualquier hosting:

```
LibreDrop_landing/
├── index.html                 # la landing (página única)
├── styles.css
├── app.js
├── logo.png / logo-mark.png   # logotipo y marca extraídos de las capturas oficiales
├── icon-32/64/180/512.png     # favicons derivados de images/libredrop_icon.jpg
├── images/                    # capturas oficiales + assets optimizados (héroes, OG)
├── scripts/
│   └── generar_assets.py      # regenera héroes, OG y favicons desde las originales
└── README.md
```

## Qué presenta

Una sola página que:

- Presenta **LibreDrop**, la plataforma Open Source (AGPLv3) para crear tiendas online
  simples: pedidos por WhatsApp, sin comisiones, multi-tenant.
- Vende **LibreDrop Cloud** como protagonista: el mismo software administrado por
  LibreLabs por **Q100/mes** (infraestructura, instalación y mantenimiento a cargo del
  equipo).
- Incluye **tarjetas de planes** con beneficios y precios de ambos.
- Cierra con Open Source, comunidad, preguntas frecuentes y un CTA hacia Cloud.

## Estética

La estética sigue la de las capturas oficiales del producto (`images/*.jpg`): limpia,
blanca, con acentos teal para LibreDrop y cian para LibreDrop Cloud.

## Fuente de información

Todo el copy está verificado contra el repositorio oficial de LibreDrop:

- Repositorio: <https://github.com/LibreLabs502/LibreDrop>
- `README.md` — qué es, stack, apps, API, instalación.
- `docs/VERSIONS.md` — estado actual (backend de v1 terminado; `customers` y `orders` en desarrollo).
- `docs/DATABASE.md` — arquitectura multi-tenant (django-tenants) y modelo de datos.
- `docs/CONTRIB.md` — guía de contribución.
- `LICENSE` — GNU AGPL v3.

No se inventaron funcionalidades: las que están en desarrollo (`customers`, `orders`,
seguimiento de pagos) se presentan como tales.

## Precio de LibreDrop Cloud

LibreDrop como software es gratuito (Open Source). **LibreDrop Cloud** es un servicio
administrado de LibreLabs con un único precio: **Q100/mes**. Los detalles operativos del
servicio (límites, almacenamiento, soporte) serán publicados oficialmente por LibreLabs.

## Preguntas frecuentes destacadas

- ¿Qué es LibreDrop? Plataforma Open Source para tiendas online simples.
- ¿Qué es LibreDrop Cloud? El mismo LibreDrop, administrado por LibreLabs, Q100/mes.
- ¿Y si no quiero pagar? LibreDrop es gratuito; autoalojalo vos.

## Botón "Empezar"

Los botones **"Empezar"** (en la sección Cloud, la tarjeta de Cloud y el CTA final) usan
`href="#"` con un comentario en el HTML indicando dónde reemplazar el enlace real de
creación de cuenta.

## SEO pendiente

- **Canonical:** `index.html` incluye un comentario donde agregar el
  `<link rel="canonical">` una vez se conozca el dominio de producción.
- **Open Graph y favicon:** ya configurados apuntando a los assets de este repo.

## Regenerar los assets

Si modificás o reemplazás las imágenes originales, podés regenerar los derivados
(héroes, OG y favicons) con el script que se usó (requiere Pillow):

```bash
python scripts/generar_assets.py
```

## Licencia

Los textos provienen de la información pública del proyecto LibreDrop. Para el software
LibreDrop en sí, ver [AGPLv3](https://github.com/LibreLabs502/LibreDrop/blob/main/LICENSE).