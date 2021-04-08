from lin_alg_djl import Vector, Plane, Line, Hyperplane, LinearSystem

print("first pair of vectors...")
v = Vector(['3', '6', '3', '101', '-1'])
w = Vector(['4', '1', '11', '23', '9'])
print('dot: ', v.dot(w))

print("first pair of vectors...")
v = Vector(['3', '2', '3'])
w = Vector(['4', '1', '3'])
print('magnitude V: ', v.magnitude())
print('magnitude w: ', w.magnitude())


print("first pair of vectors...")
v = Vector(['3', '2', '3'])
w = Vector(['4', '1', '3'])
print('angle with: ', v.angle_with(w))

print('normalized a vector')
z = Vector(['2', '4'])
print('Normalized: ', z.normalized())

p1 = Plane(normal_vector=Vector(['-.412', '3.806', '0.728']), constant_term='-3.46')
p2 = Plane(normal_vector=Vector(['1.03', '-9.515', '-1.82']), constant_term='8.65')
print('first pair of planes are parallel?: {}'.format(p1.is_parallel_to(p2)))
print('First pair of planes are equal?: {}'.format(p1 == p2))

p1 = Plane(normal_vector=Vector(['2.611','5.528','0.283']), constant_term='4.6')
p2 = Plane(normal_vector=Vector(['7.715','8.306','5.342']), constant_term='3.76')
print('first pair of planes are parallel?: {}'.format(p1.is_parallel_to(p2)))
print('First pair of planes are equal?: {}'.format(p1 == p2))

p1 = Plane(normal_vector=Vector(['-7.926','8.625','-7.212']), constant_term='-7.95')
p2 = Plane(normal_vector=Vector(['-2.642','2.875','-2.404']), constant_term='-2.44')
print('first pair of planes are parallel?: {}'.format(p1.is_parallel_to(p2)))
print('First pair of planes are equal?: {}'.format(p1 == p2))


ell1 = Line(normal_vector=Vector(['4.046', '2.836']), constant_term='1.21')
ell2 = Line(normal_vector=Vector(['10.115', '7.09']), constant_term='3.025')
print('intersection 1: ', ell1.intersection_with(ell2))

ell1 = Line(normal_vector=Vector(['7.204', '3.182']), constant_term='8.68')
ell2 = Line(normal_vector=Vector(['8.172', '4.114']), constant_term='9.883')
print('intersection 2: ', ell1.intersection_with(ell2))

ell1 = Line(normal_vector=Vector(['1.182', '5.562']), constant_term='6.744')
ell2 = Line(normal_vector=Vector(['1.773', '8.343']), constant_term='9.525')
print('Intersection 3: ', ell1.intersection_with(ell2))

# Test problems below.
p1 = Hyperplane(normal_vector=Vector(
    ['-.412', '3.806', '0.728']), constant_term='-3.46')
p2 = Hyperplane(normal_vector=Vector(
    ['1.03', '-9.515', '-1.82']), constant_term='8.65')

p1 = Hyperplane(normal_vector=Vector(['2.611','5.528','0.283']), constant_term='4.6')
p2 = Hyperplane(normal_vector=Vector(['7.715','8.306','5.342']), constant_term='3.76')
print('first pair of planes are parallel?: {}'.format(p1.is_parallel_to(p2)))
print('First pair of planes are equal?: {}'.format(p1 == p2))

p1 = Hyperplane(normal_vector=Vector(['-7.926','8.625','-7.212']), constant_term='-7.95')
p2 = Hyperplane(normal_vector=Vector(['-2.642','2.875','-2.404']), constant_term='-2.44')
print('first pair of planes are parallel?: {}'.format(p1.is_parallel_to(p2)))
print('First pair of planes are equal?: {}'.format(p1 == p2))


p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')

s = LinearSystem([p0, p1, p2, p3])
# Print initial system
print(s)

p0 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p1 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p2 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p3 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')

