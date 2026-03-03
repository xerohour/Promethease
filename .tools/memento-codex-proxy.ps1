param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("list", "get")]
    [string]$Command,
    [string]$SessionId
)

$ErrorActionPreference = "Stop"

$sessionsRoot = Join-Path $HOME ".codex\sessions"

function Get-SessionFiles {
    if (-not (Test-Path $sessionsRoot)) {
        return @()
    }

    Get-ChildItem -Path $sessionsRoot -Recurse -File -Filter "*.jsonl" |
        Sort-Object LastWriteTime -Descending
}

function Parse-SessionMeta {
    param([string]$FilePath)

    $meta = $null
    foreach ($line in Get-Content -Path $FilePath -TotalCount 250) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        try {
            $obj = $line | ConvertFrom-Json -ErrorAction Stop
        } catch {
            continue
        }

        if ($obj.type -eq "session_meta" -and $obj.payload) {
            $payload = $obj.payload
            if ($payload.id) {
                $meta = [PSCustomObject]@{
                    id        = [string]$payload.id
                    timestamp = [string]$payload.timestamp
                    cwd       = [string]$payload.cwd
                    file      = $FilePath
                }
                break
            }
        }
    }
    return $meta
}

function Get-TextFromContentItems {
    param($ContentItems)

    $parts = @()
    if ($null -eq $ContentItems) {
        return ""
    }

    foreach ($item in $ContentItems) {
        if ($null -eq $item) { continue }

        if ($item.PSObject.Properties.Name -contains "text" -and $item.text) {
            $parts += [string]$item.text
        } elseif ($item.PSObject.Properties.Name -contains "input_text" -and $item.input_text) {
            $parts += [string]$item.input_text
        } elseif ($item.PSObject.Properties.Name -contains "output_text" -and $item.output_text) {
            $parts += [string]$item.output_text
        }
    }

    return ($parts -join "`n").Trim()
}

function Normalize-Role {
    param([string]$Role)
    $safeRole = ""
    if ($null -ne $Role) { $safeRole = [string]$Role }
    switch ($safeRole.ToLowerInvariant()) {
        "user" { return "user" }
        "assistant" { return "assistant" }
        "system" { return "system" }
        "developer" { return "system" }
        "tool" { return "tool" }
        default { return "assistant" }
    }
}

if ($Command -eq "list") {
    $results = @()
    foreach ($file in Get-SessionFiles) {
        $meta = Parse-SessionMeta -FilePath $file.FullName
        if ($null -eq $meta) { continue }

        $titleParts = @()
        if ($meta.timestamp) { $titleParts += $meta.timestamp }
        if ($meta.cwd) { $titleParts += $meta.cwd }
        $title = ($titleParts -join " | ").Trim()
        if ([string]::IsNullOrWhiteSpace($title)) {
            $title = "Codex session"
        }

        $results += [PSCustomObject]@{
            id    = $meta.id
            title = $title
        }
    }

    $results |
        Group-Object id |
        ForEach-Object { $_.Group[0] } |
        ConvertTo-Json -Depth 4
    exit 0
}

if (-not $SessionId) {
    Write-Error "SessionId is required for 'get'."
    exit 1
}

$targetMeta = $null
foreach ($file in Get-SessionFiles) {
    $meta = Parse-SessionMeta -FilePath $file.FullName
    if ($null -ne $meta -and $meta.id -eq $SessionId) {
        $targetMeta = $meta
        break
    }
}

if ($null -eq $targetMeta) {
    Write-Error "Session '$SessionId' not found under $sessionsRoot."
    exit 1
}

$messages = New-Object System.Collections.Generic.List[object]
foreach ($line in Get-Content -Path $targetMeta.file) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    try {
        $obj = $line | ConvertFrom-Json -ErrorAction Stop
    } catch {
        continue
    }

    if ($obj.type -ne "response_item") { continue }
    if ($null -eq $obj.payload) { continue }
    if ($obj.payload.type -ne "message") { continue }

    $role = Normalize-Role -Role ([string]$obj.payload.role)
    $text = Get-TextFromContentItems -ContentItems $obj.payload.content
    if ([string]::IsNullOrWhiteSpace($text)) { continue }

    $messages.Add([PSCustomObject]@{
        role    = $role
        content = $text
    })
}

$sessionTitle = @($targetMeta.timestamp, $targetMeta.cwd) -ne $null
$sessionTitle = (@($targetMeta.timestamp, $targetMeta.cwd) | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }) -join " | "
if ([string]::IsNullOrWhiteSpace($sessionTitle)) {
    $sessionTitle = "Codex session $SessionId"
}

[PSCustomObject]@{
    id       = $SessionId
    title    = $sessionTitle
    messages = $messages
} | ConvertTo-Json -Depth 8
