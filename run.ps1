param(
  [switch]$InstallDeps
)

$ErrorActionPreference = "Stop"

$serverDir = Join-Path $PSScriptRoot "server"
$venvDir = Join-Path $serverDir ".venv"
$venvPython = Join-Path $venvDir "Scripts\python.exe"
$requirements = Join-Path $serverDir "requirements.txt"
$envFile = Join-Path $serverDir ".env"
$envExample = Join-Path $serverDir ".env.example"

if (-not (Test-Path $venvPython)) {
  Write-Host "Creating virtual environment..."
  python -m venv $venvDir
  $InstallDeps = $true
}

if ($InstallDeps) {
  Write-Host "Installing dependencies..."
  & $venvPython -m pip install --upgrade pip
  & $venvPython -m pip install -r $requirements
}

if (-not (Test-Path $envFile) -and (Test-Path $envExample)) {
  Copy-Item $envExample $envFile
  Write-Host "Created server/.env from .env.example"
}

if (Test-Path $envFile) {
  Get-Content $envFile | ForEach-Object {
    $line = $_.Trim()
    if (-not $line -or $line.StartsWith("#")) { return }
    $parts = $line -split "=", 2
    if ($parts.Count -eq 2) {
      [Environment]::SetEnvironmentVariable($parts[0].Trim(), $parts[1].Trim(), "Process")
    }
  }
}

$appHost = if ($env:APP_HOST) { $env:APP_HOST } else { "127.0.0.1" }
$appPort = if ($env:APP_PORT) { $env:APP_PORT } else { "8000" }
$appReload = if ($env:APP_RELOAD) { $env:APP_RELOAD.ToLower() } else { "true" }

Write-Host "Starting FastAPI on http://$appHost`:$appPort"
Set-Location $serverDir

$args = @("-m", "uvicorn", "src.main:app", "--host", $appHost, "--port", $appPort)
if ($appReload -eq "true") {
  $args += "--reload"
}

& $venvPython @args
