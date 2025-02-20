import json

def parse_json_file():
    try:
        # 修改文件路径
        file_path = '/Users/mariyaerzhan/Desktop/pp2/PP2LAB/LAB4/sample-data.json'
        with open(file_path, 'r') as file:
            data = json.load(file)

        print("Interface Status")
        print("=" * 80)
        print("{:<50}{:<20}{:<10}{:<10}".format("DN", "Description", "Speed", "MTU"))
        print("-" * 80)

        for item in data['imdata']:
            attributes = item['l1PhysIf']['attributes']
            dn = attributes['dn']
            description = attributes['descr']
            speed = attributes['speed']
            mtu = attributes['mtu']
            print("{:<50}{:<20}{:<10}{:<10}".format(dn, description, speed, mtu))

    except FileNotFoundError:
        print("未找到指定路径下的 'sample - data.json' 文件，请检查路径是否正确。")
    except KeyError:
        print("JSON 数据中没有预期的键。")
    except json.JSONDecodeError:
        print("解码 JSON 数据时出现错误。")


if __name__ == "__main__":
    parse_json_file()