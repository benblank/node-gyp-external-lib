# Type: "static_library" (no sources specified)

This [gypfile](deps/external_lib.gyp) uses `"type": "static_library"` and lets
node-gyp handle the creation of the library archive and setting up the library
dependency. Not only does the external library build correctly, but node-gyp as
a whole exits successfully. However, the library archive created by node-gyp is
empty, resulting in the addon not being linked to the external library and
therefore to fail when used.

The full output of running `node-gyp rebuild` can be found in
[node-gyp-rebuild.log](node-gyp-rebuild.log), which was generated using the
following command:

```sh
{ rm -f deps/*.a deps/*/*.o && node-gyp clean; } > /dev/null 2>&1 && V=1 node-gyp rebuild > node-gyp-rebuild.log 2>&1
```

The addon's failure (`symbol lookup error` … `undefined symbol`) can be seen by
running:

```sh
node -p 'require(".").reverse("foo-bar")'
```
