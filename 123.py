import random
from scapy.all import rdpcap, wrpcap, IP

# 随机生成一个IPv4地址
def generate_random_ip():
    return ".".join([str(random.randint(1, 255)) for _ in range(4)])

# 修改PCAP文件中每个包的源和目的IP地址
def modify_pcap(pcap_file, output_file):
    packets = rdpcap(pcap_file)  # 读取PCAP文件

    for packet in packets:
        if IP in packet:
            # 随机生成新的源和目的IP地址
            new_src_ip = generate_random_ip()
            new_dst_ip = generate_random_ip()
            
            packet[IP].src = new_src_ip
            packet[IP].dst = new_dst_ip
            
            # 删除IP校验和以便重新计算
            del packet[IP].chksum
    
    # 写回修改后的PCAP文件
    wrpcap(output_file, packets)
    print(f"Modified PCAP saved to {output_file}")

if __name__ == "__main__":
    # 指定PCAP文件路径
    pcap_file = "wo"
    
    # 指定输出文件路径
    output_file = "C:\\Users\\12461\\Desktop\\样本数据\\DNS2TCP3"
    
    # 修改PCAP
    modify_pcap(pcap_file, output_file)