s = LinearSystem([p0, p1, p2, p3])
s.swap_rows(0, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print ('test case 1 failed')

s.swap_rows(1, 3)
if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print ('test case 2 failed')

s.swap_rows(3, 1)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print ('test case 3 failed')

s.multiply_coefficient_and_row(1, 0)
if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print ('test case 4 failed')

s.multiply_coefficient_and_row(-1, 2)
new_s2 = Plane(normal_vector=Vector(['-1', '-1', '1']), constant_term='-3')
if not (s[0] == p1 and
        s[1] == p0 and
        s[2] == new_s2 and
        s[3] == p3):
    print ('test case 5 failed')

s.multiply_coefficient_and_row(10, 1)
new_s1 = Plane(normal_vector=Vector(['10', '10', '10']), constant_term='10')
if not (s[0] == p1 and
        s[1] == new_s1 and
        s[2] == new_s2 and
        s[3] == p3):
    print ('test case 6 failed')

s.add_multiple_times_row_to_row(0, 0, 1)
if not (s[0] == p1 and
        s[1] == new_s1 and
        s[2] == new_s2 and
        s[3] == p3):
    print ('test case 7 failed')

s.add_multiple_times_row_to_row(1, 0, 1)
added_s1 = Plane(normal_vector=Vector(['10', '11', '10']), constant_term='12')
if not (s[0] == p1 and
        s[1] == added_s1 and
        s[2] == new_s2 and
        s[3] == p3):
    print ('test case 8 failed')

s.add_multiple_times_row_to_row(-1, 1, 0)
new_s0 = Plane(normal_vector=Vector(['-10', '-10', '-10']),
               constant_term='-10')
if not (s[0] == new_s0 and
        s[1] == added_s1 and
        s[2] == new_s2 and
        s[3] == p3):
    print ('test case 9 failed')

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
s = LinearSystem([p1, p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2):
    print ('test case 1 failed')

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='2')
s = LinearSystem([p1, p2])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == Plane(constant_term='1')):
    print ('test case 2 failed')

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
s = LinearSystem([p1, p2, p3, p4])
t = s.compute_triangular_form()
if not (t[0] == p1 and
        t[1] == p2 and
        t[2] == Plane(normal_vector=Vector(['0', '0', '-2']),
                      constant_term='2') and
        t[3] == Plane()):
    print ('test case 3 failed')

p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1', '2', '-5']), constant_term='3')
s = LinearSystem([p1, p2, p3])
t = s.compute_triangular_form()
if not (t[0] == Plane(normal_vector=Vector(['1', '-1', '1']),
                      constant_term='2') and
        t[1] == Plane(normal_vector=Vector(['0', '1', '1']),
                      constant_term='1') and
        t[2] == Plane(normal_vector=Vector(['0', '0', '-9']),
                      constant_term='-2')):
    print('test case 4 failed')


# ***************

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='2')
s = LinearSystem([p1, p2])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1', '0', '0']),
                      constant_term='-1') and
        r[1] == p2):
    print ('test case 1 failed')

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='2')
s = LinearSystem([p1, p2])
r = s.compute_rref()
if not (r[0] == p1 and
        r[1] == Plane(constant_term='1')):
    print ('test case 2 failed')

p1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
p4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')
s = LinearSystem([p1, p2, p3, p4])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1', '0', '0']),
                      constant_term='0') and
        r[1] == p2 and
        r[2] == Plane(normal_vector=Vector(['0', '0', '-2']),
                      constant_term='2') and
        r[3] == Plane()):
    print ('test case 3 failed')

