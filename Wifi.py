import subprocess

# Lấy danh sách profile WiFi đã lưu
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')

profiles = []
for i in data:
    if "All User Profile" in i:
        profiles.append(i.split(":")[1].strip())

# Duyệt qua từng profile và lấy mật khẩu nếu có
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        password = None
        for b in results:
            if "Key Content" in b:
                password = b.split(":")[1].strip()
                break
        print("{:<30} | {:<}".format(i, password if password else "NO PASSWORD"))
    except Exception as e:
        print("{:<30} | {:<}".format(i, "ERROR OCCURRED"))
