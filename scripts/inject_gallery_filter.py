import sys, json, urllib.request
sys.stdout.reconfigure(encoding='utf-8')

HEADERS = {"X-Shopify-Access-Token": "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"}
url = "https://maxipiel.myshopify.com/admin/api/2024-01/themes/144344481892/assets.json?asset[key]=layout/theme.liquid"
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req) as r:
    data = json.load(r)

content = data['asset']['value']

GALLERY_JS = """
    <!-- FILTRO GALERÍA POR TIPO DE PIEL -->
    <script>
    (function() {
      var PERF = 'perforada';

      function filterGallery(isPerf) {
        document.querySelectorAll('li[data-media-id]').forEach(function(li) {
          var img = li.querySelector('img');
          if (!img) return;
          var src = (img.getAttribute('srcset') || img.getAttribute('src') || '').toLowerCase();
          var imgIsPerf = src.indexOf(PERF) > -1;
          li.style.display = (imgIsPerf === isPerf) ? '' : 'none';
        });
      }

      function init() {
        var checkedPerf = document.querySelector('input[type="radio"][value="Piel Perforada"]:checked');
        if (checkedPerf) filterGallery(true);

        document.addEventListener('change', function(e) {
          var inp = e.target;
          if (inp.type !== 'radio') return;
          var name = (inp.name || '').trim();
          if (name.indexOf('Tipo') !== 0) return;
          filterGallery(inp.value === 'Piel Perforada');
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

# Insertar antes de </body>
if '<!-- FILTRO GALERÍA POR TIPO DE PIEL -->' in content:
    print("Ya existe el bloque, reemplazando...")
    import re
    content = re.sub(
        r'<!-- FILTRO GALERÍA POR TIPO DE PIEL -->.*?<!-- FIN FILTRO GALERÍA -->',
        GALLERY_JS.strip(),
        content, flags=re.DOTALL
    )
else:
    content = content.replace('</body>', GALLERY_JS + '\n  </body>')

import json, urllib.request
payload = json.dumps({"asset": {"key": "layout/theme.liquid", "value": content}}).encode('utf-8')
put_req = urllib.request.Request(
    "https://maxipiel.myshopify.com/admin/api/2024-01/themes/144344481892/assets.json",
    data=payload, headers={**HEADERS, "Content-Type": "application/json"}, method="PUT"
)
with urllib.request.urlopen(put_req) as r:
    resp = json.load(r)
    print("Subido OK:", resp['asset']['updated_at'])
