program test

integer, ALLOCATABLE , DIMENSION(:)::  x
integer, ALLOCATABLE , DIMENSION(:)::  y
call essai(10,x)
!print *, x
call AddToListInt(y,15)
call AddToListInt(y,155)
call AddToListInt(y,159)
call AddToListInt(y,175)
call AddToListInt(y,185)
print *, y, size(y)
contains


    subroutine essai(n, x)
        integer, INTENT(IN) :: n
        integer, ALLOCATABLE , DIMENSION(:), INTENT(INOUT) ::  x
        integer i
        allocate(x(0:n))
        x(0)=6
        do i=1, n
            x(i)=i
        end do
    end subroutine


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