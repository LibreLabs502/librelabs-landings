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
│   └── preferencias/          # logos de tiendas de ejemplo (Sunday Shop)
├── scripts/
│   └── generar_assets.py      # regenera héroes, OG y favicons desde las originales
└── README.md
```

## Qué presenta

Una sola página que:

- Presenta **LibreDrop**, la plataforma Open Source (AGPLv3) para crear tiendas online
  simples: ventas por **WhatsApp y redes sociales** (Instagram, Facebook y TikTok), sin
  comisiones, multi-tenant.
- Explica que cada tienda **elige sus canales de compra**: WhatsApp («Comprar por») y
  redes sociales («Preguntar por»).
- Explica **LibreDrop Cloud**: qué es, cómo funciona y qué resuelve, con un precio único
  de **Q100/mes** (infraestructura, instalación y mantenimiento a cargo del equipo).
- Incluye una **tabla comparativa** entre LibreDrop (Open Source, gratis) y
  LibreDrop Cloud (servicio administrado).
- Muestra **tiendas de ejemplo** dentro de Cloud (Sunday Shop, que vende por Instagram y
  Facebook), con enlace a la tienda real.
- Cierra con Open Source, tecnología, preguntas frecuentes y un CTA hacia Cloud.

## Estética

La estética sigue la de las capturas oficiales del producto (`images/*.jpg`): limpia,
blanca, con acentos teal para LibreDrop y cian para LibreDrop Cloud.

## Fuente de información

Todo el copy está verificado contra el repositorio oficial de LibreDrop:

- Repositorio: <https://github.com/LibreLabs502/LibreDrop>
- `README.md` — qué es, stack, apps, API, instalación y producción.
- `VERSIONS.md` — estado de cada versión del proyecto.
- `docs/arquitectura.md` — multitenancy **lineal por `tenant_id`** (sin `django-tenants`
  ni esquemas por tienda), apps del backend y despliegue.
- `docs/api.md` — endpoints de la API (auth, tenants, catálogo, storefront, pagos).
- `backend/tenants/channels.py` — canales de compra por tienda (WhatsApp, Instagram,
  Facebook y TikTok; LinkedIn queda solo como enlace de contacto).
- `LICENSE` — GNU AGPL v3.

No se inventaron funcionalidades: lo que está en desarrollo se presenta como tal.

## Precio de LibreDrop Cloud

LibreDrop como software es gratuito (Open Source). **LibreDrop Cloud** es un servicio
administrado de LibreLabs con un único precio: **Q100/mes**. Los detalles operativos del
servicio (límites, almacenamiento, soporte) serán publicados oficialmente por LibreLabs.

## Preguntas frecuentes destacadas

- ¿Qué es LibreDrop? Plataforma Open Source para tiendas online simples.
- ¿Qué es LibreDrop Cloud? El mismo LibreDrop, administrado por LibreLabs, Q100/mes.
- ¿Por dónde vendo? Por los canales que actives: WhatsApp e Instagram, Facebook o TikTok.
- ¿Y si no quiero pagar? LibreDrop es gratuito; autoalojalo vos.

## Botón "Empezar"

Los botones **"Empezar"** (en la sección Cloud, en la comparación y en el CTA final)
apuntan a LibreDrop Cloud: <https://libredrop-cloud.vercel.app/>. Desde ahí el usuario
crea su perfil y su tienda; el servicio administrado (LibreDrop Cloud) cuesta **Q100/mes**.

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