
if (latitude < 0.0):
    if (sowingDay > int(sDsa_sh)):
        fixPhyll = p * (1 - rp * min(sowingDay - sDsa_sh, sDws))
    else:
        fixPhyll = p
else:
    if (sowingDay < int(sDsa_nh)):
        fixPhyll = p * (1 - rp * min(sowingDay, sDws))
    else:
        fixPhyll = p
