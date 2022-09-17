{
  "targets": [
    {
      "target_name": "external_lib",
      "type": "none",
      "sources": [],
      "link_settings": {
        "include_dirs": [
          "external_lib",
        ],
        "libraries": [
          "<!(pwd)/external_lib.a",
        ],
      },
      "actions": [
        {
          "action_name": "compile_external_lib",
          "inputs": [],
          "outputs": [
            "external_lib.a",
          ],
          "action": [
            "make",
            "--directory=external_lib",
            "../external_lib.a",
          ],
        },
      ],
    },
  ],
}
