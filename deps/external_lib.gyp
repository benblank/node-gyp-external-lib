{
  "targets": [
    {
      "target_name": "external_lib",
      "type": "none",
      "sources": [
        # "external_lib/library.c"
        # "<!@(python3 external_lib_build_tools.py external_lib get_sources)"
      ],
      "link_settings": {
        "include_dirs": [
          "external_lib"
        ],
        "libraries": [
          "./external_lib.a"
        ]
      },
      "actions": [
        {
          "action_name": "compile_external_lib",
          "inputs": [
            # "external_lib/library.h"
          ],
          "outputs": [
            "external_lib.a"
            # "external_lib/library.c"
            # "<!@(python3 external_lib_build_tools.py external_lib get_outputs)"
          ],
          "action": [
            "make",
            "--directory=external_lib",
            "--file=../external_lib.mk",
            # "../external_lib.a"
            # "python3",
            # "external_lib_build_tools.py",
            # "external_lib",
            # "compile"
          ]
        }
      ]
    }
  ]
}
