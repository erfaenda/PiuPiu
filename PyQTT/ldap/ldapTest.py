import ldap
ad = ldap.initialize("ldap://10.9.155.2")
ad.simple_bind_s("a.silantev@MFCKGN.LOCAL", "Yjdfz'hf!")
basedn = 'DC=MFCKGN,DC=LOCAL'
scope = ldap.SCOPE_ONELEVEL
filterexp = 'objectClass=organizationalUnit'
attrlist = ['name']
results = ad.search_s(basedn, scope, filterexp, attrlist)
for result in results:
    print(result[0].decode('utf-8'), result[1]['name'][0].decode('utf-8'))