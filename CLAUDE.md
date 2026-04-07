# CLAUDE.md — ariheart2026 完整移轉任務書

## 你的角色

你是這個專案的自主執行工程師。請閱讀本文件的全部任務，
依序自動完成，不需要等待我的確認（除非遇到真正的錯誤）。
每完成一個任務，在對應的 [ ] 打上 [x]。

## 專案基本資訊

- XML 來源: tools/wp_export.xml（josh039snotebook.WordPress.2026-04-07.xml）
- Hugo 網站名稱: ariheart2026
- 目標目錄: 當前目錄 ~/Projects/ariheart2026/
- GitHub repo 名稱: ariheart2026（之後手動建立）
- 語言: 中文（zh-tw），部分文章可能有英文

## 自動執行任務清單

### Phase 1 — 環境準備

- [ ] 確認 Python 3 已安裝（python3 --version）
- [ ] 確認 Hugo 已安裝（hugo version）；若無則輸出安裝指令讓我執行
- [ ] 執行 pip3 install lxml markdownify requests pyyaml pillow
- [ ] 建立 tools/requirements.txt 記錄所有依賴

### Phase 2 — 分析 XML 內容

- [ ] 讀取 tools/wp_export.xml
- [ ] 統計並輸出：文章總數、頁面數、圖片數量、使用的標籤、分類
- [ ] 把統計結果寫入 tools/audit_report.txt
- [ ] 建立 tools/taxonomy_map.json（WordPress 標籤/分類 → Hugo taxonomy）

### Phase 3 — 建立轉換腳本

- [ ] 建立 tools/wp_to_hugo.py（完整的 WordPress XML → Hugo Markdown 轉換腳本）
      規格：
  - front matter 包含 title, date, slug, tags, categories, draft: false
  - 保留原始 slug（用於 SEO）
  - 將圖片 URL 由 WordPress CDN 改寫為 /images/[year]/[filename]
  - HTML 表格轉為標準 Markdown 表格
  - 跳過 status != publish 的文章（草稿不轉）
  - 輸出目錄：content/posts/
- [ ] 執行 python3 tools/wp_to_hugo.py --dry-run 確認無錯誤
- [ ] 執行 python3 tools/wp_to_hugo.py（全量轉換）

### Phase 4 — 圖片搬遷

- [ ] 建立 tools/image_fetch.py（從 XML 解析所有圖片 URL 並下載）
      規格：
  - 下載至 static/images/[year]/[filename]
  - 跳過已存在的檔案
  - 下載失敗的記錄到 tools/image_errors.txt
- [ ] 執行 python3 tools/image_fetch.py

### Phase 5 — Hugo 初始化

- [ ] hugo new site . --force（在當前目錄初始化）
- [ ] 安裝主題 PaperMod：
      git init
      git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
- [ ] 建立完整的 config.toml（包含：baseURL, title, theme, 語言設定,
      分頁設定, 選單, 作者資訊, SEO 相關設定）
- [ ] 建立 content/about.md（About 頁面，標題「關於我」）
- [ ] 建立 content/portfolio/\_index.md（作品集索引頁）

### Phase 6 — GitHub Actions

- [ ] 建立 .github/workflows/deploy.yml
      規格：push to main → hugo build → 部署到 GitHub Pages
      使用 peaceiris/actions-hugo@v3 + actions/deploy-pages@v2

### Phase 7 — 驗證

- [ ] 建立 tools/validate.py（檢查所有 .md 檔案的 front matter 完整性）
- [ ] 執行驗證腳本，輸出問題清單到 tools/validation_report.txt
- [ ] 執行 hugo server --buildDrafts 在背景測試（確認可以啟動）
- [ ] 建立 static/robots.txt
- [ ] 確認 config.toml 已設定 sitemap

## 完成後請輸出

1. 轉換成功的文章數量
2. 下載成功的圖片數量
3. 任何需要我手動處理的事項清單
4. 執行 hugo server 的指令，讓我可以在瀏覽器預覽

## 注意事項

- 所有腳本加上 try/except 錯誤處理，不要因為單一失敗就中斷
- 圖片下載加上 time.sleep(0.5) 避免被 WordPress 封鎖
- 如果 Hugo 未安裝，在輸出安裝指令後暫停，等我安裝完再繼續
- 不要建立 GitHub repo（我自己會建），只準備好本地端的所有檔案
