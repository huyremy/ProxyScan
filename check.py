import requests
# check proxy list by HuyRemy - huynq@isi.com.vn
# Đọc các proxy từ file proxy.1st
def load_proxies(filename):
    with open(filename, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

# Hàm để kiểm tra kết nối proxy
def check_proxy(proxy):
    try:
        response = requests.get('https://httpbin.org/ip', proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Kết nối thành công với proxy: {proxy}")
            return True
    except requests.RequestException:
        print(f"Kết nối thất bại với proxy: {proxy}")
    return False

# Hàm để lưu lại các proxy thành công
def save_proxies(filename, valid_proxies):
    with open(filename, 'w') as file:
        for proxy in valid_proxies:
            file.write(proxy + '\n')

# Main function
def main():
    proxy_file = 'proxy.1st'
    proxies = load_proxies(proxy_file)
    valid_proxies = []

    for proxy in proxies:
        if check_proxy(proxy):
            valid_proxies.append(proxy)  # Thêm proxy hợp lệ vào danh sách

    # Lưu lại các proxy hợp lệ
    save_proxies(proxy_file, valid_proxies)
    print(f"\nĐã lưu {len(valid_proxies)} proxy hợp lệ vào file {proxy_file}.")

if __name__ == "__main__":
    main()
