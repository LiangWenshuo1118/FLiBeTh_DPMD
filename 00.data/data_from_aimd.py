import dpdata

# 读取数据
folder = "FLiBeTh5"
data = dpdata.LabeledSystem(f'./{folder}/OUTCAR', fmt='vasp/outcar')

# 生成等间隔抽取的训练索引
index_training = [i for i in range(len(data)) if i % 10 == 0]
# 测试索引为非训练索引
index_validation = list(set(range(len(data))) - set(index_training))

# 根据索引创建训练和测试数据子集
data_training = data.sub_system(index_training)
data_validation = data.sub_system(index_validation)

# 将训练数据保存到"training_data"目录
data_training.to_deepmd_npy(f'{folder}/training_data')
#data_training.to_deepmd_raw(f'{folder}/training_data')

# 将测试数据保存到"validation_data"目录
data_validation.to_deepmd_npy(f'{folder}/validation_data')
#data_validation.to_deepmd_raw(f'{folder}/validation_data')

# 打印数据信息
print(f'# the data contains {len(data)} frames')
print(f'# the training data contains {len(data_training)} frames')
print(f'# the validation data contains {len(data_validation)} frames')

