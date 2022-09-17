# Type: "none" (with absolute library path)

The few mentions I've found online of building an external library via its
Makefile have all used `"type": "none"`, but haven't explained why.

This [gypfile](deps/external_lib.gyp) uses `"type": "none"` and adds an explicit
library dependence on the file produced by the Makefile to `"link_settings"`.
Unlike the earlier attempt, which relied on gyp to determine where the library
was located relative to the build directory and make sure it was available, this
gypfile calls out to `pwd` so that it can provide the absolute path to the
library to its dependents. This results in a working addon.

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
