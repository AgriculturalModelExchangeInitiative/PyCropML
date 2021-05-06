
program test
use afgen
implicit none
real, DIMENSION(5:14):: x=(/10.2,52.3,14.6,75.3,36.6,152.5,40.5,160.5,45.5,178.2/)
integer:: n = 5
real res
real(8) toto
RES = afgen1(10,x, 12.2)
print *, RES, x(n)
end program test