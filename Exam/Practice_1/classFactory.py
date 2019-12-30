def details(value=False):
    if value:
        keys = ['eid', 'name', 'addr']
    else:
        keys = ['cid', 'name', 'addr']

    class CredentialsClass:
        expected_keys = set(keys)

        def __init__(self, **kwargs):
            if self.expected_keys != set(kwargs.keys()):
                raise ValueError("Proper value not found")
            for k, v in kwargs.items():
                setattr(self, k, v)

    return CredentialsClass


emp = details(True)
e1 = emp(eid='101', name='ABC', addr='Bng')

cmp = details(False)
c1 = cmp(cid='001', name='XYZ', addr='Mys')

print(type(emp))
print(type(c1))
print(e1.eid)
