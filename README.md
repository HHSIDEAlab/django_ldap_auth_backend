LDAP Authentication Backend
---------------------------


Install with the following command:

    pip install django_ldap_auth_backend
    
 
 Then add the backend module to to AUTHENTICATION_BACKENDS
 in your Django `settings` like so:


    AUTHENTICATION_BACKENDS = (
        'ldap.backends.ldap_auth.LDAPBackend',
        'django.contrib.auth.backends.ModelBackend',
        .
        .
        .
        )


Be default the backend looks for an LDAP server at `localhost` on port `10389`.

These items can be overridden in django `settings` like so:

    LDAP_HOST = "ldap.example.com"
    LDAP_PORT = 9999
    
In the above example, the backend will look for an LDAP server `ldap.example.com`
on port `9999`.