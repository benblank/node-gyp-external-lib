{
  "targets": [
    {
      "target_name": "external_lib",
      "type": "static_library",
      "sources": [],
      "link_settings": {
        "include_dirs": [
          "external_lib",
        ],
      },
      "actions": [
        {
          "action_name": "compile_external_lib",
          "inputs": [],
          "outputs": [
            "external_lib/library.o",
          ],
          "action": [
            "make",
            "--directory=external_lib",
            "library.o",
          ],
        },
      ],
    },
  ],
}
