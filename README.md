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
companys Single-Signon and your Github account. This is the data/relationships that noone wants to
do but everyone needs to know about in this BYO world.

# Plugins

There are two different kinds of plugins:
* `authenticators` which authenticate a user which you can add tokens to for verification.
* `verifiers` verifies with certainty that a user holds the token that the user provides.
