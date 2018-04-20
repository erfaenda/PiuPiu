from ldap3 import Server, Connection, SIMPLE, SYNC, ASYNC, SUBTREE, ALL

# домен - example.com
# DNS имя сервера Active Directory
AD_SERVER = 'kgndc-01'
# Пользователь (логин) в Active Directory - нужно указать логин в AD
# в формате 'EXAMPLE\aduser' или 'aduser@example.com'
AD_USER = 'dcadmin3@mfckgn.local'
AD_PASSWORD = "Yjdfz'hf!"
AD_SEARCH_TREE = 'dc=mfckgn,dc=local'

server = Server(AD_SERVER)
conn = Connection(server,user=AD_USER,password=AD_PASSWORD)
conn.bind()
# в ответ должно быть - True

# Поиск в Active Directory
# примеры ldap фильтров можно посмотреть здесь -
# https://social.technet.microsoft.com/wiki/contents/articles/8077.active-directory-ldap-ru-ru.aspx
# Я в нижеследующем фильтре:
# - исключаю всеx отключенных пользователей (!(UserAccountControl:1.2.840.113556.1.4.803:=2))
# - добавляю только тех пользователей у которых заполнено имя и фамилия
# - и вывожу атрибуты - attributes
# Все возможные атрибуты Active Directory можно посмотреть здесь -
# https://msdn.microsoft.com/en-us/library/ms675090%28v=vs.85%29.aspx
conn.search(AD_SEARCH_TREE,'(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2))(givenName=*)(sn=*))',
    SUBTREE,
    attributes =['cn','proxyAddresses','department','sAMAccountName', 'displayName', 'telephoneNumber', 'ipPhone', 'streetAddress',
    'title','manager','objectGUID','company','lastLogon']
    )
# после этого запроса в ответ должно быть - True

# можно посмотреть на результат
#print(conn.entries)
# или вывести только Common-Name - cn
i = 0
for entry in conn.entries:
    print(entry.sAMAccountName)
    i = i + 1
print(i)


# Найти пользователя с логином admin (sAMAccountName=admin) и показать информацию по нему
conn.search(AD_SEARCH_TREE,'(&(objectCategory=Person)(sAMAccountName=dcadmin))', SUBTREE,
    attributes =['cn','proxyAddresses','department','sAMAccountName', 'displayName', 'telephoneNumber', 'ipPhone', 'streetAddress',
    'title','manager','objectGUID','company','lastLogon']
    )

print(conn.entries)
