#include <stdlib.h>
#include <string.h>

char* library_reverse(const char* input) {
  size_t length = strlen(input);
  char* output = malloc(length + 1);

  for (size_t source = 0, target = length - 1; source < length; source++, target--) {
    output[target] = input[source];
  }

  output[length] = '\0';

  return output;
}
