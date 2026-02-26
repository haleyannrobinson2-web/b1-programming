
# Advanced Server Log Analyzer


import re
import logging
from collections import defaultdict
from datetime import datetime


logging.basicConfig(
    filename=f"server_analyzer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


log_pattern = re.compile(
    r'(?P<ip>\S+) \S+ \S+ \[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<url>\S+) \S+" '
    r'(?P<status>\d{3}) (?P<size>\d+|-) '
    r'"(?P<user_agent>[^"]+)"'
)


error_logs = []  # store 4xx and 5xx logs
security_incidents = []  # failed logins, suspicious user agents
failed_auth_attempts = defaultdict(int)  # track failed logins per IP

suspicious_agents = ['sqlmap', 'nikto', 'fuzzer', 'acunetix']

def analyze_log_file(log_file):
    try:
        with open(log_file, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    match = log_pattern.match(line)
                    if not match:
                        logging.warning(f"Line {line_num}: Malformed log entry skipped")
                        continue

                    ip = match.group('ip')
                    method = match.group('method')
                    url = match.group('url')
                    status = int(match.group('status'))
                    user_agent = match.group('user_agent')

                    # Capture HTTP errors
                    if 400 <= status < 600:
                        error_logs.append(line)

                        # Track failed authentication attempts (example: 401)
                        if status == 401:
                            failed_auth_attempts[ip] += 1
                            if failed_auth_attempts[ip] >= 3:
                                security_incidents.append(
                                    f"Possible brute force: IP {ip} has {failed_auth_attempts[ip]} failed logins"
                                )

                    # Detect unusual HTTP methods
                    if method not in ['GET', 'POST', 'HEAD', 'PUT', 'DELETE']:
                        security_incidents.append(f"Suspicious method {method} from IP {ip}")

                    # Detect suspicious user agents
                    if any(agent.lower() in user_agent.lower() for agent in suspicious_agents):
                        security_incidents.append(f"Suspicious user agent detected from IP {ip}: {user_agent}")

                except Exception as e:
                    logging.error(f"Line {line_num}: Error parsing log - {e}")
                    continue

        # Write error logs
        with open('error_log.txt', 'w') as ef:
            for log in error_logs:
                ef.write(log + "\n")

        # Write security incidents
        with open('security_incidents.txt', 'w') as sf:
            for incident in security_incidents:
                sf.write(incident + "\n")

        # Console summary
        print("\nLog Analysis Complete!")
        print(f"Total errors detected: {len(error_logs)}")
        print(f"Total security incidents: {len(security_incidents)}")
        logging.info(f"Processed {line_num} log lines: {len(error_logs)} errors, {len(security_incidents)} security incidents")

    except FileNotFoundError:
        logging.error(f"Log file '{log_file}' not found")
        print(f"Error: Could not find {log_file}")
    except PermissionError:
        logging.error(f"Permission denied reading '{log_file}' or writing output files")
        print("Error: Permission denied")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Error: {e}")


if __name__ == "__main__":
    analyze_log_file('access.log')  # replace with your log filename
