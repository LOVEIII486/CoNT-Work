import os
import json

rewrite_txt_path = "G:\\A\\Desktop\\CoNT Work\\ChatGPT_Aug-main\\rewrite\\rewrite_findings.txt"  # 原始数据集路径
impression_txt_path = "G:\\A\\Desktop\\CoNT Work\\ChatGPT_Aug-main\\second_for_ChatGPT\\second_for_chatgpt_impression.txt"
rewrite_jsonl_path = "G:\\A\\Desktop\\CoNT Work\\ChatGPT_Aug-main\\rewrite\\rewrite_findings_all.jsonl"  # 处理后的数据集路径



def read_txt(txt_path):
    txtfile = open(txt_path)
    text = []
    for line in txtfile:
        text.append(line.strip("\n"))
    return text



# 开始
if os.path.isfile(rewrite_jsonl_path):
    os.remove(rewrite_jsonl_path)

rewrite_findings = read_txt(rewrite_txt_path)
impressions = read_txt(impression_txt_path)

count = 0
for rewrite_finding in rewrite_findings:
    rewrite_jsonl = {'source': rewrite_finding, 'target': impressions[int(count/5)]}
    print("第"+str(int(count/5))+"个")
    print(rewrite_jsonl)
    with open(rewrite_jsonl_path, "a") as f:
        json.dump(rewrite_jsonl, f)
        f.write('\n')
    count = count + 1

