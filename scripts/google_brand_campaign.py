import sys
sys.stdout.reconfigure(encoding='utf-8')
from google.ads.googleads.client import GoogleAdsClient

config = {
    'developer_token': 'TU_DEVELOPER_TOKEN',
    'client_id': 'TU_CLIENT_ID',
    'client_secret': 'TU_CLIENT_SECRET',
    'refresh_token': 'TU_REFRESH_TOKEN',
    'login_customer_id': '4020002227',
    'use_proto_plus': False  # usar protobuf nativo para controlar campos booleanos
}

client = GoogleAdsClient.load_from_dict(config)
budget_service = client.get_service('CampaignBudgetService')
campaign_service = client.get_service('CampaignService')
ad_group_service = client.get_service('AdGroupService')
ad_group_ad_service = client.get_service('AdGroupAdService')
kw_service = client.get_service('AdGroupCriterionService')

CUSTOMER_ID = '6619664178'

# PASO 1: Presupuesto
budget_op = client.get_type('CampaignBudgetOperation')
b = budget_op.create
b.name = 'Brand Maxipiel Budget'
b.amount_micros = 30_000_000
b.delivery_method = client.enums.BudgetDeliveryMethodEnum.STANDARD

budget_resp = budget_service.mutate_campaign_budgets(customer_id=CUSTOMER_ID, operations=[budget_op])
budget_resource = budget_resp.results[0].resource_name
print(f'[1/5] Presupuesto: $30 MXN/dia')

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
c.contains_eu_political_advertising = False  # campo requerido

camp_resp = campaign_service.mutate_campaigns(customer_id=CUSTOMER_ID, operations=[camp_op])
brand_campaign_resource = camp_resp.results[0].resource_name
print(f'[2/5] Campana brand creada: Brand - Maxipiel')

# PASO 3: Ad group
ag_op = client.get_type('AdGroupOperation')
ag = ag_op.create
ag.name = 'Brand Maxipiel Keywords'
ag.campaign = brand_campaign_resource
ag.status = client.enums.AdGroupStatusEnum.ENABLED
ag.type_ = client.enums.AdGroupTypeEnum.SEARCH_STANDARD
ag.cpc_bid_micros = 5_000_000

ag_resp = ad_group_service.mutate_ad_groups(customer_id=CUSTOMER_ID, operations=[ag_op])
brand_ag_resource = ag_resp.results[0].resource_name
print(f'[3/5] Ad group brand creado')

# PASO 4: Keywords brand (exact match)
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
print(f'[4/5] {len(kw_resp.results)} keywords brand creadas')

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
    h = rsa.headlines.add()
    h.text = h_text

for d_text in [
    'Piel genuina para tapiceros. Envio a todo Mexico. Precio fijo sin regateo.',
    'Directo de curtiembre en Leon Gto. Sin intermediarios. Compra en linea 24/7.',
]:
    d = rsa.descriptions.add()
    d.text = d_text

ad.ad.final_urls.append('https://maxipiel.com')

ad_resp = ad_group_ad_service.mutate_ad_group_ads(customer_id=CUSTOMER_ID, operations=[ad_op])
print(f'[5/5] Anuncio RSA brand creado')

print()
print('=== CAMPANA BRAND LISTA ===')
print('Nombre: Brand - Maxipiel')
print('Presupuesto: $30 MXN/dia | CPC max: $8 MXN')
print('Keywords: [maxipiel], [maxi piel], [maxipiel piel], [maxipiel cuero], [maxipiel tapiceria]')
