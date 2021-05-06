program test
implicit none
integer, ALLOCATABLE , DIMENSION(:)::  x
integer, ALLOCATABLE , DIMENSION(:)::  y
real z
call AddToListInt(y,15)
call AddToListInt(y,156)
call AddToListInt(y,155)
call AddToListInt(y,175)
call AddToListInt(y,185)
z = sum_(y)
call essai(5,y)
print *, 20
contains

    subroutine essai(n, x)
        integer, INTENT(IN) :: n
        integer, ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  x
        integer i
        x = (/5,4,6,8,4,6/)
        call AddToListInt(x,63)
        do i=1, size(x)
            print *, x(i)
        end do
        i = sum_(x)
        print *, i
    end subroutine

    FUNCTION sum_(x) RESULT(y)
    INTEGER ,ALLOCATABLE, DIMENSION(: ), INTENT(IN):: x
    INTEGER:: y
    INTEGER:: i
    INTEGER:: i_cyml0
    y = 0
    DO i_cyml0 = 1, SIZE(x)
        i = x(i_cyml0)
        y = y + i
    END DO
    END FUNCTION sum_


    SUBROUTINE AddToListInt(list, element)
        IMPLICIT NONE
        INTEGER :: i, isize
        INTEGER, INTENT(IN) :: element
        INTEGER, DIMENSION(:), ALLOCATABLE, INTENT(INOUT) :: list
        INTEGER, DIMENSION(:), ALLOCATABLE :: clist
        IF(ALLOCATED(list)) THEN
            isize = SIZE(list)
            ALLOCATE(clist(isize+1))
            DO i=1,isize
                clist(i) = list(i)
            END DO
            clist(isize+1) = element
            DEALLOCATE(list)
            CALL MOVE_ALLOC(clist, list)
        ELSE
            ALLOCATE(list(1))
            list(1) = element
        END IF
    END SUBROUTINE AddToListInt
    
end program