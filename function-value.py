def cpu(usage):
    if usage > 80:
        return False
    else:
        return True
    
status = cpu(90)
print(cpu)
    