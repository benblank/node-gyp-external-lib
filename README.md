# Type: "none"

The few mentions I've found online of building an external library via its
Makefile have all used `"type": "none"`, but haven't explained why.

This [gypfile](deps/external_lib.gyp) uses `"type": "none"` and adds an explicit
library dependence on the file produced by the Makefile to `"link_settings"`.
The external library builds correctly, but then cannot be found by the
dependent's linking step.

The full output of running `node-gyp rebuild` can be found in
[node-gyp-rebuild.log](node-gyp-rebuild.log), which was generated using the
following command:

```sh
{ rm -f deps/*.a deps/*/*.o && node-gyp clean; } > /dev/null 2>&1 && V=1 node-gyp rebuild > node-gyp-rebuild.log 2>&1
```
