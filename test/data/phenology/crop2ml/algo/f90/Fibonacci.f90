        INTEGER: i, temp, b
        result = 0
        b = 1
        DO i = 0 , n - (1) , 1
            temp = result
            result = b
            b = temp + b
        END DO