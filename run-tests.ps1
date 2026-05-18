param(
  [switch]$InstallDeps
)

$ErrorActionPreference = "Stop"

$serverDir = Join-Path $PSScriptRoot "server"
$venvDir = Join-Path $serverDir ".venv"
$venvPython = Join-Path $venvDir "Scripts\python.exe"
$requirements = Join-Path $serverDir "requirements.txt"

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

Write-Host "Running tests..."
Set-Location $serverDir
& $venvPython -m pytest -q
