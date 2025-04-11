def full_atop_logs(self, write_time=15):

    from statistics import median
    import paramiko
    from time import sleep
    from datetime import datetime
    from color import color

    log_pref = str('192.168.202.221').strip().split('.')[-1]
    print(f'{color.grey("atop_stats")} {color.yellow("[START]")}')
    

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.202.221', port=22, username='user', password='stilsoft')
    

    stdin, stdout, stderr = ssh.exec_command('which atop')
    if not stdout.read().decode().strip():
        print(f'{color.red("[atop НЕ УСТАНОВЛЕН]")} на 202.221')
        return

    ssh.exec_command(f'atop -w /home/user/atop.txt 1 {write_time}')
    sleep(write_time + 1)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    

    ssh.exec_command(f'atop -r /home/user/atop.txt > /home/user/log.txt')
    sleep(1)
    

    sftp_client = ssh.open_sftp()
    sftp_client.get('/home/user/log.txt', f'D:/work/logs/{log_pref}_atop_full.txt')
    sftp_client.remove('/home/user/atop.txt')
    sftp_client.remove('/home/user/log.txt')
    sftp_client.close()
    ssh.close()


    stats = {
        'CPU': {
            'sys': [], 'user': [], 'idle': [], 'wait': [], 'steal': []
        },
        'MEM': {
            'total': [], 'free': [], 'cache': [], 'dirty': [], 'buff': []
        },
        'NET': {
            'interfaces': {},
            'transport': {
                'tcpi': [], 'tcpo': [], 'udpi': [], 'udpo': []
            }
        },
        'DSK': {
            'devices': {} 
        }
    }


    with open(f'D:/work/logs/{log_pref}_atop_full.txt', 'r') as file:
        current_section = None
        for line in file:
            parts = line.strip().split('|')
            section = parts[0].strip()

            try:
                if section == 'CPU':

                    for part in parts[1:]:
                        if 'sys' in part:
                            stats['CPU']['sys'].append(float(part.split()[1].replace('%', '')))
                        elif 'user' in part:
                            stats['CPU']['user'].append(float(part.split()[1].replace('%', '')))
                        elif 'idle' in part:
                            stats['CPU']['idle'].append(float(part.split()[1].replace('%', '')))

                elif section == 'NET' and 'bond0' in line:

                    interface = 'bond0'
                    if interface not in stats['NET']['interfaces']:
                        stats['NET']['interfaces'][interface] = {
                            'si': [], 'so': [], 'pcki': [], 'pcko': []
                        }
                    
                    for part in parts[1:]:
                        if 'si' in part:
                            value = float(part.split()[1])
                            unit = part.split()[2]
                            if unit == 'Mbps':
                                value *= 1000
                            stats['NET']['interfaces'][interface]['si'].append(value)
                        elif 'so' in part:
                            value = float(part.split()[1])
                            unit = part.split()[2]
                            if unit == 'Mbps':
                                value *= 1000
                            stats['NET']['interfaces'][interface]['so'].append(value)

            except Exception as e:
                print(f"Ошибка при парсинге строки: {e}")
                continue

    with open(f'D:/work/logs/{timestamp}_{log_pref}_ATOP_STATS.txt', 'w') as report:
        report.write(f"=== ATOP Statistics Report {timestamp} ===\n\n")
        

        report.write("CPU Statistics:\n")
        for metric, values in stats['CPU'].items():
            if values:
                report.write(f"{metric}:\n")
                report.write(f"  Peak: {max(values):.2f}%\n")
                report.write(f"  Median: {median(values):.2f}%\n")
                report.write(f"  Min: {min(values):.2f}%\n")
        

        report.write("\nNetwork Statistics:\n")
        for interface, metrics in stats['NET']['interfaces'].items():
            report.write(f"\n{interface}:\n")
            for metric, values in metrics.items():
                if values:
                    max_val = max(values)
                    med_val = median(values)
                    min_val = min(values)
                    

                    if max_val > 1000:
                        report.write(f"  {metric} Peak: {max_val/1000:.2f} Mbps\n")
                    else:
                        report.write(f"  {metric} Peak: {max_val:.2f} Kbps\n")
                        
                    if med_val > 1000:
                        report.write(f"  {metric} Median: {med_val/1000:.2f} Mbps\n")
                    else:
                        report.write(f"  {metric} Median: {med_val:.2f} Kbps\n")
                        
                    if min_val > 1000:
                        report.write(f"  {metric} Min: {min_val/1000:.2f} Mbps\n")
                    else:
                        report.write(f"  {metric} Min: {min_val:.2f} Kbps\n")

    print(f'{color.grey("atop_stats")} {color.green("[DONE]")}')  