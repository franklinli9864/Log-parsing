

```markdown
# Automated Log Collection and Parsing with Drain3

本專案實作了一個自動化的日誌分析流水線（Pipeline），能夠從 Linux 系統環境中提取原始日誌，並利用學術界廣泛使用的 **Drain3** 演算法進行結構化解析。此工具特別適用於日誌異常檢測（Anomaly Detection）的預處理階段。

## 🛠️ 技術棧
- **Language:** Python 3
- **Algorithm:** Drain (Fixed-Depth Prefix Tree)
- **Environment:** Ubuntu/Linux (Syslog support)

## 📂 專案檔案說明

- `system.py`: **數據採集模組**。負責從 `/var/log/syslog` 讀取 100% 原始日誌，並匯出至純文字檔。
- `parse_logs.py`: **日誌解析模組**。讀取採集到的 Raw Log，透過 Drain3 引擎進行模板提取與事件分類。
- `extracted_raw_logs.txt`: 採集到的原始系統日誌範例（Raw Data）。
- `parsed_results.txt`: 解析後的詳細對照表，標註每行日誌對應的 Template ID。
- `template_summary.txt`: 最終統計摘要，統計各類模板出現的頻率與分佈。

## 🚀 快速開始

### 1. 安裝環境依賴
請確保已安裝 `drain3` 庫：
```bash
pip3 install drain3
```

### 2. 數據採集

使用管理員權限執行 `system.py` 以讀取系統日誌：

```bash
sudo python3 system.py

```

### 3. 日誌解析與統計

執行 `parse_logs.py` 開始進行結構化分析：

```bash
python3 parse_logs.py

```

## 📊 解析效果演示

**原始日誌 (Raw Log):**
`Mar 9 10:05:12 ubuntu systemd[1]: Starting Daily apt upgrade...`

**Drain3 解析模板 (Event Template):**
`ID_1 | Mar 9 10:05:12 ubuntu systemd[<*>]: Starting Daily apt upgrade...`

## 📝 研究應用

本工具產出的結果符合 Loghub 等國際標準數據集格式，可用於：

1. **Log Clustering**: 自動歸類海量日誌。
2. **Anomaly Detection**: 基於 Template ID 序列進行異常行為預測。
3. **System Monitoring**: 統計系統頻發事件，優化運維效率。

---

*本專案為學術研究用途，開發於國立臺灣科技大學 (NTUST)。*

```
