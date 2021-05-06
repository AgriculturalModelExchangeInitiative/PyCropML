
module modf
implicit none

contains

FUNCTION gsumf(x) RESULT(y)
    implicit none  
    INTEGER , DIMENSION(: ), INTENT(IN) :: x
    INTEGER:: y
    INTEGER:: i
    INTEGER:: i_cyml0
    y = 0
    DO i_cyml0 = 1, SIZE(x)
        i = x(i_cyml0)
        y = y + i
    END DO
END FUNCTION gsumf

end module modf


