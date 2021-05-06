Module afgen
    IMPLICIT NONE
CONTAINS

    FUNCTION AFGEN1(n, &
        xy, &
        t) RESULT(res)
        IMPLICIT NONE
        INTEGER, INTENT(IN) :: n
        REAL , DIMENSION(n ), INTENT(IN) :: xy
        REAL, INTENT(IN) :: t
        REAL:: res
        REAL:: x1
        REAL:: x2
        REAL:: y1
        REAL:: y2
        INTEGER:: i
        IF(n .GT. 1) THEN
            i = 0
            DO WHILE ( i .LT. n - 1 .AND. t .GE. xy(i+1) )
                i = i + 2
            END DO
            IF(i .EQ. 0) THEN
                res = xy(2)
            ELSE IF ( i .GT. n - 2) THEN
                res = xy(i - 1+1)
            ELSE
                x1 = xy(i - 2+1)
                x2 = xy(i+1)
                y1 = xy(i - 1+1)
                y2 = xy(i + 1+1)
                res = (y2 - y1) / (x2 - x1) * (t - x1) + y1
            END IF
        END IF
    END FUNCTION AFGEN1

END MODULE