import sys, json, urllib.request, re
sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {"X-Shopify-Access-Token": "TU_SHOPIFY_TOKEN"}
url = "https://maxipiel.myshopify.com/admin/api/2024-01/themes/144344481892/assets.json?asset[key]=layout/theme.liquid"
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req) as r:
    data = json.load(r)
content = data['asset']['value']

NEW_JS = """    <!-- FILTRO GALERÍA POR TIPO DE PIEL -->
    <script>
    (function() {
      function norm(s) {
        return (s || '').toLowerCase()
          .replace(/é/g,'e').replace(/á/g,'a')
          .replace(/í/g,'i').replace(/ó/g,'o').replace(/ú/g,'u');
      }

      function getOpts() {
        var opts = {};
        document.querySelectorAll('form[action*="cart/add"] input[type="radio"]:checked').forEach(function(inp) {
          var name = (inp.name || '').trim();
          if (name.indexOf('Tipo') === 0)  opts.tipo  = inp.value;
          if (name.indexOf('Color') === 0) opts.color = norm(inp.value);
        });
        return opts;
      }

      function filterGallery() {
        var opts = getOpts();
        if (!opts.tipo && !opts.color) return;

        document.querySelectorAll('li[data-media-id]').forEach(function(li) {
          var img = li.querySelector('img');
          if (!img) return;
          var src = norm(img.getAttribute('srcset') || img.getAttribute('src') || '');
          var show = true;

          if (opts.tipo) {
            var isPerf = src.indexOf('perforada') > -1;
            show = show && (isPerf === (opts.tipo === 'Piel Perforada'));
          }
          if (opts.color) {
            // Para negro/negra usar "negr" para capturar ambas formas
            var keyword = opts.color === 'negro' ? 'negr' : opts.color;
            show = show && src.indexOf(keyword) > -1;
          }

          li.style.display = show ? '' : 'none';
        });
      }

      function init() {
        filterGallery();
        document.addEventListener('change', function(e) {
          var inp = e.target;
          if (inp.type !== 'radio') return;
          var name = (inp.name || '').trim();
          if (name.indexOf('Tipo') === 0 || name.indexOf('Color') === 0) {
            requestAnimationFrame(filterGallery);
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
    <!-- FIN FILTRO GALERÍA -->"""

content = re.sub(
    r'<!-- FILTRO GALER[IÍ]A POR TIPO DE PIEL -->.*?<!-- FIN FILTRO GALER[IÍ]A -->',
    NEW_JS.strip(),
    content, flags=re.DOTALL
)

payload = json.dumps({"asset": {"key": "layout/theme.liquid", "value": content}}).encode('utf-8')
put_req = urllib.request.Request(
    "https://maxipiel.myshopify.com/admin/api/2024-01/themes/144344481892/assets.json",
    data=payload, headers={**HEADERS, "Content-Type": "application/json"}, method="PUT"
)
with urllib.request.urlopen(put_req) as r:
    resp = json.load(r)
    print("Subido OK:", resp['asset']['updated_at'])
