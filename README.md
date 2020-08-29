# smeta

> `smeta` Swedish for `smear`.<br>
> `smear`<br>
> *verb (used with object)*:
> * to spread or daub (an oily, greasy, viscous, or wet substance) on or over something: to smear butter on bread.
> * to spread or daub an oily, greasy, viscous, or wet substance on: to smear bread with butter.
> * to stain, spot, or make dirty with something oily, greasy, viscous, or wet.<br>
>
> *noun*:
> * an oily, greasy, viscous, or wet substance, especially a dab of such a substance.
> * a stain, spot, or mark made by such a substance.
> * a smudge.

A meta relationship API and web UI for creating relationships between different services, e.g. your
companys Single sign-on and your Github account. This is the data/relationships that noone wants to
do but everyone needs to know about in this BYO world.

# Plugins

There are two different kinds of plugins:
* `authenticators` which authenticate a user which you can add tokens to for verification.
* `verifiers` verifies with certainty that a user holds the token that the user provides.

## authenticators
Authenticators authenticate your users to smeta and then the user can add verified external accounts
to their account.

### SAML2
Simple SAML2 Service Provider which requests attributes that map into:
* username (primary key of the user)<br>
  Probably `eduPersonPrincipalName` or `uid`.
* mail (to be able to send reminders that the user should verify a token e.g.)

### OIDC / OpenID Connect
Simple OIDC Relying Party which requests claims to map into:
* `preferred_username` (primary key of the user)
* `email` (and probably `email_verified` as well)

## verifiers

### email
Might be strange since we already got an email from the authenticator, but this is an external or
maybe a personal email. Gets verified by a secure, verification email with relative short timeout.

### ssh-keys

Upload your ssh-keys and then verify them by ssh:ing with that they into smeta with a unique
username which we then can verify that the user holds the ssh-key.

### pgpkeys

FIXME

### github

FIXME

### totp

FIXME
