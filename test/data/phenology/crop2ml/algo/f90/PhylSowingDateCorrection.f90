
    !use crop2mlModules

        IF (latitude < 0) THEN
            IF (sowingDay > sDsa_sh) THEN
                fixPhyll = p * (1 - rp * MIN(sowingDay - sDsa_sh, sDws))
            ELSE
                fixPhyll = p
            END IF
        ELSE
            IF (sowingDay < sDsa_nh) THEN
                fixPhyll = p * (1 - rp * MIN(sowingDay, sDws))
            ELSE
                fixPhyll = p
            END IF
        END IF



