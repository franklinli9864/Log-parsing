def export_raw_logs_to_file(source_path='/var/log/syslog', output_file='extracted_raw_logs.txt', limit=50):
    """
    將 Linux 原始日誌直接打包匯出為 .txt 檔案
    """
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            # 讀取日誌內容
            lines = f.readlines()
            # 取得最後 N 條
            target_content = lines[-limit:]
            
        # 寫入目標檔案
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.writelines(target_content)
            
        print(f"成功！原始日誌已打包至: {output_file}")
        print(f"共匯出 {len(target_content)} 條記錄。")

    except PermissionError:
        print("錯誤：權限不足，請使用 'sudo python3 script.py' 執行。")
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    export_raw_logs_to_file()
