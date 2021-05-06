
program test
use modf
implicit none
INTEGER, DIMENSION(2):: x
integer RES
x=[2,3]
RES = gsumf(x)
print *, RES

end program test
