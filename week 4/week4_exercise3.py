passwords = [ "Pass123",
"SecurePassword1", "weak",
"MyP@ssw0rd", "NOLOWER123"]

min_length = 8
# len counts the number items in a list

compliant = 0
non_compliant = 0

for password in passwords:
    issues = []
    
    if len (password) < min_length:
        issues.append("Too short")

    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password: 
        if "A" <= char <= "Z":
            has_upper = True
        elif "a" <= char <= "z":
            has_lower = True
        elif "0" <= char <= "9":
            has_digit = True

    if not has_upper:
        issues.append("No uppercase letter")
    if not has_lower:
        issues.append("No lowercase letter")
    if not has_digit:
        issues.append("No digit")

    if len(issues) == 0:
        compliant += 1
        print (f"PASS: {password} - Meets all requirements") 
    else: 
        non_compliant += 1
        text = ",".join(issues)
        print (f"FAIL: {password} - {text}")

print (f"Summary: {compliant} compliant, {non_compliant} non_compliant")

