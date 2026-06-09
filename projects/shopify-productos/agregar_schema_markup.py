import urllib.request, json

TOKEN = 'TU_SHOPIFY_TOKEN'
SHOP = 'maxipiel.myshopify.com'
THEME_ID = '144344481892'

def get_asset(key):
    req = urllib.request.Request(
        f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json?asset[key]={key}'
    )
    req.add_header('X-Shopify-Access-Token', TOKEN)
    with urllib.request.urlopen(req) as r:
        return json.load(r)['asset']['value']

def put_asset(key, value):
    payload = json.dumps({'asset': {'key': key, 'value': value}}).encode('utf-8')
    req = urllib.request.Request(
        f'https://{SHOP}/admin/api/2024-01/themes/{THEME_ID}/assets.json',
        data=payload, method='PUT'
    )
    req.add_header('X-Shopify-Access-Token', TOKEN)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    with urllib.request.urlopen(req) as r:
        return json.load(r)


# ── 1. SNIPPET: snippets/schema-org.liquid ────────────────────────────────────
SCHEMA_SNIPPET = """{%- comment -%} Schema.org JSON-LD — Maxipiel {%- endcomment -%}

{%- comment -%} Organization — aparece en todas las páginas {%- endcomment -%}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Maxipiel",
  "url": "https://www.maxipiel.com",
  "logo": "https://cdn.shopify.com/s/files/1/0700/9045/7188/t/3/assets/logo.png",
  "description": "Venta de piel genuina para tapiceros. Directo de las curtiembres de León, Guanajuato. Tapicería automotriz, muebles y marroquinería.",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "León",
    "addressRegion": "Guanajuato",
    "addressCountry": "MX"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+52-477-209-5652",
    "contactType": "sales",
    "areaServed": "MX",
    "availableLanguage": "Spanish"
  },
  "sameAs": [
    "https://www.facebook.com/maxipiel",
    "https://www.instagram.com/maxipiel"
  ]
}
</script>

{%- comment -%} Product schema — solo en páginas de producto {%- endcomment -%}
{%- if template == 'product' -%}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": {{ product.title | json }},
  "description": {{ product.description | strip_html | truncate: 300 | json }},
  "url": "{{ shop.url }}{{ product.url }}",
  "sku": {{ product.selected_or_first_available_variant.sku | json }},
  "brand": {
    "@type": "Brand",
    "name": "Maxipiel"
  },
  {%- if product.images.size > 0 -%}
  "image": [
    {%- for image in product.images limit: 5 -%}
      "{{ image.src | image_url: width: 800 }}"{% unless forloop.last %},{% endunless %}
    {%- endfor -%}
  ],
  {%- endif -%}
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "MXN",
    "lowPrice": {{ product.price_min | money_without_currency | remove: ',' }},
    "highPrice": {{ product.price_max | money_without_currency | remove: ',' }},
    "offerCount": {{ product.variants.size }},
    "availability": "{%- if product.available -%}https://schema.org/InStock{%- else -%}https://schema.org/OutOfStock{%- endif -%}",
    "seller": {
      "@type": "Organization",
      "name": "Maxipiel"
    }
  }
}
</script>
{%- endif -%}

{%- comment -%} BreadcrumbList — en colecciones y productos {%- endcomment -%}
{%- if template == 'collection' or template == 'product' -%}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "{{ shop.url }}"
    }
    {%- if template == 'collection' -%}
    ,{
      "@type": "ListItem",
      "position": 2,
      "name": {{ collection.title | json }},
      "item": "{{ shop.url }}{{ collection.url }}"
    }
    {%- elsif template == 'product' -%}
    {%- if collection -%}
    ,{
      "@type": "ListItem",
      "position": 2,
      "name": {{ collection.title | json }},
      "item": "{{ shop.url }}{{ collection.url }}"
    }
    ,{
      "@type": "ListItem",
      "position": 3,
      "name": {{ product.title | json }},
      "item": "{{ shop.url }}{{ product.url }}"
    }
    {%- else -%}
    ,{
      "@type": "ListItem",
      "position": 2,
      "name": {{ product.title | json }},
      "item": "{{ shop.url }}{{ product.url }}"
    }
    {%- endif -%}
    {%- endif -%}
  ]
}
</script>
{%- endif -%}
"""

# ── 2. Subir el snippet ────────────────────────────────────────────────────────
print("Subiendo snippets/schema-org.liquid...")
put_asset('snippets/schema-org.liquid', SCHEMA_SNIPPET)
print("OK")

# ── 3. Inyectar {% render 'schema-org' %} en theme.liquid antes de </head> ────
print("Modificando layout/theme.liquid...")
theme = get_asset('layout/theme.liquid')

if "render 'schema-org'" in theme:
    print("Ya estaba inyectado — no se modifica.")
else:
    theme = theme.replace('</head>', "  {%- render 'schema-org' -%}\n  </head>")
    put_asset('layout/theme.liquid', theme)
    print("OK — schema-org inyectado antes de </head>")

print("\nListo. Verifica en: https://search.google.com/test/rich-results")
print("URL de prueba: https://www.maxipiel.com/products/cuero-top-grain-negro-semi-liso")
