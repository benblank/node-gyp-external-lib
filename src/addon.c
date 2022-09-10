#include <stdlib.h>
#include <string.h>

#include <library.h>
#include <node_api.h>

static napi_value addon_reverse(napi_env env, napi_callback_info info) {
  size_t argc = 1;
  napi_value args[1];
  napi_value input_value;
  size_t input_size;
  char* input_utf8;
  char* output_utf8;
  napi_value output_value;

  napi_get_cb_info(env, info, &argc, args, NULL, NULL);
  napi_coerce_to_string(env, args[0], &input_value);
  napi_get_value_string_utf8(env, input_value, NULL, 0, &input_size);
  input_utf8 = malloc(input_size + 1);
  napi_get_value_string_utf8(env, input_value, input_utf8, input_size + 1, &input_size);
  output_utf8 = library_reverse(input_utf8);
  napi_create_string_utf8(env, output_utf8, NAPI_AUTO_LENGTH, &output_value);

  free(input_utf8);
  free(output_utf8);

  return output_value;
}

NAPI_MODULE_INIT() {
  napi_value reverse_value;

  napi_create_function(env, "reverse", NAPI_AUTO_LENGTH, addon_reverse, NULL, &reverse_value);
  napi_set_named_property(env, exports, "reverse", reverse_value);

  return exports;
}
