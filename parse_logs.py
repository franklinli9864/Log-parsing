from drain3 import TemplateMiner
from drain3.template_miner_config import TemplateMinerConfig

def run_drain_and_save(input_file='extracted_raw_logs.txt', output_file='parsed_results.txt'):
    config = TemplateMinerConfig()
    template_miner = TemplateMiner(config=config)

    print(f"--- 開始解析並打包至 {output_file} ---")

    try:
        with open(input_file, 'r', encoding='utf-8') as f_in, \
             open(output_file, 'w', encoding='utf-8') as f_out:
            
            # 寫入標題行
            f_out.write(f"{'Template_ID':<12} | {'Parsed_Template'}\n")
            f_out.write("-" * 80 + "\n")

            for line in f_in:
                line = line.strip()
                if not line:
                    continue
                
                # 執行 Drain 解析
                result = template_miner.add_log_message(line)
                cluster_id = result.get("cluster_id")
                
                # 自動偵測 Cluster 物件位置 (相容性邏輯)
                cluster = None
                if hasattr(template_miner, 'id_to_cluster'):
                    cluster = template_miner.id_to_cluster.get(cluster_id)
                elif hasattr(template_miner, 'drain'):
                    cluster = template_miner.drain.id_to_cluster.get(cluster_id)

                if cluster:
                    template = cluster.get_template()
                    # 將解析結果寫入檔案： ID | 模板內容
                    f_out.write(f"ID_{cluster_id:<9} | {template}\n")

        print(f"\n成功！解析結果已儲存至: {output_file}")
        
        # 額外產出一個摘要：每個 ID 出現了幾次
        print("正在生成統計摘要...")
        with open('template_summary.txt', 'w', encoding='utf-8') as f_sum:
            f_sum.write("=== 模板統計摘要 ===\n")
            all_clusters = []
            if hasattr(template_miner, 'get_all_clusters'):
                all_clusters = template_miner.get_all_clusters()
            elif hasattr(template_miner, 'drain'):
                all_clusters = template_miner.drain.id_to_cluster.values()
            
            for c in sorted(all_clusters, key=lambda x: x.size, reverse=True):
                f_sum.write(f"ID: {c.cluster_id:<5} | 出現次數: {c.size:<5} | 模板: {c.get_template()}\n")
        
        print("統計摘要已儲存至: template_summary.txt")

    except Exception as e:
        print(f"執行出錯: {e}")

if __name__ == "__main__":
    run_drain_and_save()

