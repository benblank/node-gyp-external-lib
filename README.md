# Type: "static_library" (with sources listed)

This [gypfile](deps/external_lib.gyp) uses `"type": "static_library"` and lets
node-gyp handle the creation of the library archive and setting up the library
dependency. Not only does the external library build correctly, but node-gyp as
a whole exits successfully. However, the library source is compiled twice —
first by the library's own Makefile, then again by node-gyp. This produces a
working addon, but listing each source file isn't feasible for libraries with
large, complex Makefiles and double compilation isn't desirable in any
situation.

The full output of running `node-gyp rebuild` can be found in
[node-gyp-rebuild.log](node-gyp-rebuild.log), which was generated using the
following command:

```sh
{ rm -f deps/*.a deps/*/*.o && node-gyp clean; } > /dev/null 2>&1 && V=1 node-gyp rebuild > node-gyp-rebuild.log 2>&1
```

The addon's output can be seen by running:

```sh
node -p 'require(".").reverse("foo-bar")'
```
