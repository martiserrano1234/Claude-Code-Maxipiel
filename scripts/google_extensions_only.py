import sys
sys.stdout.reconfigure(encoding='utf-8')
from google.ads.googleads.client import GoogleAdsClient

config = {
    'developer_token': 'qRHTvVSGPemQVQoI9w6LcQ',
    'client_id': '451512178532-ij2h08ngks7d2t5dag7138eeeefjjeon.apps.googleusercontent.com',
    'client_secret': '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',
    'refresh_token': '1//04UneP8IZhT1BCgYIARAAGAQSNwF-L9IrxC5NMccmt94Ji59DXvHb-ggvV8BtGo_eytfuAOlZqkqjzckOTl8k7mt7-pBEI0ON7Zc',
    'login_customer_id': '4020002227',
    'use_proto_plus': True
}

client = GoogleAdsClient.load_from_dict(config)
campaign_service = client.get_service('CampaignService')
asset_service = client.get_service('AssetService')
campaign_asset_service = client.get_service('CampaignAssetService')

CUSTOMER_ID = '6619664178'
MAIN_CAMPAIGN_ID = '22621305349'
main_camp = campaign_service.campaign_path(CUSTOMER_ID, MAIN_CAMPAIGN_ID)

asset_ops = []

# 5 callouts nuevos
new_callouts = [
    'Directo de curtiembre',
    'Precio fijo sin regateo',
    '30 colores disponibles',
    'Envio en 4 a 6 dias',
    'Sin intermediarios',
]
for ct in new_callouts:
    op = client.get_type('AssetOperation')
    op.create.callout_asset.callout_text = ct
    asset_ops.append(op)

# Structured snippet - tipos de piel
op_snippet = client.get_type('AssetOperation')
op_snippet.create.structured_snippet_asset.header = 'Tipos'
for v in ['Napa', 'Corrugado', 'Semi-liso', 'Grabado italiano', 'Liso premium']:
    op_snippet.create.structured_snippet_asset.values.append(v)
asset_ops.append(op_snippet)

# Sitelink adicional - Por que Maxipiel
op_sitelink = client.get_type('AssetOperation')
sl = op_sitelink.create.sitelink_asset
sl.link_text = 'Por que Maxipiel'
sl.description1 = 'Directo de curtiembre en Leon'
sl.description2 = 'Sin intermediarios, precio fijo'
op_sitelink.create.final_urls.append('https://maxipiel.com/pages/por-que-maxipiel')
asset_ops.append(op_sitelink)

asset_resp = asset_service.mutate_assets(customer_id=CUSTOMER_ID, operations=asset_ops)
asset_resources = [r.resource_name for r in asset_resp.results]
print(f'{len(asset_resources)} assets creados')

# Vincular a campana principal
ca_ops = []
callout_type = client.enums.AssetFieldTypeEnum.CALLOUT
snippet_type = client.enums.AssetFieldTypeEnum.STRUCTURED_SNIPPET
sitelink_type = client.enums.AssetFieldTypeEnum.SITELINK

# callouts (primeros 5)
for res in asset_resources[:5]:
    op = client.get_type('CampaignAssetOperation')
    op.create.asset = res
    op.create.campaign = main_camp
    op.create.field_type = callout_type
    ca_ops.append(op)

# snippet (indice 5)
op = client.get_type('CampaignAssetOperation')
op.create.asset = asset_resources[5]
op.create.campaign = main_camp
op.create.field_type = snippet_type
ca_ops.append(op)

# sitelink (indice 6)
op = client.get_type('CampaignAssetOperation')
op.create.asset = asset_resources[6]
op.create.campaign = main_camp
op.create.field_type = sitelink_type
ca_ops.append(op)

ca_resp = campaign_asset_service.mutate_campaign_assets(customer_id=CUSTOMER_ID, operations=ca_ops)
print(f'{len(ca_resp.results)} assets vinculados a campana principal')

print()
print('Callouts agregados:')
for ct in new_callouts:
    print(f'  + {ct}')
print('Structured snippet: Tipos de piel (Napa, Corrugado, Semi-liso, Grabado italiano, Liso premium)')
print('Sitelink: Por que Maxipiel -> maxipiel.com/pages/por-que-maxipiel')
