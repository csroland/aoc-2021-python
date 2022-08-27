def bits_to_int(inp):
    num = 0
    for i, bit in enumerate(inp):
        num += int(bit)*2**(len(inp)-i-1)
    return num
        
def part1():
    with open("data.txt", "r") as f:
        dataset = f.read().splitlines()
        length_of_report = len(dataset)
        length_of_data = len(dataset[0])
        zeros_at_index = [0] * length_of_data
        gamma_rate_bits, epsilon_rate_bits = [], []
        for data in dataset:
            data_bits = [x for x in data]
            for i, bit in enumerate(data_bits):
                if bit == "0":
                    zeros_at_index[i] += 1
        for count in zeros_at_index:
            if count < length_of_report/2:
                gamma_rate_bits.append(1)
                epsilon_rate_bits.append(0)
            else:
                gamma_rate_bits.append(0)
                epsilon_rate_bits.append(1)
        gamma_rate, epsilon_rate = bits_to_int(gamma_rate_bits), bits_to_int(epsilon_rate_bits)
    return gamma_rate*epsilon_rate
    
def part2():
    with open("data.txt", "r") as f:
        dataset = f.read().splitlines()
        length_of_report = len(dataset)
        length_of_data = len(dataset[0])
        oxy_gen_rate, co2_rate, data_to_remove = 0, 0, []
        found = False
        dataset_copy = [x for x in dataset]
        while not found:
            for bit in range(length_of_data):
                zero_bits_counted = 0
                for data in dataset_copy:
                    if data[bit] == "0":
                        zero_bits_counted += 1
                if zero_bits_counted <= len(dataset_copy)/2:
                    for data in dataset_copy:
                        if data[bit] == "0":
                            data_to_remove.append(data)
                else:
                    for data in dataset_copy:
                        if data[bit] == "1":
                            data_to_remove.append(data)
                for data in data_to_remove:
                    dataset_copy.remove(data)
                data_to_remove.clear()
                zero_bits_counted = 0
                if len(dataset_copy) == 1:
                    oxy_gen_rate = bits_to_int(dataset_copy[0])
                    found = True
                    break
        dataset_copy = [x for x in dataset]
        found = False
        while not found:
            for bit in range(length_of_data):
                zero_bits_counted = 0
                for data in dataset_copy:
                    if data[bit] == "0":
                        zero_bits_counted += 1
                if zero_bits_counted > len(dataset_copy)-zero_bits_counted:
                    for data in dataset_copy:
                        if data[bit] == "0":
                            data_to_remove.append(data)
                else:
                    for data in dataset_copy:
                        if data[bit] == "1":
                            data_to_remove.append(data)
                for data in data_to_remove:
                    dataset_copy.remove(data)
                data_to_remove.clear()
                if len(dataset_copy) == 1:
                    co2_rate = bits_to_int(dataset_copy[0])
                    return oxy_gen_rate*co2_rate
    
def main():
    print(part1())
    print(part2())
    
if __name__ == "__main__":
    main()
