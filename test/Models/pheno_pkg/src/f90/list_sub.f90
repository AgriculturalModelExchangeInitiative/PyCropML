MODULE list_sub
    IMPLICIT NONE
    TYPE container
        CLASS(*), ALLOCATABLE :: item
        CLASS(*), ALLOCATABLE :: items(:)
    END TYPE

    interface Add
        module procedure AddToListFloat
        module procedure AddToListInt
        module procedure AddToListChar
        module procedure AddToListIntArray
    end interface
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


    SUBROUTINE AddToListFloat(list, element)
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
    END SUBROUTINE AddToListFloat

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


    SUBROUTINE AddToListIntArray(a, e)
        INTEGER, ALLOCATABLE, INTENT(INOUT) :: a(:)
        INTEGER, ALLOCATABLE, INTENT(IN) :: e(:)
        INTEGER, ALLOCATABLE:: tmp(:)

        IF (.NOT.ALLOCATED(a)) THEN
            ALLOCATE(a(1))
            ALLOCATE(a(SIZE(e)), source = e)
        ELSE
            CALL MOVE_ALLOC(a,tmp)
            ALLOCATE(a(SIZE(tmp)+SIZE(e)), source = e)
            a(1:SIZE(tmp)) = tmp
            a(SIZE(tmp)+1:SIZE(a)) = e
        END IF
    END SUBROUTINE AddToListIntArray

END MODULE list_sub
