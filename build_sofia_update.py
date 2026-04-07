import json, uuid

path = 'C:/Users/maxip/.claude/projects/c--Users-maxip-Claude-Code-Maxipiel/7d1a06e0-af0d-4202-b6a5-4866eca7705c/tool-results/mcp-n8n-mcp-n8n_get_workflow-1775073613534.txt'
with open(path, encoding='utf-8') as f:
    data = json.load(f)
wf = json.loads(data[0]['text'])['data']

id_if     = str(uuid.uuid4())
id_token  = str(uuid.uuid4())
id_enviar = str(uuid.uuid4())

node_if = {
    "parameters": {
        "conditions": {
            "options": {"caseSensitive": False, "leftValue": "", "typeValidation": "loose"},
            "conditions": [{
                "id": str(uuid.uuid4()),
                "leftValue": "={{ $json.mensaje }}",
                "rightValue": "cat[aá]logo|col[oó]res.{0,20}(tienen|disponibles|manejan)|tonos.{0,20}(tienen|disponibles|manejan)",
                "operator": {"type": "string", "operation": "regex"}
            }],
            "combinator": "and"
        },
        "options": {}
    },
    "type": "n8n-nodes-base.if",
    "typeVersion": 2,
    "position": [640, 350],
    "id": id_if,
    "name": "Pide Catalogo?"
}

node_token = {
    "parameters": {
        "documentId": {
            "__rl": True,
            "value": "1PhUkvUWQRx0lHuKXPNYcpN2ShgV8Kf3N2d8hKxvQw1Q",
            "mode": "list",
            "cachedResultName": "token facebook"
        },
        "sheetName": {
            "__rl": True,
            "value": "gid=0",
            "mode": "list",
            "cachedResultName": "Hoja 1"
        },
        "options": {}
    },
    "type": "n8n-nodes-base.googleSheets",
    "typeVersion": 4.5,
    "position": [860, 480],
    "id": id_token,
    "name": "Token FB Catalogo",
    "credentials": {
        "googleSheetsOAuth2Api": {"id": "wAxnYIinSrAIQGuD", "name": "Google Sheets account 2"}
    }
}

json_body = json.dumps({
    "messaging_product": "whatsapp",
    "to": "={{ $('Webhook').item.json.body.conversation.messages[0].conversation.contact_inbox.source_id }}",
    "type": "document",
    "document": {
        "link": "https://drive.google.com/uc?export=download&id=1GNN_ZBpwEyJxE0vXMyovrhunNJWfrx2t",
        "filename": "Catalogo_Maxipiel.pdf",
        "caption": "¡Aquí está nuestro catálogo de pieles Maxipiel! Cualquier duda estamos para ayudarte 🐄"
    }
}, ensure_ascii=False)

node_enviar = {
    "parameters": {
        "method": "POST",
        "url": "https://graph.facebook.com/v19.0/606947975845418/messages",
        "sendHeaders": True,
        "headerParameters": {
            "parameters": [{
                "name": "Authorization",
                "value": "=Bearer {{ $('Token FB Catalogo').item.json.token }}"
            }]
        },
        "sendBody": True,
        "specifyBody": "json",
        "jsonBody": "=" + json_body,
        "options": {}
    },
    "type": "n8n-nodes-base.httpRequest",
    "typeVersion": 4.2,
    "position": [1080, 480],
    "id": id_enviar,
    "name": "Enviar Catalogo PDF"
}

wf['nodes'] += [node_if, node_token, node_enviar]

conns = wf['connections']

# Redirigir Mensaje -> IF (antes iba a Text Classifier)
conns['Mensaje']['main'][0] = [{"node": "Pide Catalogo?", "type": "main", "index": 0}]

# IF: true -> Token FB, false -> Text Classifier
conns['Pide Catalogo?'] = {
    "main": [
        [{"node": "Token FB Catalogo", "type": "main", "index": 0}],
        [{"node": "Text Classifier", "type": "main", "index": 0}]
    ]
}

# Token -> Enviar
conns['Token FB Catalogo'] = {
    "main": [[{"node": "Enviar Catalogo PDF", "type": "main", "index": 0}]]
}

out_path = 'C:/Users/maxip/Claude-Code-Maxipiel/sofia_modified.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(wf, f, ensure_ascii=False, indent=2)

print('IDs nuevos:')
print('  IF:', id_if)
print('  Token:', id_token)
print('  Enviar:', id_enviar)
print('Nodos totales:', len(wf['nodes']))
print('OK - guardado en sofia_modified.json')
