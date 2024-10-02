import os
import binascii

def read_binary_file_to_hex(input_file, output_file):
    """
    读取二进制文件并将其内容转换为十六进制格式，保存到文本文件中。

    :param input_file: 要读取的二进制文件路径
    :param output_file: 保存十六进制内容的文本文件路径
    """
    try:
        # 以二进制方式打开文件
        with open(input_file, 'rb') as f:
            # 读取文件内容
            binary_data = f.read()
            
        # 将二进制数据转换为十六进制字符串
        hex_data = binascii.hexlify(binary_data).decode('utf-8')

        # 在每两个字符之间添加空格
        spaced_hex_data = ' '.join([hex_data[i:i+2] for i in range(0, len(hex_data), 2)])

        # 将十六进制字符串分行，每行32个字符（包含空格）
        hex_lines = [spaced_hex_data[i:i+48] for i in range(0, len(spaced_hex_data), 48)]
        #如果不需要空格，可以将第21行删掉，并且按需要更改24行的代码

        # 保存到文本文件
        with open(output_file, 'w') as f:
            for line in hex_lines:
                f.write(line + '\n')

        print(f"十六进制数据已成功保存到: {output_file}")

    except Exception as e:
        print(f"发生错误: {str(e)}")

# 文件路径设置
input_file_path = '你的文件路径/test.wdnmd'  # 输入文件路径
output_file_path = '你的文件路径/test_hex.txt'  # 输出文件路径

# 调用函数
read_binary_file_to_hex(input_file_path, output_file_path)
