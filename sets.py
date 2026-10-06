a={1,2,3}
b={3,4}

print(a & b)
print(a|b)
print(a-b)



#print permissions only admins have
admin_perm={"read","write","delete","ban"}
editor_perm={"read","write"}
print(admin_perm-editor_perm)