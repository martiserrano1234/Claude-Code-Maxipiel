import sys
sys.stdout.reconfigure(encoding='utf-8')
from google.ads.googleads.client import GoogleAdsClient

config = {
    'developer_token': 'TU_DEVELOPER_TOKEN',
    'client_id': 'TU_CLIENT_ID',
    'client_secret': 'TU_CLIENT_SECRET',
    'refresh_token': 'TU_REFRESH_TOKEN',
    'login_customer_id': '4020002227',
    'use_proto_plus': True
}

client = GoogleAdsClient.load_from_dict(config)
budget_service = client.get_service('CampaignBudgetService')
campaign_service = client.get_service('CampaignService')
ad_group_service = client.get_service('AdGroupService')
ad_group_ad_service = client.get_service('AdGroupAdService')
kw_service = client.get_service('AdGroupCriterionService')
asset_service = client.get_service('AssetService')
campaign_asset_service = client.get_service('CampaignAssetService')

CUSTOMER_ID = '6619664178'
MAIN_CAMPAIGN_ID = '22621305349'

# PASO 1: Presupuesto brand
budget_op = client.get_type('CampaignBudgetOperation')
b = budget_op.create
b.name = 'Presupuesto Brand Maxipiel 2'
b.amount_micros = 30_000_000
b.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD

budget_resp = budget_service.mutate_campaign_budgets(customer_id=CUSTOMER_ID, operations=[budget_op])
budget_resource = budget_resp.results[0].resource_name
print('[1/6] Presupuesto brand: $30 MXN/dia')

# PASO 2: Campana brand
camp_op = client.get_type('CampaignOperation')
c = camp_op.create
c.name = 'Brand - Maxipiel'
c.status = client.enums.CampaignStatusEnum.ENABLED
c.advertising_channel_type = client.enums.AdvertisingChannelTypeEnum.SEARCH
c.campaign_budget = budget_resource
c.target_spend.cpc_bid_ceiling_micros = 8_000_000
c.network_settings.target_google_search = True
c.network_settings.target_search_network = False
c.network_settings.target_content_network = False
c.contains_eu_political_advertising = False

camp_resp = campaign_service.mutate_campaigns(customer_id=CUSTOMER_ID, operations=[camp_op])
brand_campaign_resource = camp_resp.results[0].resource_name
print('[2/6] Campana brand creada: Brand - Maxipiel')

# PASO 3: Ad group brand
ag_op = client.get_type('AdGroupOperation')
ag = ag_op.create
ag.name = 'Brand - Keywords Maxipiel'
ag.campaign = brand_campaign_resource
ag.status = client.enums.AdGroupStatusEnum.ENABLED
ag.type_ = client.enums.AdGroupTypeEnum.SEARCH_STANDARD
ag.cpc_bid_micros = 5_000_000

ag_resp = ad_group_service.mutate_ad_groups(customer_id=CUSTOMER_ID, operations=[ag_op])
brand_ag_resource = ag_resp.results[0].resource_name
print('[3/6] Ad group brand creado')

# PASO 4: Keywords brand (exact)
brand_keywords = ['maxipiel', 'maxi piel', 'maxipiel piel', 'maxipiel cuero', 'maxipiel tapiceria']
kw_ops = []
for kw in brand_keywords:
    op = client.get_type('AdGroupCriterionOperation')
    k = op.create
    k.ad_group = brand_ag_resource
    k.status = client.enums.AdGroupCriterionStatusEnum.ENABLED
    k.keyword.text = kw
    k.keyword.match_type = client.enums.KeywordMatchTypeEnum.EXACT
    kw_ops.append(op)

kw_resp = kw_service.mutate_ad_group_criteria(customer_id=CUSTOMER_ID, operations=kw_ops)
print(f'[4/6] {len(kw_resp.results)} keywords brand: {brand_keywords}')

# PASO 5: Anuncio RSA brand
ad_op = client.get_type('AdGroupAdOperation')
ad = ad_op.create
ad.ad_group = brand_ag_resource
ad.status = client.enums.AdGroupAdStatusEnum.ENABLED

rsa = ad.ad.responsive_search_ad
for h_text in [
    'Maxipiel - Piel Genuina Oficial',
    'Maxipiel - Directo de Leon Gto',
    'Tienda Oficial Maxipiel',
    'Maxipiel - 30 Colores en Stock',
    'Compra en Maxipiel.com',
]:
    h = client.get_type('AdTextAsset')
    h.text = h_text
    rsa.headlines.append(h)

for d_text in [
    'Piel genuina para tapiceros. Envio a todo Mexico. Precio fijo sin regateo.',
    'Directo de curtiembre en Leon Gto. Sin intermediarios. Compra en linea 24/7.',
]:
    d = client.get_type('AdTextAsset')
    d.text = d_text
    rsa.descriptions.append(d)

ad.ad.final_urls.append('https://maxipiel.com')

ad_resp = ad_group_ad_service.mutate_ad_group_ads(customer_id=CUSTOMER_ID, operations=[ad_op])
print('[5/6] Anuncio RSA brand creado')

# PASO 6: Nuevas extensiones para campana principal
asset_ops = []

new_callouts = [
    'Directo de curtiembre',
    'Precio fijo sin regateo',
    '30 colores disponibles',
    'Envio en 4 a 6 dias',
    'Sin intermediarios',
]
for ct in new_callouts:
    op = client.get_type('AssetOperation')
    a = op.create
    a.callout_asset.callout_text = ct
    asset_ops.append(op)

# Structured snippet - tipos de piel
op_snippet = client.get_type('AssetOperation')
s = op_snippet.create
s.structured_snippet_asset.header = 'Tipos de piel'
for v in ['Napa', 'Corrugado', 'Semi-liso', 'Grabado italiano', 'Liso premium']:
    s.structured_snippet_asset.values.append(v)
asset_ops.append(op_snippet)

asset_resp = asset_service.mutate_assets(customer_id=CUSTOMER_ID, operations=asset_ops)
asset_resources = [r.resource_name for r in asset_resp.results]
print(f'[6/6] {len(asset_resources)} assets creados')

# Vincular a campana principal
ca_ops = []
callout_type = client.enums.AssetFieldTypeEnum.CALLOUT
snippet_type = client.enums.AssetFieldTypeEnum.STRUCTURED_SNIPPET
main_camp = campaign_service.campaign_path(CUSTOMER_ID, MAIN_CAMPAIGN_ID)

for res in asset_resources[:-1]:
    op = client.get_type('CampaignAssetOperation')
    ca = op.create
    ca.asset = res
    ca.campaign = main_camp
    ca.field_type = callout_type
    ca_ops.append(op)

op = client.get_type('CampaignAssetOperation')
ca = op.create
ca.asset = asset_resources[-1]
ca.campaign = main_camp
ca.field_type = snippet_type
ca_ops.append(op)

ca_resp = campaign_asset_service.mutate_campaign_assets(customer_id=CUSTOMER_ID, operations=ca_ops)
print(f'   {len(ca_resp.results)} assets vinculados a campana principal')

print()
print('=== TODO LISTO ===')
print('Campana brand: Brand - Maxipiel ($30 MXN/dia, CPC max $8 MXN)')
print('Keywords: [maxipiel], [maxi piel], [maxipiel piel], [maxipiel cuero], [maxipiel tapiceria]')
print('Callouts nuevos: Directo de curtiembre | Precio fijo | 30 colores | Envio 4-6 dias | Sin intermediarios')
print('Structured snippet: Tipos de piel (Napa, Corrugado, Semi-liso, Grabado italiano, Liso premium)')
