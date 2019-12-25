def details(value=False):
    if value:
        keys = ['empid', 'emp_name', 'emp_addr']
    else:
        keys = ['cmpid', 'cmp_name', 'cmp_addr']

    class CredentialsClass:
        expected_keys = set(keys)

        def __init__(self, **kwargs):
            if self.expected_keys != set(kwargs.keys()):
                raise ValueError("Value Error")
            for k, v in kwargs.items():
                setattr(self, k, v)

    return CredentialsClass


emp = details(True)
e1 = emp(empid='101', emp_name='ABC', emp_addr='Bangalore')

cmp = details(False)
c1 = cmp(cmpid='c111', cmp_name='XYZ', cmp_addr='Mysore')

print(type(emp))
print(type(e1))
print(e1.empid)