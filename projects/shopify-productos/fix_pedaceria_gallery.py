import urllib.request, json

TOKEN = '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'
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

SNIPPET = r"""
{% assign is_pedaceria = false %}
{% for tag in product.tags %}
  {% if tag == 'pedaceria' %}
    {% assign is_pedaceria = true %}
  {% endif %}
{% endfor %}
{% if is_pedaceria %}
<script>
(function(){
  var COLOR_MAP = {
    'Café':         'Cafe',
    'Rojo Ladrillo':  'Ladrillo',
    'Miel':           'Miel',
    'Chocolate':      'Chocolate',
    'Gris':           'Gris',
    'Beige':          'Beige',
    'Camel':          'Camel',
    'Mixto':          'Mixto',
  };

  function getColorInput() {
    return document.querySelector('input[name="Color-1"]:checked')
        || document.querySelector('input[name^="Color"]:checked');
  }

  function getSuffix(colorName) {
    return COLOR_MAP[colorName] || null;
  }

  // Returns true if img alt or src contains the color suffix
  function matchesSuffix(li, suffix) {
    var img = li.querySelector('img');
    if (!img) return false;
    var alt = (img.getAttribute('alt') || '').toLowerCase();
    var src = (img.getAttribute('src') || img.getAttribute('data-src') || '').toLowerCase();
    var key = suffix.toLowerCase();
    return alt.indexOf(key) !== -1 || src.indexOf(key) !== -1;
  }

  function filterGallery(colorName) {
    var suffix = getSuffix(colorName);
    if (!suffix) return;

    // Target ALL li inside any product media list or thumbnail slider
    // Dawn uses .product__media-list for main slider and .thumbnail-list for thumbnails
    var selectors = [
      '.product__media-list > li',
      '.thumbnail-list > li',
      '.product__media-wrapper li',
    ];

    var handled = new Set();

    selectors.forEach(function(sel) {
      document.querySelectorAll(sel).forEach(function(li) {
        if (handled.has(li)) return;
        handled.add(li);

        var show = matchesSuffix(li, suffix);
        li.style.display = show ? '' : 'none';
        // Also hide/show the corresponding thumbnail button if it exists
        var btn = li.querySelector('button, a');
        // Pointer-events: none on hidden items so Dawn can't accidentally focus them
        li.style.pointerEvents = show ? '' : 'none';
      });
    });

    // Click the first visible thumbnail to update the main image
    setTimeout(function() {
      var firstVisible = null;
      document.querySelectorAll('.product__media-list > li').forEach(function(li) {
        if (!firstVisible && li.style.display !== 'none') {
          firstVisible = li;
        }
      });
      if (firstVisible) {
        // Try clicking the thumbnail in the thumbnail list that corresponds to this media
        var mediaId = firstVisible.getAttribute('data-media-id')
                   || (firstVisible.querySelector('[data-media-id]') || {}).dataset && firstVisible.querySelector('[data-media-id]').getAttribute('data-media-id');

        // Fallback: click the first visible thumbnail button
        var thumbBtn = null;
        document.querySelectorAll('.thumbnail-list > li').forEach(function(li) {
          if (!thumbBtn && li.style.display !== 'none') {
            thumbBtn = li.querySelector('button') || li.querySelector('a');
          }
        });
        if (thumbBtn) {
          thumbBtn.click();
        } else {
          // No thumbnail list — click the main slide directly
          var mainBtn = firstVisible.querySelector('button') || firstVisible.querySelector('a');
          if (mainBtn) mainBtn.click();
        }
      }
    }, 80);
  }

  function init() {
    var el = getColorInput();
    if (el) filterGallery(el.value);

    document.addEventListener('change', function(e) {
      if (e.target && e.target.type === 'radio' &&
          e.target.name && e.target.name.indexOf('Color') === 0) {
        filterGallery(e.target.value);
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>
{% endif %}
"""

print("Subiendo fix v2 del gallery filter...")
put_asset('snippets/pedaceria-gallery-filter.liquid', SNIPPET)
print("OK")

print("Verificando inyeccion en theme.liquid...")
theme = get_asset('layout/theme.liquid')
if "pedaceria-gallery-filter" in theme:
    print("OK — ya esta inyectado.")
else:
    updated = theme.replace('</body>', "{% render 'pedaceria-gallery-filter' %}\n</body>")
    put_asset('layout/theme.liquid', updated)
    print("OK — inyectado.")
