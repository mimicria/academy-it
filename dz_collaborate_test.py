import dz_collaborate as test

a = []
test.Create_random(a, 5)
b = []
test.Create_manual(b, 5)
test.Print_array(a)
print(test.Find_value(b, 25))
print(test.Delete_value(b, 25))
print(test.Everage(a))
print(test.Sum_array(a, b))
