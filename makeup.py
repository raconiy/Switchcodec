import os
import shutil
import re

def group_files_by_condition(dataset_path):
    """
    将数据集中的文件按照cond后的数字分组到对应文件夹
    例如：将包含"cond1"的文件移动到cond1文件夹
    """
    # 创建输出目录（如果不存在）
    output_dir = os.path.join(dataset_path, "grouped_conditions")
    os.makedirs(output_dir, exist_ok=True)
    
    # 创建10个分组文件夹
    for i in range(1, 11):
        cond_dir = os.path.join(output_dir, f"cond{i}")
        os.makedirs(cond_dir, exist_ok=True)
    
    # 遍历数据集中的所有文件
    for filename in os.listdir(dataset_path):
        filepath = os.path.join(dataset_path, filename)
        
        # 跳过目录和非文件项
        if not os.path.isfile(filepath):
            continue
        
        # 使用正则表达式查找cond后面的数字
        match = re.search(r'cond(\d+)', filename)
        
        if match:
            cond_num = match.group(1)
            dest_dir = os.path.join(output_dir, f"cond{cond_num}")
            
            # 移动文件到对应分组文件夹
            try:
                shutil.copy2(filepath, os.path.join(dest_dir, filename))
                print(f"已复制: {filename} -> cond{cond_num}")
            except Exception as e:
                print(f"移动文件失败: {filename} - {str(e)}")
        else:
            print(f"跳过文件（未找到cond编号）: {filename}")
    
    print(f"\n文件分组完成！结果保存在: {output_dir}")

if __name__ == "__main__":
    # 设置你的数据集路径
    dataset_path = r"/home/wangxiangbo0126/NHS-SE-master/mushra"  # 替换为你的实际路径
    
    # 执行分组
    group_files_by_condition(dataset_path)