MODULE Crop2mlModules
    IMPLICIT NONE
CONTAINS

    FUNCTION indice(vectorElem, elem)
        CHARACTER(LEN=*), DIMENSION(:):: vectorElem
        INTEGER::iterator, indice
        CHARACTER(LEN=*):: elem
        DO iterator= 1, SIZE(vectorElem)
            IF(vectorElem(iterator)==elem) THEN
                indice = iterator
            END IF
        END DO
        RETURN
    END FUNCTION indice

    FUNCTION fibonacci(n)
        INTEGER::n, fibonacci,b=1, i, temp
        fibonacci=0
        DO i=0, n-1
            temp = fibonacci;
            fibonacci=b;
            b=temp+b;
        END DO
        RETURN
    END FUNCTION fibonacci

    SUBROUTINE AddToList(list, element)
        IMPLICIT NONE
        INTEGER :: i, isize
        REAL, INTENT(IN) :: element
        REAL, DIMENSION(:), ALLOCATABLE, INTENT(INOUT) :: list
        REAL, DIMENSION(:), ALLOCATABLE :: clist
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
    END SUBROUTINE AddToList

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

    SUBROUTINE AddToListChar(list, element)
        IMPLICIT NONE
        INTEGER :: i, isize, l
        CHARACTER(LEN=*), INTENT(IN) :: element
        CHARACTER(LEN=*), DIMENSION(:), ALLOCATABLE, INTENT(INOUT) :: list
        CHARACTER(LEN=65), DIMENSION(:), ALLOCATABLE :: clist
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
            l=1
            ALLOCATE(list(l))
            list(l) = element
        END IF
    END SUBROUTINE AddToListChar
END MODULE Crop2mlModules
