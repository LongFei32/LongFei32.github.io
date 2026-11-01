# 一键发布：生成网站 → 部署到 gh-pages → 备份源码到 main
# 用法：  .\publish.ps1 "这次改了什么"
# 不加参数也行，默认提交信息是"更新站点"

param(
    [string]$Message = "更新站点"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "[1/4] 生成静态文件..." -ForegroundColor Cyan
npx hexo clean | Out-Null
npx hexo generate | Select-Object -Last 1

Write-Host "[2/4] 部署到 GitHub Pages..." -ForegroundColor Cyan
npx hexo deploy | Select-Object -Last 1
if ($LASTEXITCODE -ne 0) {
    Write-Host "      部署失败，先解决上面的报错" -ForegroundColor Red
    exit 1
}

Write-Host "[3/4] 提交源码..." -ForegroundColor Cyan
git add -A
git diff --cached --quiet
if ($LASTEXITCODE -eq 0) {
    Write-Host "      没有源码改动，跳过提交" -ForegroundColor DarkGray
} else {
    git commit -m $Message | Out-Null
    # 先同步远端，避免"remote contains work you do not have"导致 push 被拒
    git pull --rebase --autostash origin main 2>&1 | Out-Null
    git push 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "      推送失败，运行 git status 看看冲突" -ForegroundColor Red
        exit 1
    }
    Write-Host "      已推送到 main" -ForegroundColor DarkGray
}

Write-Host "[4/4] 完成。约 30~60 秒后刷新：" -ForegroundColor Cyan
Write-Host "      https://longfei32.github.io/" -ForegroundColor Green
