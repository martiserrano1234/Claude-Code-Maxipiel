# Helper SP-API Maxipiel — carga credenciales (gitignored), obtiene access token y llama a la API.
# Uso:
#   . .\projects\amazon-maxipiel\spapi.ps1      (cargar funciones)
#   $r = Invoke-SpApi "/sellers/v1/marketplaceParticipations"
#   $r = Invoke-SpApi "/catalog/2022-04-01/items/B0FN31DR63?marketplaceIds=A1AM78C64UM0Y8&includedData=summaries"

$script:SpApiSecretsPath = Join-Path $PSScriptRoot "secrets.local.json"

function Get-SpApiToken {
  $s = Get-Content $script:SpApiSecretsPath -Raw | ConvertFrom-Json
  $body = @{
    grant_type    = 'refresh_token'
    refresh_token = $s.refresh_token
    client_id     = $s.lwa_client_id
    client_secret = $s.lwa_client_secret
  }
  $tok = Invoke-RestMethod -Uri $s.token_endpoint -Method Post -Body $body -ContentType 'application/x-www-form-urlencoded'
  return @{ token = $tok.access_token; endpoint = $s.region_endpoint; marketplace = $s.marketplace_id_mx }
}

function Invoke-SpApi {
  param(
    [Parameter(Mandatory=$true)][string]$Path,
    [string]$Method = 'GET',
    $Body = $null
  )
  $ctx = Get-SpApiToken
  $headers = @{ 'x-amz-access-token' = $ctx.token }
  $uri = "$($ctx.endpoint)$Path"
  if ($Body) {
    return Invoke-RestMethod -Uri $uri -Method $Method -Headers $headers -Body ($Body | ConvertTo-Json -Depth 20) -ContentType 'application/json'
  } else {
    return Invoke-RestMethod -Uri $uri -Method $Method -Headers $headers
  }
}
