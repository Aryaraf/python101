def cpu(usage):
    if usage > 80:
        print(f"WARNING: CPU {usage}% is high!")
    else:
        print(f"CPU {usage}% is safe")
        
cpu(80)
cpu(85)