p1 = Plane(normal_vector=Vector(['0', '1', '1']), constant_term='1')
p2 = Plane(normal_vector=Vector(['1', '-1', '1']), constant_term='2')
p3 = Plane(normal_vector=Vector(['1', '2', '-5']), constant_term='3')
s = LinearSystem([p1, p2, p3])
r = s.compute_rref()
if not (r[0] == Plane(normal_vector=Vector(['1', '0', '0']),
                      constant_term=Decimal('23') / Decimal('9')) and
        r[1] == Plane(normal_vector=Vector(['0', '1', '0']),
                      constant_term=Decimal('7') / Decimal('9')) and
        r[2] == Plane(normal_vector=Vector(['0', '0', '1']),
                      constant_term=Decimal('2') / Decimal('9'))):
    print ('test case 4 failed')


# first system
p1 = Plane(Vector([5.862, 1.178, -10.366]), -8.15)
p2 = Plane(Vector([-2.931, -0.589, 5.183]), -4.075)
system1 = LinearSystem([p1, p2])
print ('first system: {}'.format(system1.do_gaussian_elimination()))


# # second system
p1 = Plane(Vector([8.631, 5.112, -1.816]), -5.113)
p2 = Plane(Vector([4.315, 11.132, -5.27]), -6.775)
p3 = Plane(Vector([-2.158, 3.01, -1.727]), -0.831)
system2 = LinearSystem([p1, p2, p3])
print ('second system: {}'.format(system2.do_gaussian_elimination()))


# third system
p1 = Plane(Vector([5.262, 2.739, -9.878]), -3.441)
p2 = Plane(Vector([5.111, 6.358, 7.638]), -2.152)
p3 = Plane(Vector([2.016, -9.924, -1.367]), -9.278)
p4 = Plane(Vector([2.167, -13.543, -18.883]), -10.567)
system3 = LinearSystem([p1, p2, p3, p4])
print ('thrid system: {} '.format(system3.do_gaussian_elimination()))


p1 = Plane(normal_vector=Vector([0.786, 0.786, 0.588]), constant_term=-0.714)
p2 = Plane(normal_vector=Vector([-0.131, -0.131, 0.244]), constant_term=0.319)

system = LinearSystem([p1, p2])
print (system.compute_solution())


p1 = Plane(Vector([8.631, 5.112, -1.816]), -5.113)
p2 = Plane(Vector([4.315, 11.132, -5.27]), -6.775)
p3 = Plane(Vector([-2.158, 3.01, -1.727]), -0.831)

system = LinearSystem([p1, p2, p3])
print (system.compute_solution())

p1 = Plane(Vector([0.935, 1.76, -9.365]), -9.955)
p2 = Plane(Vector([0.187, 0.352, -1.873]), -1.991)
p3 = Plane(Vector([0.374, 0.704, -3.746]), -3.982)
p4 = Plane(Vector([-0.561, -1.056, 5.619]), 5.973)

print (system.compute_solution())


# The systems bellow are just to test hyperplanes

p1 = Hyperplane(normal_vector=Vector([0.786, 0.786]), constant_term=0.786)
p2 = Hyperplane(normal_vector=Vector([-0.131, -0.131]), constant_term=-0.131)

system = LinearSystem([p1, p2])
print (system.compute_solution())


p1 = Hyperplane(normal_vector=Vector([2.102, 7.489, -0.786]),
                constant_term=-5.113)
p2 = Hyperplane(normal_vector=Vector([-1.131, 8.318, -1.209]),
                constant_term=-6.775)
p3 = Hyperplane(normal_vector=Vector([9.015, 5.873, -1.105]),
                constant_term=-0.831)

system = LinearSystem([p1, p2, p3])
print (system.compute_solution())

p1 = Hyperplane(normal_vector=Vector([0.786, 0.786, 8.123, 1.111, -8.363]),
                constant_term=-9.955)
p2 = Hyperplane(normal_vector=Vector([0.131, -0.131, 7.05, -2.813, 1.19]),
                constant_term=-1.991)
p3 = Hyperplane(normal_vector=Vector([9.015, -5.873, -1.105, 2.013, -2.802]),
                constant_term=-3.982)

system = LinearSystem([p1, p2, p3])
print(system.compute_solution())
